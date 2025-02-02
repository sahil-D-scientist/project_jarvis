import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

# Use macOS-specific voices (Try different options)
engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")  # Default macOS English voice

def talk(text):
    print(f"Jarvis: {text}")  # Debugging output
    engine.say(text)
    engine.runAndWait()

talk("Hello, Sahil! This is Jarvis speaking.")
