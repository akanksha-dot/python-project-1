# python-project-1
THIS PROJECT IS BASED ON  AI  ASSISTANT DESKTOP .IN THIS PROJECT THERE IS ONE IRON MAN WHOSE NAME IS J.A.R.V.I.S. WHO WILL AUTOMATE OUT TASK WHICH WE WILL GOING TO SAY -. 
IT CAN DO WIKIPEDIA SEARCHES FOR US
IT IS CAPABLE OF OPENING WEBSITES LIKE GOOGLE,YOUTUBE ETC.
IT IS CAPABLE OF OPENING YOUR CODE EDITOR .


MOST IMPORTANT FOR AI ASSISTANT TO ABLE TO SPEAk.For that we make a function called SPEAK().It will take audio as argument and then it will pronounce it.

TO SUPPLY AUDIO - WE  NEED TO INSTALL MODULE -pyttsx3(python library which convert text to speech)
  TO recognise voice we need Speech API (sapi5)
  
  Voice id helps to select different voices- for male voice -voice[0].id
  for female voice - voice[1].id
  
  TO PERFORM TASK ITS IMPORTANT FOR AI ASSISTANT TO TAKE COMMAND WITH THE HELP OF MICTROPHONE OF THE USER'S SYSTEM .WITH THE HELP OF THIS IT WILL ABLE TO RETURN STRING OUTPUT.
  FOR THAT FIRST IMPORT MODULE - pip install speechRecognition and then import speechRecognition as sr
  
  
DEFINING TASK- TO SEARCH SOMETHING ON WIKIPEDIA-pip install wikipedia
import wikipedia
in this task i have used if to check whether wikipedia is in the search query of the user or not. If found then one sentence from the summary of the wikipedia page will converted into speech with the help of speak function.


TO OPEN GOOGLE.COM

It having in-built module . we dont need to install. jist import it.import webbrowser

we are using elif to check whether google.com is in the query.we will say -jarvis open google.com .so in this case elif condition is true so it will open google.com for us.
