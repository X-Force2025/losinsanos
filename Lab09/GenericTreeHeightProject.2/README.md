# Generic Tree Height Project

## Description
This project implements a method to calculate the height (maximum depth) of a generic tree using recursion.

## Files
- `tree_height.py`: Contains the `GenericTree` and `GenericTreeNode` class implementations and test cases.

## How it works
- If the tree is empty (`root` is `None`), height is `-1`.
- If the node is a leaf (no children), height is `0`.
- Otherwise, recursively calculate the height of each child and return `1 + max(children heights)`.

## Diagram (Conceptual)
```
        A
       /|\
      B C D
     /|\   \
    E F G    H
```

## Test Cases
- Empty tree: should return -1
- Single node: should return 0
- Linear tree: should return 2
- Balanced tree: should return 2
- Unbalanced tree: should return 3

## Language
Python 3
