from score import Score

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

    def sort_by_register(self, order="asc"):
        if order == "asc":
            sorted_scores = sorted(self._scores.items())
        elif order == "des":
            sorted_scores = sorted(self._scores.items(), reverse=True)

        result = ""
        for key, item in sorted_scores:
            result = result + str(key) + ","
            result = result + item.sid + ","
            result = result + item.name + ","
            result = result + str(int(item.scoree)) + ","
            result = result + str(int(item.scoree_2)) + ","
            result = result + str(int(item.scoree_3)) + ","
            result = result + str(int(item.totalscore)) +"\n"
        return result.strip()