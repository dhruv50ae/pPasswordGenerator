studentScores = input(
    "Input a list of student scores with a space between them. ").split()
for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
print(studentScores)
highestScore = 0
for score in studentScores:
    if score > highestScore:
        highestScore = score
print(f"The highest score in the class is: {highestScore}")
