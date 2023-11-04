import speech_recognition as sr

recognizer = sr.Recognizer()

while(1):
	try:
		with sr.Microphone() as source:
			print('Listening to your mic, please say something in English')
			recognizer.adjust_for_ambient_noise(source, duration=0.2)
			audio = recognizer.listen(source)
		
		text = recognizer.recognize_google(audio)
		text = text.lower()
		print(f"Text = {text}")

	except KeyboardInterrupt:
		print("A keyboard interrupt occured, Terminating the program!!")
		exit(0)

	except sr.UnknownValueError:
		print("No user voice detected or voice could not be understood!")
