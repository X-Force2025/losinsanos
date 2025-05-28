# Challenge 3: Validate BST Property

## Prompt Engineering (If applicable)
**Prompt:** Determine if a binary tree is a valid Binary Search Tree (BST).

## Code Developed
See `main.py` for implementation and tests.

## Explanation (Line-by-Line with Comments)

```python
class TreeNode:
    """A node in a binary tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```
Defines a node of the binary tree with `val`, `left`, and `right`.

```python
def is_valid_bst(root):
    return validate(root, float('-inf'), float('inf'))
```
Entry function to check if the BST is valid. Initializes bounds from -infinity to +infinity.

```python
def validate(node, min_val, max_val):
    if not node:
        return True
```
If the current node is `None`, return `True` (base case for recursion).

```python
    if not (min_val < node.val < max_val):
        return False
```
Check if the node’s value lies within the valid range.

```python
    left_is_valid = validate(node.left, min_val, node.val)
    right_is_valid = validate(node.right, node.val, max_val)
    return left_is_valid and right_is_valid
```
Recursively validate left and right subtrees with updated bounds.

## Test Cases

```python
# Test 1: Valid BST
tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)
print(is_valid_bst(tree1) == True)  # ✅

# Test 2: Invalid BST (Right child violates rule)
tree2 = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(6)
print(is_valid_bst(tree2) == False)  # ❌

# Test 3: Valid larger BST
tree3 = TreeNode(10)
tree3.left = TreeNode(5)
tree3.right = TreeNode(15)
tree3.right.left = TreeNode(12)
tree3.right.right = TreeNode(20)
print(is_valid_bst(tree3) == True)  # ✅

# Test 4: Invalid BST (Left child > root)
tree4 = TreeNode(10)
tree4.left = TreeNode(12)
tree4.right = TreeNode(15)
print(is_valid_bst(tree4) == False)  # ❌
```

## Directory Structure

```
bst_validator/
├── main.py       # Implementation and test cases
└── README.md     # Problem statement, explanation, and prompt
```
