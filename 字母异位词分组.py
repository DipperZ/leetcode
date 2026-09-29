

class solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        cache = {}
        ans = []
        for words in strs:
            key = "".join(sorted(words))
            if key not in cache:
                cache[key] = []
            cache[key].append(words)
        ans = list(cache.values())
        return ans
if __name__ == "__main__":
    s = solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(strs))
