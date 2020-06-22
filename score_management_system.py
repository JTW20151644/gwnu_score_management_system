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
        result = ""
        for key, item in scores:
            result = result + str(key) + ","
            result = result + item.sid + ","
            result = result + item.name + ","
            result = result + str(int(item.scoree)) + ","
            result = result + str(int(item.scoree_2)) + ","
            result = result + str(int(item.scoree_3)) + ","
            result = result + str(int(item.totalscore)) +"\n"
        return result.strip()

    def sort(self, order_key="register", order_way="asc"):
        if order_key == "register" and order_way == "asc":
            pass

    def sort_by_register(self, order="asc"):
        if order == "asc":
            sorted_scores = sorted(self._scores.items())
        elif order == "des":
            sorted_scores = sorted(self._scores.items(), reverse=True)

        result = self._make_scores_string(sorted_scores)
        return result

    def sort_by_totalscore(self, order="asc"):
        if order == "asc":
            sorted_scores = sorted(self._scores.items(), key = key_totalscore)
        elif order == "des":
            sorted_scores = sorted(self._scores.items(), key= key_totalscore, reverse=True)

        result = self._make_scores_string(sorted_scores)
        return result