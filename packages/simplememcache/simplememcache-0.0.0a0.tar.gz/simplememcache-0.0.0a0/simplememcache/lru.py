from dataclasses import dataclass
from .base import BaseCache
from typing import Dict, Optional, TypeVar, Generic, List

T = TypeVar("T")


@dataclass
class LRUNode(Generic[T]):
    """
    Linked List node to maintain the LRU order
    """

    key: str
    value: T
    prev: Optional["LRUNode[T]"] = None
    next: Optional["LRUNode[T]"] = None

    def __str__(self) -> str:
        return f"Node(key={self.key}, value={self.value})"


class LRUCache(BaseCache[T]):
    __max_size: int
    __node_map: Dict[str, LRUNode[T]]
    __head: Optional[LRUNode[T]]
    __tail: Optional[LRUNode[T]]

    def __init__(self, max_size: int) -> None:
        """
        Args:
            max_size (int): Maximum size of the cache.
        """
        if max_size < 0:
            raise ValueError("Invalid cache size")

        self.__max_size = max_size
        self.__node_map = {}
        self.__head = None
        self.__tail = self.__head
        super().__init__()

    @property
    def max_size(self) -> int:
        return self.__max_size

    @property
    def size(self) -> int:
        return len(self.__node_map)

    @property
    def key_order(self) -> List[str]:
        curr = self.__head
        res = []
        while curr:
            res.append(curr.key)
            curr = curr.next

        return res

    def __move_node_to_front(self, node: LRUNode[T]):
        """Moves the given node to the front of the linked list

        Args:
            node (LRUNode[T]): Node to be moved to the front

        Raises:
            ValueError: If the cache is empty
        """
        if not self.__head:
            raise ValueError("Unsupported operation")

        # if this node is at tail
        if node.next is None:
            self.__tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        node.next = self.__head
        node.prev = None
        self.__head.prev = node
        self.__head = node

    def __remove_lru_node(self):
        """Removes the LRU node from the linked list"""
        if self.__tail is None:
            # Nothing to do
            return

        if self.__tail.prev is None:
            # only one node
            self.__head = None
            self.__tail = None
            # Emptying the map
            self.__node_map = {}
        else:
            old_tail = self.__tail
            # Updating tail
            self.__tail = self.__tail.prev
            # Removing old tail
            self.__tail.next = None
            # Removing reference from map
            del self.__node_map[old_tail.key]

    def get(self, key: str) -> T:
        """Returns the value for the given key

        Args:
            key (str): Key to be searched

        Raises:
            KeyError: If the key is not present in the cache

        Returns:
            T: Item value
        """
        if key not in self.__node_map or not self.__head:
            raise KeyError(f"Item with key {key} does not exists")

        target_node: LRUNode[T] = self.__node_map[key]
        self.__move_node_to_front(target_node)
        return target_node.value

    def get_or_default(self, key: str, default: Optional[T] = None) -> Optional[T]:
        """Returns the value for the given key or default if the key is not present

        Args:
            key (str): Key to be searched
            default (Optional[T], optional): Default value to return if not found. Defaults to None.

        Returns:
            Optional[T]: Value for the given key or default.
        """
        try:
            return self.get(key=key)
        except KeyError:
            return default

    def insert(self, key: str, value: T):
        if key in self.__node_map:
            raise ValueError(f"key {key} already present")

        new_node = LRUNode(key=key, value=value)
        # Modifying linked list
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            # Inserting at the head
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

        self.__node_map[key] = new_node

        # If cache size is full then removing the last item
        if self.size > self.max_size:
            self.__remove_lru_node()

    def upsert(self, key: str, value: T) -> bool:
        """Updates the value for the given key if present or inserts a new item

        Args:
            key (str): Key to be updated
            value (T): Value to be updated

        Returns:
            bool: True if a new item was inserted, False otherwise
        """
        try:
            self.insert(key=key, value=value)
            return True
        except ValueError:
            pass

        # Update value in the node
        target_node = self.__node_map[key]
        target_node.value = value

        # modify order
        self.__move_node_to_front(target_node)
        return False

    def delete(self, key: str) -> T:
        """Deletes the item with the given key

        Args:
            key (str): Key to be deleted

        Raises:
            KeyError: If the key is not present in the cache

        Returns:
            T: Deleted item value
        """
        if key not in self.__node_map:
            raise KeyError(f"Item with key {key} does not exists")

        target_node = self.__node_map[key]
        # Removing from map
        del self.__node_map[key]
        prev_node = target_node.prev
        next_node = target_node.next
        if prev_node and next_node:
            next_node.prev = prev_node
            prev_node.next = next_node
        elif prev_node:
            # this is a tail node
            prev_node.next = None
            self.__tail = prev_node
        elif next_node:
            # this is a head node
            next_node.prev = None
            self.__head = next_node

        return target_node.value

    def delete_or_default(self, key: str, default: Optional[T] = None) -> Optional[T]:
        try:
            return self.delete(key=key)
        except KeyError:
            return default
