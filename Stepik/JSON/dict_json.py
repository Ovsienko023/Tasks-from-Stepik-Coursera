import json
import difflib


data = json.load(open("dict.json"))



def user():
    word_user = (input("Введи ключ: "))
    dif_word = difflib.get_close_matches(word_user, data) #cutoff=0.88  

    if word_user in data:
        print(data[word_user])
    else:
        print("Ключа нет!, возможно вы имели в виду: ", dif_word[0])
        action = input("(Y/n)?")
        if action == 'y':
            print('-',*data[dif_word[0]])
        if action == 'n':
            return False


user()

