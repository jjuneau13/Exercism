import re
class PhoneNumber:
    def __init__(self, number):
        if re.search("[a-zA-Z]", number):
            raise ValueError("letters not permitted")
        if re.search("[^a-zA-Z0-9().+ -]", number):
            raise ValueError("punctuations not permitted")
        self.number = ''.join(re.findall('[0-9]', number))
        self.area_code = self.number[-10:-7]
        if len(self.number) < 10:
            raise ValueError('must not be fewer than 10 digits')
        if len(self.number) > 11:
            raise ValueError('must not be greater than 11 digits')
        if len(self.number) == 11 and self.number[0] != '1':
            raise ValueError('11 digits must start with 1')
        if self.number[-7] == '0':
            raise ValueError("exchange code cannot start with zero")
        if self.number[-7] == '1':
            raise ValueError("exchange code cannot start with one")
        if self.number[-10] == '0':
            raise ValueError("area code cannot start with zero")
        if self.number[-10] == '1':
            raise ValueError("area code cannot start with one")
        if len(self.number) == 11:
            self.number = self.number[1:]
    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}"