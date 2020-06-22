from score_management_system import ScoreManagementSystem

if __name__ == "__main__":
    sms = ScoreManagementSystem()
    print("-----------------------------------")
    sms.read('score.csv')
    print(sms.sort("totalscore", "des"))
    print("-----------------------------------")
    sms.write('result.csv', "totalscore", "des")