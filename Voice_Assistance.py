import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Please speak.")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results; check your internet connection.")
            return ""
        except sr.WaitTimeoutError:
            speak("Listening timed out; please try speaking more clearly.")
            return ""

# Main function to handle commands
def run_voice_assistant():
    speak("Hello! How can I help you?")
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hi there! How can I assist you?")
        
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        
        elif "date" in command:
            current_date = datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}")
        
        elif "bye" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("Sorry, I can only respond to 'hello,' 'time,' 'date,' and 'bye' commands.")

# Run the assistant
if __name__ == "__main__":
    run_voice_assistant()
