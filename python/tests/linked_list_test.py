# -*- coding: utf-8 -*-
from lists.linked_lists.linked_list import LinkedList

__author__ = 'ilyakamens'
__date__ = '9/20/14'

import unittest


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_empty_list(self):
        self.assertEqual(self.ll.head, None)
        self.assertEqual(self.ll.tail, None)

    def test_constructor(self):
        self.test_empty_list()

    def test_add(self):
        one = self.ll.add(1)
        self.assertEqual(self.ll.head, one)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next, None)
        self.assertEqual(self.ll.tail, one)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.tail.next, None)

        two = self.ll.add(2)
        self.assertEqual(self.ll.head, one)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next, self.ll.tail)
        self.assertEqual(self.ll.tail, two)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.tail.next, None)

        three = self.ll.add(3)
        self.assertEqual(self.ll.head, one)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next, two)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertEqual(self.ll.head.next.next, self.ll.tail)
        self.assertEqual(self.ll.tail, three)
        self.assertEqual(self.ll.tail.value, 3)

    def test_delete(self):
        one = self.ll.add(1)
        deleted = self.ll.delete(2)
        self.assertEqual(deleted, None)
        self.assertEqual(self.ll.head, one)
        self.assertEqual(self.ll.tail, one)
        deleted = self.ll.delete(1)
        self.assertEqual(deleted.value, 1)
        self.assertEqual(deleted.next, None)
        self.test_empty_list()

        one = self.ll.add(1)
        two = self.ll.add(2)
        deleted = self.ll.delete(2)
        self.assertEqual(two, deleted)
        self.assertEqual(deleted.value, 2)
        self.assertEqual(deleted.next, None)
        self.assertEqual(self.ll.head, one)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail, one)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.head.next, None)

        two = self.ll.add(2)
        deleted = self.ll.delete(1)
        self.assertEqual(one, deleted)
        self.assertEqual(one.next, None)
        self.assertEqual(deleted.value, 1)
        self.assertEqual(self.ll.head, two)
        self.assertEqual(self.ll.tail, two)
        self.assertEqual(two.value, 2)
        self.assertEqual(two.next, None)

        three = self.ll.add(3)
        four = self.ll.add(4)
        deleted = self.ll.delete(2)
        self.assertEqual(deleted, two)
        self.assertEqual(deleted.value, 2)
        self.assertEqual(deleted.next, None)
        self.assertEqual(three, self.ll.head)
        self.assertEqual(three.value, 3)
        self.assertEqual(three.next, self.ll.tail)
        self.assertEqual(four, self.ll.tail)
        self.assertEqual(four.value, 4)
        self.assertEqual(four.next, None)

    def test_delete_node(self):
        one = self.ll.add(1)
        two = self.ll.add(2)
        three = self.ll.add(3)
        deleted = self.ll.delete_node(one, three)
        self.assertEqual(deleted, None)
        deleted = self.ll.delete_node(None, None)
        self.assertEqual(deleted, None)
        deleted = self.ll.delete_node(None, self.ll.tail)
        self.assertEqual(deleted, None)
        deleted = self.ll.delete_node(self.ll.head, None)
        self.assertEqual(deleted, None)
        deleted = self.ll.delete_node(None, self.ll.head)
        self.assertEqual(deleted.value, 1)
        self.assertEqual(deleted.next, None)
        deleted = self.ll.delete_node(self.ll.head, self.ll.tail)
        self.assertEqual(deleted.value, 3)
        self.assertEqual(deleted.next, None)

    def test_delete_all(self):
        one = self.ll.add(1)
        one = self.ll.add(1)
        two = self.ll.add(2)
        three = self.ll.add(3)
        one = self.ll.add(1)
        two = self.ll.add(2)
        three = self.ll.add(3)
        one = self.ll.add(1)
        two = self.ll.add(2)
        three = self.ll.add(3)
        three = self.ll.add(3)

        deleted = self.ll.delete_all(4)
        self.assertEqual(deleted, [])

        deleted = self.ll.delete_all(1)
        self.assertEqual(len(deleted), 4)
        for node in deleted:
            self.assertEqual(node.value, 1)
            self.assertEqual(node.next, None)

        deleted = self.ll.delete_all(2)
        self.assertEqual(len(deleted), 3)
        for node in deleted:
            self.assertEqual(node.value, 2)
            self.assertEqual(node.next, None)

        deleted = self.ll.delete_all(3)
        self.assertEqual(len(deleted), 4)
        for node in deleted:
            self.assertEqual(node.value, 3)
            self.assertEqual(node.next, None)

        self.test_empty_list()

        deleted = self.ll.delete_all(1)
        self.assertEqual(deleted, [])

    def test_reverse_iteratively(self):
        self.ll.reverse_iteratively()
        self.test_empty_list()

        one = self.ll.add(1)
        self.ll.reverse_iteratively()
        self.assertEqual(self.ll.head, self.ll.tail)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next, None)

        two = self.ll.add(2)
        self.ll.reverse_iteratively()
        self.assertEqual(self.ll.head, two)
        self.assertEqual(self.ll.head.value, 2)
        self.assertEqual(self.ll.head.next, self.ll.tail)
        self.assertEqual(self.ll.tail, one)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.tail.next, None)
        self.ll.reverse_iteratively()

        three = self.ll.add(3)
        self.ll.reverse_iteratively()
        self.assertEqual(self.ll.head, three)
        self.assertEqual(self.ll.head.value, 3)
        self.assertEqual(self.ll.head.next, two)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertEqual(self.ll.head.next.next, self.ll.tail)
        self.assertEqual(self.ll.tail, one)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.tail.next, None)

    def test_reverse_recursively(self):
        self.ll.reverse_recursively()
        self.test_empty_list()

        one = self.ll.add(1)
        self.ll.reverse_recursively()
        self.assertEqual(self.ll.head, self.ll.tail)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next, None)

        two = self.ll.add(2)
        self.ll.reverse_recursively()
        self.assertEqual(self.ll.head, two)
        self.assertEqual(self.ll.head.value, 2)
        self.assertEqual(self.ll.head.next, self.ll.tail)
        self.assertEqual(self.ll.tail, one)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.tail.next, None)
        self.ll.reverse_recursively()

        three = self.ll.add(3)
        self.ll.reverse_recursively()
        self.assertEqual(self.ll.head, three)
        self.assertEqual(self.ll.head.value, 3)
        self.assertEqual(self.ll.head.next, two)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertEqual(self.ll.head.next.next, self.ll.tail)
        self.assertEqual(self.ll.tail, one)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.tail.next, None)


if __name__ == '__main__':
    unittest.main()
