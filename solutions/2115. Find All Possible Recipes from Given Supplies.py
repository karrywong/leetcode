class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
     #brute force O(N^2*M) = N*M+(N-1)*M+(N-2)*M +...+1*M, where N= len(recipes), M = average len(ingredients[i]) 
        #Mock interview, time O(N^2), space O(N)
        lookup = {}
        for r, lst in zip(recipes, ingredients):
            lookup[r] = lst #key: recipe, values: lst of ingredients
        seen = set() #purpose detect cycle
        can_make = set(supplies)
        cannot_make = set()
​
        def dfs(dish) -> bool: #True or False
            if dish in can_make:
                return True
            
            if dish in cannot_make:
                return False
            
            if dish in seen: #cycle case
                cannot_make.add(dish)
                return False 
            seen.add(dish)
​
            if dish in supplies:
                can_make.add(dish)
                return True
​
            if dish in lookup:
                lst = lookup[dish]  
                bo = True
                for ele in lst:
                    if dfs(ele) is False:
                        break   
                else:
                    can_make.add(dish)
                    return True
                
            cannot_make.add(dish)
            return False
​
        for recipe in recipes:
            dfs(recipe)
​
        ans = []
        for recipe in recipes:
            if recipe in can_make:
                ans.append(recipe)
        return ans
        
