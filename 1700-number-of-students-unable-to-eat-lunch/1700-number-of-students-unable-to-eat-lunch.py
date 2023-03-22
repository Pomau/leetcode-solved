import queue
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = queue.Queue()
        for st in students:
            q.put(st)
        count = [students.count(0), students.count(1)]
        l = 0
        while not q.empty() and count[sandwiches[l]] != 0:
            st = q.get()
            if sandwiches[l] != st:
                q.put(st)
            else:
                count[st] -= 1
                l += 1
        ans = 0
        while not q.empty():
            ans += 1
            q.get()
        return ans