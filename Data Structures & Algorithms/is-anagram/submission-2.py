class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char = {}
        for ch in s:
            char[ch] = char.get(ch,0)+1
        for ch in t:
            if ch not in char:
                return False
            else:
                if char[ch] == 0:
                    return False
                else:
                    char[ch] -= 1
        return True
        