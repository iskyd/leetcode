"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al = [int(d) for d in a][::-1]
        bl = [int(d) for d in b][::-1]
        res = []
        cur = 0
        remainder = 0
        while cur < max(len(al), len(bl)) or remainder == 1:
            d1 = al[cur] if cur < len(al) else 0
            d2 = bl[cur] if cur < len(bl) else 0
            r = 1 if bool(d1) ^ bool(d2) ^ bool(remainder) else 0
            remainder = 1 if d1 + d2 + remainder > 1 else 0
            res.append(r)
            cur += 1

        return "".join([str(d) for d in res][::-1])


s = Solution()
print(s.addBinary("11", "1"))
assert s.addBinary("11", "1") == "100"
assert s.addBinary("1010", "1011") == "10101"
print("passed")
