import pygame
from gtts import gTTS
from playsound import playsound
# Import required libraries
from newspaper import Article
#newspaper3k is working
print("newspaper3k is installed and working!")

import nltk

#Initialize pygame mixer

pygame.mixer.init()

# URL of the news article
url = "https://pitchfork.com/reviews/albums/lisha-g-trini-viv-groovy-steppin-shit/"  # Replace with a valid URL
article = Article(url)

# Download punkt for sentence tokenization
nltk.download('punkt')



# Fetch and parse the article
article.download()
article.parse()

# Perform natural language processing
article.nlp()

# Display the text
print("Article Text:\n", article.text)

# Extracted text from the article
text = article.text

# Convert text to speech
tts = gTTS(text, lang='en')

# Save the audio file
tts.save("news_audio.mp3")
print("Audio saved as news_audio.mp3")

# Play the audio file using pygame
pygame.mixer.music.load("news_audio.mp3")
pygame.mixer.music.play()

#Keep the program running while audio plays

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

