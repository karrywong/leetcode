class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        # n = 4
        # [0,1,2,3] -> # permutations: 4! = 24
        # lookup = {0: [ , , , ], 1, 2, 3}
        
        lookup = defaultdict(list)
        n = len(students)
        for student_id in range(n):
            for mentor_id in range(n):
                score = sum([s == m for s, m in zip(students[student_id], mentors[mentor_id])])
                lookup[student_id].append(score)
        
        ans = 0
        for permuted_ids in itertools.permutations(range(n)):
            total_match = 0 
            for student_id, mentor_id in zip(range(n), permuted_ids):  
                    total_match += lookup[student_id][mentor_id]
            ans = max(ans, total_match)
        return ans
                    
            
        
