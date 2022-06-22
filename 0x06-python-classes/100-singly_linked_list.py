#!/usr/bin/python3
"""Defination classes of singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes node data
        Args:
            data (int): value to be assigned to `data`
            next_node (Node): object of type Node
        Raises:
            TypeError: `data` isn't an integer or `next_node` not a
                        node object
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves value of data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets a new value to `data` attribute
        Args:
            value (int): number to assign to `data`
        Raises:
            TypeError: if data isn't an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves value of `next_node`"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets a new value to `next_node`
        Args:
            value (Node): object of Noden to assign to `next_node`
        Raises:
            TypeError: if value is not a Node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines implementation of a singly linked list"""

    def __init__(self):
        """Initializes instance data"""
        self.__head = None

    def __str__(self):
        """Prints the entire list in stdout"""
        head = self.__head
        values = []
        while head is not None:
            values.append("{}".format(head.data))
            head = head.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the list
        Args:
            value (int): integer to assign to `data` of Node object
        """
        head = self.__head
        if head is None or (head is not None and head.data >= value):
            new_node = Node(value, head)
            self.__head = new_node
            return
        while head is not None:
            next_node = head.next_node
            if next_node is None or next_node.data >= value:
                new_node = Node(value, next_node)
                head.next_node = new_node
                break
            head = next_node
