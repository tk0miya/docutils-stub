# Stubs for docutils.transforms.parts (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes
from docutils.nodes import bullet_list, Node
from docutils.transforms import Transform
from typing import Callable, List, Optional, Tuple, Union

__docformat__: str

class SectNum(Transform):
    default_priority: int = ...
    maxdepth: Optional[int] = ...
    startvalue: int = ...
    prefix: str = ...
    suffix: str = ...
    def apply(self) -> None: ...  # type: ignore
    def update_section_numbers(self, node: Node, prefix: Tuple[str] = ..., depth: int = ...) -> None: ...

class Contents(Transform):
    default_priority: int = ...
    toc_id: str = ...
    backlinks: str = ...
    def apply(self) -> None: ...  # type: ignore
    def build_contents(self, node: Node, level: int = ...) -> Union[bullet_list, list]: ...
    def copy_and_filter(self, node: Node) -> List[nodes.Node]: ...

class ContentsFilter(nodes.TreeCopyVisitor):
    def get_entry_text(self) -> List[nodes.Node]: ...
    def visit_citation_reference(self, node: nodes.citation_reference) -> None: ...
    def visit_footnote_reference(self, node: nodes.footnote_reference) -> None: ...
    def visit_image(self, node: nodes.image) -> None: ...
    def ignore_node_but_process_children(self, node: nodes.Element) -> None: ...
    visit_interpreted: Callable[[nodes.Element], None] = ...
    visit_problematic: Callable[[nodes.Element], None] = ...
    visit_reference: Callable[[nodes.Element], None] = ...
    visit_target: Callable[[nodes.Element], None] = ...
