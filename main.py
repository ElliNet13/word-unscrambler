import requests
import json
from itertools import permutations
from os import system as shell
from time import sleep as wait
import sys

# Check if there are command-line arguments
if len(sys.argv) > 1:
    # Loop through the arguments
    for arg in sys.argv[1:]:
        # Check if the argument starts with a hyphen
        if arg == ('-debug'):
          print("Made by ElliNet13")
          print("| Debug mode |")
          print(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + input("Word: ")).text)


def text_select_screen(options):
    while True:
        def show_options():
            for index, option in enumerate(options, start=1):
                print(f"{index}. {option}")

        def get_user_choice():
            while True:
                try:
                    choice = int(input("Enter the number of your choice: "))
                    if 1 <= choice <= len(options):
                        return options[choice - 1]
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Show options and get user choice
        show_options()
        selected_option = get_user_choice()

        return selected_option

def scramble(input_str):
    return [''.join(p) for p in permutations(input_str)]

print("Made by ElliNet13")
words = scramble(input("Unscramble: "))
print("Firstly let's scramble the word even more")
print("Now let's see what looks right!")
print("Getting unscrambled words")
good = []
for word in words:
    try:
     url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
     response = requests.get(url)
     data = json.loads(response.text)
     try:
      if data[0]["word"]:
          print("Successful word", word)
          good.append(word)
     except KeyError:
       print("Unsuccessful word", word)
       pass
     else:
       print("Unsuccessful word", word)
    except Exception as e:
      print("Error on word " + word + ". Error: " + str(e))

print("Got the unscrambled words!")
wait(2)
try:
    while True:
        shell("clear")
        print("Made by ElliNet13")
        print("Select one to view info about it!")
        getwordinfoeord = text_select_screen(good)
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + getwordinfoeord
        response = requests.get(url)
        wordinfo = json.loads(response.text)[0]
        print("Info for word:", wordinfo["word"])
        print("Part of speech:", wordinfo["meanings"][0]["partOfSpeech"])
        print("Definition:", wordinfo["meanings"][0]["definitions"][0]["definition"])
        try:
          print("Audio of saying it: ", wordinfo["phonetics"][0]["audio"])
        except:
          pass
        print("More info: ", "https://en.wiktionary.org/wiki/" + wordinfo["word"])
        input("Press enter to get info about a different word...")

except KeyboardInterrupt:
    print("Exiting...")