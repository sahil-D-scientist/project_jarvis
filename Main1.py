import os
import time
import pyttsx3
import speech_recognition as sr
import pyautogui
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import re
import keyboard
import requests
import random
import os
import time
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary as diction
import pygame
import asyncio
from googletrans import Translator
from turtle import *
from random import randrange
from freegames import square, vector
import feedparser
import pywhatkit
from word2number import w2n
from time import sleep
import sys
from PyQt5.QtWidgets import QApplication
score = 0  # Initialize score
# Initialize voice engine
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")  # Default macOS English voice

def talk(text):
    """ Speak out the provided text """
    print(f"Jarvis: {text}")  
    engine.say(text)
    engine.runAndWait()

def take_command():
    """ Listen for user commands and return as text """
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
                print(f"Recognized: {command}")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
    except Exception as e:
        print(f"Error: {e}")
    return command if command else "None"


def run_alexa():
    """ Core function to execute commands """
    talk("Jarvis is online. How can I assist you,sir?")

    while True:
        command = take_command()
        print(f"Command: {command}")

        if 'play a song on youtube named as' in command:   #checked
            song = command.replace('play a song on youtube named as', '').strip()
            talk(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif 'Current time' in command: #checked
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"Current time is {current_time}")

        elif 'wikipedia about' in command: #checked
            person = command.replace('wikipedia about', '').strip()
            info = wikipedia.summary(person, 2)
            talk(f"According to Wikipedia: {info}")

        elif 'joke' in command:  #checked
            joke = pyjokes.get_joke()
            talk(joke)
            # print(joke)

        elif 'google search' in command:  #checked
            query = command.replace('google search', '').strip()
            talk(f"Searching Google for {query}")
            pywhatkit.search(query)

        elif 'youtube search' in command:  #checked
            query = command.replace('youtube search', '').strip()
            web = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(web)

        elif 'screenshot' in command:    #checked
            talk("What should I name the file?")
            filename = take_command().strip() + ".png"
            path = os.path.join(os.path.expanduser("~/Documents/"), filename)
            pyautogui.screenshot().save(path)
            talk("Screenshot saved!")

        elif 'shutdown my system' in command:   #checked
            talk("Are you sure you want to shut down? Say yes or no.")
            if 'yes' in take_command():
                talk("Shutting down...")
                os.system("shutdown -h now")

        elif "who made you" in command: #checked
            talk("I am the creation of Sahil sir")

        elif "open a website" in command: #checked
            talk("Which website should I open?")
            site = take_command().strip()
            if site:
                webbrowser.open(f"https://{site}.com")
                talk(f"Opening {site}")

        # elif "open link" in command:
        #     talk("Please provide the link")
        #     link = input("Enter the link here: ")
        #     webbrowser.open(link)
        #     talk("Done!")



        elif "pause" in command: #checked
            keyboard.press("space")

        elif "restart video" in command:  #checked
            keyboard.press("0")

        elif "full screen mode" in command:  #checked
            keyboard.press("f")

        elif "where i am" in command: #checked
            talk("Fetching your location...")

            # Open Google Maps at the user's current location
            webbrowser.open("https://www.google.com/maps/search/?api=1&query=my+location")

            talk("Opening your location on Google Maps...")



        elif "meaning of" in command or "define" in command:  # Corrected condition
            word = command.replace("meaning of", "").replace("define", "").strip()

            # Fetch definition from Dictionary API
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and "meanings" in data[0] and data[0]["meanings"]:
                    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                    talk(f"The meaning of {word} is: {definition}")
                else:
                    talk(f"Sorry, I couldn't find the meaning of {word}.")
            else:
                talk(f"Sorry, I couldn't find the meaning of {word}.")


        elif "hello" in command: #checked
            talk("Hello! sir")

        elif "antonym of" in command: # checked
            word = command.replace("antonym of", "").strip()
            
            # Fetch antonyms from Datamuse API
            url = f"https://api.datamuse.com/words?rel_ant={word}"
            response = requests.get(url)
            print(response)
            if response.status_code == 200 and response.json():
                antonyms = [entry["word"] for entry in response.json()]
                talk(f"The antonyms of {word} are: {', '.join(antonyms[:5])}")
            else:
                talk("Sorry, I couldn't find the antonym.")

        elif "tell me the weather of" in command: #checked
            city = command.replace("tell me the weather of", "").strip()
            talk(f"Fetching weather for {city}...")

            # Fetch weather data from wttr.in
            url = f"https://wttr.in/{city}?format=%C+%t"
            response = requests.get(url)

            if response.status_code == 200:
                weather_info = response.text.strip()
                talk(f"The weather in {city} is {weather_info}.")
            else:
                talk(f"Sorry, I couldn't find the temperature for {city}.")


        elif "who are you" in command: #checked
            talk("I am Jarvis, your AI assistant,Created by Sahil sir.")

        elif "how are you" in command: #checked
            talk("I'm doing well, thank you for asking!,how about you ")

        elif "goodbye" in command or "exit" in command or "thank you" in command: #checked
            talk("Goodbye! Have a great day.")
            QApplication.instance().quit()  # Properly exit PyQt5 GUI
            sys.exit(0)  # Ensure full program termination

        elif 'hello boy' in command: #checked

            command.replace('hello boy', '')
            talk("hello sir!")
        elif "play a game" in command: #checked
            talk("Launching a simple game for you.")
            choices = ["rock", "paper", "scissors"]
            talk("Choose rock, paper, or scissors.")
            user_choice = take_command().strip()
            bot_choice = random.choice(choices)

            if user_choice in choices:
                talk(f"I chose {bot_choice}.")
                if user_choice == bot_choice:
                    talk("It's a tie!")
                elif (user_choice == "rock" and bot_choice == "scissors") or \
                     (user_choice == "scissors" and bot_choice == "paper") or \
                     (user_choice == "paper" and bot_choice == "rock"):
                    talk("You win!")
                else:
                    talk("I win!")
            else:
                talk("Invalid choice. Try again.")



        elif "snake game" in command: #checked
            talk("Starting the snake game.")
            food = vector(0, 0)
            snake = [vector(10, 0)]
            aim = vector(0, -10)

            wn = Screen()
            wn.title("Snake game by Sahil")
            wn.bgcolor('red')
            wn.setup(width=500, height=600)

            def change(x, y):
                aim.x = x
                aim.y = y

            def inside(head):
                return -200 < head.x < 190 and -200 < head.y < 190

            def quit_game():
                wn.bye()  # Close the turtle graphics window

            def move():
                global score  # Use global to modify score inside function
                head = snake[-1].copy()
                head.move(aim)

                if not inside(head) or head in snake:
                    square(head.x, head.y, 9, 'red')
                    update()
                    print("Game Over! Final Score:", score)
                    return

                snake.append(head)

                if head == food:
                    score += 1  # Increase score
                    food.x = randrange(-15, 15) * 10
                    food.y = randrange(-15, 15) * 10
                else:
                    snake.pop(0)

                clear()
                for body in snake:
                    square(body.x, body.y, 9, 'black')

                square(food.x, food.y, 9, 'green')

                # Display score on the UI
                penup()
                goto(-190, 170)
                color("white")
                write(f"Score: {score}", font=("Arial", 16, "bold"))
                pendown()

                update()
                ontimer(move, 100)

            hideturtle()
            tracer(False)
            listen()
            onkey(lambda: change(10, 0), 'Right')
            onkey(lambda: change(-10, 0), 'Left')
            onkey(lambda: change(0, 10), 'Up')
            onkey(lambda: change(0, -10), 'Down')
            onkey(quit_game, 'Escape')  # Quit on Escape key
            onkey(quit_game, 'x')  # Quit on 'x' key
            move()
            done()



        elif "calculate" in command: #checked
            def convert_to_number(text):
                try:
                    return w2n.word_to_num(text)  # Converts spoken words like 'twenty-five' to 25
                except ValueError:
                    talk("I couldn't understand the number. Please say it again.")
                    return None
            talk("Tell me the first number.")
            num1_text = take_command()
            num1 = convert_to_number(num1_text)

            if num1 is None:
                talk("Invalid first number. Try again.")
            
            talk("Tell me the operation (add, subtract, multiply, divide).")
            operation = take_command().strip().lower()

            talk("Tell me the second number.")
            num2_text = take_command()
            num2 = convert_to_number(num2_text)

            if num2 is None:
                talk("Invalid second number. Try again.")

            elif operation == "add":
                result = num1 + num2
                talk(f"The result is {result}")
            elif operation == "subtract":
                result = num1 - num2
                talk(f"The result is {result}")

            elif operation == "multiply":
                result = num1 * num2
                talk(f"The result is {result}")

            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                    talk(f"The result is {result}")
                else:
                    talk("Division by zero is not allowed.")

            else:
                talk("Invalid operation. Please try again.")

        


        elif "calculator" in command: #checked
            talk("Opening calculator.")
            os.system("open -a Calculator")

        elif "notepad" in command: #checked
            talk("Opening Notepad.")
            os.system("open -a TextEdit")

        elif "translate" in command: #checked

            translator = Translator()
            talk("Say the sentence you want to translate.")
            text_to_translate = take_command()
            if text_to_translate:
                translation = asyncio.run(translator.translate(text_to_translate, dest="en"))  # Run in event loop
                talk(f"The translation is: {translation.text}")
            else:
                talk("I didn't catch that. Please try again.")

        elif "don't listen" in command or "stop listening" in command or "sleep" in command:  # Checked


            talk("For how much time do you want me to go to sleep")


            try:
                talk("Please say the duration in seconds.")
                duration_text = take_command()  # Using your existing function

                if duration_text:  # Ensure command is not empty
                    duration_text = duration_text.lower().strip()  # Convert to lowercase and remove extra spaces
                    
                    # Extract number (handles both words and digits)
                    match = re.search(r'\d+', duration_text)  # Extracts a numeric value
                    if match:
                        a = int(match.group())  # Convert extracted number to integer
                    else:
                        a = w2n.word_to_num(duration_text)  # Convert words to number

                    talk(f"Okay, I will stop listening for {a} seconds.")
                    sleep(a)
                    talk("I am back, ready to assist you, sir.")
                    print(f"Resuming listening after {a} seconds...")

            except ValueError:
                talk("Sorry, I couldn't understand the duration. Please try again.")



        elif "news" in command: #checked
            talk("Fetching the latest news for you.")
            
            # Using Google News RSS feed for reliable extraction
            rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
            feed = feedparser.parse(rss_url)

            if not feed.entries:
                talk("Sorry, I couldn't fetch the news at the moment.")
                return

            # Fetch top 5 news articles
            for entry in feed.entries[:3]:
                title = entry.title
                talk(title)
                print(title)

        elif "good boy" in command: #checked
            talk("thank you sir, my pleasure")
        elif "i am fine" in command or "i am great" in command:  # checked
            word = command.replace("i am fine", "").replace("i am great", "").strip()
            talk('Good to see you sir Please tell me how may I help you?')

        elif 'work bestie ' in command: #checked
            command.replace('good work bestie keep it up', '')
            talk("thank you sir,anything else..")

        elif "open safari" in command: #checked
            os.system("open -a Safari")
            talk("Opening Safari browser.")


        elif "what's your name" in command: #checked
            talk("my name is jarvis,your assistant! how may i help you sir.")

        elif 'tesla game'in command: #checked
            command.replace('tesla game', ' ')
            talk('opening sir...')


            pygame.init()
            window = pygame.display.set_mode((1200, 400))
            track = pygame.image.load('track6.png')
            car = pygame.image.load('tesla car.png')
            car = pygame.transform.scale(car, (30, 60))
            car_x = 155
            car_y = 300
            focal_dis = 25
            cam_x_offset = 0
            cam_y_offset = 0
            direction = 'up'
            drive = True
            clock = pygame.time.Clock()
            while drive:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        drive = False
                clock.tick(60)
                cam_x = car_x + cam_x_offset + 15
                cam_y = car_y + cam_y_offset + 15
                up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
                down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
                right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
                print(up_px, right_px, down_px)

                # change direction (take turn)
                if direction == 'up' and up_px != 255 and right_px == 255:
                    direction = 'right'
                    cam_x_offset = 30
                    car = pygame.transform.rotate(car, -90)
                elif direction == 'right' and right_px != 255 and down_px == 255:
                    direction = 'down'
                    car_x = car_x + 30
                    cam_x_offset = 0
                    cam_y_offset = 30
                    car = pygame.transform.rotate(car, -90)
                elif direction == 'down' and down_px != 255 and right_px == 255:
                    direction = 'right'
                    car_y = car_y + 30
                    cam_x_offset = 30
                    cam_y_offset = 0
                    car = pygame.transform.rotate(car, 90)
                elif direction == 'right' and right_px != 255 and up_px == 255:
                    direction = 'up'
                    car_x = car_x + 30
                    cam_x_offset = 0
                    car = pygame.transform.rotate(car, 90)
                # drive
                if direction == 'up' and up_px == 255:
                    car_y = car_y - 2
                elif direction == 'right' and right_px == 255:
                    car_x = car_x + 2
                elif direction == 'down' and down_px == 255:
                    car_y = car_y + 2
                window.blit(track, (0, 0))
                window.blit(car, (car_x, car_y))
                pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
                pygame.display.update()
        elif "smile me" in command: #checked


            pygame.init()
            
            # Create a fullscreen window
            window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

            # Initialize sound mixer
            pygame.mixer.init()

            # Play the sound
            sound_file = 'scary.mp3'
            if os.path.exists(sound_file):
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
            else:
                print("Error: Sound file not found!")

            # Load and display the image
            image_file = 'scr.jpg'
            if os.path.exists(image_file):
                image = pygame.image.load(image_file)
                window.blit(image, (0, 0))
                pygame.display.update()
            else:
                print("Error: Image file not found!")

            time.sleep(2)
            pygame.quit()


        elif "shutdown" in command or "quit" in command: #checked
            talk("Goodbye! Have a great day.")
            QApplication.instance().quit()  # Properly exit PyQt5 GUI
            sys.exit(0)  # Ensure full program termination

        else:
            talk("Please say again sir")


# run_alexa()
