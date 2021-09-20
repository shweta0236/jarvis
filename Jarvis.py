import pyttsx3, math
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import sys
import pytemperature

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning...have a great day")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon... i hope you're doing great")
    else:
        speak("Good evening...")

    speak("I'm Jarvis, please tell how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        r.dynamic_energy_ratio = 1.5
        r.energy_threshold = 500
        r.non_speaking_duration = 0.3
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query} \n")
    except Exception as e:
        return ""
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            try:
                speak("searching Wikipedia..")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                query = takeCommand().lower()


        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com')

        elif 'stack overflow' in query:
            webbrowser.open('https://www.stackoverflow.com')

        elif 'play music' in query:
            music_dir = ("C:\\Users\\Shweta\\Desktop\\new")
            songs = os.listdir(music_dir)
            # print(songs)
            choice = random.choice(songs)
            os.startfile(os.path.join(music_dir, choice))


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f" time is {strTime}")


        elif 'weather' in query:
            speak("searching Weather..")
            query = query.replace("weatdeher", "")
            results = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            speak("speak city name")
            city = takeCommand().lower()
            url = results + city
            json_data = requests.get(url).json()
            speak("according to Open Weather, weather condtion is")
            y = json_data["main"]
            current_temperature = math.ceil(pytemperature.k2c((y["temp"])))
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]

            weather_des = json_data['weather'][0]["description"]

            print(" Temperature  = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_des))

            speak(
                f" Temperature is {current_temperature} degree celcius. atmospheric pressure (in hPa unit) is {current_pressure}. humidity (in percentage) is {current_humidiy} and {weather_des}")
            speak(f"in {city}")

            if "rain" in weather_des:
                speak('take your umbrella with you')
            else:
                speak("")

        elif 'open india news' in query:
            api_address = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=a665a34767034eab8bc9e94d21f8e4ae'
            json_data = requests.get(api_address).json()

            formatted_data = json_data['articles'][0]['title']
            formatted_data1 = json_data['articles'][1]['title']
            formatted_data2 = json_data['articles'][2]['title']
            formatted_data3 = json_data['articles'][3]['title']
            formatted_data4 = json_data['articles'][4]['title']
            formatted_data5 = json_data['articles'][5]['title']
            formatted_data6 = json_data['articles'][6]['title']
            formatted_data7 = json_data['articles'][7]['title']
            formatted_data8 = json_data['articles'][8]['title']
            formatted_data9 = json_data['articles'][9]['title']

            print(formatted_data)
            print(formatted_data1)
            print(formatted_data2)
            print(formatted_data3)
            print(formatted_data4)
            print(formatted_data5)
            print(formatted_data6)
            print(formatted_data7)
            print(formatted_data8)
            print(formatted_data9)

            speak(formatted_data)
            speak('next news is ')
            speak(formatted_data1)
            speak('next news is ')
            speak(formatted_data2)
            speak('next news is ')
            speak(formatted_data3)
            speak('next news is ')
            speak(formatted_data4)
            speak('next news is ')
            speak(formatted_data5)
            speak('next news is ')
            speak(formatted_data6)
            speak('next news is ')
            speak(formatted_data7)
            speak('next news is ')
            speak(formatted_data8)
            speak('next news is ')
            speak(formatted_data9)
            speak('news is end')

        elif 'quit' in query:
            sys.exit()

        elif 'how are you jarvis' in query:
            speak("I'm fine, how about you?")

        elif 'who are you' in query:
            speak("I'm Jarvis, your laptop voice assistant")

        elif 'where are you from' in query:
            speak('i belong from your thinking')

        elif 'where do you live' in query:
            speak('i live in virtual world')

        elif 'what do you do' in query:
            speak('i work for you for your convenient')

        elif 'good job' in query:
            speak('thank you')

        elif 'thank you' in query:
            speak('you are welcome .')

        elif 'can you speak english' in query:
            speak('yes i can speak english')



        elif "search" in query:
            query = query.replace("search", "")
            webbrowser.open('https://www.google.com/search?q=' + query)

       
