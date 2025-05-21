def test_tree_structure():
    def check(node, value, left=None, right=None):
        return node.value == value and                (left is None or node.left.value == left) and                (right is None or node.right.value == right)

    tokens1 = ['2', '3', '+']
    t1 = build_expression_tree(tokens1)
    print(check(t1, '+', '2', '3'))  # True

    tokens2 = ['2', '3', '4', '*', '+']
    t2 = build_expression_tree(tokens2)
    print(check(t2, '+', '2', '*'))

    tokens3 = ['1', '2', '+', '3', '4', '-', '*']
    t3 = build_expression_tree(tokens3)
    print(check(t3, '*', '+', '-'))

    tokens4 = ['a', 'b', 'c', '*', '+']
    t4 = build_expression_tree(tokens4)
    print(check(t4, '+', 'a', '*'))

    tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
    t5 = build_expression_tree(tokens5)
    print(check(t5, '/', '+', '-'))

# Ejecutar pruebas
test_tree_structure()
