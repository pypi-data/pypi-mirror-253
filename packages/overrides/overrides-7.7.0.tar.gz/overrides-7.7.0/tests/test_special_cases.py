from abc import ABC, abstractmethod
from collections.abc import MutableMapping
from concurrent.futures import Future
from typing import Callable, Any

from overrides import override


class MyInterface(ABC):
    @abstractmethod
    def run(self) -> "Future[str]":
        pass


class MyInterface2(ABC):
    @abstractmethod
    def run(self, callback: Callable[[str], None]):
        pass


def test_future_is_fine():
    class FutureWorks(MyInterface):
        @override
        def run(self) -> "Future[str]":
            pass


def test_callable_is_fine():
    class CallableWorks(MyInterface2):
        @override
        def run(self, callback: Callable[[str], None]):
            pass


def test_overriding_untyped_from_other_package_is_fine():
    class Params(MutableMapping):
        DEFAULT = object()

        @override
        def pop(
            self, key: str, default: Any = DEFAULT, keep_as_dict: bool = False
        ) -> Any:
            pass
