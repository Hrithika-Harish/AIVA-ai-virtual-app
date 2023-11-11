# # Python program to translate
# # speech to text and text to speech


# import speech_recognition as sr
# import pyttsx3 

# # Initialize the recognizer 
# r = sr.Recognizer() 

# # Function to convert text to
# # speech
# def SpeakText(command):
	
# 	# Initialize the engine
# 	engine = pyttsx3.init()
# 	engine.say(command) 
# 	engine.runAndWait()
	
	
# # Loop infinitely for user to
# # speak

# while(1): 
	
# 	# Exception handling to handle
# 	# exceptions at the runtime
# 	try:
		
# 		# use the microphone as source for input.
# 		with sr.Microphone() as source2:
			
# 			# wait for a second to let the recognizer
# 			# adjust the energy threshold based on
# 			# the surrounding noise level 
# 			r.adjust_for_ambient_noise(source2, duration=0.2)
			
# 			#listens for the user's input 
# 			audio2 = r.listen(source2)
			
# 			# Using google to recognize audio
# 			MyText = r.recognize_google(audio2)
# 			MyText = MyText.lower()

# 			print("Did you say ",MyText)
# 			SpeakText(MyText)
			
# 	except sr.RequestError as e:
# 		print("Could not request results; {0}".format(e))
		
# 	except sr.UnknownValueError:
# 		print("unknown error occurred")

#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('Recording.wav') as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')