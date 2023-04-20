from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    """Evaluates the given answer to the riddle.

        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should
                be returned. Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
     """
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        return answer.lower() == self.answer.lower()
    
        """Evaluates the given answer to the riddle.

        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should
                be returned. Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
        """

    def get_hint(self) -> Iterator[str]:
        yield from iter(self.answer)
    
        """Evaluates the given answer to the riddle.

        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should
                be returned. Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
        """
