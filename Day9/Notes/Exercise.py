# This is the scoring criteria:
#
# - Scores 91 - 100: Grade = "Outstanding"
#
# - Scores 81 - 90: Grade = "Exceeds Expectations"
#
# - Scores 71 - 80: Grade = "Acceptable"
#
# - Scores 70 or lower: Grade = "Fail"
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
}
#Itera sobre cada elemento do dicionario, grades representa o valor de cada key, no caso o nome dos alunos , e student_scores[grades] retorna o valor
#da key, no caso, as notas dos alunos, apos isso, adiciona o nome dos alunos seguidos do valor da checagem das notas(Outstading, Exceeds Expectations etc...)
#Em seguida, itera sobre o novo dicionario student_grades com a nova checagem exibindo uma lista com nomes e checagem
for grades in student_scores:
    # print(grades , student_scores[grades])

    if student_scores[grades] >= 91:
        student_grades[grades] = "Outstanding"

    elif 81 <= student_scores[grades] <= 90:
        student_grades[grades] = "Exceeds Expectations"

    elif 71 <= student_scores[grades] <= 80:
        student_grades[grades] = "Acceptable"

    else:
        student_grades[grades] = "Fail"

for i in student_grades:
    print(i,":" ,  student_grades[i])
