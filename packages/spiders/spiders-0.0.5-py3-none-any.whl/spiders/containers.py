import random


class RandomList:
    """
    The random list data structure.

    The container has O(1) (amortized*) insertion and O(1) popping time complexity. The insertions
    are at a random positions. While creating a RandomList one must provide at least one random
    element to put in the container.

    Attributes:
        random_elements (list): A list of initial values to store in the data structure.
        max_len (int): the max length of the random-list beyond which new insertion will be dropped

    Raises:
        AssertionError: If the starting container does not contain at least one element.

    Note:
        The starting container must have an initial value because in random.randint(a, b) both a
        and b are included and hence if the list is empty a = 0 and b = -1 it raises ValueError.

    Examples:
    >>> initial_list = [2, 1, 3]
    >>> random_list = RandomList(initial_list)
    >>> random_list.put(4)
    >>> print(random_list)
    [2, 4, 1, 3]
    >>> random_list.put(5)
    >>> print(random_list)
    [5, 2, 4, 1, 3]

    """

    def __init__(self, random_elements: list, max_len: int) -> None:
        assert max_len > 0,  "Max length of a RandomList object must be greater than zero."

        self.max_len = max_len
        self._list = [*random_elements]

    def __repr__(self) -> str:
        return str(self._list)

    def put(self, elem) -> None:
        """
        Adds an element

        Check if the length of the random list is not more than the `max_len` attribute. If not
        append the new element to the random-list. The insertion happens at the very end of the list
        and then it is swapped with another randomly chosen element

        Args:
            elem: The new element to add
        """

        if len(self._list) == self.max_len:
            return

        rand_index = random.randint(0, len(self._list) - 1)
        rand_index_val = self._list[rand_index]

        self._list[rand_index] = elem
        self._list.append(rand_index_val)

    def pop(self) -> None:
        """
        Remove an element
        """

        self._list.pop()

    def empty(self) -> bool:
        """
        Check if the random list is empty

        Returns:
            bool: Whether the random list empty
        """

        return len(self._list) == 0

    def __len__(self) -> int:
        """
        Get the size of the container.

        Returns:
            int: Length of the RandomList container instance
        """

        return len(self._list)
