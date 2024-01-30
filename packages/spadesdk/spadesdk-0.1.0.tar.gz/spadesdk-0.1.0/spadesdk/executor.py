import abc
import dataclasses


@dataclasses.dataclass
class Process:
    """
    Dataclass representing a Spade process.
    """

    code: str
    system_params: dict | None = None


@dataclasses.dataclass
class RunResult:
    """
    Base class for the result of a process run.
    """

    process: Process
    status: str
    result: str | None = None
    error_message: str | None = None
    output: dict | None = None

    def __post_init__(self):
        if self.status not in ("new", "running", "finished", "failed"):
            raise ValueError("status must be one of 'new', 'running', 'finished', or 'failed'")
        if self.result and self.result not in ("success", "warning", "failed"):
            raise ValueError("result must be one of 'success', 'warning', or 'failed'")


class Executor:
    """
    Executor executes a Spade process using the run method.
    It can either directly run some code or call an external service,
    form example trigger an Airflow DAG.
    """

    @classmethod
    @abc.abstractmethod
    def run(cls, process: Process, user_params: dict) -> RunResult:
        """
        Execute a process using the executor.

        :param process: Process to run and its system parameters
        :param user_params: User parameters - provided by the user when running the process

        :return: RunResult
        """
