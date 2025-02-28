import logging

from flask import Response

from .input_fields import FieldId

logger: logging.Logger | None

HTML_HEAD: str
HTML_TAIL: str

class Executor:
    RAW_CMD_PATH: str

    def __init__(self) -> None: ...
    def exec(self, command_path: str) -> Response: ...
    def _exec_raw(self, command: list[str]) -> Response: ...  # undocumented
    def _exec_html(self, command_path: str) -> Response: ...  # undocumented
    def _run_script_and_generate_stream(self) -> None: ...  # undocumented
    def _create_cmd_header(self, commands: list[CmdPart]) -> str: ...  # undocumented
    def _create_result_footer(self) -> str: ...  # undocumented

def _get_download_link(field_info: FieldFileInfo) -> str: ...  # undocumented

class CommandLineRaw:
    def __init__(self, script_file_path: str, command: str) -> None: ...
    def append(self, part: str, secret: bool = False) -> None: ...
    def get_commandline(self, obfuscate: bool = False) -> list[str]: ...
    def get_download_field_infos(self) -> list[FieldInfo]: ...
    def after_script_executed(self) -> None: ...

class CommandLineForm:
    def __init__(self, script_file_path: str, commands: list[str]) -> None: ...
    def append(self, part: str, secret: bool = False) -> None: ...
    def get_commandline(self, obfuscate: bool = False) -> list[str]: ...
    def get_download_field_infos(self) -> list[FieldInfo]: ...
    def after_script_executed(self) -> None: ...

def _get_python_interpreter() -> str: ...

class CmdPart:
    def __init__(self, part: str, secret: bool = False) -> None: ...

class FormToCommandLineBuilder:
    def __init__(self, command_line: CommandLineForm) -> None: ...
    def add_command_args(self, command_index: int) -> None: ...
    @staticmethod
    def _is_option(cmd_option: str) -> bool: ...
    def _process_option(self, field_info: FieldInfo) -> None: ...

class FieldInfo:
    @staticmethod
    def factory(key: str) -> FieldInfo: ...
    def __init__(self, param: FieldId) -> None: ...
    def before_script_execute(self) -> None: ...
    def after_script_executed(self) -> None: ...
    def __lt__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...

class FieldFileInfo(FieldInfo):
    def __init__(self, fimeta: FieldId) -> None: ...
    def before_script_execute(self) -> None: ...
    @classmethod
    def temp_dir(cls) -> str: ...
    def save(self) -> None: ...

class FieldOutFileInfo(FieldFileInfo):
    def __init__(self, fimeta: FieldId) -> None: ...
    def save(self) -> None: ...

class FieldPathInfo(FieldFileInfo):
    def save(self) -> None: ...
    def after_script_executed(self) -> None: ...

class FieldPathOutInfo(FieldOutFileInfo):
    def save(self) -> None: ...
    def after_script_executed(self) -> None: ...

def zip_folder(folder_path: str, out_folder: str, out_prefix: str) -> str: ...
