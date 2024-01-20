class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target: return letters[0]
        l, r = 0, len(letters)-1
        
        while l < r:
            mid = (l+r)//2
            if letters[mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        return letters[l] if letters[l] > target else letters[l+1]
    
    #[c,f,j], a -> (0,2) -> (0,0), c
    #[c,f,j], c -> (0,2) -> (0,0), f
    #[c,f,j], i -> (0,2) -> (2,2), j
    #[c,f,j,j], i -> (0,3) -> (2,3) -> (2,1), j
    #[x,y], z -> (0,1) -> (0,1)      
        
