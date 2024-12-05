class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious

class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    def insertion(self, pos, item):
        '''
        Adds a new node at the given position with item as its data.
        :param pos: Index value of position that item will be added at.
        :param item: Item to be added.
        :return: None
        '''

        # Handle case where Position = 0 or at the head of the list.

        if team_name == 0:
            temp = DLinkedListNode(item, self.__head, None)
            if self.__head != None:
                self.__head.setPrevious(temp)
            else:
                self.__tail = temp

            self.__head = temp
            self.__size += 1  # Increase the size of the list by one to account for inserted item.

        # Handle case where Position = self.__size or rather tail position.
        # Borrow from the append function.
        elif pos == self.__size:
            temp = DLinkedListNode(item, None, self.__tail)
            if self.__tail:
                self.__tail.setNext(temp)
            else:
                self.__head = temp
            self.__tail = temp
            self.__size += 1  # Increase the size of the list by one to account for inserted item.

        # Handle case where Position is not head or tail.

        elif 0 < pos < self.__size:

            current = self.__head
            count = 0
            previous = None

            while (count < pos):
                previous = current
                current = current.getNext()
                count += 1

            temp = DLinkedListNode(item, current, previous)
            previous.setNext(temp)
            current.setPrevious(temp)

            self.__size += 1  # Increase the size of the list by one to account for inserted item.

        else:
            raise("Not a valid integer.") # Raises an error if the pos is not an integer.

    def deletion(self, item):
        # removes the first element in the list that is equal to the item

        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())

        if (current.getNext() != None):
            current.getNext().setPrevious(previous)

        else:
            self.__tail = previous

        self.__size -= 1

    # Fix Later. Placeholder for now. Need to adapt for double linked list.
    def sorting(self, data):
        '''
        Insertion sort algorithm. Sort the given Array with insertion sort method in Ascending order.
        :return: None
        '''
        for index in range(1, len(data)):
            temp = data[index]
            position = index
            while position > 0 and data[position - 1] > temp:
                data[position] = data[position - 1]
                position = position - 1

            data[position] = temp

    def traverse(self):
        '''
        Iterate over the DlinkedList, appending each nodes data to the list result.
        :return: (list) result: A list with all the nodes from the linked list.
        '''
        current = self.__head
        result = []

        while current:
            result.append(current.getData())
            current = current.getNext()

        return result

    # Display Function
    def __str__(self):
        '''
        Returns a string representation of the list
        :return: string - a string representation of the list.
        '''
        # create the string representation of the linked list

        # Similar implementation as seen in SLinkedList.py document and lecture slides.
        current = self.__head
        string = ''
        while current != None:
            string = string + str(current.getData())
            if current.getNext() != None: # If the next item in the list, is not the end of the list.
                string = string + " " # Ensures that there is a space between each item in the list.
            current = current.getNext()
        return string