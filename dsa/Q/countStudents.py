class Solution(object):
    def countStudents(self, students, sandwiches):
        studentPtr = 0
        while studentPtr < len(students):
            if students[studentPtr] == sandwiches[0]:
                students.pop(studentPtr)
                sandwiches.pop(0)
                studentPtr=0
            else:
                studentPtr+=1
        return len(students)

sln = Solution()
print(sln.countStudents([1,1,0,0], [0,1,0,1]))