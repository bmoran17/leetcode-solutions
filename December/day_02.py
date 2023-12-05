# 1450. Number of Students Doing Homework at a Given Time - https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/

def busyStudent(startTime: list[int], endTime: list[int], queryTime: int) -> int:
  # initialize count for students doing hw at query
  students = 0
  for i in range(len(startTime)):
    if startTime[i] <= queryTime <= endTime[i]:
      students += 1
  return students

print(busyStudent([1,2,3],[3,2,7],4)) # 1
print(busyStudent([4],[4],4)) #1
