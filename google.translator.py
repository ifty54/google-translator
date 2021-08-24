# google-translator
#print(googletrans.LANGUAGES)
import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
conv_lang = 'fi'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice)
        print(text)
except:
    pass

translated = translator.translate(text, dest=conv_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=conv_lang)
converted_audio.save('audio.mp3')
playsound.playsound('audio.mp3')
