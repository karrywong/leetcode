class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        #Stefan Pochmann's one-liner brute force, time O(1), space O(1)
        return ['%d:%02d' % (h,m) for h in range(12) for m in range(60) if bin(h).count('1') + bin(m).count('1') == turnedOn]
