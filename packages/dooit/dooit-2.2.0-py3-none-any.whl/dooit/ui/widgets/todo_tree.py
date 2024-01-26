from typing import List, Literal, Type
from dooit.api.model import Model
from dooit.api.todo import Todo
from dooit.api.workspace import Workspace
from dooit.ui.events.events import SwitchTab
from dooit.ui.widgets.todo import TodoWidget
from dooit.utils.conf_reader import config_man
from .tree import Tree

INITIAL_URGENCY = config_man.get("TODO").get("initial_urgency")


class TodoTree(Tree):
    """
    Subclass of `Tree` widget to represent todos
    """

    _empty = "todo"

    ModelType = Todo
    WidgetType = TodoWidget

    def __init__(self, model: Workspace):
        super().__init__(model, classes="right-dock")

    @property
    def widget_type(self) -> Type[TodoWidget]:
        return TodoWidget

    @property
    def model_class_kind(self) -> Literal["todo"]:
        return "todo"

    def get_children(self, parent: Model) -> List[ModelType]:
        return parent.todos

    async def add_node(
        self, type_: Literal["child", "sibling"], edit: bool = True
    ) -> None:
        await super().add_node(type_, edit=edit)
        await self.current.set_urgency(INITIAL_URGENCY)

    async def switch_pane(self) -> None:
        self.post_message(SwitchTab())

    async def increase_urgency(self) -> None:
        await self.current.increase_urgency()

    async def decrease_urgency(self) -> None:
        await self.current.decrease_urgency()

    async def toggle_complete(self) -> None:
        await self.current.toggle_complete()

    async def switch_pane_workspace(self):
        await self.switch_pane()
