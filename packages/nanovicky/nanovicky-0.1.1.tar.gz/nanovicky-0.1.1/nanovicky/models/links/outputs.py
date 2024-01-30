from typing import Tuple


class OutputType:
    FIFO: int = 0  # First In First Out type
    LIFO: int = 1  # Last In First Out type


class OutputMode:
    BUFF: int = 0  # Buffered mode (all values are store and treated)
    FLOW: int = 1  # Flow mode (values are yielded and therefor can be skipped)


class Output:
    def __init__(
        self,
        output_type: OutputType = OutputType.FIFO,
        output_mode: OutputMode = OutputMode.BUFF,
    ) -> None:
        self._output_type: OutputType = output_type
        self._output_mode: OutputMode = output_mode
        self._link = []

    def set(self, value):
        [link.set(value) for link in self._link]

    def set_link(self, link):
        self._link.append(link)
        return self

    def is_linked(self):
        return self._link is not None

    def output_settings(self) -> Tuple[OutputMode, OutputType]:
        """Return the settings of the link (mode and type).

        Returns:
            Tuple[OutputMode, OutputType]: The output mode.
        """
        return self._output_mode, self._output_type


class FrameOutput(Output):
    def __init__(
        self,
        output_type: OutputType = OutputType.FIFO,
        output_mode: OutputMode = OutputMode.BUFF,
    ) -> None:
        super().__init__(output_type, output_mode)
