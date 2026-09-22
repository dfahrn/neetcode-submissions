class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping characater count to list of Anagrams

        for s in strs:
            count = [0] * 26 # a-z

            for char in s: # char is the first character we look at
                count[ord(char) - ord("a")] += 1 # we map 'a' to index 0

            result[tuple(count)].append(s) # tuples are non-mutable

        return list(result.values()) # how we return list of character count

        # O(m * n) time complexity

