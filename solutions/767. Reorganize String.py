class Solution:
    def reorganizeString(self, s: str) -> str:
        #First attempt, use heap, idea comes from hint "Alternate placing the most common letters."
        count = collections.Counter(s)
        maxHeap = [(-1*freq, char) for char, freq in count.items()]
        heapq.heapify(maxHeap)
        ans = ""
        if len(s) % 2 == 0 and -1*maxHeap[0][0] >= len(s)//2 +1:
            return ans
        elif len(s) % 2 == 1 and -1*maxHeap[0][0] >= (len(s)+1)//2 + 1:
            return ans
        while maxHeap:
            size = len(maxHeap)
            freq, char = heapq.heappop(maxHeap)
            if ans and ans[-1] == char:
                freq2, char2 = heapq.heappop(maxHeap)
                ans += char2 + char
                if -1*freq2 > 1:
                    heapq.heappush(maxHeap,(freq2+1, char2))
            else:
                ans += char
            if -1*freq > 1:
                heapq.heappush(maxHeap,(freq+1, char))
        return ans
