from Stack import Stack
from CircularLinkedList import CircularLinkedList
from BinarySearchTree import BinarySearchTree
from TreeItem import TreeItem

stack = Stack()
list = CircularLinkedList()
BST = BinarySearchTree()

def testStack():
    """
                >>> stack = Stack()
                >>> stack.isEmpty()
                True
                >>> stack.push(5)
                True
                >>> stack.isEmpty()
                False
                >>> stack.getTop()
                (5, True)
                >>> stack.push(4)
                True
                >>> stack.getTop()
                (4, True)
                >>> stack.pop()
                (4, True)
                >>> stack.pop()
                (5, True)
                >>> stack.pop()
                (None, False)
    """

def testList():
    """
                >>> list = CircularLinkedList()
                >>> list.insert(1, 5)
                False
                >>> list.isEmpty()
                True
                >>> list.insert(0, 5)
                True
                >>> list.isEmpty()
                False
                >>> list.insert(1, 8)
                True
                >>> list.insert(1, 6)
                True
                >>> list.retrieve(1)
                (6, True)
                >>> list.delete(1)
                True
                >>> list.retrieve(0)
                (5, True)
                >>> list.retrieve(1)
                (8, True)
                >>> list.delete(0)
                True
                >>> list.delete(1)
                False
                >>> list.delete(0)
                True
                >>> list.isEmpty()
                True
    """

def testBST():
    """
                >>> b = BinarySearchTree()
                >>> b.isEmpty()
                True
                >>> b.searchTreeInsert(TreeItem("Test", 5))
                >>> b.isEmpty()
                False
                >>> b.searchTreeInsert(TreeItem("Test Links", 2))
                >>> b.searchTreeInsert(TreeItem("Test Rechts", 9))
                >>> b.searchTreeInsert(TreeItem("Test Rechts Rechts", 11))
                >>> b.searchTreeInsert(TreeItem("Test Rechts Rechts Rechts", 13))
                >>> b.searchTreeInsert(TreeItem("Test Rechts Links", 7))
                >>> b.searchTreeDelete(9)
                True
                >>> b.searchTreeRetrieve(9)
                False
                >>> b.searchTreeDelete(4)
                False
                >>> b.print() #prints the inorder traversal for testing purposes
                Test Links
                Test
                Test Rechts Links
                Test Rechts Rechts
                Test Rechts Rechts Rechts
    """

if __name__ == '__main__':
    testStack()
    testList()
    testBST()