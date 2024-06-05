import pyttsx3
import speech_recognition
import ollama

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
def chat_with_lamda(query):
  """Sends the user query to LaMDA through Ollama and returns the response."""
  response = ollama.chat(
      model='llama2',
      messages=[
          {'role': 'user', 'content': f"{query} in 100 words"},
      ]
  )
  return response['message']['content']

while True:
  user_query = takeCommand().lower()
  lamda_response = chat_with_lamda(user_query)
  speak(lamda_response)
  print(lamda_response)
  print(user_query)
  # You can add additional functionalities here based on the LaMDA response