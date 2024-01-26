from __future__ import annotations

import datetime
import re
from decimal import Decimal
from typing import Annotated, Optional

from annotated_types import Ge, Le
from ormspace.annotations import OptionalFloat, OptionalInteger
from ormspace.keys import TableKey
from ormspace.metainfo import MetaInfo
from pydantic import AfterValidator, BeforeValidator, Field


def body_measure_range(value: float | int | None) -> str|None:
    if value is not None:
        if value < 0:
            raise ValueError('Value must be greater than 0')
        elif value > 300:
            raise ValueError('Value must be lesser than 300')
    return value


# StringList = Annotated[list[str], BeforeValidator(string_to_list), Field(default_factory=list)]
ProfileKey = Annotated[TableKey, MetaInfo(tables=['Patient', 'Doctor', 'Employee'], item_name='profile'), Field('Doctor.admin', title='chave do perfil')]
StaffKey = Annotated[TableKey, MetaInfo(tables=['Doctor', 'Employee'], item_name='staff'), Field('Doctor.admin', title='chave da equipe')]
# OptionalFloat = Annotated[Optional[float], BeforeValidator(none_if_empty_string), Field(None)]
# OptionalInteger = Annotated[Optional[int], BeforeValidator(none_if_empty_string), Field(None)]
# OptionalDate = Annotated[Optional[datetime.date], BeforeValidator(none_if_empty_string), Field(None)]
# OptionalDecimal = Annotated[Optional[Decimal], BeforeValidator(none_if_empty_string), Field(None)]
BodyMeasureFloat = Annotated[OptionalFloat, AfterValidator(body_measure_range)]
BodyMeasureInteger = Annotated[OptionalInteger, AfterValidator(body_measure_range)]
