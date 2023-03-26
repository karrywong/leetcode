/* The knows API is defined for you.
      bool knows(int a, int b); */
​
class Solution {
public:
    int findCelebrity(int n) {
    // start with node-i 
    // node-i, find terminal node
    // if there is a cycle, continue to node-(i+1)
    // terminal node: node-j, check if node-j is celebrity. If yes, return node-j
        int nodeA = 0;
        for (int nodeB = 1; nodeB < n; nodeB++) {
            if (knows(nodeA, nodeB))
                nodeA = nodeB;
        }
        // Check if nodeA is a celebrity  
        for (int nodeC = 0; nodeC < n; nodeC++){
            if (nodeC == nodeA) 
                continue;
            if (!knows(nodeC, nodeA) || knows(nodeA, nodeC)) 
                return -1;
        }
        return nodeA;
    }
};
