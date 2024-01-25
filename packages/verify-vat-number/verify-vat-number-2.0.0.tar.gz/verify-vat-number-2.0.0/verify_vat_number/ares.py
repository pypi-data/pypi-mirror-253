"""
Load data from ARES at https://ares.gov.cz/.

https://ares.gov.cz/stranky/vyvojar-info
    ARES - Technická dokumentace Katalog veřejných služeb v 1.0
    https://www.mfcr.cz/assets/attachments/2023-08-01_ARES-Technicka-dokumentace-Katalog-verejnych-sluzeb_v05.pdf
"""
import logging
import os
from typing import Any, Dict, List, Optional, Union, cast

import requests

from .data import (CompanyEntity, CompanyEntityType, LegalPerson, Member, MemberRoleType, NaturalPerson, RegisterType,
                   VerifiedCompany, VerifiedCompanyPublicRegister)
from .exceptions import (InvalidVatNumber, ServiceTemporarilyUnavailable, UnexpectedResponseFormat, VatNotFound,
                         VerifyVatException)
from .utils import (is_deletion_date, join_by_separator, make_lower_with_capital, only_str, parse_date,
                    strip_vat_id_number, value_to_str)

JsonData = Dict[str, Any]
JsonItem = Optional[Union[str, int, JsonData]]


SERVICE_API_URL = 'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest'
ECONOMIC_ENTITY = 'ekonomicke-subjekty'
PUBLIC_REGISTER = 'ekonomicke-subjekty-vr'

LOGGER = logging.getLogger(__name__)


def get_from_cz_ares_ee(vat_ident_number: str) -> VerifiedCompany:
    """
    Verify VAT identifier number via ARES Basic register (Economic Entities).

    Return data about company such as name and address.
    """
    url = f'{SERVICE_API_URL}/{ECONOMIC_ENTITY}/{parse_vat_ident_number(vat_ident_number)}/'
    return get_economic_entity_basis(get_response_json(url))


def get_from_cz_ares_vr(vat_ident_number: str) -> VerifiedCompanyPublicRegister:
    """Verify VAT identifier number via ARES Public register. Return data about company and entities."""
    url = f'{SERVICE_API_URL}/{PUBLIC_REGISTER}/{parse_vat_ident_number(vat_ident_number)}/'
    return get_public_register(get_response_json(url))


def get_from_cz_ares(
        vat_ident_number: str,
        register_type: Optional[RegisterType] = None
) -> Union[VerifiedCompany, VerifiedCompanyPublicRegister]:
    """
    Verify VAT identifier number via ARES Basic or Public register.

    Return data about company such as name and address. With parse_entities return company entities.
    """
    if register_type == RegisterType.PUBLIC_REGISTER:
        try:
            return get_from_cz_ares_vr(vat_ident_number)
        except VatNotFound:
            pass
    return get_from_cz_ares_ee(vat_ident_number)


def parse_vat_ident_number(vat_ident_number: str) -> str:
    """Parse VAT Ident number."""
    vat_ident_number = strip_vat_id_number(vat_ident_number)
    if vat_ident_number == '':
        raise InvalidVatNumber('Invalid number format.')
    if len(vat_ident_number) > 8:
        raise InvalidVatNumber('The number cannot be more than 8 digits long.')
    return vat_ident_number


def get_response_json(service_url: str) -> JsonData:
    """Get json from ARES."""
    LOGGER.info(service_url)
    try:
        response = requests.get(service_url)
    except requests.exceptions.Timeout as err:
        raise ServiceTemporarilyUnavailable(err)
    except requests.exceptions.RequestException as err:
        source = err.response.content if err.response else b''
        raise VerifyVatException(err, source=source)
    if not response.ok:
        if response.status_code == 404:
            raise VatNotFound(source=response.content)
        if response.status_code == 400:
            raise InvalidVatNumber("Input error", source=response.content)
        raise VerifyVatException(f'[{response.status_code}] {response.reason}', source=response.content)
    LOGGER.debug(response.content.decode('UTF-8'))
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError as err:
        raise VerifyVatException(err, source=response.content)


def get_economic_entity_basis(source: JsonData) -> VerifiedCompany:
    """Map source to VerifiedCompany.

    Administrativní registr ekonomických subjektů.

    3.10.1. EkonomickySubjektZaklad
    - datumAktualizace  Datum_T                   [1] Datum aktualizace záznamu
    - datumVzniku       Datum_T                [0..1] Datum vzniku ekonomického subjektu
    - datumZaniku       Datum_T                [0..1] Datum zániku ekonomického subjektu
    - dic               SubjektDIC_T           [0..1] Daňové identifikační číslo ve formátu CZNNNNNNNNNN
    - financniUrad      KodFinancniUrad_T      [0..1] Správně příslušný finanční úřad – kód
                                                      (ciselnikKod: FinancniUrad, zdroj:ufo)
    - ico               Ico_T                  [0..1] Identifikační číslo osoby - IČO
    - obchodniJmeno     SubjektObchodniJmeno_T [0..1] Obchodní jméno ekonomického subjektu
    - pravniForma       KodPravniForma_T       [0..1] Právní forma – kód (ciselnikKod: PravniForma, zdroj: res, com)
    - sidlo             Adresa                 [0..1] Sídlo ekonomického subjektu
    """
    data = VerifiedCompany(company_name=str(source.get('obchodniJmeno', '')))
    map_address(data, source.get('sidlo'))
    if (legal_form := source.get("pravniForma")):
        data.legal_form = int(legal_form)
    return data


def get_public_register(source: JsonData) -> VerifiedCompanyPublicRegister:
    """Map source to VerifiedCompany.

    Veřejný rejstřík (VR), vedený rejstříkovými soudy.

    3.1.40. ZaznamVrZaklad
    - adresy                AdresaVr            [0..*] Sídlo firmy
    - akcie                 EmiseAkcieVr        [0..*] Údaje popisující vlastnosti konkrétní akcie
    - cinnosti              CinnostiVr          [0..1] Předmět podnikání, předmět činnosti, účel
    - datumAktualizace      Datum_T                [1] Datum aktualizace
    - datumVymazu           Datum_T             [0..1] Datum výmazu subjektu z VR
    - datumVzniku           DatumVr             [0..*] Datum vzniku
    - datumZapisu           Datum_T             [0..1] Datum zápisu subjektu do VR
    - exekuce               ObecnyTextVr        [0..*] Exekuce
    - financniUrad          KodFinancniUrad_T   [0..1] Finanční úřad – kód (ciselnikKod: FinancniUrad, zdroj: ufo)
    - ico                   IcoVr               [0..*] IČO
    - kategorieZO           KategorieZoVr       [0..*] Kategorie zahraniční osoby
    - nazevNejvyssihoOrganu ObecnyTextVr        [0..*] Název nejvyššího řídícího orgánu
    - obchodniJmeno         ObchodniJmenoVr     [0..*] Obchodní jméno firmy
    - obchodniJmenoCizi     ObchodniJmenoCiziVr [0..*] Obchodní jméno firmy - zahraniční
    - ostatniSkutecnosti    ObecnyTextVr        [0..*] Ostatní skutečnosti
    - pravniDuvodVymazu     ObecnyTextVr        [0..*] Právní důvod výmazu subjektu z VR
    - pravniForma           PravniFormaVr       [0..*] Právní forma - ROS
    - primarniZaznam        boolean                [1] Primární záznam

    3.1.17. ZaznamVr (ZaznamVrZaklad)
    - insolvence            InsolvencniRizeniVr [0..*] Konktétní zápis insolvenčního řízení nad daným subjektem
    - konkursy              KonkursVr           [0..*] Údaj s informací z konkurzního řízení podle zákona 328/1991Sb.
    - odstepneZavody        OdstepnyZavodVr     [0..*] Základní informace o odštěpných závodech daného subjektu
    - ostatniOrgany         OrganVr             [0..*]
    - podnikatel            PodnikatelVr        [0..*]
    - spolecnici            SpolecniciVr        [0..*]
    - statutarniOrgany      StatutarniOrganVr   [0..*]

    3.1.16. EkonomickySubjektVr
    - icoId                 IcoId_T                [1] ičo/id ekonomického subjektu
    - zaznamy               ZaznamVr            [1..*] Seznam záznamů daného iča

    3.1.23. DatumZapisuVymazuUdajeVr
    - datumVymazu           Datum_T             [0..1] Datum výmazu údaje
    - datumZapisu           Datum_T                [1] Datum zápisu údaje

    3.1.43. ObchodniJmenoVr (DatumZapisuVymazuUdajeVr)
    - hodnota SubjektObchodniJmeno_T [0..1] Hodnota obchodního jména
    """
    company = VerifiedCompanyPublicRegister(company_name='')
    for record in source['zaznamy']:
        if not record['primarniZaznam']:
            continue
        company.company_name = value_to_str(get_active_record(record.get('obchodniJmeno', [])))
        map_address(company, get_active_record(record.get('adresy', []), 'adresa'))
        company.company_entities.extend(
            get_company_bodies(record.get('statutarniOrgany', []), CompanyEntityType.GOVERNING_BODY)
        )
        company.company_entities.extend(get_company_bodies(record.get('ostatniOrgany', []), CompanyEntityType.OTHER))
        company.company_entities.extend(get_partners(record.get('spolecnici', []), CompanyEntityType.PARTNER))
        if (legal_form := get_active_record(record.get("pravniForma", []))):
            company.legal_form = int(cast(str, legal_form))
    return company


def get_active_record(data: List[JsonData], key: str = 'hodnota') -> JsonItem:
    """Get active record by key."""
    for item in data:
        if is_deletion_date(item.get('datumVymazu')):
            continue
        return item.get(key)
    return None


def map_address(company: VerifiedCompany, address: JsonItem) -> None:
    """Map address.

    3.10.2. / 3.1.1. Adresa
    - cisloDoAdresy            CisloDoAdresy_T          [0..1] Nestrukturované číslo/a použíté v adrese
    - cisloDomovni             CisloDomovni_T           [0..1] Číslo domovní
    - cisloOrientacni          CisloOrientacni_T        [0..1] Číslo orientační - číselná část
    - cisloOrientacniPismeno   CisloOrientacniPismeno_T [0..1] Číslo orientační - písmenná část
    - doplnekAdresy            AdresaTxt_T              [0..1] Doplňující informace adresního popisu
    - kodAdresnihoMista        KodPrvkuRuian9_T         [0..1] Kód adresního místa
    - kodCastiObce             KodPrvkuRuian6_T         [0..1] Kód časti obce
    - kodKraje                 KodPrvkuRuian3_T         [0..1] Kód kraje
    - kodMestskeCastiObvodu    KodPrvkuRuian6_T         [0..1] Kód městské části statutárního města
    - kodMestskehoObvodu       KodPrvkuRuian3_T         [0..1] Kód městského obvodu Prahy
    - kodObce                  KodPrvkuRuian6_T         [0..1] Kód obce
    - kodOkresu                KodPrvkuRuian4_T         [0..1] Kód okresu
    - kodSpravnihoObvodu       KodPrvkuRuian3_T         [0..1] Kód správního obvodu Prahy
    - kodStatu                 KodStatu_T               [0..1] Kód státu (ciselnikKod: Stat)
    - kodUlice                 KodPrvkuRuian7_T         [0..1] Kód ulice, veřejného prostranství ze zdroje
    - nazevCastiObce           NazevPrvkuRuian48_T      [0..1] Název části obce
    - nazevKraje               NazevPrvkuRuian32_T      [0..1] Název kraje
    - nazevMestskeCastiObvodu  NazevPrvkuRuian48_T      [0..1] Název městské části statutárního města
    - nazevMestskehoObvodu     NazevPrvkuRuian32_T      [0..1] Název městského obvodu Prahy
    - nazevObce                NazevPrvkuRuian48_T      [0..1] Název obce
    - nazevOkresu              NazevPrvkuRuian32_T      [0..1] Název okresu
    - nazevSpravnihoObvodu     NazevPrvkuRuian32_T      [0..1] Název správního obvodu Prahy
    - nazevStatu               NazevStatu_T             [0..1] Název státu
    - nazevUlice               NazevPrvkuRuian48_T      [0..1] Název ulice, veřejného prostranství
    - psc                      Psc_T                    [0..1] Poštovní směrovací číslo adresní pošty
    - pscTxt                   PscTxt_T                 [0..1] Psč zahraničních definovaných čísel
    - standardizaceAdresy      boolean                  [0..1] Stav standardizace adresy dle RÚIAN
    - textovaAdresa            AdresaTxt_T              [0..1] Nestrukturovaná adresa (formátovaná adresa)
    - typCisloDomovni          KodCiselnikuDefault_T    [0..1] Typ čísla domu nebo nestandardně
                                                               (ciselnikKod: TypCislaDomovniho)
    """
    if address is None:
        return
    if isinstance(address,  (str, int)):
        raise UnexpectedResponseFormat('map_address', source=str(address))

    company.country_code = address.get('kodStatu')
    company.city = address.get('nazevObce')

    # Extension for Prague:
    if company.city == 'Praha':
        if (city_district := address.get('nazevMestskehoObvodu')):
            company.city = city_district

    # Include city name into the district due to compatibility with VIES.
    district = address.get("nazevCastiObce")
    if company.city is not None and company.city in str(district):
        company.district = district
    else:
        company.district = join_by_separator(' - ', (company.city, district))  # District does not include city name.

    street_name = address.get('nazevUlice')
    street_numbers = join_by_separator("/", (address.get('cisloDomovni'), address.get('cisloOrientacni')))
    company.street_and_num = join_by_separator(' ', (street_name, street_numbers)) if street_numbers else street_name
    company.postal_code = address.get('psc')
    if company.postal_code is not None:
        company.postal_code = str(company.postal_code)
    city_pc = join_by_separator(" ", (company.postal_code, company.city)) if company.postal_code else company.city
    company.address = join_by_separator('\n', (company.street_and_num, city_pc))


def get_natural_person(data: JsonData) -> NaturalPerson:
    """Parse natural person.

    3.1.32. OsobaVr
    - adresa          Adresa            [0..1] Primární adresa dané osoby (u fyzické pobyt, u právnické sídlo)
    - textOsoba       Text_T            [0..1] Doplňková informace k osobě
    - textOsobaDo     Datum_T           [0..1] Platnost doplňkové informace o osobě od data
    - textOsobaOd     Datum_T           [0..1] Platnost doplňkové informace o osobě od data

    3.1.25. FyzickaOsobaVr (OsobaVr)
    - bydliste        Adresa            [0..1] Adresa bydliště fyzické osoby
    - datumNarozeni   Datum_T           [0..1] Datum narození
    - jmeno           JmenoOsoby_T      [0..1] Jméno
    - prijmeni        PrijmeniOsoby_T   [0..1] Příjmení
    - statniObcanstvi KodStatu_T        [0..1] Státní občanství osoby – kod (ciselnikKod: Stat)
    - titulPredJmenem TitulPredJmenem_T [0..1] Titul před jménem
    - titulZaJmenem   TitulZaJmenem_T   [0..1] Titul za jménem
    """
    str_formater = (lambda t: t) if os.environ.get('ARES_KEEP_CASE') else make_lower_with_capital  # noqa: E731
    return NaturalPerson(
        str_formater(data.get('jmeno')),
        str_formater(data.get('prijmeni')),
        parse_date(data.get('datumNarozeni')),
    )


def get_legal_person(data: JsonData) -> LegalPerson:
    """Parse legal person.

    3.1.10. PravnickaOsobaVr (OsobaVr)
    - ico           Ico_T                   [0..1] Idenitifikační číslo právnické osoby
    - obchodniJmeno SubjektObchodniJmeno_T  [0..1] Název právnické osoby
    - pravniForma   KodPravniForma_T        [0..1] Právní forma – kód (ciselnikKod: PravniForma, zdroj: res, com)
    - zastoupeni    AngazmaFyzickaOsobaVr   [0..*] Zastoupení právnické osoby
    """
    return LegalPerson(
        only_str(data.get('ico')),
        data.get('obchodniJmeno'),
        get_representatives(data.get('zastoupeni', []))
    )


def get_representatives(representatives: List[JsonData]) -> List[NaturalPerson]:
    """Map natural person engagement.

    3.1.3. AngazmaFyzickaOsobaVr (DatumZapisuVymazuUdajeVr)
    - clenstvi      AngazmaClenstviVr [0..1] Členství
    - fyzickaOsoba  FyzickaOsobaVr    [0..1] Fyzická osoba
    - nazevAngazma  Text255_T         [0..1] Název angažmá - nestandardní
    - typAngazma    KodAngazmaAres_T     [1] Typ angažmá - kód (ciselnikKod: TypAngazma, zdroj: vr)
    - datumZapisu   Datum_T           [0..1] Datum zápisu údaje
    - datumVymazu   Datum_T           [0..1] Datum výmazu údaje
    """
    persons = []
    for member in representatives:
        if is_deletion_date(member.get('datumVymazu')):
            continue
        if (natural_person := member.get('fyzickaOsoba')):
            persons.append(get_natural_person(natural_person))
    return persons


def get_member_role_type(code: Optional[str]) -> Optional[Union[MemberRoleType, str]]:
    """Set Member MemberRoleType."""
    if code is None:
        return code
    try:
        return MemberRoleType(code)
    except ValueError:
        return code


def get_company_bodies(records: List[JsonData], entity_type: CompanyEntityType) -> List[CompanyEntity]:
    """Map statutory bodies.

    3.1.8. OrganVr (DatumZapisuVymazuUdajeVr)
    - clenoveOrganu AngazmaOsobaVr   [0..*] nazevAngazma Text255_T [0..1] Název orgánu - nestandardní
    - nazevOrganu   Text255_T        [0..1] Název orgánu - nestandardní
    - pocetClenu    PocetClenuVr     [0..*] typAngazma KodAngazmaAres_T [1] Typ orgánu – kód
                                            (ciselnikKod: TypOrganu, zdroj: vr)
    - typOrganu     KodAngazmaAres_T    [1] Typ orgánu - kód (ciselnikKod: TypOrganu, zdroj: vr)
                                            Typ angažmá - kód (ciselnikKod: TypAngazma, zdroj: vr)

    3.1.14. StatutarniOrganVr (OrganVr)
    - zpusobJednani  ObecnyTextVr    [0..*] Způsob jednání statutárního orgánu
    """
    entities = []
    for data in records:
        if is_deletion_date(data.get('datumVymazu')):
            continue
        members = []
        for member in data.get('clenoveOrganu', []):
            if is_deletion_date(member.get('datumVymazu')):
                continue
            entity_member = Member(get_member_role_type(member.get('typAngazma')), None)
            if (natural_person := member.get('fyzickaOsoba')):
                entity_member.identity = get_natural_person(natural_person)
            elif (legal_person := member.get('pravnickaOsoba')):
                entity_member.identity = get_legal_person(legal_person)
            members.append(entity_member)
        entities.append(CompanyEntity(
            entity_type,
            data.get('nazevAngazma'),
            members,
        ))
    return entities


def get_partners(partnersData: List[JsonData], entity_type: CompanyEntityType) -> List[CompanyEntity]:
    """Map company partners.

    3.1.11. SpolecniciVr (DatumZapisuVymazuUdajeVr)
    - nazev             Text255_T         [0..1] Název orgánu - nestandardní
    - nazevOrganu       Text255_T         [0..1] Název orgánu - nestandardní
    - spolecnik         SpolecnikVr       [0..*] spolecnyPodil SpolecnyPodilVr [0..*] Společný podíl společníků
    - typOrganu         KodAngazmaAres_T     [1] Typ orgánu – kód (ciselnikKod: TypOrganu, zdroj: vr)
    - uvolnenyPodil     UvolnenyPodilVr   [0..*]

    3.1.12. SpolecnikVr (DatumZapisuVymazuUdajeVr)
    - osoba             AngazmaOsobaVr    [0..1]
    - podil             PodilVr           [0..1]

    3.1.4. AngazmaOsobaVr (DatumZapisuVymazuUdajeVr)
    - clenstvi          AngazmaClenstviVr [0..1] Členství
    - fyzickaOsoba      FyzickaOsobaVr    [0..1] Fyzická osoba
    - nazevAngazma      Text255_T         [0..1] Název angažmá - nestandardní
    - pravnickaOsoba    PravnickaOsobaVr  [0..1] Právnická osoba
    - skrytyUdaj        ObecnyTextVr      [0..1] Skrytý údaj
    - typAngazma        KodAngazmaAres_T     [1] Typ angažmá - kód (ciselnikKod: TypAngazma, zdroj: vr)
    """
    entities = []
    for data in partnersData:
        if is_deletion_date(data.get('datumVymazu')):
            continue
        partnets = []
        for partner in data.get('spolecnik', []):
            if is_deletion_date(partner.get('datumVymazu')):
                continue
            if (person := partner.get('osoba')):
                entity_partner = Member(get_member_role_type(person['typAngazma']))
                if not is_deletion_date(person.get('datumVymazu')):
                    if (natural_person := person.get('fyzickaOsoba')):
                        entity_partner.identity = get_natural_person(natural_person)
                    elif (legal_person := person.get('pravnickaOsoba')):
                        entity_partner.identity = get_legal_person(legal_person)
                partnets.append(entity_partner)
        entities.append(CompanyEntity(
            entity_type,
            data.get('nazevOrganu'),
            partnets,
        ))
    return entities
