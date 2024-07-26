from collections import defaultdict
​
​
class Solution:
    def _is_high_access(self, times: str) -> bool:
        for idx, time in enumerate(times[:-2]):
            upper_bound = int(time) + 100
            if int(times[idx+1]) < upper_bound and int(times[idx+2]) < upper_bound:
                return True
        return False
    
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        lookup = defaultdict(list)
        for employee_id, time in access_times:
            lookup[employee_id].append(time)
            
        high_access = []
        for employee_id, times in lookup.items():
            if len(times) < 3:
                continue
            times.sort()
            if self._is_high_access(times):
                high_access.append(employee_id)
                
        return high_access
