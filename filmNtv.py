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
 <h2>Film & TV</h2>

 # Defining Score variables 
x = 0
score = x

# Question 1 
print("Who directed Titanic, Avatar and The Terminator??")
answer_1 = input("a)Steven Spielberg\nb)James Cameron\nc)Alfred Hitchcock\nd)Baz Luhrmann\n:")
if answer_1.lower() == "b" or answer_1.lower() == "James Cameron":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The director of Titanic, Avatar and The Terminator was James Cameron")

# Question 2
print("What island is Jurrasic Park on?")
answer_2 = input("a)Isla Nublar\nb)Island of Sodor\nc)Treasure Island\nd)Neverland\n:")
if answer_2.lower() == "a" or answer_2.lower() == "Isla Nublar":
    print("Correct, Isla Nublar is the island where Jurrasic Park is located")
    x = x + 1
else:
    print("Incorrect, The island Jurrasic Park is on is Isla Nublar")

# Question 3
print("Aidensfield is the name of a fictional village in which TV drama?")
answer_2 = input("a)Emmerdale\nb)Coronation Street\nc)Heartbeat\nd)Casualty\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Heartbeat":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Aidensfield is the name of the fictional village in the 60's police drama Heartbeat")

# Question 4
print(" 'We were on a break!' is a famous line from which American sit-com?")
answer_4 = input("a)The Big Bang Theory\nb)Friends\nc)Brooklyn 99\nd)The Simpsons\n:")
if answer_4.lower() == "b" or answer_4 == "Friends":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is Friends and is recurring dialogue between the characters Ross and Rachel")

# Question 5 
print("True or False... Saturday Night Live (SNL) isn't the first show to be called Saturday Night Live?")
answer_5 = input(":")
if answer_5.lower() == "True" or answer_5.lower() == "True":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question 6
print(" 'Eat my shorts!' is the famous catchphrase of which Simpsons character?")
answer_4 = input("a)Ned Flanders\nb)Mr.Burns\nc)Bart Simpson\nd)Marge Simpson\n:")
if answer_4.lower() == "c" or answer_4 == "Bart Simpson":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is Bart Simpson...Ay Caramba!!")

#Total Score
score = float(x / 6) * 100
print(x,"out of 6, that is",score, "%")
 
 


</text>

<button><a href="Brain_Stormer.py">Home</a></button>  <button><a href="HowToPlay.py">How to Play</a></button>  <button<a href="LetsPlay.py">Lets Play</a></button>  
 </body > <html > ’’’

 return page

 if __name__ == " __main__ ":
 app . run ( host =’0.0.0.0 ’, debug = True ) 
 