class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def bfs_is_tree_balanced(tree_head):

    if (tree_head.left is None) & (tree_head.right is None):
        return True

    visited = []
    to_visit = [tree_head]
    current_node = tree_head
    current_level = 0
    lowest_leaf = 0
    highest_leaf = 0

    while len(to_visit) != 0:

        if current_node.left is not None:
            to_visit.append(current_node.left)
        else:
            if current_level > highest_leaf:
                highest_leaf = current_level

        if current_node.right is not None:
            to_visit.append(current_node.right)
        else:
            if current_level > highest_leaf:
                highest_leaf = current_level

        current_level += 1
        current_node = to_visit.pop()

    if (highest_leaf - lowest_leaf) <= 1:
        return True
    else:
        return False


def dfs_balanced_tree(tree_head):

    if tree_head is None:
        return True

    depths = set()
    nodes = []
    nodes.append((tree_head, 0))

    while len(nodes):
        node, depth = nodes.pop()

        if node.left is not None:
            nodes.append((node.left, depth + 1))
        if node.right is not None:
            nodes.append((node.right, depth + 1))
        if (not node.left) and (not node.right):
            depths.add(depth)

    max_depth = max(depths)
    min_depth = min(depths)

    return max_depth - min_depth <= 1


node = BinaryTreeNode(1)
node.insert_left(2)
node.insert_right(3)
node.left.insert_left(4)
node.right.insert_right(5)
node.right.right.insert_right(6)
node.right.right.right.insert_left(7)

print(dfs_balanced_tree(node))
