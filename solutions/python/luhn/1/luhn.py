class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) <= 1:
            return False
        result = 0
        for x in range(-1, -len(self.card_num) - 1, -1):
            if not self.card_num[x].isdigit():
                return False
            temp = 0
            if x%2 == 0:
                temp += int(self.card_num[x]) * 2
            else:
                temp += int(self.card_num[x])
            if temp >= 10:
                temp -= 9
            print(temp)
            result += temp
        print(result)
        return result % 10 == 0