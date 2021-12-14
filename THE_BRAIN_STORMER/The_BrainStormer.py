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
 <h2> Welcome to Brain-Stormer</h2> 

<style> 

body {
	background-image: url('coolbackground.jpg'); 
}

h1 { color: lightblue;
	 font-family: Monospace, Monaco, Monospace;
     left: : 40px;
}

h2 { color: lightblue;
     font-family: Monospace, Monaco, Monospace;
     left: 40px;
}

p { color: lightblue;
	font-family: Monospace, Monaco, Monospace;
    left: 40px
}

button {

  background-color: lightblue;
  font-family: Monospace, Monaco, Monospace;
  border: none;
  color: white;
  padding: 12px 8px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}


</style> 


<section>

<button><a href="Rules.html">Rules</a></button> 

&nbsp;&nbsp;&nbsp; 

<button><a href="HowToPlay.html">How to Play</a></button> 

&nbsp;&nbsp;&nbsp; 

<button><a href="LetsPlay.html">Lets Play</a></button>  

</section>

 <h2>Put your general knowledge to the test and take your brain for a ride!</h2> 

 <p>Grab a beer, chill and get cracking!! Oh..other drinks are available!!</p>








 </body > <html > ’’’

 return page

 if __name__ == " __main__ ":
 app . run ( host =’0.0.0.0 ’, debug = True )

	







