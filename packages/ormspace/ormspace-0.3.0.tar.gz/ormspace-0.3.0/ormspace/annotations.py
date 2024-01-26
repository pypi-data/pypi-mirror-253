from __future__ import annotations

import datetime
import re
from decimal import Decimal
from typing import Annotated, Optional

from annotated_types import Ge, Le
from pydantic import AfterValidator, BeforeValidator, Field, PlainSerializer

from ormspace import functions
from ormspace.functions import bytes_to_str, none_if_empty_string, string_to_list
from ormspace.metainfo import MetaInfo


BytesField = Annotated[bytes, PlainSerializer(bytes_to_str, return_type=str)]
PasswordField = Annotated[bytes, PlainSerializer(bytes_to_str, return_type=str)]
TitleField = Annotated[str, AfterValidator(functions.title_caps)]
LowerStringField = Annotated[str, AfterValidator(lambda x: x.lower() if x else '')]
BirthDateField = Annotated[datetime.date, Ge((lambda : functions.today() - datetime.timedelta(days=365*125))()), Le(functions.today()), MetaInfo(form_field='date')]
DateField = Annotated[datetime.date, Field(default_factory=functions.today)]
DateTimeField = Annotated[datetime.datetime, Field(default_factory=functions.now)]
MultiLineTextField = Annotated[str, MetaInfo(form_field='textarea', style={'height': '4rem'})]
StringField = Annotated[str, MetaInfo(form_field='text')]
PositiveIntegerField = Annotated[int, Ge(0), MetaInfo(form_field='number', config='min="0"')]
PositiveDecimalField = Annotated[Decimal, Ge(0), MetaInfo(form_field='number', config='min="0"')]
IntegerField = Annotated[int, BeforeValidator(functions.parse_number), MetaInfo(form_field='number', config='step="1"')]
FloatField = Annotated[float, BeforeValidator(functions.parse_number), MetaInfo(form_field='number', config='step="0.01"')]
DecimalField = Annotated[Decimal, BeforeValidator(functions.parse_number), MetaInfo(form_field='number', config='step="0.01"')]
PositiveFloatField = Annotated[float, Ge(0), MetaInfo(form_field='number', config='step="0.01"')]
ListOfStrings = Annotated[list[str], BeforeValidator(string_to_list), Field(default_factory=list)]
OptionalFloat = Annotated[Optional[float], BeforeValidator(none_if_empty_string), Field(None)]
OptionalInteger = Annotated[Optional[int], BeforeValidator(none_if_empty_string), Field(None)]
OptionalDate = Annotated[Optional[datetime.date], BeforeValidator(none_if_empty_string), Field(None)]
OptionalDecimal = Annotated[Optional[Decimal], BeforeValidator(none_if_empty_string), Field(None)]