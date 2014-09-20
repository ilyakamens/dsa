# -*- coding: utf-8 -*-
from lists.linked_lists.abc_linked_list import ABCLinkedList
from lists.linked_lists.linked_list_node import LinkedListNode

__author__ = 'ilyakamens'
__date__ = '9/16/14'


class LinkedList(ABCLinkedList):
    """Singly linked list class."""

    def add(self, value):
        """Add the value to the list.
        :param value:   The value to be added to the list.
        :return:        The added node.
        """
        node = LinkedListNode(value)

        if not self.head:
            self.head = node
            self.tail = node
        elif self.head is self.tail:
            self.tail = node
            self.head.next = node
        else:
            self.tail.next = node
            self.tail = node
        return node

    def delete(self, value):
        """Remove the value from the list.
        :param value:   The value to be remove.
        :return:        The deleted node, or None if the value wasn't found.
        """
        node = self.head
        prev = None

        while node:
            if node.value == value:
                break
            prev = node
            node = node.next

        return self.delete_node(prev, node)

    def delete_node(self, prev, node):
        """Remove the node from the list.
        :param prev:    The previous item in the list, which we need a reference to.
        :param node:    The node to be removed.
        :return:        The deleted node, or None if the node didn't exist.
        """
        if not node:
            return None

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.next = None
        elif node is self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = node.next
            node.next = None
        return node

    def delete_all(self, value):
        """Delete all nodes with a certain value.
        :param value:   The value of the nodes to be deleted.
        :return:        A list of nodes that were deleted.
        """
        result = []
        node = self.head
        prev = None

        while node:
            if node.value == value:
                next = node.next
                result.append(self.delete_node(prev, node))
                node = next
            else:
                prev = node
                node = node.next

        return result

    def reverse_iteratively(self):
        """Reverse the list in an iterative manner."""
        if not self.head:
            return

        prev = self.head
        node = self.head.next
        self.head.next = None

        # Switch head and tail
        self.head = self.tail
        self.tail = prev

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

    def reverse_recursively(self, curr=None, prev=None):
        """Recursively reverse the list.
        :param curr:    The current node we're reversing.
        :param prev:    The node before curr.
        """
        if not self.head or self.head is self.tail:
            return
        if not prev:
            curr = self.head.next
            prev = self.head
            self.head.next = None
            self.head = self.tail
            self.tail = prev
        if not curr:
            return

        next = curr.next
        curr.next = prev
        self.reverse_recursively(next, curr)

    def print_ends(self):
        """Print the head and tail info.
        """
        print 'head:',
        if self.head:
            self.head.print_node()
        else:
            print None
        print
        print 'tail:',
        if self.tail:
            self.tail.print_node()
        else:
            print None
        print

    def print_list(self):
        """Print the head, tail, and entire list."""
        self.print_ends()

        node = self.head
        while node:
            node.print_node()
            node = node.next
        print