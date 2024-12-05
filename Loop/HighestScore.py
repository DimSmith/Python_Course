student_scores = [100, 59 ,60 ,45 ,55 ,65 ,78 , 48, 100 ,78 ,89 ,99 ,44 ,65]

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)