class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_b(self, data):
        node = Node(data, self.head)
        self.head = node
        # print(node)

    def pr(self):
        if self.head is None:
            print('Its empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str((itr.data)) + ' '
            itr = itr.next
        print(llstr)

    def insert_e(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_value(self, data_list):
        self.head = None
        for d in data_list:
            self.insert_e(d)

    def len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_item(self, index):
        if index < 0 or index >= self.len():
            raise Exception("Enter a proper value")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.len():
            raise Exception('Enter valid index')

        if index == 0:
            self.insert_b(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    lls = linkedlist()
    lls.insert_b(0)
    lls.insert_b(1)
    lls.insert_b(2)
    lls.insert_b(3)
    lls.insert_e(90)
    lls.insert_e(910)
    # lls.insert_value([1, 2, 3, 4, 5])
    lls.pr()

    # lls.remove_item(2)
    lls.insert_at(3, 10)
    lls.insert_at(3, 10)
    lls.pr()
    # print(lls.len())
