import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pytz
import pyautogui
import time
import keyboard
import requests
import facebook_api
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
os.environ['DISPLAY'] = '73.157.126.110'

#Initialize the T5ext-to-speech engine
def text_to_speech(text, api_key):
    url = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + api_key
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "input": {"text": text},
        "voice": {"languageCode": "en-US", "name": "en-US-Wavenet-D"},
        "audioConfig": {"audioEncoding": "MP3", "pitch": 0, "speakingRate": 1},
    }
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        return None

api_key = "AIzaSyAr2pE5Thp73No-BfAY65dARQIIYqka4Iw"
text = "Hello, world!"
audio = text_to_speech(text, api_key)

import tkinter as tk
import facial_recognition
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak text passed as argument
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function that will launch the facial recognition program and speak a message
def start_facial_recognition():
    speak("Starting facial recognition")
    facial_recognition.run()

# Create a Tkinter window
window = tk.Tk()
window.title("Facial Recognition")

# Create a button that will launch the facial recognition program
button = tk.Button(window, text="Start Facial Recognition", command=start_facial_recognition)
button.pack()

# Run the Tkinter main loop
window.mainloop()


# Function to speak the text passed as argument
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, your personal assistant. How may I assist you?")

# Function to take voice input from user and recognize it
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry, I could not understand that. Please say that again.")
        return "None"
    return query

if __name__  == '__main__':
    greet()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on user's query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code...")
            codePath = "C:\\Users\\USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Replace USERNAME with your system's username
            os.startfile(codePath)

        elif 'exit' in query:
            speak("Goodbye!")
            exit()

   
# Get the user's current time and location
def get_user_context():
    user_location = "New York" # Replace with code to get user's location
    user_timezone = pytz.timezone("America/New_York") # Replace with code to get user's timezone
    current_time = datetime.datetime.now(user_timezone)
    
    return {
        "location": user_location,
        "timezone": user_timezone,
        "time": current_time
    }

# Use the user's context to provide relevant responses
def provide_response(query):
    user_context = get_user_context()
    current_time = user_context["time"]
    location = user_context["location"]
    
    if "what's the weather" in query:
        # Replace with code to get weather for user's location
        weather = "Sunny"
        response = f"The weather in {location} is currently {weather}."
        
        # Add context-specific response
        if current_time.hour > 18:
            response += " It looks like it's going to be a nice evening!"
    
    elif "what time is it" in query:
        response = f"The time in {location} is currently {current_time.strftime('%I:%M %p')}."
        
        # Add context-specific response
        if current_time.hour > 20:
            response += " It's getting late, time to wind down!"
    
    else:
        response = "I'm sorry, I don't understand. Please try again."
    
    return response

# Example usage
query = "what's the weather like?"
response = provide_response(query)
print(response)

# Get the user's current location
def get_user_location():
    # Replace with code to get user's location
    user_location = "Spokane Valley"
    return user_location

# Get the current time in the user's location
def get_current_time(user_location):
    # Replace with code to get user's timezone based on user's location
      user_timezone = pytz.timezone("America/Los_Angeles")
      current_time = datetime.datetime.now(user_timezone)
      return current_time

# Check if it's morning, afternoon, or evening in the user's location
def get_time_of_day(current_time):
    hour = current_time.hour
    if hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"

# Use the user's context to provide relevant responses
def provide_response(query):
    user_location = get_user_location()
    current_time = get_current_time(user_location)
    time_of_day = get_time_of_day(current_time)

    if "play some music" in query:
        if time_of_day == "morning":
            # Replace with code to play morning music
            response = "Playing some upbeat music to start your day off right!"
        elif time_of_day == "afternoon":
            # Replace with code to play afternoon music
            response = "Playing some chill music to help you relax and unwind."
        else:
            # Replace with code to play evening music
            response = "Playing some mellow tunes to wind down your day."

    elif "what's on my schedule" in query:
        if time_of_day == "morning":
            # Replace with code to get morning schedule
            response = "You have a meeting at 10 AM and a doctor's appointment at 2 PM."
        elif time_of_day == "afternoon":
            # Replace with code to get afternoon schedule
            response = "You have a team brainstorming session at 4 PM."
        else:
            # Replace with code to get evening schedule
            response = "You don't have any events scheduled for tonight."

    else:
        response = "I'm sorry, I don't understand. Please try again."

    return respons

def get_facebook_data(api_key):
    # Make a request to the Facebook Graph API
    response = requests.get(f"https://graph.facebook.com/me?access_token={api_key}")
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the data as a dictionary
        return response.json()
    else:
        # Raise an exception if the request failed
        raise Exception("Failed to retrieve Facebook data")

# Load the credentials from a saved file
creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])

# Create a Gmail API client
service = build('gmail', 'v1', credentials=creds)

# Retrieve the user's Gmail labels
results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

if not labels:
    print('No labels found.')
else:
    print('Labels:')
    for label in labels:
        print(label['name'])

def get_gmail_messages(api_key):
    # Code to make Gmail API request using api_key parameter
    ...
my_api_key = ("AIzaSyAr2pE5Thp73No-BfAY65dARQIIYqka4Iw")
get_gmail_messages(my_api_key)


# Example usage
query = "play some music"
response = provide_response(query)
print(response)

# Open the Start menu
pyautogui.press('win')

# Search for Snapchat and open it
pyautogui.write('Snapchat')
pyautogui.press('enter')

# Wait for Snapchat to load
time.sleep(5)

# Click the Log In button
login_btn = pyautogui.locateCenterOnScreen('login_button.png')
pyautogui.click(login_btn)

# Enter your username and password
time.sleep(2)
pyautogui.write('Jdafler4200')
pyautogui.press('tab')
pyautogui.write('your_password_here')
pyautogui.press('enter')

# Function to open applications
def open_app(app_name):
    os.system(f'start {app_name}')

# Function to pause media playback
def pause_media():
    keyboard.press('space')

# Function to skip to the next media item
def skip_media():
    keyboard.press_and_release('ctrl + right')

# Main function that listens for voice commands
def listen():
    # Implement speech recognition to get voice commands here
    # For the purpose of this example, we'll just use a text input
    command = input("Enter a command: ")
    
if 'open' in command:
    # Get the name of the application to open
    app_name = command.split('open ')[1]
    open_app(app_name)
    print(f"{app_name} opened successfully.")
elif 'pause' in command:
    pause_media()
    print("Media playback paused.")
elif 'skip' in command:
    skip_media()
    print("Skipped to the next media item.")
else:
    print("Command not recognized.")


# Call the listen function in a loop to continuously listen for voice commands
while True:
    command = listen()
    execute_command(command)

# Call the listen function in a loop to continuously listen for voice commands
while True:
    command = listen()
    execute_command(command)
