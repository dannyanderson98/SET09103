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
 <h2>Music</h2>

 # Defining Score variables 
x = 0
score = x

# Question 1 
print("Who was the lead singer to the rock band Queen?")
answer_1 = input("a)Lady Gaga\nb)Freddie Mercury\nc)Paul McCartney\nd)Ed Sheeran\n:")
if answer_1.lower() == "b" or answer_1.lower() == "Freddie Mercury":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The leader singer of the rock band Queen was Freddie Mercury")

# Question 2
print("What was the Beatles 5th album?")
answer_2 = input("a)Help!\nb)Dark Side of the Moon\nc)Sgt Pepper's Lonely Hearts Club Band\nd)The Queen Is Dead\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Help!":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The Beatles 5th album was Help! released in 1965")

# Question 3
print("True or False... The Smith's song 'Frankly Mr Shankly' was aimed at the founder of Rough Trade Goeff Harris?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")  

# Question 4
print("What is the name of the duet recorded by Robbie Williams and Gary Barlow in 2010 ?")
answer_4 = input("a)Heaven Knows I'm Miserable Now\nb)Hey Jude\nc)Break on through (to the other side)\nd)Shame\n:")
if answer_4.lower() == "d" or answer_4 == "Shame":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The 2010 duet recorded by Gary Barlow and Robbie Williams was 'Shame'")

# Question 5 
print("True or False... The nickname of The Doors lead singer Jim Morrison was 'The Lizard King'?")
answer_5 = input(":")
if answer_5.lower() == "True" or answer_5.lower() == "f":
    print("Correct, Jim Morrison's nickname was 'The Lizard King'")
    x = x + 1
else:
    print("Incorrect, The nickname of The Doors lead singer Jim Morrison was The Lizard King")

# Question 6
print("In what year were the hit songs 'Uptown Funk', 'Bad Blood', 'Chandelier', 'Fancy', 'Rather Be' and 'Anaconda' released ?")
answer_4 = input("a)1998\nb)1998\nc)2014\nd)1970\n:")
if answer_4.lower() == "c" or answer_4 == "2014":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, 'Uptown Funk', 'Bad Blood', 'Chandelier', 'Fancy', 'Rather Be' and 'Anaconda' were released in 2014")
#Total Score
score = float(x / 6) * 100
print(x,"out of 6, that is",score, "%")
 
 


</text>

<button><a href="Brain_Stormer.py">Home</a></button>  <button><a href="HowToPlay.py">How to Play</a></button>  <button<a href="LetsPlay.py">Lets Play</a></button>  
 </body > <html > ’’’

 return page

 if __name__ == " __main__ ":
 app . run ( host =’0.0.0.0 ’, debug = True ) 
