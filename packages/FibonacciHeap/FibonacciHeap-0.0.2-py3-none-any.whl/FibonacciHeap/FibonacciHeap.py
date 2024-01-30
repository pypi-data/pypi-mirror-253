import math


class Node:
    """
    Node class that represents each individual node in the Fibonacci Heap
    Contains characteristic information of each node
    """

    def __init__(self, key):
        """
        - key: unique identifier attached to each. the information each node contains
        - left, right: the node's adjacent siblings in a doubly linked list
        - child: the representative child of the node
        - parent: the node's parent
        - degree: the number of children this node has
        - mark: bool value indicating whether the node is marked
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.child = None
        self.degree = 0
        self.mark = False

    def __repr__(self):
        return str(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __hash__(self):
        return hash(self.key)

    def add_child(self, node):
        """
        Function used to add a child to a node's list of children
        This function adds the child node and also updates child's parent, mark, and degree

        :param node: the child node to be removed
        :type Node (defined class)
        :return: NA
        """

        # Updating the degree, mark, and child node's new parent
        self.degree += 1
        node.mark = False
        node.parent = self

        # If this is the first child node of the parent
        if not self.child:
            # New child node made representative child node of the parent
            self.child = node
            node.left, node.right = node, node
            return

        # If the parent node previously already had at least 1 child node
        # this child node is added to the right of the representative child node
        right_neighbor = self.child.right

        self.child.right = node
        right_neighbor.left = node

        node.left, node.right = self.child, right_neighbor

        return

    def remove_child(self, node):
        """
        Function used to remove a child from a node's list of children
        This function only removes the child node and does not update child's new parent

        :param node: the child node to be removed
        :type Node (defined class)
        :return: NA
        """

        # If the node does not have any child nodes
        if self.degree == 0:
            raise ValueError('This node does not have any child nodes')

        # If this node only has 1 child
        if self.degree == 1:
            self.child = None

        # If this node has multiple child nodes
        else:
            if self.child is node:
                self.child = node.right
            node.left.right = node.right
            node.right.left = node.left

        # Update node's degree after child is successfully removed
        self.degree -= 1

        return


class FibonacciHeap:
    """
    Class that defines the structure and functionality of the Fibonacci Heap
    Contains all trees and individual nodes in the heap
    Functionality defined to insert, extract, and delete nodes, decrease key of nodes,
    and merge (union) 2 different Fibonacci heaps
    """

    def __init__(self):
        """
        - min: points to the node with the smallest key
        - num_nodes: number of nodes currently in the heap
        - num_trees: number of trees currently in the heap (also defined by number of "root nodes")
        - num_marks: number of marked nodes in the heap
        """
        self.min = None
        self.num_nodes = 0
        self.num_trees = 0
        self.num_marks = 0

    def is_empty(self):
        """
        Checks whether the Fibonacci Heap is empty

        :return: boolean value representing whether Fibonacci Heap is empty
        :rtype: bool
        """
        return True if self.num_nodes == 0 else False

    def get_potential(self):
        """
        Calculates the potential of the Fibonacci Heap at any given moment

        /"The amount of time saved for later use is measured at any given moment by a potential function.
        The potential of a Fibonacci heap is given by:
        Potential = t + 2*m
        where t is the number of trees in the Fibonacci heap, and m is the number of marked nodes
        /"

        :return: potential value of the Fibonacci Heap at the given moment
        :rtype: int
        """
        return self.num_trees + 2 * self.num_marks

    def remove_root(self, node):
        """
        Removes the given root node from the list of root nodes of the heap.
        This action removes a tree from the Fibonacci Heap
        Updates the connections of the circular doubly linked list containing root nodes of the heap
        This function does not update the state of its children, or the left and right connections of the removed node

        :param node: the root node to be removed
        :type Node (defined class)
        :return: NA
        """

        # Updates the right and left connections of the adjacent root
        node.right.left = node.left
        node.left.right = node.right

        # Number of trees reduces by one when a root node is removed
        self.num_trees -= 1

        return

    def add_root(self, node):
        """
        Adds the given node to the list of roots of the heap.
        This action introduces a new tree in the Fibonacci Heap
        The function updates the circular doubly linked list connections (of the node and its adjacent nodes as well)
        This function does not update the min value of the Fibonacci Heap

        :param node: node to be added as a root node
        :type Node (defined class)
        :return: NA
        """

        # Number of trees increases by 1
        self.num_trees += 1

        # If there are no previous root nodes
        if self.min is None:
            node.left, node.right = node, node
            return

        # If there previously are nodes in the list of root nodes
        # Node is always added to the right of the previous min node
        node.left = self.min
        node.right = self.min.right

        self.min.right.left = node
        self.min.right = node

        return

    def insert(self, node):
        """
        Function to insert a new node into the Fibonacci Heap
        Inserts the given node as a root node o the list of root nodes of the heap.
        Calls the "add_root" helper function to complete insertion
        This function also updates the min value of the Fibonacci Heap

        :param node: node to be added as a root node
        :type Node (defined class)
        :return: NA
        """

        # Calls the add_root helper function to correctly insert new node
        self.add_root(node)

        # Updates the min value of the Fibonacci Heap
        if self.min is None:
            self.min = node
        elif node.key < self.min.key:
            self.min = node

        # Increments the number of nodes in the Fibonacci Heap
        self.num_nodes += 1

        return

    def get_min(self):
        """
        Returns the node with the smallest key i.e. min of the Fibonacci Heap

        :return: Node containing the smallest key in the Fibonacci Heap
        :rtype: Node (defined class)
        """
        return self.min

    def extract_min(self):
        """
        Extracts and returns the min node i.e. the node with the smallest key in the Fibonacci heap
        This function correctly updates the structure of the Fibonacci Heap after min node is removed
        Utilizes helper function to correctly update and restore structure of the heap, including
        previously deferred processes

        :return: Min node i.e. Node containing the smallest key in the Fibonacci Heap
        :rtype: Node (defined class)
        """
        # Check to see if Fibonacci Heap is empty
        if self.is_empty():
            return None

        # Assigning the extract node to the min node
        extract_node = self.min

        # If the Fibonacci heap has only 1 node
        # Trivial solution to avoid unnecessary computation
        if self.num_nodes == 1:
            # self.min = None
            # self.num_nodes = 0
            # self.num_trees = 0
            # self.num_marks = 0
            self.__init__()
            return extract_node

        # Converts all child nodes of the extract node to root nodes of the heap
        # (This actions mimics re-insertion of nodes to the Fibonacci heap)
        # These nodes will be correctly re-positioned when consolidate() is called
        child_node = extract_node.child
        for _ in range(extract_node.degree):
            adjacent_child = child_node.right
            self.add_root(child_node)
            child_node.parent = None
            child_node = adjacent_child

        # Updates the root list by removing the extract node from the list
        self.remove_root(extract_node)

        # Reassigning min value to the adjacent node
        # this will be correctly assigned to the next smallest node in consolidate()
        self.min = extract_node.right

        # Consolidates the Fibonacci Heap by repositioning nodes/trees
        self.consolidate()

        # Updating number of nodes in the Fibonacci Heap
        self.num_nodes -= 1

        # If the extract node was marked, updating number of marked nodes
        if extract_node.mark:
            self.num_marks -= 1

        return extract_node

    def consolidate(self):
        """
        Consolidates the Fibonacci Heap after the smallest node is extracted
        This action restores structure in the Fibonacci Heap by repositioning the nodes
        Primarily objective of this action is to reduce number of trees in the heap
        Merges trees of same the degree until none of the remaining trees have the same order
        """

        # Creating aa list to store trees of each order
        # Finding the largest integer exponent e such that "2^e <= total number of nodes"
        # Using this as size of array
        A = [None] * math.frexp(self.num_nodes)[1]

        root = self.min
        counter = self.num_trees

        # Looping through all trees in the Fibonacci Heap
        while counter:
            x = root
            root = root.right
            d = x.degree

            # Linking two trees with same order into one
            # Identifying same order trees by checking the corresponding position in the list
            # Link if tree exists in the list, store if not. Repeat until tree is stored in the list
            # Linking increases order by 1
            while A[d]:
                y = A[d]
                # Assigning tree with smaller key of the root node as parent while linking
                if x.key > y.key:
                    x, y = y, x
                self.link(y, x)

                # Clearing the space of that order on the list
                A[d] = None
                # Incrementing degree of list,
                # in accordance with the linking
                d += 1

            A[d] = x
            counter -= 1

        # Resetting min node. Reassigned correctly in the next step
        self.min = None

        # Identifying and assigning the new correct min node
        for i in range(len(A)):
            if A[i]:
                if self.min is None:
                    self.min = A[i]
                else:
                    if A[i].key < self.min.key:
                        self.min = A[i]

        return

    def link(self, node, new_parent_node):  # y>x
        """
        Repositions given node by making it a child of given new parent node
        Used to consolidate two trees of the same order into one

        :param node: node that needs to be repositioned as a child of new parent node
        :type Node (defined class)
        :param new_parent_node: the new parent node for the child node
        :type Node (defined class)
        :return: NA
        """

        # Removing the node from the root list
        self.remove_root(node)

        # Adding the node as a child of new_parent_node
        new_parent_node.add_child(node)

        # Updating number of marked nodes, if node was marked
        if node.mark:
            self.num_marks -= 1

        return

    def union(self, other):
        """
        Creates a union of two Fibonacci Heaps into one by simply concatenating and extending the root list.
        Function also updates the new Fibonacci Heap information (min node, num_nodes, num_trees, num_marked_nodes)

        :param other: the other Fibonacci Heap
        :type FibonacciHeap (defined class)
        :return: NA
        """

        # If the other Fibonacci Heap is empty, no concatenation necessary
        if other.min is None:
            return

        # If this Fibonacci Heap is empty
        # Just taking on the characteristics of the other Fibonacci Heap
        if self.min is None:
            self.min = other.min
        else:
            self.min.right.left = other.min.left
            other.min.left.right = self.min.right
            self.min.right = other.min
            other.min.left = self.min

            # Identifying and assigning the correct min node of the new Fibonacci Heap
            if other.min.key < self.min.key:
                self.min = other.min

        # Updating new Fibonacci Heap's characteristics
        self.num_nodes += other.num_nodes
        self.num_trees += other.num_trees
        self.num_marks += other.num_marks

        return

    def decrease_key(self, node, decreased_key):
        """
        Function to decrease a node's key
        This action changes the priority and, if necessary, position of the node in the Fibonacci Heap
        If the change in key violates Fibonacci Heap requirements, the nodes are cut and repositioned, but only until
        requirements are restored.
        Min value of Fibonacci Heap is updated if necessary

        :param node: node whose key need to be reassigned to decreased value
        :type Node (defined class)
        :param decreased_key: new decreased key value
        :type Float
        :return: NA
        """

        # Check to make sure the key is being decreased and not increased
        if decreased_key > node.key:
            raise ValueError('new key is greater than current key')

        # Updating node with new decreased key
        node.key = decreased_key

        # Comparing with parent node to check if the node needs to be cut and repositioned
        parent_node = node.parent
        if parent_node and node.key < parent_node.key:
            self.cut(node, parent_node)
            self.cascading_cut(parent_node)

        # Updating min node of the Fibonacci Heap, if necessary
        if node.key < self.min.key:
            self.min = node

        return

    def cut(self, node, parent_node):
        """
        Cuts a given node from its parent node and makes it a root node
        Action used on nodes whose keys are decreased or are marked and have a child not cut

        :param node: node that needs to be cut and repositioned as a root node
        :type Node (defined class)
        :param parent_node: node whose child node needs to be cut
        :type Node (defined class)
        :return: NA
        """

        # Unmarking the node because it is being repositioned
        if node.mark:
            self.num_marks -= 1
            node.mark = False

        # Removes the node and makes it a root node
        parent_node.remove_child(node)
        self.add_root(node)
        node.parent = None

        return

    def cascading_cut(self, node):
        """
        Recursively implements the cut function to correctly reposition nodes in the Fibonacci Heap
        Cuts nodes and makes them root nodes until an unmarked node is encountered
        Marks the unmarked node since one of its child nodes was cut

        :param node: node checked for a cascading cut
        :type Node (defined class)
        :return: NA
        """

        # Checks if the node has a parent node
        # Ensure it is not a root node, since root nodes are not cut
        parent_node = node.parent
        if parent_node:
            # If an unmarked node is encountered
            if not node.mark:
                node.mark = True
                self.num_marks += 1
                return

            # If the node is marked, the node is cut
            # Recursively does the same check for parent and grandparent nodes
            self.cut(node, parent_node)
            self.cascading_cut(parent_node)

        return

    def delete(self, node):
        """
        Deletes a given node from the Fibonacci Heap
        The key of the node is decreased to negtaive infinity and is then extracted

        :param node: node to be deleted from the Fibonacci Heap
        :type Node (defined class)
        :return: NA
        """

        # Decrease the key of the node to negative infinity
        self.decrease_key(node, -math.inf)

        # Extract the node since it now hold the smallest key
        self.extract_min()

        return
