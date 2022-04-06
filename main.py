studentHeights = input(
    "Input a list of student heights ").split()
for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])

totalHeight = 0

for height in studentHeights:
    totalHeight += height
numberOfStudent = 0
for student in studentHeights:
    numberOfStudent += 1
averageHeight = round(totalHeight/numberOfStudent)
print(averageHeight)
