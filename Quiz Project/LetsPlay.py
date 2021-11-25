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
 <h2>Right...lets do this!!</h2>
 <section>
<h2>Please choose your theme</h2>
</section>

<button><a href="Music.py">Music</a></button>  <button>

<button><a href="filmNtv.py">Film & TV</a></button>  <button>

<button><a href="generalknowledge.py">General Knowledge</a></button>  <button>

<button><a href="worldcultures.py">World Cultures</a></button>  <button>


<button><a href="Brain_Stormer.py">Home</a></button>  <button><a href="HowToPlay.py">How to Play</a></button>  <button<a href="Rules.py">Lets Play</a></button>  
 </body > <html > ’’’

 return page

 if __name__ == " __main__ ":
 app . run ( host =’0.0.0.0 ’, debug = True )