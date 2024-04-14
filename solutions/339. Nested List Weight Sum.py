#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
​
class Solution:
    def depthSum(self, nestedList: List[NestedInteger], level: int = 1) -> int:
        ans = 0
        for ele in nestedList:
            if ele.isInteger():
                ans += level * ele.getInteger()
            else:
                ans += self.depthSum(ele.getList(), level+1)
        return ans
        
#  nestedList = [[1,1],2,[1,1]]
# ele = [1,1], depthSum([1,1], 2) -> 2 +2 = 4
# ans = 4 +2 *1 + 4 = 10
        
