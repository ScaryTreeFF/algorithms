class TreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.data = value
        if parent is None:
            self.parent = self
        else:
            self.parent = parent


class BinaryTree:
    def __init__(self):
        self.root = None

    def put(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._put(value, self.root)

    def _put(self, value, node):
        if (value < node.data):
            if (node.left is not None):
                self._put(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if (node.right is not None):
                self._put(value, node.right)
            else:
                node.right = TreeNode(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if (value == node.data):
            return node
        elif (value < node.data and node.left is not None):
            self._find(value, node.left)
        elif (value > node.value and node.right is not None):
            self._find(value, node.right)
        else:
            return None

    def print_tree(self):
        if self.root is not None:
            self._print(self.root)
        else:
            return None

    def _print(self, node):
        if node.left is not None:
            self._print(node.left)

        print("'" + node.data + "'")

        if node.right is not None:
            self._print(node.right)

# def next(self, node):
#     pass
# def delete(self, value):
#     node = self.find(value)
#     if node == None:
#         print(value, "isn't in the tree")
#     else:
#         if node.right == None:
#             if node.left == None:
#                 if node.data < node.parent.data:
#                     node.parent.left = None
#                     del node
#                 else:
#                     node.parent.right = None
#                     del node
#             else:
#                 node.data = node.left.data
#                 node.left = None
#         else:
#             value = self.next(node)
#             node.data = value.data
#             value = None
