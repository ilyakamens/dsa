# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

__author__ = 'ilyakamens'
__date__ = '9/20/14'


class ABCLinkedList(object):
    """Linked list abstract class"""
    __metaclass__ = ABCMeta

    def __init__(self):
        """Initialize the list with head and tail pointers."""
        self.head = None
        self.tail = None

    @abstractmethod
    def add(self, value):
        """Add the value to the linked list.
        :param value:   The value to be added.
        :return:        The added node.
        """
        pass

    @abstractmethod
    def delete(self, value):
        """Remove the value from the list.
        :param value:   The value to be deleted.
        :return:        The deleted node, or None if nothing was removed.
        """
        pass

    @abstractmethod
    def print_list(self):
        """Print the contents of the list in a human-readable way."""
        pass