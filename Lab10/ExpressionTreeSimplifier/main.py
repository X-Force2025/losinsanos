from tree import Node, simplify_expression_tree

# Example use
if __name__ == "__main__":
    node = Node('+')
    node.left = Node('2')
    node.right = Node('3')
    simplified = simplify_expression_tree(node)
    print(f"Simplified value: {simplified.value}")
