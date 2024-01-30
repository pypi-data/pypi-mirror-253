from _typeshed import Incomplete
from typing import Dict, List as TypingList, Optional
from typing_extensions import TypeAlias

F: str
C: str
E: str
W: str
N: str
I: str
D: str
T: str
all_levels: Incomplete
MsgTuple: TypeAlias

class msg(Exception):
    M322_nonetype_recall__fname_line: Incomplete
    M472_method_deprecated__method_replacement: Incomplete
    M473_want_oftypelist_not_typelist__list: Incomplete
    M542_field_not_found_on_get__key_type_item: Incomplete
    M543_field_not_found_on_set__key_type_item: Incomplete
    M544_called_class_constructor: Incomplete
    M545_item_not_found_in_list__key_item_list: Incomplete
    M546_item_not_iterable__item: Incomplete
    M547_set_invalid_type__field_key_rtype_etype: Incomplete
    M548_argtype_mismatch__rtype_etype: Incomplete
    M572_missing_property_value__listname_propname: Incomplete
    M573_appending_existing_items__list_items: Incomplete
    M574_unknown_datatype__itemname_propname: Incomplete
    M575_method_removed__method_replacement: Incomplete
    M576_fieldnotfound_find__key_type_list_item: Incomplete
    M577_nonetype_attributeerror__orig_fname_line: Incomplete
    M578_nonetype_typeerror__orig_fname_line: Incomplete
    M582_field_not_found__field: Incomplete
    M722_unexpected_exception__exception: Incomplete
    M822_server_invalid_url__url: Incomplete
    M823_connection_error__url: Incomplete
    M824_invalid_handshake__url: Incomplete
    M825_oserr_connection_error__errno_url: Incomplete
    M826_server_timeout__url: Incomplete
    unknown_encountered_filename: Optional[str]
    unknown_encountered_lineno: Optional[int]
    column_code: int
    column_long_text: int
    @staticmethod
    def create_exception_short_traceback(python_class: type | int, short_desc_message: str, long_desc_message: Optional[TypingList[str]], from_e: Optional[Exception] = None) -> BaseException: ...
    class TellDevException(BaseException):
        e_msg: Incomplete
        e_args: Incomplete
        def __init__(self, msg: MsgTuple, args: Dict[str, str]) -> None: ...
