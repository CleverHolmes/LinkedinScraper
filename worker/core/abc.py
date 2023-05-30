from abc import ABC, abstractmethod, abstractproperty
from typing import List, Callable


class AbstractEngine(ABC):
    base_url: str
    _tasks: list
    @abstractproperty
    def tasks(self): ...
    @abstractproperty
    def data(self): ...
    @abstractmethod
    async def setup(self): ...
    @abstractmethod
    async def tear_down(self): ...
    @abstractmethod
    async def execute(self): ...
    @abstractmethod
    def get_task_kwargs(self, task): ...


class AbstractBrowserCrawler(AbstractEngine):
    @abstractmethod
    async def base_action(
        self, browser, xpath, raise_error, timeout, action
    ): ...
    async def tear_down(self): ...
    @abstractmethod
    async def setup(self): ...
    @abstractmethod
    async def click_xpath(self, browser, xpath, raise_error, timeout): ...
    @abstractmethod
    async def read_from_xpath(self, browser, xpath, raise_error, timeout): ...
    @abstractmethod
    async def get_all_elements(self, browser, xpath, raise_error, timeout): ...


class AbstractBaseRepository(ABC):
    @abstractmethod
    async def gather_tasks(self, tasks: List[Callable]): ...
