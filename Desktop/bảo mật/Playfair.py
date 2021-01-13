class Playfair:
    keys = "abcdefhiklmnopqrstuvwxyz"
    def encrypt(self,key,plaintext):
        str = self.keys
        for x in key:
            str = str.replace(x, "")
        D = {}
        str1 = ""
        for x in key:
            if x not in D.keys():
                str1 += x
                D[x] = True
        str = str1 + str
        print(str)
if __name__ == '__main__':
    plaintext="anhyeuemnhieulam"
    key="likefal"
    Playfair = Playfair()
    Playfair.encrypt(key,plaintext)