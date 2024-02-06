#given a binary string s,
#return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s
#or return false otherwise.
#For example, in s = "110100010" the longest continuous segment of 0's has length 3.
#Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
#The same applies if there is no 1's.
def main():
    s = "111100010"
    print(check(s))
def check(s):
    longZero = 0
    longOne = 0
    currentZero = 0
    currentOne = 0
    for char in s:
        if char == "1":
            currentOne+=1
            longOne = max(longOne, currentOne)
            currentZero = 0
        else:
            currentZero+=1
            longZero = max(longZero, currentZero)
            currentOne = 0
    if (longOne > longZero):
        return True
    return False
if __name__ == '__main__':
    main()