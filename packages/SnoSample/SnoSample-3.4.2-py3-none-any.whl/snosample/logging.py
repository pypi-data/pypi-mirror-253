# Default Python packages.
from datetime import datetime


class Logger:
    """
    Class to create and show logging messages with.
    """
    def __init__(self, console: bool = True, console_level: str = "info",
                 file: str = None, file_level: str = "debug",
                 layout: str = "<time> | <level> | <message>"):
        """
        Parameters
        ----------
        console: bool
            Print the logging messages in the console.
        file: str
            Relative or absolute path to the logging file.
            No file will be created if None.
        console_level: str
            Logging level threshold for the console messages.
            Accepted values are: 'debug', 'info', 'warning', 'error'.
        file_level: str
            Logging level threshold for the file messages.
            Accepted values are: 'debug', 'info', 'warning', 'error'.
        layout: str
            Fully customisable layout of the logging messages.
            Must contain '<message>', can contain: '<time>', '<level>'.
        """
        self._console = console
        self._accepted = ["debug", "info", "warning", "error"]
        self._file = file

        # Check if input thresholds are acceptable.
        if console_level is not None and console_level not in self._accepted:
            raise ValueError(f"'{console_level}' is not in: {self._accepted}")
        if file_level is not None and file_level not in self._accepted:
            raise ValueError(f"'{file_level}' is not in: {self._accepted}")

        # Check if input layout is acceptable.
        if "<message>" not in layout:
            raise ValueError(f"'{layout}' does not contain '<message>'")

        self._layout = layout

        # Change input thresholds to integers for easier comparison later.
        self._level_console = self._accepted.index(console_level)
        self._level_file = self._accepted.index(file_level)

        # Always start with an empty file.
        if file is not None:
            with open(self._file, "w") as file:
                file.close()

    def _create_message(self, message: str, level: str) -> str:
        """
        Create a logging message from a given message.

        Parameters
        ----------
        message: str
            Message from which to create the logging message.
        level: str
            Message level.

        Returns
        -------
        str:
            Logging message.
        """
        # Get the datetime string excluding microseconds.
        now = round(datetime.now().timestamp())
        now = str(datetime.fromtimestamp(now))

        # Replace the message placeholders with the data.
        message = self._layout.replace("<message>", message)
        message = message.replace("<time>", now)
        message = message.replace("<level>", level.upper())
        return message

    def _print_message(self, message: str) -> None:
        """
        Print a logging message in the console.

        Parameters
        ----------
        message: str
            Logging message to be printed.
        """
        if self._console:
            print(message)

    def _write_message(self, message: str) -> None:
        """
        Write a logging message in a text file.

        Parameters
        ----------
        message: str
            Logging message to be written to the file.
        """
        if self._file is not None:
            message = f"{message}\n"

            with open(self._file, "a") as file:
                file.write(message)

    def message(self, message: str, level: str = "info") -> None:
        """
        Create and show a logging message from a given message..

        Parameters
        ----------
        message: str
            Message from which to create the logging message.
        level: str
            Message level.
        """
        if level not in self._accepted:
            raise ValueError(f"accepted message levels are: debug, info, warning, error")

        message = self._create_message(message=message, level=level)
        level = self._accepted.index(level)

        if level >= self._level_console:
            self._print_message(message=message)
        if level >= self._level_file:
            self._write_message(message=message)
