import os
from gtts import gTTS

Text = "I want to be successful"

print("please wait...processing")
TTS = gTTS(text=Text, lang='ja')

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# from googletrans import Translator

# translator = Translator()

# translated = translator.translate('svízelná situace', src='cs', dest='hu')

# print(translated.text)