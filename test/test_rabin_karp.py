import unittest
from rabin_karp import rabin_karp

class TestRabinKarp(unittest.TestCase):
    def test_result(self):
        haystack = "DEFBCCDEFG"
        needle = "EFB"
        q = 13
        expected = 1
        result = rabin_karp(haystack, needle, q)
        self.assertEqual(result, expected)

    def test_no_result(self):
        haystack = "DEFBCCDEFG"
        needle = "XOM"
        q = 13
        expected = -1
        result = rabin_karp(haystack, needle, q)
        self.assertEqual(result, expected)

    def test_collision(self):
        haystack = "ABC" * 100  
        needle1 = "ABC"
        needle2 = "BAC"  
        q = 101  
        expected = 0  
        result = rabin_karp(haystack, needle1, q)
        self.assertEqual(result, expected)

        expected = -1  
        result = rabin_karp(haystack, needle2, q)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
