from typing import Self


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data) -> Node:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, next_node: Node, data):
        if self.head is None:
            return

        if self.head == next_node:
            self.insert_at_beginning(data)
            return

        prev_node = self.head
        while prev_node and prev_node.next != next_node:
            prev_node = prev_node.next

        if prev_node is None:
            return

        new_node = Node(data)
        new_node.next = next_node
        prev_node.next = new_node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return

        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur is None:
            return

        prev.next = cur.next

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print(' ')

    # ------------------------------------------
    # THE CODE FOR THE FINAL PROJECT STARTS HERE
    # ------------------------------------------

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def sort(self) -> None:
        self.head = LinkedList.merge_sort(self.head)

    def merge(self, list_: Self) -> Self:
        """
        Returns a new linked list
        """
        new_list = LinkedList()
        new_list.head = LinkedList.merge_sorted(self.head, list_.head)
        return new_list

    @staticmethod
    def merge_sorted(left: Node | None, right: Node | None):
        """
        Static method to merge two linked lists
        """
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = LinkedList.merge_sorted(left.next, right)
        else:
            result = right
            result.next = LinkedList.merge_sorted(left, right.next)
        return result

    @staticmethod
    def merge_sort(h: Node | None):
        """
        Sort linked list with merge sort algorithm
        """
        if h is None or h.next is None:
            return h

        # get the middle of the list
        middle = LinkedList.get_middle(h)

        # sort right list
        right = LinkedList.merge_sort(middle.next)

        # sort left list
        middle.next = None
        left = LinkedList.merge_sort(h)

        # merge sorted lists
        sortedlist = LinkedList.merge_sorted(left, right)
        return sortedlist

    @staticmethod
    def get_middle(head: Node) -> Node:
        slow = head
        fast = head

        while (fast.next is not None and
               fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":

    llist = LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(34)
    llist.insert_at_beginning(1)
    llist.insert_at_beginning(12)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(67)

    print("Unsorted LL1:")
    llist.print_list()

    llist.reverse()
    print("Reversed LL1:")
    llist.print_list()

    llist.sort()
    print("Sorted LL1:")
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_beginning(33)
    llist2.insert_at_beginning(2)
    llist2.insert_at_beginning(99)
    llist2.sort()

    print("Sorted LL2:")
    llist2.print_list()

    print("Merge result of LL1 and LL2:")
    llist.merge(llist2).print_list()







