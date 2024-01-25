import json
import os
from datetime import date
from unittest import TestCase, mock

import responses
from freezegun import freeze_time
from requests.exceptions import RequestException, Timeout

from verify_vat_number.ares import (ECONOMIC_ENTITY, PUBLIC_REGISTER, SERVICE_API_URL, RegisterType,
                                    UnexpectedResponseFormat, get_active_record, get_company_bodies,
                                    get_economic_entity_basis, get_from_cz_ares, get_from_cz_ares_ee,
                                    get_from_cz_ares_vr, get_legal_person, get_member_role_type, get_natural_person,
                                    get_partners, get_public_register, get_representatives, get_response_json,
                                    map_address)
from verify_vat_number.data import (CompanyEntity, CompanyEntityType, LegalPerson, Member, MemberRoleType,
                                    NaturalPerson, VerifiedCompany, VerifiedCompanyPublicRegister)
from verify_vat_number.exceptions import (InvalidVatNumber, ServiceTemporarilyUnavailable, VatNotFound,
                                          VerifyVatException)
from verify_vat_number.tests.utils import get_file_content

DATA_DIR_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


def data_json_response(vat: str = '67985726', registry: str = 'basic') -> str:
    """Get response of VAT number from registry."""
    return get_file_content(os.path.join(DATA_DIR_PATH, f'ares_{registry}_{vat}.json'))


class TestAres(TestCase):

    logger_name = 'verify_vat_number.ares'
    api_url = f'{SERVICE_API_URL}/{ECONOMIC_ENTITY}/67985726/'
    api_log = f'INFO:verify_vat_number.ares:{SERVICE_API_URL}/{ECONOMIC_ENTITY}/67985726/'

    def test_get_response_json_request_exception(self):
        with self.assertLogs(self.logger_name, level='INFO') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, body=RequestException())
                with self.assertRaises(VerifyVatException) as context:
                    get_response_json(self.api_url)
        self.assertEqual(context.exception.source, '')
        self.assertEqual(logs.output, [self.api_log])

    def test_get_response_json_timeout(self):
        with self.assertLogs(self.logger_name, level='INFO') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, body=Timeout())
                with self.assertRaises(ServiceTemporarilyUnavailable) as context:
                    get_response_json(self.api_url)
        self.assertIsNone(context.exception.source)
        self.assertEqual(logs.output, [self.api_log])

    def test_get_response_json_response_is_not_ok(self):
        with self.assertLogs(self.logger_name, level='INFO') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, status=404, body="Page not found.")
                with self.assertRaises(VerifyVatException) as context:
                    get_response_json(self.api_url)
        self.assertEqual(context.exception.source, 'Page not found.')
        self.assertEqual(logs.output, [self.api_log])

    def test_get_response_base_67985726(self):
        body = data_json_response()
        with self.assertLogs(self.logger_name, level='DEBUG') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, body=body)
                response_json = get_response_json(self.api_url)
        ref_json = json.loads(body)
        self.assertEqual(response_json, ref_json)
        self.assertEqual(logs.output, [self.api_log, f'DEBUG:verify_vat_number.ares:{body}'])

    def test_get_response_vr_67985726(self):
        body = data_json_response(registry='vr')
        with self.assertLogs(self.logger_name, level='INFO') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, f'{SERVICE_API_URL}/{PUBLIC_REGISTER}/67985726', body=body)
                response_json = get_response_json(f'{SERVICE_API_URL}/{PUBLIC_REGISTER}/67985726')
        ref_json = json.loads(body)
        self.assertEqual(response_json, ref_json)
        self.assertEqual(logs.output, [
            f'INFO:verify_vat_number.ares:{SERVICE_API_URL}/{PUBLIC_REGISTER}/67985726',
        ])

    def test_invalid_json(self):
        with self.assertLogs(self.logger_name, level='DEBUG') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, body='{[')
                with self.assertRaises(VerifyVatException) as context:
                    get_response_json(self.api_url)
        self.assertEqual(context.exception.source, '{[')
        self.assertEqual(logs.output, [self.api_log, 'DEBUG:verify_vat_number.ares:{['])

    def test_error_code_400(self):
        with self.assertLogs(self.logger_name, level='DEBUG') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, status=400,
                         body='{"kod": "OBECNA_CHYBA", "popis": "Bad Request"}')
                with self.assertRaises(InvalidVatNumber):
                    get_response_json(self.api_url)
        self.assertEqual(logs.output, [self.api_log])

    def test_error_code_401(self):
        with self.assertLogs(self.logger_name, level='DEBUG') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, status=401,
                         body='{"kod": "OBECNA_CHYBA", "popis": "Unauthorized"}')
                with self.assertRaises(VerifyVatException):
                    get_response_json(self.api_url)
        self.assertEqual(logs.output, [self.api_log])

    def test_error_code_403(self):
        with self.assertLogs(self.logger_name, level='DEBUG') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, status=403, body='{"kod": "OBECNA_CHYBA", "popis": "Forbidden"}')
                with self.assertRaises(VerifyVatException):
                    get_response_json(self.api_url)
        self.assertEqual(logs.output, [self.api_log])

    def test_error_code_404(self):
        with self.assertLogs(self.logger_name, level='DEBUG') as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, status=404, body='{"kod": "OBECNA_CHYBA", "popis": "Not Found"}')
                with self.assertRaises(VatNotFound):
                    get_response_json(self.api_url)
        self.assertEqual(logs.output, [self.api_log])

    def test_get_from_cz_ares_ee(self):
        with self.assertLogs(self.logger_name) as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, body=data_json_response())
                response = get_from_cz_ares_ee('67985726')
        self.assertEqual(
            response,
            VerifiedCompany(
                company_name='CZ.NIC, z.s.p.o.',
                address='Milešovská 1136/5\n13000 Praha 3',
                street_and_num='Milešovská 1136/5',
                city='Praha 3',
                postal_code='13000',
                district='Praha 3 - Vinohrady',
                country_code='CZ',
                legal_form=751
            )
        )
        self.assertEqual(logs.output, [self.api_log])

    def test_get_from_cz_ares_vr(self):
        with self.assertLogs(self.logger_name) as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, f'{SERVICE_API_URL}/{PUBLIC_REGISTER}/67985726/',
                         body=data_json_response(registry='vr'))
                response = get_from_cz_ares_vr('67985726')
        entities = [
            CompanyEntity(
                CompanyEntityType.GOVERNING_BODY,
                "Statutární orgán - Představenstvo",
                [
                    Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson("Marek", "Antoš", date(1979, 12, 18))),
                    Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson("Tomáš", "Košňar", date(1965, 6, 21))),
                    Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson("Martin", "Kukačka",
                                                                               date(1980, 10, 30))),
                    Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson("Karel", "Taft", date(1971, 5, 26))),
                    Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson("Ilona", "Filípková", date(1972, 7, 8))),
                ],
            ),
            CompanyEntity(
                CompanyEntityType.OTHER,
                "Kontrolní orgán - Dozorčí rada",
                [
                    Member(MemberRoleType.AUDIT_COMMITTEE_MEMBER, NaturalPerson("Jan", "Redl", date(1972, 3, 18))),
                    Member(MemberRoleType.AUDIT_COMMITTEE_MEMBER, NaturalPerson("Vlastimil", "Pečínka",
                                                                                date(1975, 9, 12))),
                    Member(MemberRoleType.AUDIT_COMMITTEE_MEMBER, NaturalPerson("Jan", "Gruntorád",
                                                                                date(1951, 10, 19))),
                ],
            ),
        ]
        self.assertEqual(
            response,
            VerifiedCompanyPublicRegister(
                company_name="CZ.NIC, z.s.p.o.",
                address="Milešovská 1136/5\n13000 Praha 3",
                street_and_num="Milešovská 1136/5",
                city="Praha 3",
                postal_code="13000",
                district="Praha 3 - Vinohrady",
                country_code="CZ",
                company_entities=entities,
                legal_form=751
            )
        )
        self.assertEqual(logs.output, [f'INFO:verify_vat_number.ares:{SERVICE_API_URL}/{PUBLIC_REGISTER}/67985726/'])

    def test_get_from_cz_ares_vr_14347890(self):
        with self.assertLogs(self.logger_name) as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, f'{SERVICE_API_URL}/{PUBLIC_REGISTER}/14347890/',
                         body=data_json_response('14347890', 'vr'))
                response = get_from_cz_ares_vr('14347890')
        entities = [
            CompanyEntity(CompanyEntityType.GOVERNING_BODY, "Statutární orgán", [
                Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson('Monika', 'Všianská', date(1980, 5, 1))),
            ]),
            CompanyEntity(CompanyEntityType.PARTNER, "Společníci", [
                Member(MemberRoleType.PARTNER_PERSON, NaturalPerson('Monika', 'Všianská', date(1980, 5, 1))),
            ]),
        ]
        self.assertEqual(
            response,
            VerifiedCompanyPublicRegister(
                company_name="LIMO SERVICES EUROPE s.r.o.",
                address="Křižovnická 86/6\n11000 Praha 1",
                street_and_num="Křižovnická 86/6",
                city="Praha 1",
                postal_code="11000",
                district="Praha 1 - Staré Město",
                country_code="CZ",
                company_entities=entities,
                legal_form=112
            ),
        )
        self.assertEqual(logs.output, [f'INFO:verify_vat_number.ares:{SERVICE_API_URL}/{PUBLIC_REGISTER}/14347890/'])

    def test_get_from_cz_ares_type_vr(self):
        with self.assertLogs(self.logger_name) as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, f'{SERVICE_API_URL}/{PUBLIC_REGISTER}/14347890/',
                         body=data_json_response('14347890', 'vr'))
                response = get_from_cz_ares('14347890', RegisterType.PUBLIC_REGISTER)
        entities = [
            CompanyEntity(CompanyEntityType.GOVERNING_BODY, "Statutární orgán", [
                Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson('Monika', 'Všianská', date(1980, 5, 1))),
            ]),
            CompanyEntity(CompanyEntityType.PARTNER, "Společníci", [
                Member(MemberRoleType.PARTNER_PERSON, NaturalPerson('Monika', 'Všianská', date(1980, 5, 1))),
            ]),
        ]
        self.assertEqual(
            response,
            VerifiedCompanyPublicRegister(
                company_name="LIMO SERVICES EUROPE s.r.o.",
                address="Křižovnická 86/6\n11000 Praha 1",
                street_and_num="Křižovnická 86/6",
                city="Praha 1",
                postal_code="11000",
                district="Praha 1 - Staré Město",
                country_code="CZ",
                company_entities=entities,
                legal_form=112
            ),
        )
        self.assertEqual(logs.output, [f'INFO:verify_vat_number.ares:{SERVICE_API_URL}/{PUBLIC_REGISTER}/14347890/'])

    def test_get_from_cz_ares_no_vr(self):
        with self.assertLogs(self.logger_name) as logs:
            with responses.RequestsMock() as mock:
                mock.add(responses.GET, self.api_url, body=data_json_response())
                response = get_from_cz_ares('67985726')
        self.assertEqual(
            response,
            VerifiedCompany(
                company_name="CZ.NIC, z.s.p.o.",
                address="Milešovská 1136/5\n13000 Praha 3",
                street_and_num="Milešovská 1136/5",
                city="Praha 3",
                postal_code="13000",
                district="Praha 3 - Vinohrady",
                country_code="CZ",
                legal_form=751
            ),
        )
        self.assertEqual(logs.output, [
            f'INFO:verify_vat_number.ares:{SERVICE_API_URL}/{ECONOMIC_ENTITY}/67985726/',
        ])

    def test_get_from_cz_ares_empty_number(self):
        with self.assertRaisesRegex(InvalidVatNumber, 'Invalid number format.'):
            get_from_cz_ares('!')

    def test_get_from_cz_ares_too_long_number(self):
        with self.assertRaisesRegex(InvalidVatNumber, 'The number cannot be more than 8 digits long.'):
            get_from_cz_ares('123456789')


class GetActiveRecordTest(TestCase):

    def test_empty(self):
        self.assertIsNone(get_active_record([]))

    def test_key(self):
        self.assertEqual(get_active_record([{'hodnota': 'foo'}]), 'foo')

    def test_custom_key(self):
        self.assertEqual(get_active_record([{'custom': 'foo'}], 'custom'), 'foo')

    def test_deleted(self):
        self.assertIsNone(get_active_record([{'datumVymazu': '2024-01-08'}]))

    @freeze_time("2024-01-04")
    def test_not_yet_deleted(self):
        self.assertEqual(get_active_record([{'datumVymazu': '2024-01-08', 'hodnota': 'foo'}]), 'foo')


class GetNaturalPersonTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_natural_person({}), NaturalPerson())

    def test_first_name(self):
        self.assertEqual(get_natural_person({"jmeno": "ARNOLD"}), NaturalPerson('Arnold'))

    def test_last_name(self):
        self.assertEqual(get_natural_person({"prijmeni": "RIMMER"}), NaturalPerson(last_name='Rimmer'))

    def test_birth_date(self):
        self.assertEqual(get_natural_person({"datumNarozeni": "2024-01-09"}), NaturalPerson(date_of_birth=date(
            2024, 1, 9)))

    @mock.patch.dict(os.environ, {"ARES_KEEP_CASE": "y"}, clear=True)
    def test_keep_case(self):
        self.assertEqual(
            get_natural_person({"jmeno": "ARNOLD", "prijmeni": "RIMMER"}), NaturalPerson('ARNOLD', 'RIMMER'))


class GetLegalPersonTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_legal_person({}), LegalPerson())

    def test_vat_number(self):
        self.assertEqual(get_legal_person({'ico': 42}), LegalPerson('42'))

    def test_bussiness_name(self):
        self.assertEqual(get_legal_person({'obchodniJmeno': 'The Name'}), LegalPerson(name='The Name'))

    def test_representatives(self):
        self.assertEqual(get_legal_person({'zastoupeni': [
            {'fyzickaOsoba': {'jmeno': 'Dave', 'prijmeni': 'Lister'}},
            {'fyzickaOsoba': {'jmeno': 'Arnold', 'prijmeni': 'Rimmer'}},

        ]}), LegalPerson(representatives=[
            NaturalPerson('Dave', 'Lister'),
            NaturalPerson('Arnold', 'Rimmer'),
        ]))


class GetEngagementTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_representatives([]), [])

    def test_persons(self):
        self.assertEqual(get_representatives([{}]), [])

    def test_persons_identity(self):
        self.assertEqual(get_representatives([
            {'fyzickaOsoba': {'jmeno': 'Dave', 'prijmeni': 'Lister'}},
            {'fyzickaOsoba': {'jmeno': 'Arnold', 'prijmeni': 'Rimmer'}, 'datumVymazu': '2024-01-08'},
        ]), [
            NaturalPerson('Dave', 'Lister'),
        ])


class MapAddressTest(TestCase):

    def setUp(self):
        self.company = VerifiedCompany('')

    def test_empty(self):
        map_address(self.company, None)
        self.assertEqual(self.company, VerifiedCompany(''))

    def test_str(self):
        with self.assertRaises(UnexpectedResponseFormat):
            map_address(self.company, "yes")

    def test_int(self):
        with self.assertRaises(UnexpectedResponseFormat):
            map_address(self.company, 42)

    def test_country_code(self):
        map_address(self.company, {'kodStatu': 'CZ'})
        self.assertEqual(self.company, VerifiedCompany("", country_code='CZ'))

    def test_city(self):
        map_address(self.company, {'nazevObce': 'City'})
        reference = VerifiedCompany('', address='City', city='City', district='City')
        self.assertEqual(self.company, reference)

    def test_city_prague(self):
        map_address(self.company, {'nazevObce': 'Praha'})
        self.assertEqual(self.company, VerifiedCompany('', address='Praha', city='Praha', district='Praha'))

    def test_city_prague_district(self):
        map_address(self.company, {'nazevObce': 'Praha', 'nazevMestskehoObvodu': 'Praha 8'})
        self.assertEqual(self.company, VerifiedCompany('', address='Praha 8', city='Praha 8', district='Praha 8'))

    def test_district(self):
        map_address(self.company, {'nazevCastiObce': 'District'})
        self.assertEqual(self.company, VerifiedCompany('', district='District'))

    def test_city_district(self):
        map_address(self.company, {'nazevObce': 'City', 'nazevCastiObce': 'District'})
        self.assertEqual(self.company, VerifiedCompany('', address='City', city='City', district='City - District'))

    def test_city_in_district(self):
        map_address(self.company, {'nazevObce': 'City', 'nazevCastiObce': 'City 8'})
        self.assertEqual(self.company, VerifiedCompany('', address='City', city='City', district='City 8'))

    def test_street(self):
        map_address(self.company, {'nazevUlice': 'Street'})
        self.assertEqual(self.company, VerifiedCompany('', address='Street', street_and_num='Street'))

    def test_street_number(self):
        map_address(self.company, {'cisloOrientacni': 88})
        self.assertEqual(self.company, VerifiedCompany('', address='88', street_and_num='88'))

    def test_house_number(self):
        map_address(self.company, {'cisloDomovni': 42})
        self.assertEqual(self.company, VerifiedCompany('', address='42', street_and_num='42'))

    def test_postal_code(self):
        map_address(self.company, {'psc': 12000})
        self.assertEqual(self.company, VerifiedCompany('', address='12000', postal_code='12000'))

    def test_all_values(self):
        map_address(self.company, {
            'kodStatu': 'CZ',
            'nazevObce': 'City',
            'nazevCastiObce': 'District',
            'nazevUlice': 'Street',
            'cisloOrientacni': 88,
            'cisloDomovni': 42,
            'psc': 12000
        })
        reference = VerifiedCompany(
            '', address='Street 42/88\n12000 City', street_and_num='Street 42/88', city='City', postal_code='12000',
            district='City - District', country_code='CZ')
        self.assertEqual(self.company, reference)


class GetCompanyBodiesTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_company_bodies([], CompanyEntityType.GOVERNING_BODY), [])

    def test_deleted(self):
        self.assertEqual(get_company_bodies([
            {'datumVymazu': '2024-01-08', 'clenoveOrganu': [{'typAngazma': 'STATUTARNI_ORGAN_CLEN'}]},
        ], CompanyEntityType.GOVERNING_BODY), [])

    def test_no_members(self):
        self.assertEqual(get_company_bodies([
            {'clenoveOrganu': [{'datumVymazu': '2024-01-08', 'typAngazma': 'STATUTARNI_ORGAN_CLEN'}]},
        ], CompanyEntityType.GOVERNING_BODY), [
            CompanyEntity(CompanyEntityType.GOVERNING_BODY)
        ])

    def test_members(self):
        self.assertEqual(get_company_bodies([
            {'clenoveOrganu': [
                {'typAngazma': 'STATUTARNI_ORGAN_CLEN'},
                {'typAngazma': 'KONTROLNI_KOMISE_CLEN'},
            ]},
        ], CompanyEntityType.GOVERNING_BODY), [
            CompanyEntity(CompanyEntityType.GOVERNING_BODY, members=[
                Member(MemberRoleType.STATUTORY_BODY_MEMBER),
                Member(MemberRoleType.AUDIT_COMMITTEE_MEMBER),
            ])
        ])

    def test_members_identity(self):
        self.assertEqual(get_company_bodies([
            {'clenoveOrganu': [
                {'typAngazma': 'STATUTARNI_ORGAN_CLEN', 'fyzickaOsoba': {
                    'jmeno': 'DAVE',
                    'prijmeni': 'LISTER',
                }},
                {'typAngazma': 'KONTROLNI_KOMISE_CLEN', 'pravnickaOsoba': {
                    'ico': 42,
                    'obchodniJmeno': 'Hologram',
                }},
            ]},
        ], CompanyEntityType.GOVERNING_BODY), [
            CompanyEntity(CompanyEntityType.GOVERNING_BODY, members=[
                Member(MemberRoleType.STATUTORY_BODY_MEMBER, NaturalPerson(first_name='Dave', last_name='Lister')),
                Member(MemberRoleType.AUDIT_COMMITTEE_MEMBER, LegalPerson('42', 'Hologram')),
            ])
        ])


class GetPartnersTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_partners([], CompanyEntityType.PARTNER), [])

    def test_no_person(self):
        self.assertEqual((get_partners([{}], CompanyEntityType.PARTNER)), [CompanyEntity(CompanyEntityType.PARTNER)])

    def test_deleted(self):
        self.assertEqual(get_partners([
            {'datumVymazu': '2024-01-08', 'spolecnik': [{'osoba': {'typAngazma': 'SPOLECNIK_OSOBA'}}]},
        ], CompanyEntityType.PARTNER), [])

    def test_no_partners(self):
        self.assertEqual(get_partners([
            {'spolecnik': [{'osoba': {'typAngazma': 'SPOLECNIK_OSOBA'}, 'datumVymazu': '2024-01-08'}]},
        ], CompanyEntityType.PARTNER), [
            CompanyEntity(CompanyEntityType.PARTNER)
        ])

    def test_partners(self):
        self.assertEqual(get_partners([
            {'spolecnik': [
                {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA'}},
                {'osoba': {'typAngazma': 'AKCIONAR'}},
                {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA'}, 'datumVymazu': '2024-01-08'},
            ]},
        ], CompanyEntityType.PARTNER), [
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON),
                Member(MemberRoleType.SHAREHOLDER),
            ])
        ])

    def test_partners_identity(self):
        self.assertEqual(get_partners([
            {'spolecnik': [
                {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Dave', 'prijmeni': 'Lister'}}},
                {'osoba': {'typAngazma': 'AKCIONAR'}},
                {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Arnold', 'prijmeni': 'Rimmer'}},
                 'datumVymazu': '2024-01-08'},
            ]},
        ], CompanyEntityType.PARTNER), [
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON, NaturalPerson('Dave', 'Lister')),
                Member(MemberRoleType.SHAREHOLDER)
            ])
        ])

    def test_partners_identity_legal(self):
        self.assertEqual(get_partners([
            {'spolecnik': [
                {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Dave', 'prijmeni': 'Lister'}}},
                {'osoba': {'typAngazma': 'AKCIONAR'}},
                {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'pravnickaOsoba': {'ico': 42,
                                                                               'obchodniJmeno': 'Hologram'}}},
            ]},
        ], CompanyEntityType.PARTNER), [
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON, NaturalPerson('Dave', 'Lister')),
                Member(MemberRoleType.SHAREHOLDER),
                Member(MemberRoleType.PARTNER_PERSON, LegalPerson('42', 'Hologram'))
            ])
        ])


class GetEconomicEntityBasisTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_economic_entity_basis({}), VerifiedCompany(''))

    def test_bussiness_name(self):
        self.assertEqual(get_economic_entity_basis({'obchodniJmeno': 'The Name'}), VerifiedCompany('The Name'))

    def test_address(self):
        self.assertEqual(get_economic_entity_basis({'sidlo': {
            'kodStatu': 'CZ',
            'nazevObce': 'City',
            'nazevCastiObce': 'District',
            'nazevUlice': 'Street',
            'cisloOrientacni': 88,
            'cisloDomovni': 42,
            'psc': 12000
        }}), VerifiedCompany('', 'Street 42/88\n12000 City', 'Street 42/88', 'City', '12000', 'City - District', 'CZ'))

    def test_legal_form(self):
        self.assertEqual(get_economic_entity_basis({'pravniForma': 42}), VerifiedCompany('', legal_form=42))


class GetPublicRegisterTest(TestCase):

    def test_empty(self):
        self.assertEqual(get_public_register({'zaznamy': []}), VerifiedCompanyPublicRegister(''))

    def test_business_name(self):
        self.assertEqual(get_public_register({'zaznamy': [
            {'primarniZaznam': False,
             'obchodniJmeno': [{"hodnota": "CZ.NIC"}],
             },
            {'primarniZaznam': True,
             'obchodniJmeno': [{"hodnota": "CZ.NIC, z.s.p.o."}],
             },
        ]}), VerifiedCompanyPublicRegister('CZ.NIC, z.s.p.o.'))

    def test_address(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'obchodniJmeno': [{"hodnota": "CZ.NIC, z.s.p.o."}],
             'adresy': [{
                'adresa': {
                    'kodStatu': 'CZ',
                    'nazevObce': 'City',
                    'nazevCastiObce': 'District',
                    'nazevUlice': 'Street',
                    'cisloOrientacni': 88,
                    'cisloDomovni': 42,
                    'psc': 12000,
                }
             }]},
        ]})
        ref = VerifiedCompanyPublicRegister(
            'CZ.NIC, z.s.p.o.', 'Street 42/88\n12000 City', 'Street 42/88', 'City', '12000', 'City - District', 'CZ')
        self.assertEqual(company, ref)

    def test_governing_body(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'statutarniOrgany': [{
                'clenoveOrganu': [{
                    'fyzickaOsoba': {
                        'jmeno': 'Dave',
                        'prijmeni': 'Lister'
                    }
                }, {'pravnickaOsoba': {
                        'ico': 42,
                        'obchodniJmeno': 'Red Dwarf'
                    }}]
             }]},
        ]})
        ref = VerifiedCompanyPublicRegister('', company_entities=[
            CompanyEntity(CompanyEntityType.GOVERNING_BODY, members=[
                Member(identity=NaturalPerson('Dave', 'Lister')),
                Member(identity=LegalPerson('42', 'Red Dwarf')),
            ])
        ])
        self.assertEqual(company, ref)

    def test_other_bodies(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'ostatniOrgany': [{
                'clenoveOrganu': [{
                    'fyzickaOsoba': {
                        'jmeno': 'Dave',
                        'prijmeni': 'Lister'
                    }
                }, {'pravnickaOsoba': {
                        'ico': 42,
                        'obchodniJmeno': 'Red Dwarf'
                    }}]
             }]},
        ]})
        ref = VerifiedCompanyPublicRegister('', company_entities=[
            CompanyEntity(CompanyEntityType.OTHER, members=[
                Member(identity=NaturalPerson('Dave', 'Lister')),
                Member(identity=LegalPerson('42', 'Red Dwarf')),
            ])
        ])
        self.assertEqual(company, ref)

    def test_partners(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'spolecnici': [
                {'spolecnik': [
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Dave',
                                                                                 'prijmeni': 'Lister'}}},
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'pravnickaOsoba': {'ico': 42,
                                                                                   'obchodniJmeno': 'Dwarf'}}},
                ]},
                {'spolecnik': [
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Arny',
                                                                                 'prijmeni': 'Rimmer'}}},
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'pravnickaOsoba': {'ico': 40,
                                                                                   'obchodniJmeno': 'Hologram'}}},
                ]},
             ]}
        ]})
        ref = VerifiedCompanyPublicRegister('', company_entities=[
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON, identity=NaturalPerson('Dave', 'Lister')),
                Member(MemberRoleType.PARTNER_PERSON, identity=LegalPerson('42', 'Dwarf'))
            ]),
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON, identity=NaturalPerson('Arny', 'Rimmer')),
                Member(MemberRoleType.PARTNER_PERSON, identity=LegalPerson('40', 'Hologram'))
            ])],
            legal_form=None)
        self.assertEqual(company, ref)

    def test_partners_no_persons(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'spolecnici': [
                {'spolecnik': [
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Dave',
                                                                                 'prijmeni': 'Lister'}}},
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'pravnickaOsoba': {'ico': 42,
                                                                                   'obchodniJmeno': 'Dwarf'}}},
                ]},
                {'spolecnik': [{}]},
             ]}
        ]})
        ref = VerifiedCompanyPublicRegister('', company_entities=[
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON, identity=NaturalPerson('Dave', 'Lister')),
                Member(MemberRoleType.PARTNER_PERSON, identity=LegalPerson('42', 'Dwarf'))
            ]),
            CompanyEntity(CompanyEntityType.PARTNER, members=[])],
            legal_form=None)
        self.assertEqual(company, ref)

    def test_partners_deleted_person(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'spolecnici': [
                {'spolecnik': [
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'fyzickaOsoba': {'jmeno': 'Dave',
                                                                                 'prijmeni': 'Lister'}}},
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'pravnickaOsoba': {'ico': 42,
                                                                                   'obchodniJmeno': 'Dwarf'}}},
                ]},
                {'spolecnik': [
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'datumVymazu': '2024-01-09', 'fyzickaOsoba': {
                        'jmeno': 'Arny', 'prijmeni': 'Rimmer'}}},
                    {'osoba': {'typAngazma': 'SPOLECNIK_OSOBA', 'pravnickaOsoba': {'ico': 40,
                                                                                   'obchodniJmeno': 'Hologram'}}},
                ]},
             ]}
        ]})
        ref = VerifiedCompanyPublicRegister('', company_entities=[
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON, identity=NaturalPerson('Dave', 'Lister')),
                Member(MemberRoleType.PARTNER_PERSON, identity=LegalPerson('42', 'Dwarf'))
            ]),
            CompanyEntity(CompanyEntityType.PARTNER, members=[
                Member(MemberRoleType.PARTNER_PERSON),
                Member(MemberRoleType.PARTNER_PERSON, identity=LegalPerson('40', 'Hologram'))
            ])],
            legal_form=None)
        self.assertEqual(company, ref)

    def test_legal_form(self):
        company = get_public_register({'zaznamy': [
            {'primarniZaznam': True,
             'pravniForma': [
                 {"hodnota": 42}
             ]}
        ]})
        self.assertEqual(company, VerifiedCompanyPublicRegister('', legal_form=42))


class GetMemberRoleTypeTest(TestCase):

    def test_none(self):
        self.assertIsNone(get_member_role_type(None))

    def test_value(self):
        self.assertEqual(get_member_role_type('SPOLECNIK_OSOBA'), MemberRoleType.PARTNER_PERSON)

    def test_unknown_value(self):
        self.assertEqual(get_member_role_type('FOO'), 'FOO')
