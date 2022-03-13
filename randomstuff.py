class Class1:
    def __init__(self, txt):
        self.txt = txt

    def random(self):
        for end in range(len(self.txt)-1):
            s = ""
            for ind in range(len(self.txt)-1):
                if ind - end < 0:
                    s = self.txt[len(self.txt)-1 - ind] + " " + s
                else:
                    s += self.txt[ind-end] + " "
            print(s)

c = Class1("Left")
c.random()