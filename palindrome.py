def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        #snew="".join(char for char in s if char.isalnum()).lower()
        #n=len(snew)
        n=len(s)
        """for i in range(-(-n//2)):
            if snew==" ":
                return True
            else:
                if snew[i]==snew[n-i-1]:
                    continue
                else:
                    return False
        return True"""
        if n==1 or n==0:
            return True
        else:
            if (s[0]==s[-1]):
                return isPalindrome(s[1:-1])
            else:
                return False
print(isPalindrome("abcdcba"))
