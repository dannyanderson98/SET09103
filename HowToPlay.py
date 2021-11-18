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
 <h2>How to play</h2>
 
 <text>1.) Choose your topic of interest </text> 
 <text>2.) Select your answer by clicking on the check box </text>
 <text>3.) If you dont know the answer skip to the next question </text>
 <text>4.) If you get an answer wrong you will be automatically told its incorrect along with the correct answer </text>

<h2> Good luck! </h2> 


</text>

<button><a href="Brain_Stormer.py">Home</a></button>  <button><a href="Rules.py">How to Play</a></button>  <button<a href="LetsPlay.py">Lets Play</a></button>  
 </body > <html > ’’’

 return page

 if __name__ == " __main__ ":
 app . run ( host =’0.0.0.0 ’, debug = True )