from tree import Node, simplify_expression_tree

def run_tests():
    # Test 1: All constants
    node1 = Node('+')
    node1.left = Node('2')
    node1.right = Node('3')
    result1 = simplify_expression_tree(node1)
    assert result1.value == '5' and result1.left is None and result1.right is None

    # Test 2: Mixed variables and constants
    node2 = Node('+')
    node2.left = Node('x')
    node2.right = Node('3')
    result2 = simplify_expression_tree(node2)
    assert result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3'

    # Test 3: Partial simplification
    node3 = Node('+')
    node3.left = Node('*')
    node3.right = Node('-')
    node3.left.left = Node('2')
    node3.left.right = Node('3')
    node3.right.left = Node('8')
    node3.right.right = Node('3')
    result3 = simplify_expression_tree(node3)
    assert result3.value == '+' and result3.left.value == '6' and result3.right.value == '5'

    # Test 4: All variables
    node4 = Node('+')
    node4.left = Node('x')
    node4.right = Node('y')
    result4 = simplify_expression_tree(node4)
    assert result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y'

    # Test 5: Complex nested simplification
    node5 = Node('+')
    node5.left = Node('/')
    node5.right = Node('*')
    node5.left.left = Node('10')
    node5.left.right = Node('2')
    node5.right.left = Node('z')
    node5.right.right = Node('4')
    result5 = simplify_expression_tree(node5)
    assert result5.value == '+' and result5.left.value == '5' and result5.right.left.value == 'z'

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
