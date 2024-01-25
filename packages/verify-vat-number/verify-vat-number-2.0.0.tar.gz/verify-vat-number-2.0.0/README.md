# Verify VAT registration number

The module for verification *VAT registration number* in EU and *VAT identification number* in Czechia. This module is used in the [Django Verify VAT registration number](https://gitlab.nic.cz/django-apps/django-verify-vat-number) module and then in the [DjangoCMS Verify VAT registration number](https://gitlab.nic.cz/djangocms-apps/djangocms-verify-vat-number) module.


## VIES

[VIES VAT number validation for European union](https://ec.europa.eu/taxation_customs/vies). It is an electronic mean of validating VAT-identification numbers of economic operators registered in the European Union for cross border transactions on goods or services.

Supported countries:

    AT - Austria
    BE - Belgium
    BG - Bulgaria
    CY - Cyprus
    CZ - Czechia
    DE - Germany
    DK - Denmark
    EE - Estonia
    EL - Greece
    ES - Spain
    FI - Finland
    FR - France
    HR - Croatia
    HU - Hungary
    IE - Ireland
    IT - Italy
    LT - Lithuania
    LU - Luxembourg
    LV - Latvia
    MT - Malta
    NL - The Netherlands
    PL - Poland
    PT - Portugal
    RO - Romania
    SE - Sweden
    SI - Slovenia
    SK - Slovakia
    XI - Northern Ireland

## ARES

[ARES](https://ares.gov.cz/) - Access to Registers of Economic Subjects / Entities is an information system allowing a retrieval of information on economic entities registered in the Czech Republic. This system intermediates a display of data from particular registers of the state administration (called source registers) in which the data concerned is kept.


## Installation

This library is available on PyPI, it's recommended to install it using `pip`:

```shell
pip install verify-vat-number
```

## Usage

```python
from verify_vat_number.ares import get_from_cz_ares
from verify_vat_number.vies import get_from_eu_vies
from verify_vat_number.exceptions import VatNotFound, VerifyVatException, UnsupportedCountryCode

def dump_reg(vat):
    print('\nVAT-REG-NUM:', vat)
    try:
        data = get_from_eu_vies(vat)
    except VatNotFound:
        print("VAT not found for", vat)
    except UnsupportedCountryCode as err:
        print("Unsupported country code:", err)
    except VerifyVatException as err:
        print(err)
        print(err.source)
    else:
        print(data)

def dump_vid(ic):
    print('\nVAT-ID-NUM:', ic)
    try:
        data = get_from_cz_ares(ic)
    except VatNotFound:
        print("IC not found for", ic)
    except VerifyVatException as err:
        print(err)
        print(err.source)
    else:
        print(data)


for vat in ("CZ67985726", "DE306401413", "SK2020317068", "CZ67985728", "BE0404616494", "BE0400853488", "BG127015636", "XX67985726"):
    dump_reg(vat)

for ic in ("67985726", "67985728", "456456456"):
    dump_vid(ic)
```

```shell
VAT-REG-NUM: CZ67985726
VerifiedCompany(
    company_name='CZ.NIC, z.s.p.o.',
    address='Milešovská 1136/5\nPRAHA 3 - VINOHRADY\n130 00  PRAHA 3',
    street_and_num='Milešovská 1136/5',
    city='PRAHA 3',
    postal_code='130 00',
    district='PRAHA 3 - VINOHRADY',
    country_code='CZ',
    legal_form=None
)

VAT-REG-NUM: DE306401413
VerifiedCompany(
    company_name='',
    address=None,
    street_and_num=None,
    city=None,
    postal_code=None,
    district=None,
    country=None,
    legal_form=None
)

VAT-REG-NUM: SK2020317068
VerifiedCompany(
    company_name='ESET, spol. s r.o.',
    address='Einsteinova 24\n85101 Bratislava - mestská časť Petržalka\nSlovensko',
    street_and_num='Einsteinova 24',
    city='Bratislava - mestská časť Petržalka',
    postal_code='85101',
    district=None,
    country_code='SK',
    legal_form=None
)

VAT-REG-NUM: CZ67985728
VAT not found for CZ67985728

VAT-REG-NUM: BE0404616494
VerifiedCompany(
    company_name='NV ACKERMANS & VAN HAAREN',
    address='Begijnenvest 113\n2000 Antwerpen',
    street_and_num='Begijnenvest 113',
    city='Antwerpen',
    postal_code='2000',
    district=None,
    country_code='BE',
    legal_form=None
)

VAT-REG-NUM: BE0400853488
VerifiedCompany(
    company_name='NV BRUSSELS AIRLINES',
    address='Ringbaan 26\n1831 Machelen (Brab.)',
    street_and_num='Ringbaan 26',
    city='Machelen (Brab.)',
    postal_code='1831',
    district=None,
    country_code='BE',
    legal_form=None
)

VAT-REG-NUM: BG127015636
VerifiedCompany(
    company_name='КАРЛСБЕРГ БЪЛГАРИЯ - АД',
    address='жк МЛАДОСТ 4БИЗНЕС ПАРК СОФИЯ  №1 бл.сграда 10 ет.4 обл.СОФИЯ, гр.СОФИЯ 1715',
    street_and_num='жк МЛАДОСТ 4БИЗНЕС ПАРК СОФИЯ  №1 бл.сграда 10 ет.4 обл.СОФИЯ',
    city='гр.СОФИЯ',
    postal_code='1715',
    district=None,
    country_code='BG',
    legal_form=None
)

VAT-REG-NUM: XX67985726
Unsupported country code: XX

VAT-ID-NUM: 67985726
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

VAT-ID-NUM: 67985728
IC not found for 67985728

VAT-ID-NUM: 456456456
The number cannot be more than 8 digits long.
None
```

Work with logging:

```python
import sys
import logging
from verify_vat_number.ares import get_from_cz_ares
from verify_vat_number.vies import get_from_eu_vies
from verify_vat_number.exceptions import VatNotFound

logger = logging.getLogger('verify_vat_number.vies')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

get_from_eu_vies("CZ67985726")
```

```shell
https://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl Country code: CZ VAT: 67985726

<ns0:Envelope
    xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ns1="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
    <ns0:Body>
        <ns1:checkVat>
            <ns1:countryCode>CZ</ns1:countryCode>
            <ns1:vatNumber>67985726</ns1:vatNumber>
        </ns1:checkVat>
    </ns0:Body>
</ns0:Envelope>

<ns0:Envelope
    xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ns1="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
    <ns0:Body>
        <ns1:checkVatResponse>
            <ns1:countryCode>CZ</ns1:countryCode>
            <ns1:vatNumber>67985726</ns1:vatNumber>
            <ns1:requestDate>2022-05-20+02:00</ns1:requestDate>
            <ns1:valid>true</ns1:valid>
            <ns1:name>CZ.NIC, z.s.p.o.</ns1:name>
            <ns1:address>Milešovská 1136/5
PRAHA 3 - VINOHRADY
130 00  PRAHA 3</ns1:address>
        </ns1:checkVatResponse>
    </ns0:Body>
</ns0:Envelope>

VerifiedCompany(
    company_name='CZ.NIC, z.s.p.o.',
    address='Milešovská 1136/5\n13000 Praha 3',
    street_and_num='Milešovská 1136/5',
    city='Praha 3',
    postal_code='13000',
    district='Praha 3 - Vinohrady',
    country_code='CZ',
    legal_form=None
)
```

```python
logger = logging.getLogger('verify_vat_number.ares')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

try:
    get_from_cz_ares("67985728")
except VatNotFound:
    print('VAT not found.')
```

```shell
https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/67985728/
VAT not found.
```

### Multiple ARES output: Economic entity / Public registry

The `get_from_cz_ares` function is an umbrella function for individual registers.
It currently covers the Economic entity (`get_from_cz_ares_ee`) and the Public registry (`get_from_cz_ares_vr`).
The default is the Economic entity. Data from the Public registry is returned using the `register_type` attribute with the value `RegisterType.PUBLIC_REGISTER`.
The Public registry contains information about owners and members of notable governing bodies.

```python
from verify_vat_number.ares import get_from_cz_ares, get_from_cz_ares_vr, RegisterType

get_from_cz_ares("67985726", RegisterType.PUBLIC_REGISTER)
# or
get_from_cz_ares_vr("67985726")


VerifiedCompanyPublicRegister(
    company_name='CZ.NIC, z.s.p.o.',
    address='Milešovská 1136/5\n13000 Praha 3',
    street_and_num='Milešovská 1136/5', city='Praha 3',
    postal_code='13000', district='Praha 3 - Vinohrady',
    country_code='CZ',
    company_entities=[
        CompanyEntity(
            entity_type=<CompanyEntityType.GOVERNING_BODY: 'Statutární orgán'>,
            name='Statutární orgán - Představenstvo',
            members=[
                Member(
                    role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Josef',
                        last_name='Novák',
                        date_of_birth=datetime.date(1992, 11, 8))),
                Member(
                    role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Jana',
                        last_name='Novotná',
                        date_of_birth=datetime.date(1962, 9, 17))),
                Member(
                    role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Karel',
                        last_name='Svoboda',
                        date_of_birth=datetime.date(1981, 12, 3))),
                Member(
                    role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Hana',
                        last_name='Horáková',
                        date_of_birth=datetime.date(1974, 4, 12))),
                Member(
                    role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Jiří',
                        last_name='Dvořák',
                        date_of_birth=datetime.date(1978, 6, 21)))
        ]),
        CompanyEntity(
            entity_type=<CompanyEntityType.OTHER: 'Jiný orgán'>,
            name='Kontrolní orgán - Dozorčí rada',
            members=[
                Member(
                    role=<MemberRoleType.AUDIT_COMMITTEE_MEMBER: 'KONTROLNI_KOMISE_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Eva',
                        last_name='Kopecká',
                        date_of_birth=datetime.date(1982, 8, 12))),
                Member(
                    role=<MemberRoleType.AUDIT_COMMITTEE_MEMBER: 'KONTROLNI_KOMISE_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Milan',
                        last_name='Dostál',
                        date_of_birth=datetime.date(1985, 7, 10))),
                Member(
                    role=<MemberRoleType.AUDIT_COMMITTEE_MEMBER: 'KONTROLNI_KOMISE_CLEN'>,
                    identity=NaturalPerson(
                        first_name='Jan',
                        last_name='Beneš',
                        date_of_birth=datetime.date(1952, 11, 12)))
        ])
    ],
    legal_form=751
)
```

### ARES - various registry

ARES data are drawn from a variety of sources. Currently two are implemented:

 - Economic entities
 - Public register

Economic entities are obtained by the function `get_from_cz_ares_ee(VAT)`, which is the same as calling the function
`get_from_cz_ares(VAT)`.
Data from Public register are given by the function `get_from_cz_ares_vr(VAT)`, which is almost same as calling the function
`get_from_cz_ares(VAT, RegisterType.PUBLIC_REGISTER)`. The difference is that if the data is not found in the Public Register,
the data is returned from the default register Economic entities.
Thus, the `get_from_cz_ares_ee` function may raise a `VatNotFound` exception, while the `get_from_cz_ares` function will return a record of the company, but of course, without entities.

### ARES - Lowercase names of persons in entities

Unfortunately, ARES Public register returns the names of people with capital letters. The program converts them back to lower case.
If you wish to keep the original data, you can disable this conversion with the `ARES_KEEP_CASE` environment variable.

```
python -c 'from verify_vat_number.ares import get_from_cz_ares_vr;print(get_from_cz_ares_vr("67985726"))'
```

```python
VerifiedCompanyPublicRegister(
    company_name='CZ.NIC, z.s.p.o.',
    ...
    company_entities=[
        CompanyEntity(entity_type=<CompanyEntityType.GOVERNING_BODY: 'Statutární orgán'>, name='Statutární orgán',
        members=[
            Member(
                role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                identity=NaturalPerson(first_name='Josef', last_name='Novák', ...)),
        ...
    ...
)
```

```
ARES_KEEP_CASE=y python -c 'from verify_vat_number.ares import get_from_cz_ares_vr;print(get_from_cz_ares_vr("67985726"))'
```

```python
VerifiedCompanyPublicRegister(
    company_name='CZ.NIC, z.s.p.o.',
    ...
    company_entities=[
        CompanyEntity(entity_type=<CompanyEntityType.GOVERNING_BODY: 'Statutární orgán'>, name='Statutární orgán',
        members=[
            Member(
                role=<MemberRoleType.STATUTORY_BODY_MEMBER: 'STATUTARNI_ORGAN_CLEN'>,
                identity=NaturalPerson(first_name='JOSEF', last_name='NOVÁK', ...)),
        ...
    ...
)
```

## License

[GPLv3+](https://www.gnu.org/licenses/gpl-3.0.html)
