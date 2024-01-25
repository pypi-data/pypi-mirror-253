"""Utils for VAT numbers."""
import re
from collections.abc import Sequence
from datetime import date
from typing import Any, Optional


def strip_vat_reg_number(number: str) -> str:
    """Remove all characters except letters and numbers."""
    return re.sub(r'[\W_]+', '', number)


def strip_vat_id_number(number: str) -> str:
    """Remove all characters except numbers."""
    return re.sub(r'\D+', '', number)


def join_by_separator(separator: str, data: Sequence) -> Optional[str]:
    """Join data by separator."""
    retval = separator.join([str(value) for value in data if value is not None])
    return None if retval == '' else retval


def parse_date(value: Optional[str]) -> Optional[date]:
    """Parse date or None."""
    return None if value is None else date.fromisoformat(value)


def is_deletion_date(value: Optional[str]) -> bool:
    """Check if deletion date is valid."""
    if value is None:
        return False
    return date.fromisoformat(value) <= date.today()


def value_to_str(value: Optional[Any]) -> str:
    """Convert value to str."""
    return "" if value is None else str(value)


def only_str(value: Optional[Any]) -> Optional[str]:
    """Convert value to str only if it is not None."""
    if value is not None:
        return str(value)
    return value


def make_lower_with_capital(value: Optional[str]) -> Optional[str]:
    """Make name lower case with a capital first letter."""
    if value is None:
        return None
    names = []
    for index, text in enumerate(re.split(r'(\S+)', value)):
        if index % 2:
            if text == 'DE':
                name = text.lower()
            else:
                if '-' in text:
                    name = "-".join([name.capitalize() for name in text.split('-')])
                else:
                    name = text.capitalize()
                if (match := re.match("D(['’‘])", name)):
                    name = "d" + match.group(1) + name[2:].capitalize()
            names.append(name)
        else:
            names.append(text)
    return "".join(names)
