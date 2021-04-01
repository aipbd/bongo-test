from pytest import fixture

from third_problem import Node, find_lca


class TestThirdProblem:
    @fixture
    def test_data(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        return root

    def test_find_lca(self, test_data):
        assert find_lca(test_data, 9, 5).value == 2
        assert find_lca(test_data, 8, 7).value == 1

        assert find_lca(test_data, 1, 1).value == 1
        assert find_lca(test_data, 6, 6).value == 6
        assert not find_lca(test_data, 100, 200)
