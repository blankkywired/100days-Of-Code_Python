

def calculate_love_score(name1, name2):
    name1 = name1.upper()  
    name2 = name2.upper()

    score1 = 0
    score2 = 0

    for i in "TRUE":
        name1_count = name1.count(i)
        name2_count = name2.count(i)
        score1 += name1_count + name2_count
    # print(score1)

    for i in "LOVE":
        name1_count = name1.count(i)
        name2_count = name2.count(i)

        score2 += name1_count + name2_count
    # print(score2)

    total = str(score1) + str(score2)
    print(total)

calculate_love_score("Nara", "Guilherme")

     