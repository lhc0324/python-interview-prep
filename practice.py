from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        gragh = []
        for i in range(numCourses):
           gragh.append([])
        indegree = []
        for i in range(numCourses):
           indegree.append(0)
        for course,pre in prerequisites:
           gragh[pre].append([course])
           indegree[course] += 1

        q = deque()
        for i in range(numCourses):
           if indegree[course] == 0:
              q.append(i)
        taken = 0
        while q:
           cur = q.popleft()
           taken += 1
           for nex in gragh[cur]:
              indegree[nex] -= 1
              if indegree[nex] == 0:
                 q.append(nex)
        if taken == numCourses:
           return True
        else:
           return False
           
               

                
        
if __name__ == "__main__":
  s = Solution()
  print(s.groupAnagrams(["eat","tea","tan"]))