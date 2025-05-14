class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    """Expression tree implementation"""

    def __init__(self):
        self.root = None

    @classmethod
    def from_infix(cls, tokens):
        def precedence(op):
            if op in ('+', '-'):
                return 1
            elif op in ('*', '/'):
                return 2
            return 0

        def is_operator(token):
            return token in '+-*/'

        def infix_to_postfix(tokens):
            output = []
            stack = []
            for token in tokens:
                if token.isalnum():
                    output.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()  # remove '('
                elif is_operator(token):
                    while stack and precedence(stack[-1]) >= precedence(token):
                        output.append(stack.pop())
                    stack.append(token)
            while stack:
                output.append(stack.pop())
            return output

        def build_tree(postfix):
            stack = []
            for token in postfix:
                if is_operator(token):
                    right = stack.pop()
                    left = stack.pop()
                    node = TreeNode(token)
                    node.left = left
                    node.right = right
                    stack.append(node)
                else:
                    stack.append(TreeNode(token))
            return stack[0]

        postfix = infix_to_postfix(tokens)
        tree = cls()
        tree.root = build_tree(postfix)
        return tree

#  Test cases
if __name__ == "__main__":
    # Test 1: Simple addition (2 + 3)
    tree1 = ExpressionTree.from_infix(['2', '+', '3'])
    print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # True

    # Test 2: Operator precedence (2 + 3 * 4)
    tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
    print(tree2.root.value == '+' and tree2.root.right.value == '*')  # True

    # Test 3: Parentheses (2 + 3) * 4
    tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
    print(tree3.root.value == '*' and tree3.root.left.value == '+')  # True

    # Test 4: Variables (x + y * z)
    tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
    print(tree4.root.value == '+' and tree4.root.right.value == '*')  # True

    # Test 5: Nested expressions ((a + b) / (c - d))
    tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
    print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')  # True
