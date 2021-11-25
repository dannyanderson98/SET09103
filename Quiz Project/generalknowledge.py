from flask import Flask , request
 app = Flask ( __name__ )

 @app . route ("/ account /", methods =[ ’POST ’,’GET ’])
 def account () :
 if request . method == ’POST ’:
 print ( request . form )
 name = request . form [’name ’]
 return " Hello %s" % name
 else :
 page = ’’’
 <html > <body >
 <h1>BRAIN-STORMER</h1>
 <h2>General Knowledge</h2>

 # Defining Score variables 
x = 0
score = x

# Question One 
print("Which Shakespeare couple appears in the NATO Phonetic Alphabet?")
answer_1 = input("a)Macbeth & Lady Macbeth\nb)Antony & Cleopatra\nc)Romeo & Juliet\nd)Benedict & Beatrice\n:")
if answer_1.lower() == "c" or answer_1.lower() == "Romeo & Juliet":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, Romeo & Juliet are the Shakespeare couple that appear in the NATO Phonetic Alphabet")

# Question Two
print("What year did the RMS Titanic sink??")
answer_2 = input("a)1912\nb)1974\nc)1950\nd)1066\n:")
if answer_2.lower() == "a" or answer_2.lower() == "1912":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The RMS Titanic sank in 1912 after a fatal collison with an iceberg on it's maiden voyage")

# Question Two
print("Who is credited as the 5th Beatle?")
answer_2 = input("a)Brian Epstien\nb)Mick Jagger\nc)Yoko Ono\nd)George Martin\n:")
if answer_2.lower() == "d" or answer_2.lower() == "George Martin":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The 5th Beatle is the bands producer George Martin") 

# Question Four
print("What is the fastest steam locomotive in the world?")
answer_4 = input("a)Flying Scotsman\nb)Mallard\nc)Stephenson's Rocket\nd)Locomotion\n:")
if answer_4.lower() == "b" or answer_4 == "Mallard":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is Mallard which broke the world speed record for steam in 1937 achieving a whopping 126 mph")

# Question Five 
print("True or False... The meaning of the name given to the famous dinosaur Tyrannosaurus Rex is 'Tyrant lizard'?")
answer_5 = input(":")
if answer_5.lower() == "True" or answer_5.lower() == "True":
    print("Correct")
    x = x + 1
else:
    print("Incorrect") 

# Question Six
print("What was the name of the plane that dropped the atomic bomb on Hiroshima in 1945?")
answer_4 = input("a)The Spirit of St Louis\nb)Enola Gay\nc)Memphis Bell\nd)Air Force One\n:")
if answer_4.lower() == "b" or answer_6 == "Enola Gay":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is the Enola Gay")

#Total Score
score = float(x / 6) * 100
print(x,"out of 6, that is",score, "%")
 
 
