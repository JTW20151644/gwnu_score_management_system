import unittest
from score import Score

class TestScore(unittest.TestCase):
    def test_constructor(self):
        my_score = Score("1,강호민,85,90,95")
        self.assertIsNotNone(my_score)

    def test_sid(self):
        my_score = Score("1,강호민,85,90,95")
        self.assertEqual("1", my_score.sid)

    def test_sid_2(self):
        my_score = Score("2,김광호,80,70,60")
        self.assertEqual('2', my_score.sid)

if __name__ == "__main__":
    unittest.main()



