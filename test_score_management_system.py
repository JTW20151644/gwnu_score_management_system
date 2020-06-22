import unittest
from score_management_system import ScoreManagementSystem

class TestScoreManagementSystem(unittest.TestCase):

    def test_constructor(self):
        sms = ScoreManagementSystem()
        self.assertIsNotNone(sms)

    def test_read_1(self):
        sms = ScoreManagementSystem()
        self.assertEqual(1, sms.read('score_data.csv'))

    def test_read_2(self):
        sms = ScoreManagementSystem()
        self.assertEqual(2, sms.read('score_data1.csv'))

if __name__ == "__main__":
    unittest.main()
