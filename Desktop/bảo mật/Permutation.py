class permutation:
    def encrypt(self,n,plaintext):
        result=''
        for i in range(n):
            for j in range(len(plaintext)):
                if j%n == i:
                    result += plaintext[j]
            result += " "
        return result
if __name__ == '__main__':
    plaintext = input()
    n = int(input())
    permutation = permutation()
    print(permutation.encrypt(n,plaintext))