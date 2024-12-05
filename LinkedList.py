# References:
#               https://www.geeksforgeeks.org/bubble-sort-on-doubly-linked-list/
#               https://www.geeksforgeeks.org/bubble-sort-algorithm/

class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initPoints, initNext, initPrevious):
        self.data = initData # Team Name
        self.points = initPoints # Team points.
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

    def getPoints(self):
        return self.points

    def setPoints(self, newPoints):
        self.points = newPoints

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


def insert(self, team_name, points):
    '''
    Insert a team inside the linked list.
    :param self:
    :param team_name: (str) The name of the team.
    :param points: (int) The number of points they have.
    :return: None
    '''
    new_node = DLinkedListNode(team_name, points, None, None)
    current = self.__head

    if self.__size == 0:
        self.add(team_name, points)
    else:
        while (current.getNext() != None):
            current = current.getNext()
        current.setNext(new_node)
        self.__size = self.__size + 1


def delete(self, team_name):
    '''
    Remove a team from the linked list if they are eliminated.

    Traverse the list to find the team and remove them from the rankings.
    :param self:
    :param team_name: The name of the team.
    :return: None
    '''
    current = self.__head
    previous = None
    found = False
    while not found:
        if current.getData() == team_name:
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

def sort(self):
    '''
    Sort the linked list based on points in descending order, using the BubbleSort Algorithm.

    Function traverses the list, comparing nodes and
    updates their positions to reflect the correct order.
    :param self:
    :return: None
    '''

    exchange = True
    last = None
    while exchange:
        exchange = False
        current = self.__head # Starting position for traversal.

        while current.getNext() != last:
            if current.getPoints() > current.getNext().getPoints(): # Sort in descending order. From Highest Points to Lowers Points.
                current.data, current.getNext().data = current.getNext.data, current.data # Swap the Data of the two Nodes.
                current.points, current.getNext().points = current.getNext().points, current.points # Swap the Points of the two Nodes.
                exchange = True

            current = current.getNext() # Move onto the next node.

        last = current


def display_rankings(self):
    '''
    Display the current rankings of all teams in the list.

    Traverse the linked list and print rach team's name and points.
    '''
    current = self.__head
    string = ''
    while current != None:
        string = string + str(current.getData())
        if current.getNext() != None:  # If the next item in the list, is not the end of the list.
            string = string + " "  # Ensures that there is a space between each item in the list.
        current = current.getNext()

    return string