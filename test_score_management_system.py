import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestScoreManagementSystem(unittest.TestCase):

    def setUp(self):
        self.m_open_1 = mock_open(read_data="1,강호민,85,90,95\n")
        self.m_open_2 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n\n")
        self.m_open_3 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n3,김민식,75,85,80\n")

    def test_constructor(self):
        sms = ScoreManagementSystem()
        self.assertIsNotNone(sms)

    def test_read_1(self):

        with patch('score_management_system.open',self.m_open_1):
            sms = ScoreManagementSystem()
            self.assertEqual(1, sms.read('score_data.csv'))

        self.m_open_1.assert_called_with('score_data.csv', 'rt', encoding="utf=8")

    def test_read_2(self):

        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            self.assertEqual(2, sms.read('score_data1.csv'))

    def test_read_3(self):
        
        with patch('score_management_system.open', self.m_open_3):
            sms = ScoreManagementSystem()
            self.assertEqual(3, sms.read('score_data1.csv'))

    def test_sort_1(self):
        with patch('score_management_system.open', self.m_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')       
          #  result = sms.sort_by_register(order='asc')
            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,1,강호민,85,90,95,270', result)

    def test_sort_2(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')       
            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,1,강호민,85,90,95,270\n2,2,김광호,80,70,60,210', result)

    def test_sort_3(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort(order_key="register", order_way="des")
            self.assertEqual('2,2,김광호,80,70,60,210\n1,1,강호민,85,90,95,270', result)


    def test_sort_4(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "asc")
            self.assertEqual('2,2,김광호,80,70,60,210\n1,1,강호민,85,90,95,270', result)

    def test_sort_5(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "des")
            self.assertEqual('1,1,강호민,85,90,95,270\n2,2,김광호,80,70,60,210', result)

    def test_sort_6(self):
        with patch('score_management_system.open', self.m_open_3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "asc")
            self.assertEqual('2,2,김광호,80,70,60,210\n3,3,김민식,75,85,80,240\n1,1,강호민,85,90,95,270', result)

    def test_sort_7(self):
        with patch('score_management_system.open', self.m_open_3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "des")
            self.assertEqual('1,1,강호민,85,90,95,270\n3,3,김민식,75,85,80,240\n2,2,김광호,80,70,60,210', result)
    

if __name__ == "__main__":
    unittest.main()
