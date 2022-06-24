class AVLNode():
    """
    A class to store required data for individual AVL nodes
    Data members are being left public for now
    """
    def __init__(self, value):
        """
        Initializes a node with a provided value.
        Parent and child values initialized to None
        Parent and child values are tracked to make rotations easier
        Initializes balance_factor to 0
        """
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self._balance_factor = 0

class AVLTree():
    """
    Class to represent AVL Tree as a whole
    Contains public methods for addition, removal, and retrieval of a specific node
    Also contains other simple public methods, such as is_empty and get_size
    May also add traversal methods to practice different traversal algorithms
    Methods for calculating balance factor are private
    """
    def __init__(self, input_list=None) -> None:
        """
        Initializing an AVL Tree instance
        Accepts an optional input list to populate the AVL tree on initialization
        """
        if input_list:
            for item in input_list:         # The add_node method will take care of setting a value as the root
                self.insert_node(item)
        self.root = None
        self.size = 0
    
    def is_empty(self) -> bool:
        """Returns True if root is None, False otherwise"""
        if self.root:
            return False
        return True

    def get_size(self) -> int:
        """Returns size of AVL Tree"""
        return self.size

    def insert_node(self, value: object) -> None:
        """
        If tree is empty, sets new node as root of the tree
        Creates a new node and inserts it into the AVL Tree
        Calculates balance factor and rebalances the tree if necessary
        """
        if self.is_empty():
            self.root = AVLNode(value)
            return
        node = self.root
        while node.left_child or node.right_child:
            if value > node.value:
                if node.right_child:
                    node = node.right_child
                else:
                    new_node = AVLNode(value)
                    node.right_child = new_node
                    new_node.parent = node
                    break
            elif value < node.value:
                if node.left_child:
                    node = node.left_child
                else:
                    new_node = AVLNode(value)
                    node.left_child = new_node
                    new_node.parent = node
                    break
        return

    def delete_node(self, value: object) -> bool:
        """
        Searches for desired value in the tree
        Deletes that node, then performs rebalancing if necessary
        """
        pass

    def _rotate_right(self, center_node: AVLNode) -> None:
        """
        Takes center node of the rotation as input
        Changes pointers for the center node and connected nodes to rotate the tree
        """
        pass

    def _rotate_left(self, center_node: AVLNode) -> None:
        """
        Takes center node of rotation as input
        Changes pointers for the center node and connected nodes to rotate the tree
        """
        pass