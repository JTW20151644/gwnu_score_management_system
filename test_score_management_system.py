import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestScoreManagementSystem(unittest.TestCase):

    def test_constructor(self):
        sms = ScoreManagementSystem()
        self.assertIsNotNone(sms)

    def test_read_1(self):
        m_open = mock_open(read_data="가123,가나다,90,1\n")

        with patch('score_management_system.open',m_open):
            sms = ScoreManagementSystem()
            self.assertEqual(1, sms.read('score_data.csv'))

        m_open.assert_called_with('score_data.csv', 'rt', encoding="utf=8")

    def test_read_2(self):
        m_open = mock_open(read_data="가123,가나다,90,1\n나234,나다라,80,2\n\n")

        with patch('score_management_system.open', m_open):
            sms = ScoreManagementSystem()
            self.assertEqual(2, sms.read('score_data1.csv'))

    def test_read_3(self):
        m_open = mock_open(read_data="가123,가나다,90,1\n나234,나다라,80,2\n다345,다라마,75,3\n")

        with patch('score_management_system.open', m_open):
            sms = ScoreManagementSystem()
            self.assertEqual(3, sms.read('score_data1.csv'))

if __name__ == "__main__":
    unittest.main()
