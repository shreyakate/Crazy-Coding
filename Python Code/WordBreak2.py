def wordBreak2(s, wordDict):
    memo = {len(s): ['']}
    def sentences(i):
        if i not in memo:
        	for j in range(i+1, len(s)+1):
        		if s[i:j] in wordDict:
        			for tail in sentences(j):
        				print (tail and ' ' + tail)
        				memo[i].append((tail and ' ' + tail))

        return memo[i]

    memo1 = {len(s): ['']}
    def sentences1(i):
        if i not in memo1:
            memo1[i] = [s[i:j] + (tail and ' ' + tail) for j in range(i+1, len(s)+1)  if s[i:j] in wordDict for tail in sentences1(j)]
            print i, memo1[i]
        return memo1[i]

    print sentences(0)
    print sentences1(0)

print wordBreak2("catsanddog", ["cat", "cats", "and", "sand", "dog"])