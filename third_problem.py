from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: int = None
    right: int = None


def find_lca(root, node1, node2):

    """

    :param root:
    :param node1:
    :param node2:
    :return:
    :memory: it calls itself two times with dividing the tree in left and write, since it is a recursive function each
    call will push a new function call in memory


    """

    if not root:
        return

    if root.value == node1 or root.value == node2:
        return root

    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    if left_lca and right_lca:
        return root

    if left_lca:
        return left_lca
    return right_lca


