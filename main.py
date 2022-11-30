class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data_in):
        NewNode = Node(data_in, self.head)
        self.head = NewNode

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Sorry, we don't have any data on this index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Please, write correct index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()
    while True:
        data = str(input("What would you like to do? add ,remove or finish?"))
        if data == "remove":
            y = int(input("Which index do you want to remove?"))
            ll.remove_at(y)
            ll.print()
        elif data == "finish":
            ll.print()
            print("See you!")
            break
        elif data == "add":
            c = str(input("Where do you want to add an index? first, last or mid?"))
            if c == "first":
                r = int(input("Which data do you want to add to first index?"))
                ll.insert_at_begining(r)
                ll.print()
            elif c == "last":
                z = int(input("Which data do you want to add to last index?"))
                ll.insert_at_end(z)
                ll.print()
            elif c == "mid":
                b = int(input("Which data do you want to add"))
                w = int(input("Which index do you want to add"))
                ll.insert_at(w, b)
                ll.print()
