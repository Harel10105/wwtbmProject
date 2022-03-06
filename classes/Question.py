import random
from random import randint

from HQ import *


class Question:
    def __init__(self, level):
        self.new_question = True
        self.two_option = True
        self.level = level
        hq = QH()
        qList = QH.get_questions(hq)
        self.level_question = QH.get_questions_level_return(hq, qList, self.level)
        self.question_index = random.randint(0, len(self.level_question) - 1)
        self.question = self.level_question[self.question_index]

    def get_question(self):
        str1 = self.question[1]
        return str1

    def get_50_50(self):
        if self.two_option:
            self.two_option = False
            half = []
            temp = []
            ans = self.question[2:-1]
            for answer in ans:
                if '$' in answer:
                    half.append(answer)
                else:
                    temp.append(answer)
            second = random.randint(0, len(temp) - 1)
            half.append(temp.pop(second))
            print(ans)
            return half
        return None

    def get_other_question(self):
        if self.new_question:
            self.new_question = False
            new_question_index = random.randint(0, len(self.level_question) - 1)
            while new_question_index == self.question_index:
                new_question_index = random.randint(0, len(self.level_question) - 1)
            self.question = self.level_question[new_question_index]
            return self.question
        return None

    def get_answer(self):
        ans = self.question[2:-1]
        for answer in ans:
            if '$' in answer:
                return answer[:-1]

    def get_max_time(self):
        if int(self.level_question) <= 5:
            return 20
        return 60