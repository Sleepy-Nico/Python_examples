#Gör 3 frågor
points = 0
questions = ["What year was Cinnamoroll created?","What animal is Cinnamoroll","What is Cinnamoroll's eye collor?"]
answers= [" a.2003 \n b.2000 \n c.2001", " a.dog \n b.bunny \n c.cat", " a.red \n b.blue \n c.green"]
correctanswer = ["c", "a", "b"]

index= 0
while(index < 3):
    print(questions[index])
    print(answers[index])
    answer = input("Choose a, b or c? ")
    #skapa 3 alternativ
    #håll koll på hur många rätt svar
    if(answer == correctanswer[index]):
        points = points + 1
    index +=1
print(points)
    #få veta resultat i slutet