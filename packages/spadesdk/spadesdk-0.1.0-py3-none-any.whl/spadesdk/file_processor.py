import abc
import dataclasses


@dataclasses.dataclass
class File:
    """
    Dataclass representing a Spade file.
    """

    name: str
    format: str
    system_params: dict | None = None


@dataclasses.dataclass
class FileUpload:
    """
    Dataclass representing the result of a file upload.
    """

    file: File
    result: str
    rows: int | None = None
    error_message: str | None = None
    output: dict | None = None

    def __post_init__(self):
        if self.result not in ("success", "warning", "failed"):
            raise ValueError("result must be one of 'success', 'warning', or 'failed'")


class FileProcessor:
    """
    FileProcessor processes a Spade file using the process method.
    """

    @classmethod
    @abc.abstractmethod
    def process(cls, file: File, filename: str, data, user_params: dict | None) -> FileUpload:
        """
        Process a file using the file processor.

        :param file: File to process and its system parameters
        :param filename: Name of the file uploaded
        :param data: Data of the file uploaded
        :param user_params: User parameters - provided by the user when uploading the file
        """
