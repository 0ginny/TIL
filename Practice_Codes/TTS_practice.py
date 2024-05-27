from gtts import gTTS
text ="He studied for his undergraduate degree at Harvard, and he even writes scenario."

tts = gTTS(text=text, lang='en')
tts.save("helloEN.mp3")
