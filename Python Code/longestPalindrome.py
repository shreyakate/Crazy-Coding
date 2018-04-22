def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n] * n
    res = ''
    for i in range(n-1,-1,-1):
        for j in range(i, n):
            print i , j , s[i], s[j], s[i] ==s[j]
            dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
            
            if dp[i][j] and ( not res or j- i+1> len(res)):
                print s[i:j+2]
                res = s[i:j+1]

    print dp 

    print res

longestPalindrome('abaaba')