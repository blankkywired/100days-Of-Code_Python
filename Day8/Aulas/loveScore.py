def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    for letter in name1:
        if letter in "true":
            score1 += 1
    
    for letter in name1:
        if letter in "love":
            score1 += 1
    
    for letter2 in name2:
        if letter in "true":
            score2 += 1
    for letter2 in name2:
        if letter2 in "love":
            score2 += 1
    total = str(score1) + str(score2)
    print(total)
        

calculate_love_score('stefany' , 'guilherme')