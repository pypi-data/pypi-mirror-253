"""Dataclass VerifiedCompany with verified values."""
from dataclasses import dataclass, field
from datetime import date
from enum import Enum, unique
from typing import List, Optional, Union


@unique
class CompanyEntityType(str, Enum):
    """Specific to cz and ARES declarations."""

    GOVERNING_BODY = "Statutární orgán"
    OTHER = "Jiný orgán"
    PARTNER = "Společnici"


@unique
class MemberRoleType(str, Enum):
    """ARES member role type."""

    SHAREHOLDER = "AKCIONAR"
    SUPERVISORY_BOARD_MEMBER = "DOZORCI_RADA_CLEN"
    AUDIT_COMMITTEE_MEMBER = "KONTROLNI_KOMISE_CLEN"
    LIQUIDATOR_PERSON_VR = "LIKVIDATOR_OSOBA_VR"
    ATTORNEY_PERSON = "PROKURA_OSOBA"
    PARTNER_PERSON = "SPOLECNIK_OSOBA"
    STATUTORY_BODY_MEMBER = "STATUTARNI_ORGAN_CLEN"


@unique
class RegisterType(Enum):
    """ARES Register type."""

    ECONOMIC_ENTITY = 'ECONOMIC'
    PUBLIC_REGISTER = 'PUBLIC'


@dataclass
class NaturalPerson:
    """Structure representing a natural person, are:TypFyzickaOsoba."""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None


@dataclass
class LegalPerson:
    """Structure representing a legal person, are:TypPravnickaOsoba."""

    vat_id: Optional[str] = None
    name: Optional[str] = None
    representatives: List[NaturalPerson] = field(default_factory=list)


@dataclass
class Member:
    """Company members."""

    role: Optional[Union[MemberRoleType, str]] = None
    identity: Optional[Union[NaturalPerson, LegalPerson]] = None


@dataclass
class CompanyEntity:
    """Structure blocks of a company."""

    entity_type: Union[CompanyEntityType, str]
    name: Optional[str] = None
    members: List[Member] = field(default_factory=list)


@dataclass
class VerifiedCompany:
    """Company name and address verified by VAT number."""

    company_name: str
    address: Optional[str] = None
    street_and_num: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    district: Optional[str] = None
    country_code: Optional[str] = None
    legal_form: Optional[int] = None


@dataclass
class VerifiedCompanyPublicRegister(VerifiedCompany):
    """Company name and address verified by VAT number."""

    company_entities: List[CompanyEntity] = field(default_factory=list)
