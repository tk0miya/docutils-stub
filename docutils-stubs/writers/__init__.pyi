# Stubs for docutils.writers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import Component
from docutils.io import Output
from docutils.transforms import Transform
from types import ModuleType
from typing import Any, Dict, List, Type, Union

__docformat__: str

class Writer(Component):
    component_type: str = ...
    config_section: str = ...
    def get_transforms(self) -> List[Type[Transform]]: ...
    document: Any = ...
    output: Union[bytes, str] = ...
    language: ModuleType = ...
    destination: Output = ...
    parts: Dict[Any, Any] = ...
    def __init__(self) -> None: ...
    def write(self, document: Any, destination: Output) -> Any: ...
    def translate(self) -> None: ...
    def assemble_parts(self) -> None: ...

class UnfilteredWriter(Writer):
    def get_transforms(self) -> List[Type[Transform]]: ...

def get_writer_class(writer_name) -> Type[Writer]: ...
