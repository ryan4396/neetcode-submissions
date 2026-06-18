class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = []

        while True:
            added_list = []
            not_added_list = []
            if len(strs) >= 2:
                val = strs.pop(0)
                added_list.append(val)
                for i in range(len(strs)):
                    if len(strs[i]) == len(val) and sorted(strs[i]) == sorted(val):
                        added_list.append(strs[i])
                    else:
                        not_added_list.append(strs[i])
                strs = not_added_list
                anagram_groups.append(added_list)

            elif len(strs) == 1:
                anagram_groups.append([strs[0]])
                break
            
            else:
                break
        
        return anagram_groups
                        