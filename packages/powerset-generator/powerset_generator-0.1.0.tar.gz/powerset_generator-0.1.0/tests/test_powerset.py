import unittest

from powerset_generator import subsets


class TestPowerset(unittest.TestCase):
    three_list: list[int] = [1, 2, 3]

    three_repetition: list[int] = [1, 2, 3, 1, 2, 2, 3, 3, 3]

    empty_set: set[int] = set()

    power_three: list[set[int]] = [
        empty_set,
        {1},
        {2},
        {3},
        {1, 2},
        {1, 3},
        {2, 3},
        {1, 2, 3},
    ]

    def test_powerset(self) -> None:
        result: list[set[int]] = [s for s in subsets(self.three_list)]

        # AssertCountEqual requires elements to be hashable, which they
        # aren't in our case. So we do it the slow way
        self.assertEqual(len(result), 2 ** len(self.three_list))
        self.assertTrue(
            all(result.count(i) == self.power_three.count(i) for i in result)
        )

    def test_powerset_repeated(self) -> None:
        result: list[set[int]] = [s for s in subsets(self.three_repetition)]

        # AssertCountEqual requires elements to be hashable, which they
        # aren't in our case. So we do it the slow way
        self.assertEqual(len(result), 2 ** len(self.three_list))
        self.assertTrue(
            all(result.count(i) == self.power_three.count(i) for i in result)
        )

    def test_cardinality(self) -> None:
        vectors: list[tuple[int, list[int]]] = [
            (1, []),
            (1024, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            (16, [1, 2, 3, 4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]),
            # ( "ℵ_1", ["the natural numbers"]),
        ]

        for v in vectors:
            count = 0
            for _ in subsets(v[1]):
                count += 1

            self.assertEqual(v[0], count)


if __name__ == "__main__":
    unittest.main()
