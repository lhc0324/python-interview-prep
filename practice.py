from collections import defaultdict


class Solution(object):
  def groupAnagrams(self,strs):
    mp = defaultdict(list)
    for u in strs:
      key = ''.join(sorted(u))
      mp[key].append(u)
    return list(mp.values())

if __name__ == "__main__":
  s = Solution()
  print(s.groupAnagrams(["eat","tea","tan"]))