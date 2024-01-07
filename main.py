from plyer import notification
from random import choice
import requests

file = open("words-all.txt")

all_words = file.readlines()

random_word = choice(all_words).split(",")

notification.notify(

    title = "Vocabulary",
    message = "Word : " + random_word[0] + "\nMeaning : " + random_word[1],
    timeout = 10
)