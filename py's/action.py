import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data=data.lower()

    if "what is your name" in   user_data:
        text_to_speech.text_to_speech("my name is virtual Assistant")
        return 'my name is virtual Assistant'

    elif "hello" in user_data  or "hye" in user_data  or "hay" in user_data:  
        text_to_speech.text_to_speech("Hey sir, How i can  help you !")  
        return 'Hey sir, How i can  help you !'
     
    elif "good morning" in user_data:  
         text_to_speech.text_to_speech("Hey sir, good morning!")  
         return 'Hey sir, How i can  help you !'
   
    elif "time now" in user_data:  
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          text_to_speech.text_to_speech(Time)     

    elif "shutdown" in user_data:
          text_to_speech.text_to_speech("ok sir")
          return 'ok sir'


    elif "play music"in user_data:
          webbrowser.open("https://open.spotify.com/")
          text_to_speech.text_to_speech("Spotify.com is now ready ") 
          return 'Spotify.com is now ready'

    elif "play youtube"in user_data:
          webbrowser.open("https://www.youtube.com/")
          text_to_speech.text_to_speech("youtube.com is now ready ")   
          return 'youtube.com is now ready'
    

    elif "Bangtan"in user_data:
          webbrowser.open("https://www.youtube.com/c/BANGTANTV/videos/")
          text_to_speech.text_to_speech("BTS is now ready ")   
          return 'BTS is now ready'


    elif "open google"in user_data:
          webbrowser.open("https://www.google.com/")
          text_to_speech.text_to_speech("google.com is now ready ")  
          return 'google.com is now ready '

    elif "weather"in user_data: 
          ans   = weather.weather()     
          text_to_speech.text_to_speech(ans)  
          return 'ans'

    else :
          text_to_speech.text_to_speech ( "i'm not able to understand!")

          


 
     
     

     

     

            