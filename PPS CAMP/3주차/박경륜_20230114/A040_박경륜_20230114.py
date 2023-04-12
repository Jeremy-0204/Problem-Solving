class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:int(len(s)/2)]
        b = s[int(len(s)/2):]

        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        countb = 0

        for i in a:
            if i in vowel:
                count += 1
        
        for i in b:
            if i in vowel:
                countb += 1
        
        if count == countb: return True
        else: return False