# Author: John Landeholt [TA]
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    # "greather than" magic_method
    def __gt__(self, other):
        """Dictates whether self or other is greather"""
        # YOUR CODE HERE
        return None
    
    def find(self, data):
        """Search recursive in left and right node"""
        # YOUR CODE HERE
        return None
    
    def put(self, node):
        """Find position in left or right node recursively"""
        # YOUR CODE HERE
        return None
    
    def preorder(self, l):
        """(root, left, right)"""
        l.append(self.data)
        if self.left: self.left.preorder(l)
        if self.right: self.right.preorder(l)
        return l

    def inorder(self, l):
        if self.left: self.left.inorder(l)
        l.append(self.data)
        if self.right: self.right.inorder(l)
        return l
    
    def postorder(self, l):
        """(left, right, root)"""
        # YOUR CODE HERE
        return l

class Binary_search_tree:

    def __init__(self):
        self.root = None

    @staticmethod
    def build(self,l):
        """ Builds a tree from a list """
        tree = Binary_search_tree()
        for data in l:
            tree.put(data)
        return tree

    def put(self, data):
        """ Put a Node into the tree """
        if self.root:
            # YOUR CODE HERE
            pass
        else:
            # YOUR CODE HERE
            pass 

    def __contains__(self, data):
        """ Recurses down from the root-node """
        if self.root:
            # YOUR CODE HERE
            pass
        return False
    
    @property
    def inorder(self):
        if self.root:
            l = []
            return self.root.inorder(l)

    @property
    def preorder(self):
        # YOUR CODE HERE
        return None
    
    @property
    def postorder(self):
        # YOUR CODE HERE
        return None

if __name__ == "__main__":
    tree = Binary_search_tree.build([6,3,9,1,5,7,11])

    if 6 in tree:
        print('no.', 6, 'exists in the tree')
    if 12 not in tree:
        print('no.', 12, 'does not exist in the tree')
    if tree.inorder == [1,3,5,6,7,9,11]:
        print('inorder works as it should')
    if tree.postorder == [1,5,3,7,11,9,6]:
        print('postorder works as it should')