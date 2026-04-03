count1 = 0
def recursion(s,l,r):
    global count1
    count1 = count1+1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s,l+1,r-1)
def isPalindrome(s):
    return recursion(s,0,len(s)-1)

n = int(input())
for i in range(n):
    s=input()
    a=isPalindrome(s)
    print(a,count1)
    count1 = 0