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
 <h2>Rules</h2>
 
 <text>1.) Its a quiz so obviously NO Google! </text> 
 <text>2.) Take your time </text>
 <text>3.) Most importantly...Enjoy! </text>


</text>

<button><a href="Brain_Stormer.py">Home</a></button>  <button><a href="HowToPlay.py">How to Play</a></button>  <button<a href="LetsPlay.py">Lets Play</a></button>  
 </body > <html > ’’’

 return page

 if __name__ == " __main__ ":
 app . run ( host =’0.0.0.0 ’, debug = True )