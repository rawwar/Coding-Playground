class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        curr_node = self
        while(True):
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right
            return self

    
    def contains(self, value):
        curr_node = self
        while(curr_node):
            if value < curr_node.value:
                curr_node= curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                return True
        return False
    
    def remove(self, value,parent_node=None):
        curr_node = self
        while(curr_node):
            if value < curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.left
            elif value > curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.right
            else:
                if curr_node.left and curr_node.right:
                    curr_node.value = curr_node.right.get_min_value()
                    curr_node.right.remove(curr_node.value, curr_node)
                elif parent_node is None:
                    if curr_node.left:
                        curr_node.value = curr_node.left.value
                        curr_node.left = curr_node.left.left
                        curr_node.right = curr_node.left.right
                    elif curr_node.right:
                        curr_node.value = curr_node.right.value
                        curr_node.left = curr_node.right.left
                        curr_node.right = curr_node.right.right
                    else:
                        curr_node = None
                elif parent_node.left == curr_node:
                    parent_node.left = curr_node.left if curr_node.left else curr_node.right
                elif parent_node.right == curr_node:
                    parent_node.right = curr_node.left if curr_node.left else curr_node.right
    
    def get_min_value(self):
        curr_node = self
        while(curr_node.left):
            curr_node = curr_node.left
        return curr_node.value