class GenericTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class GenericTree:
    def __init__(self, root=None):
        self.root = root

    def height(self):
        def _height(node):
            if not node:
                return -1
            if not node.children:
                return 0
            child_heights = [_height(child) for child in node.children]
            return 1 + max(child_heights)

        return _height(self.root)

# Test cases
empty_tree = GenericTree(None)
print(empty_tree.height() == -1)

single = GenericTree(GenericTreeNode('A'))
print(single.height() == 0)

linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.height() == 2)

balanced_root = GenericTreeNode('A')
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')
balanced_root.children = [b, c, d]
b.children = [e, f, g]
d.children = [h]
balanced_tree = GenericTree(balanced_root)
print(balanced_tree.height() == 2)

unbalanced_root = GenericTreeNode('A')
ub_b = GenericTreeNode('B')
ub_c = GenericTreeNode('C')
ub_d = GenericTreeNode('D')
unbalanced_root.children = [ub_b]
ub_b.children = [ub_c]
ub_c.children = [ub_d]
unbalanced_tree = GenericTree(unbalanced_root)
print(unbalanced_tree.height() == 3)
