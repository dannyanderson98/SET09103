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
 <h2>World Cultures</h2>

 # Defining Score variables 
x = 0
score = x

# Question One 
print("The religeous festival Diwali is celebrated by which religon")
answer_1 = input("a)Hinduism\nb)Islam\nc)Christianity\nd)Judaism\n:")
if answer_1.lower() == "a" or answer_1.lower() == "Hinduism":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, Diwali is celebrated by the Hindu religon")

# Question Two
print("In India it is customed to bow and say what?")
answer_2 = input("a)Howdy!)\nb)Bonjour\nc)Namaste\nd)Konnichiwa\n:")
if answer_2.lower() == "c" or answer_2.lower() == "":
    print("Correct, in India it is customed to bow and say Namaste")
    x = x + 1
else:
    print("Incorrect, in India it is customed to bow and say Namaste")

# Question Three
print("Which continent is the most linguistically diverse in the world?")
answer_2 = input("a)Europe\nb)Australiasia\nc)Africa\nd)North America\n:")
if answer_2.lower() == "c" or answer_2.lower() == "":
    print("Correct, the most linguistically diverse continent is Africa")
    x = x + 1
else:
    print("Incorrect, Africa is the most linguistically diverse continent")

# Question Four
print("In what culture observes the Christmas tradition of having a hidden figurine in the cake and whoever finds it is king or queen for the day?  ")
answer_4 = input("a)French\nb)Chinese\nc)Irish\nd)German\n:")
if answer_4.lower() == "a" or answer_4 == "":
    print("Correct, In French culure the one who finds the figurine hidden in the Christmas cake is king or queen for the day")
    x = x + 1
else:
    print("Incorrect, the correct answer was French")

# Question Five 
print("True or False...  ")
answer_5 = input(":")
if answer_5.lower() == "True" or answer_5.lower() == "True":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Six
print(" ")
answer_4 = input("a)\nb)\nc)\nd)\n:")
if answer_4.lower() == "a" or answer_4 == "":
    print("Correct")
    x = x + 1
else:
    print("")

#Total Score
score = float(x / 6) * 100
print(x,"out of 6, that is",score, "%")
 
 
