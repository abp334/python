# wap to create class string and make method to find 
# vowels
# consonants
# spaces
# uppercase
# lowercase
class String:
    def __init__(self,s):
        self.s = s
    def vowels(self):
        vcount = 0
        for i in self.s:
            if i in ["a","e","i","o","u","A","E","I","O","U"]:
                vcount += 1
        return vcount
    def consonant(self):
        ccount = 0
        for i in self.s:
            if i.isalpha() and i not in ["a","e","i","o","u","A","E","I","O","U"]:
                ccount += 1
        return ccount
    def spaces(self):
        scount = 0
        for i in self.s:
            if i.isspace():
                scount += 1
        return scount
    def uppercase(self):
        ucount = 0
        for i in self.s:
            if i.isupper():
                ucount += 1
        return ucount
    def lowercase(self):
        lcount = 0
        for i in self.s:
            if i.islower():
                lcount += 1
        return lcount
    def display(self):
        print("Vowels:",self.vowels())
        print("Consonants:",self.consonant())
        print("Spaces:",self.spaces())
        print("Uppercase:",self.uppercase())
        print("Lowercase:",self.lowercase())
s = input("Enter your string: ")
st = String(s)
st.display()

