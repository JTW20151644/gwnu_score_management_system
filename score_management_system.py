from score import Score

def key_totalscore(item):
    return item[1].totalscore

class ScoreManagementSystem:
    
    def __init__(self):
        self._scores = {}

    def read(self, score_data_file):
        with open(score_data_file, 'rt', encoding='utf=8') as fo:
          data = fo.read()
          lines = data.strip().split('\n')

        num = 0
        for line in lines:
            num = num + 1
            self._scores[num] = Score(line.strip())

        return len(self._scores)
    
    def _make_scores_string(self, scores):
        rank_asc = len(self._scores)
        rank_des = 1
        result = ""
        for key, item in scores:
            #result = result + str(key) + ","
            result = result + item.sid + ",이름 :"
            result = result + item.name + ",국어점수 :"
            result = result + str(int(item.scoree)) + ", 영어점수 :"
            result = result + str(int(item.scoree_2)) + ",수학점수 :"
            result = result + str(int(item.scoree_3)) + ", 총점 :"
            result = result + str(int(item.totalscore)) +",평균 :"
            result = result + str(int(item.avg)) +"\n"
        return result.strip()

    def sort(self, order_key="register", order_way="asc"):
        if order_key == "register" and order_way == "asc":
            sorted_scores = sorted(self._scores.items())
        elif order_key == "register" and order_way == "des":
            sorted_scores = sorted(self._scores.items(), reverse=True)
        elif order_key == "totalscore" and order_way == "asc":
            sorted_scores = sorted(self._scores.items(), key=key_totalscore)
        elif order_key == "totalscore" and order_way == "des":
            sorted_scores = sorted(self._scores.items(), key=key_totalscore, reverse=True)


        result = self._make_scores_string(sorted_scores)
        return result

    def write(self, file_name, order_key="register", order_way="asc"):
        with open(file_name, 'wt', encoding="utf=8") as fo:
            result = self.sort(order_key, order_way)
            fo.write(result)
