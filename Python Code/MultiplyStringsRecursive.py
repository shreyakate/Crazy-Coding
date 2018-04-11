class Solution(object):
    def addStrings(self, num1, num2):
        if not num1 or not num2: return '0'
        carry, i, j= 0, len(num1)-1, len(num2)-1
        res = ''
        while i>=0 or j>=0:
            if i>=0 and j>=0:
                res = str((int(num1[i]) + int(num2[j]) + carry)%10) + res
                carry = (int(num1[i]) + int(num2[j]) + carry)/10
                i -= 1
                j -= 1
            elif j>=0 and i<=0:
                res = str((int(num2[j]) + carry)%10) + res
                carry = (int(num2[j]) + carry)/10
                j -= 1
            elif i>=0 and j<=0:
                res = str((int(num1[i]) + carry)%10) + res
                carry = (int(num1[i]) + carry)/10
                i -= 1
        if carry>0:
            res = str(carry)+res
        return res
    
    def partialResult(self,num1,n,pow):
        carry = 0
        res = ''
        i = len(num1)-1
        while i>=0:
            res = str(((int(n) * int(num1[i])) + carry)%10) + res
            carry = ((int(n) * int(num1[i])) + carry)/10
            i -=1
        if carry>0:
            res = str(carry)+res
        return res+'0'*pow
    
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0' : return '0'
        res = '0'
        n = len(num2)-1
        i = n
        while i>=0:
            res = self.addStrings(self.partialResult(num1,num2[i],n-i),res)
            i -= 1
        
        return res
            
            
                
s = Solution()
print s.multiply("123","456")