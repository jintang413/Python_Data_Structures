class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(" " + str(temp.data), end="")
            temp = temp.next

    # function insert a node at the end of the list.
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    # function insert a node after a given prev_node.
    def insert_after(self, prev_node, new_data):

        if prev_node is None:
            print('The given previous node cannot be NULL.')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # function insert a new node at the beginning.
    def push(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        # if head node itself holds the key to be deleted.
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def delete_node(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.Next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    def swap_nodes(self, x, y):

        if x == y:
            return

        cur_x = self.head
        prev_x = None

        while cur_x is not None and cur_x.data != x:
            prev_x = cur_x
            cur_x = cur_x.next

        if cur_x is None:
            return

        cur_y = self.head
        prev_y = None

        while cur_y is not None and cur_y.data != y:
            prev_y = cur_y
            cur_y = cur_y.next

        if cur_y is None:
            return

        if prev_x is None:
            self.head = cur_y
        else:
            prev_x.next = cur_y

        if prev_y is None:
            self.head = cur_x
        else:
            prev_y.next = cur_x

        temp = cur_x.next
        cur_x.next = cur_y.next
        cur_y.next = temp

    def reverse(self):

        if self.head is None or self.head.next is None:
            return;

        prev = None
        cur = self.head
        next = None

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def print_middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            return

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        print(slow.data)


if __name__ == '__main__':

    llist = LinkedList()

    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print ("Linked list before calling swapNodes() ")
    llist.print_middle()
    llist.print_list()
    llist.reverse()
    print ("\nLinked list after calling swapNodes() ")
    llist.print_list()
