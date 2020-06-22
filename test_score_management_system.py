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

        self.m_write_open_1 = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open_1.side_effect = [self.m_open_3.return_value, self.m_w]

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
            self.assertEqual('1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90', result)

    def test_sort_2(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')       
            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90\n2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70', result)

    def test_sort_3(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort(order_key="register", order_way="des")
            self.assertEqual('2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70\n1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90', result)


    def test_sort_4(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "asc")
            self.assertEqual('2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70\n1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90', result)

    def test_sort_5(self):
        with patch('score_management_system.open', self.m_open_2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "des")
            self.assertEqual('1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90\n2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70', result)

    def test_sort_6(self):
        with patch('score_management_system.open', self.m_open_3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "asc")
            self.assertEqual('2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70\n3,이름 :김민식,국어점수 :75, 영어점수 :85,수학점수 :80, 총점 :240,평균 :80\n1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90', result)

    def test_sort_7(self):
        with patch('score_management_system.open', self.m_open_3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')   

            result = sms.sort("totalscore", "des")
            self.assertEqual('1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90\n3,이름 :김민식,국어점수 :75, 영어점수 :85,수학점수 :80, 총점 :240,평균 :80\n2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70', result)

    def test_write_1(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv')
        
        self.m_w.write.assert_called_with("1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90\n2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70\n3,이름 :김민식,국어점수 :75, 영어점수 :85,수학점수 :80, 총점 :240,평균 :80")

    def test_write_2(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'register', "des")
        
        #self.m_w.write.assert_called_with("1,1,강호민,85,90,95,270\n2,2,김광호,80,70,60,210\n3,3,김민식,75,85,80,240")
        self.m_w.write.assert_called_with("3,이름 :김민식,국어점수 :75, 영어점수 :85,수학점수 :80, 총점 :240,평균 :80\n2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70\n1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90")
    def test_write_3(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'totalscore', "asc")
        
        self.m_w.write.assert_called_with("2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70\n3,이름 :김민식,국어점수 :75, 영어점수 :85,수학점수 :80, 총점 :240,평균 :80\n1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90")

    def test_write_4(self):
        with patch('score_management_system.open', self.m_write_open_1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'totalscore', "des")
        
        self.m_w.write.assert_called_with("1,이름 :강호민,국어점수 :85, 영어점수 :90,수학점수 :95, 총점 :270,평균 :90\n3,이름 :김민식,국어점수 :75, 영어점수 :85,수학점수 :80, 총점 :240,평균 :80\n2,이름 :김광호,국어점수 :80, 영어점수 :70,수학점수 :60, 총점 :210,평균 :70")
if __name__ == "__main__":
    unittest.main()
