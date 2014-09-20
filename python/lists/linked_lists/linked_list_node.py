# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/16/14'


class LinkedListNode(object):
    """A simple linked list node class with a value
    and a reference to the next node in the list.
    """

    def __init__(self, value, next=None):
        """Initialize the node with a value and reference to the next node in the list.
        :param value:   The value of the node
        :param next:    The reference to the next node in the list
        """
        self.value = value
        self.next = next

    def get_dict(self):
        """Return a dictionary used for printing a readable version of this node."""
        dict = {'val': self.value}
        dict['next'] = self.next.value if self.next else None
        return dict

    def print_node(self):
        """Print a humand-readable version of this node"""
        print str(self.get_dict()) + ',',