# 程序测试

def add(x,y):
    return x+y

class Sentence:
    def __init__(self,text):
        self.text = text

    def length(self):
        return len(self.text)

    def word_counts(self):
        return self.text.split()

    def sentence_counts(self):
        return self.text.upper()