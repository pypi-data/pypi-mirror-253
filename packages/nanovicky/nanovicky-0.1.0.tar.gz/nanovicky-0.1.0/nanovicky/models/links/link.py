from typing import Dict, Generator, Any, List, Tuple

from components import BaseComponent, ExecutionErrorException
from models import Frame


class BaseLink:
    def __init__(
        self, from_component: BaseComponent = None, to_component: BaseComponent = None
    ):
        self._from_component: BaseComponent = from_component
        self._to_component: str = to_component

        self._DATA_BUFFER: List[Any] = []

    # Status of link

    def is_linked(self) -> bool:
        return self._to_component is not None

    def is_provided(self) -> bool:
        return self._from_component is not None

    def is_complete(self) -> bool:
        return self.is_linked() and self.is_provided()

    # Manages Inputs and outputs

    def entrypoint(self, component: BaseComponent, value: str):
        try:
            self._from_component = component
            self._from_component.outputs[value].set_link(self)
            return self
        except KeyError:
            print(f"ERROR >>> Component {component} does not have output value {value}")
            return self

    def destination(self, component: BaseComponent, value: str):
        try:
            self._to_component = component
            self._to_component.inputs[value].set_link(self)
            return self
        except KeyError:
            print(f"ERROR >>> Component {component} does not have input value {value}")
            return self

    def get(self) -> Any:
        if self._DATA_BUFFER:
            output = self._DATA_BUFFER[0]
            self._DATA_BUFFER.pop(0)
            return output
        return None

    def set(self, value):
        self._DATA_BUFFER.append(value)
        return self

    def __str__(self) -> str:
        return f"{self._from_component.name}=>{self._to_component}"


class GenericLink(BaseLink):
    def __init__(
        self,
        link_type: type,
        from_component: BaseComponent,
        to_component: BaseComponent = None,
    ):
        super().__init__(from_component, to_component)
        self._link_type: type = link_type

    def get(self):
        element = super().get()
        if element is None or isinstance(element, self._link_type):
            return element
        raise ValueError(
            f"In link {self} : received value {element}, which is of type {type(element)}."
        )

    def __str__(self) -> str:
        return super().__str__() + f"[{self._link_type}]"


class FrameLink(GenericLink):
    def __init__(
        self, from_component: BaseComponent = None, to_component: BaseComponent = None
    ):
        super().__init__(Frame, from_component, to_component)

    def get(self) -> Frame:
        return super().get()


class ListLink(BaseLink):
    def __init__(
        self,
        from_components: List[Tuple[BaseComponent, str]] = None,
        to_component: BaseComponent = None,
        link_type: type = None,
    ) -> None:
        super().__init__(to_component=to_component)
        self._from_components: List[Tuple[BaseComponent, str]] = from_components

    def entrypoint(self, from_components: List[Tuple[BaseComponent, str]]):
        self._from_components = from_components
        for component, value in self._from_components:
            super().set_input(component, value)
        return self


class FlowLink(BaseLink):
    def __init__(
        self, from_component: BaseComponent = None, to_component: BaseComponent = None
    ):
        super().__init__(from_component, to_component)

    def set(self, value):
        self._DATA_BUFFER = [value]

    def get(self) -> Any:
        if self._DATA_BUFFER:
            output = self._DATA_BUFFER[0]
            self._DATA_BUFFER.pop(0)
            return output
        return None


class OneShotLink(BaseLink):
    def __init__(
        self, from_component: BaseComponent = None, to_component: BaseComponent = None
    ):
        super().__init__(from_component, to_component)

    def set(self, value):
        if not self._DATA_BUFFER:
            self._DATA_BUFFER = [value]

    def get(self) -> Any:
        if self._DATA_BUFFER:
            return self._DATA_BUFFER[0]
        return None
