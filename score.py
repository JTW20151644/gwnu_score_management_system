class Score:
    def __init__(self, data):
        items = data.split(',')

        self._sid = items[0]   #학번
        self._name = items[1]   #이름
        self._scoree = int(items[2])    #점수1
        self._scoree_2 = int(items[3])  #점수2
        self._scoree_3 = int(items[4])  #점수3

    @property
    def sid(self):
        return self._sid

    @property
    def name(self):
        return self._name

    @property
    def scoree(self):
        return self._scoree

    @property
    def scoree_2(self):
        return self._scoree_2

    @property
    def totalscore(self):
        return self._scoree + self._scoree_2 + self._scoree_3
