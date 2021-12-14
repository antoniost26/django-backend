from datetime import date

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _("%(value)s must be positive."),
            params={"value": value},
        )


def validate_cnp(value):
    if len(str(value)) != 13:
        raise ValidationError(
            _("%(value)s needs to have 13 digits."),
            params={"value": value},
        )


def stringvalidator(value):
    if isinstance(value, str):
        raise ValidationError(
            _("$(value) must be a number."), params={"value": value}
        )


def validate_year(value):
    if value > int(date.today().strftime("%Y")) or value < 1900:
        raise ValueError(_("Year must be valid."))


def validate_date(value):
    if value.year > int(date.today().strftime("%Y")):
        raise ValueError((f"Year must be valid."))


def validate_string(value):
    n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for x in n:
        if x in value:
            raise ValueError(f"Digits are not allowed in model names.")
