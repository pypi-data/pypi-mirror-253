from typing import Optional, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar("T")


class BaseCache(ABC, Generic[T]):
    @property
    @abstractmethod
    def size(self) -> int:
        """
        Returns the no. of items in the cache
        """
        ...

    @abstractmethod
    def get(self, key: str) -> T:
        """
        Gets the item from the cache with the given `key`
        Raises `KeyError` if key not found in cache
        Returns Cache Item of the mentioned type
        """
        ...

    @abstractmethod
    def get_or_default(self, key: str, default: Optional[T] = None) -> Optional[T]:
        """
        Gets the item from the cache with the given `key`
        Returns Cache Item of the mentioned type
        If key not found, returns `default` value
        """
        ...

    @abstractmethod
    def insert(self, key: str, value: T) -> None:
        """
        Inserts the item in cache with given `key`.
        Raises `ValueError` if key already exists.
        """
        ...

    @abstractmethod
    def upsert(self, key: str, value: T) -> bool:
        """
        Upserts the item in cache with given `key`.
        Returns `True` if new item was inserted
        Returns `False` if `key` already existed and updates the value
        """
        ...

    @abstractmethod
    def delete(self, key: str) -> T:
        """
        Deletes the item in cache with given `key`.
        Raises `KeyError` if key doesn't exists.
        Returns deleted item.
        """
        ...

    @abstractmethod
    def delete_or_default(self, key: str, default: Optional[T] = None) -> Optional[T]:
        """
        Deletes the item in cache with given `key`.
        Returns deleted item `key` existed.
        Returns `default` value if `key` didnt existed.
        """
        ...
