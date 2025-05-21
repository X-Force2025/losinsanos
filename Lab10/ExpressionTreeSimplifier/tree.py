class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def simplify_expression_tree(root):
    """
    Simplifies constant subtrees in a binary expression tree.
    """
    if root is None:
        return None

    # Recursively simplify left and right subtrees
    root.left = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    # Try to evaluate if both children are constants (digits)
    if root.left and root.right and root.left.value.isdigit() and root.right.value.isdigit():
        a = int(root.left.value)
        b = int(root.right.value)
        op = root.value

        try:
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    return root
                result = a // b
            else:
                return root
            return Node(str(result))
        except:
            return root
    return root
