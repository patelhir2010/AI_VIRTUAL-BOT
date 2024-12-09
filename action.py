import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data :
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return 'My name is virtual assistant'

    elif "Hello" in user_data or "hii" in user_data:
        text_to_speech.text_to_speech("Hey , sir How can i help you")
        return 'hey , sir how can i help you'

    elif "Good morning" in user_data:
        text_to_speech.text_to_speech("Good morning Sir")
        return 'Good morning Sir'

    elif "What is the time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://ganna.com")
        text_to_speech.text_to_speech("ganna.com is now ready to play music for you")
        return "ganna.com is now ready to play music for you"
        
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com")
        text_to_speech.text_to_speech("youtube is now ready for you")
        return 'youtube is now ready for you'

    elif "open Google" in user_data:
        webbrowser.open("https://google.com")
        text_to_speech.text_to_speech("Google is now ready for you to search")
        return "Google is now ready for you to search"
    
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
    else :
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"