sentences = "Love's Philosophy by Percy Bysshe Shelley. And the sunlight clasps the earth, And the moonbeams kiss the sea;What are all these kissings worth, If thou kiss not me."
m,n,count=0.05,0.1,0
for y in range(12, -12, -1):
   row_sentence=""
   for x in range(-30, 30):
      function = ((x*m)**2+(y*n)**2-1)**3-(x*m)**2*(y*n)**3
      if function <= 0:
         row_sentence+=sentences[(count) % len(sentences)]
         count+=1
      else:
         row_sentence+=" "
   print(row_sentence)
   f=open("../PycharmProject/words.txt", "a+")
   f.write(row_sentence+"\n")
   f.close()