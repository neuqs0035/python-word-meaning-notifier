from plyer import notification
from random import choice
from time import sleep

while True:

    file = open("dictionary.csv")

    all_words = file.readlines()

    random_word = choice(all_words).split(",")

    notification.notify(

        title = "Vocabulary",
        message = "Word : " + random_word[0] + "\nMeaning : " + random_word[2],
        app_icon = "dictionary.ico",
        timeout = 10
    )

    sleep(10)