# Jarvis-with-AI
#Use Python 3.10
Project Title: Jarvis Voice Assistant

Description:

Jarvis Voice Assistant is a Python-based voice-controlled assistant that performs various tasks such as answering queries, opening applications, retrieving news, searching the web, and more, all through voice commands. The assistant is designed to provide a hands-free experience for users, allowing them to interact with their computer using natural language.

Key Features:

Voice-controlled interface using speech recognition.
Text-to-speech synthesis for providing responses and feedback.
Integration with various APIs for performing tasks such as fetching news, searching the web, and retrieving information.
Modular design for easy customization and extension of functionality.
User-friendly interface with intuitive voice commands.
Installation:

Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/DatagenieSK/Jarvis-with-AI.git
Install the required dependencies:

Copy code
pip install -r requirements.txt
Run the main script:

Copy code
python jarvis.py
Usage:

Launch the assistant by running the jarvis.py script.
Speak the wake-up command ("Wake up") to activate the assistant.
Issue voice commands to perform various tasks, such as asking for the time, setting alarms, searching the web, etc.
Use the "Go to sleep" command to deactivate the assistant when not in use.
Contributing:

Contributions to the project are welcome! If you have any ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request. Please follow the guidelines outlined in the CONTRIBUTING.md file.

License:

This project is licensed under the MIT License. See the LICENSE file for more details.

Highlighted Function:

python
Copy code
elif "jarvis" or "Jarvis" or "JARVIS" in query:
    def chat_with_lamda(query):
        query = query.replace("jarvis", "")
        query = query.replace("Jarvis", "")
        query = query.replace("JARVIS", "")

        response = ollama.chat(
            model='llama2',
            messages=[
                {'role': 'user', 'content': f"{query} in 100 words"},
            ]
        )
        return response['message']['content']

    user_query = takeCommand().lower()
    lamda_response = chat_with_lamda(user_query)
    speak(lamda_response)
    print(lamda_response)
    print(user_query)
This function handles user queries containing variations of the word "Jarvis" and interacts with the OpenAI language model (Llama2) to generate a response based on the input query. It demonstrates the core functionality of the assistant in understanding and responding to user commands using natural language processing techniques.

Acknowledgements:

Special thanks to META for providing access to the language model used in the project.
Credits to the developers of the libraries and APIs used in the implementation of the voice assistant.
