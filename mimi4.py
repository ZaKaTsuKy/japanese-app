from random import choices, randint
from os import system
from gtts import gTTS
from io import BytesIO
import pygame
from time import sleep
import pandas as pd
from math import ceil
import csv
from itertools import islice


# Main function that make user to select what he wanna train
def main():
    system('cls')
    which = input("Que voulez vous étudier : \n \t ▷ Lecture        -- 1  \n \t ▷ Compréhension  -- 2  \n \t ▷ Audio          -- 3  \n \t ▷ Expression     -- 4 \n \t ▷ Nombre         -- 5 \n\t ▷ Grammaire      -- 6 \n\t ▷ Conjugaison    -- 7 \n \t ▷ Paramètres     -- 8\n")
    while which not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Non valide.")
        which = input("Que voulez vous étudier : \n \t ▷ Lecture        -- 1  \n \t ▷ Compréhension  -- 2  \n \t ▷ Audio          -- 3  \n \t ▷ Expression     -- 4 \n \t ▷ Nombre         -- 5 \n \t ▷ Paramètres     -- 6\n")
    match which:
        case "1": lecture()
        case "2": comprehension()
        case "3": audio()
        case "4": expression()
        case "5": nombre()
        case "6": train_lecture("grammaire")
        case "7": conjugaison()
        case "8": parametres()


# user chose lecture mode
def lecture():
    system('cls')
    which = input("Que voulez vous entraîner : \n \t ▷ Hiragana -- 1  \n \t ▷ Katakana -- 2 \n \t ▷ Kanji    -- 3 \n")
    while which not in ["1", "2", "3"]:
        print("Non valide.")
        which = input("Que voulez vous entraîner : \n \t - Hiragana -- 1  \n \t - Katakana -- 2  \n \t - Kanji    -- 3\n")
    match which:
        case "1": train_lecture("hiragana")
        case "2": train_lecture("katakana")
        case "3": train_lecture("kanji")


# function that makes user to train kanji's writing
def comprehension():
    print("Mode non disponible à l'heure actuelle.")
    sleep(2)
    main()    


# user chose audio mode
def audio():
    system('cls')
    which = input("Que voulez vous entraîner : \n \t ▷ Mots    -- 1  \n \t ▷ Phrases -- 2\n")
    while which not in ["1", "2"]:
        print("Non valide.")
        which = input("Que voulez vous entraîner : \n \t ▷ Mots -- 1  \n \t ▷ Phrases -- 2\n")
    match which:
        case "1": train_audio("kanji")
        case "2": print("Mode non disponible à l'heure actuelle."),sleep(2),main()  


# user chose expression mode
def expression():
    print("Mode non disponible à l'heure actuelle.")
    sleep(2)
    main()

        
        
# function that makes user train with number
def nombre():
    system('cls')
    which = input("Comment voulez-vous vous entraîner : \n \t ▷ Lecture  -- 1  \n \t ▷ Ecriture -- 2\n \t ▷ Audio    -- 3  \n")
    while which not in ["1", "2", "3"]:
        print("Non valide.")
        which = input("Que voulez vous entraîner : \n \t - Lecture  -- 1  \n \t - Ecriture -- 2\n \t ▷ Audio    -- 3  \n")
    match which:
        case "1": train_nombre("lecture")
        case "2": train_nombre("ecriture")  
        case "3": train_nombre("audio") 
        
        
# function that makes user go in settings
def parametres():
    system('cls')
    which = input("Que voulez vous faire : \n \t ▷ Ajouter kanjis -- 1  \n \t ▷ Reset scores   -- 2  \n \t ▷ Statistiques   -- 3  \n")
    while which not in ["1", "2", "3"]:
        print("Non valide.")
        which = input("Que voulez vous faire : \n \t ▷ Ajouter kanjis -- 1  \n \t ▷ Reset scores   -- 2  \n \t ▷ Statistiques   -- 3  \n")
    match which:
        case "1": add_kanjis_csv()
        case "2": reset()
        case "3": statistiques()


# function that makes user chose for which scores he wants to reset 
def reset():
    system('cls')
    which = input("Que voulez vous reset : \n \t ▷ Hiragana -- 1  \n \t ▷ Katakana -- 2  \n \t ▷ Kanji    -- 3  \n")
    while which not in ["1", "2", "3"]:
        print("Non valide.")
        which = input("Que voulez vous reset : \n \t ▷ Hiragana -- 1  \n \t ▷ Katakana -- 2  \n \t ▷ Kanji    -- 3  \n")
    match which:
        case "1": reset_scores_taux("hiragana")
        case "2": reset_scores_taux("katakana")
        case "3": reset_scores_taux("kanji")
        

# function that makes user chose for which stats he wants to see
def statistiques():
    system('cls')
    which = input("Quelles statistiques voulez vous voir : \n \t ▷ Hiragana -- 1  \n \t ▷ Katakana -- 2  \n \t ▷ Kanji    -- 3  \n")
    while which not in ["1", "2", "3"]:
        print("Non valide.")
        which = input("Quelles statistiques voulez vous voir : \n \t ▷ Hiragana -- 1  \n \t ▷ Katakana -- 2  \n \t ▷ Kanji    -- 3  \n")
    match which:
        case "1": get_current_stat("hiragana")
        case "2": get_current_stat("katakana")
        case "3": get_current_stat("kanji")
    
      
def conjugaison():
    print("Mode en cours de construction.")
    sleep(2)
    main()  
            
# function that makes user to learn kanas and kanjis
def train_lecture(exercice):
    system('cls')
    count_error, count_good, count = 0, 0, 0
    how_much = int(input("Combien d'exercices de {} voulez-vous pour vous entraîner ? \n".format(exercice)))
    level_target = input("Un jlpt de JLPT particulier ?\n") if exercice == "kanji" else ""
    for i in range(int(how_much)):
        count += 1
        system('cls')
        get_error = False
        kana = probability(exercice, level_target)
        answer = input(f"De quel {exercice} s'agit-il ? {kana[0][0]}".ljust(30) + f"{count}/{how_much}\n".ljust(7))
        while answer not in kana[0][1] and answer not in kana[0][2] and answer != "":
            answer = input("Faux ! De quel kana s'agit-il ? {} \n".format(kana[0][0]))
            get_error = True
        if answer == "":
            get_error = True
        print(f"{kana[0][0]} <=> {kana[0][1]}" if exercice != "kanji" else f"Kanji : {kana[0][0]} \nOnyomi : {kana[0][1]} \nKunyomi : {kana[0][2]} \nTraduction : {kana[0][3]}")
        if not get_error:
            count_good += 1
            modify_score(exercice, True, kana)
            if not (level_target == "" and exercice == "kanji"):
                modify_taux(exercice, level_target)
        else:
            count_error += 1
            modify_score(exercice, False, kana)
            if not (level_target == "" and exercice == "kanji"):
                modify_taux(exercice, level_target)
        sleep(4 if exercice == "kanji" else 2)
    call_stat_session(count_good, count_error, how_much)
    again = input("Voulez-vous recommencer ? \n \t - Oui \n \t - Non \n")
    match again:
        case "oui": train_lecture(exercice)
        case _: main()
    

# function that selects a kanji and speech it
def train_audio(exercice):
    system('cls')
    count_error, count_good, count = 0, 0, 0
    how_much = (int(input("Combien de nombres voulez-vous pour vous entraîner ? \n")))
    for i in range(int(how_much)):
        count += 1
        system('cls')
        get_error = False
        kana = probability(exercice, "")
        make_audio(kana[0][0])
        answer = input(f"De quel {exercice} s'agit-il ?".ljust(30) + f"{count}/{how_much}\n".ljust(7))
        while answer not in kana[0][1] and answer not in kana[0][2] and answer != " ":
            if answer != "":
                get_error = True
                count_error += 1
            else:
                print("Re écoutez.")
                sleep(1)
                make_audio(kana[0][0])
            answer = input("Quel kanji s'agit-il ? \n")
        if answer == " ":
            get_error = True
            print(f"Kanji : {kana[0][0]} \nOnyomi : {kana[0][1]} \nKunyomi : {kana[0][2]} \nTraduction : {kana[0][3]}")
        if not get_error:
            count_good += 1
        else:
            count_error += 1
        #print(f"Kanji : {kana[0][0]} \nOnyomi : {kana[0][1]} \nKunyomi : {kana[0][2]} \nTraduction : {kana[0][3]}")
        sleep(4)
    call_stat_session(count_good, count_error, how_much)
    again = input("Voulez-vous recommencer ? \n \t - Oui \n \t - Non \n")
    match again:
        case "oui": train_audio(exercice)
        case _: main()
  
    
# function that makes the audio physically, used in the preivous function    
def make_audio(element):
    tts = gTTS(element, lang='ja')
    buffer = BytesIO()
    tts.write_to_fp(buffer)
    pygame.init()
    buffer.seek(0)
    pygame.mixer.music.load(buffer)
    pygame.mixer.music.play()
    pygame.time.wait(int(3000))
    pygame.quit()
  

# function that makes user train reading numbers
def train_nombre(exercice):
    system('cls')
    count_error, count_good, count = 0, 0, 0
    how_much = int(input("Combien de nombres voulez-vous pour vous entraîner ?\n"))
    for i in range(int(how_much)):
        count += 1
        system('cls')
        get_error = False
        scale = randint(1, 99999)
        random_number = generate_number_kanji(scale)
        if exercice == "audio":
            make_audio(random_number)
        answer = input("De quel nombre s'agit-il ? {}".format(scale if exercice == "ecriture" else random_number if exercice == "lecture" else "").ljust(50) + f"{count}/{how_much}\n".ljust(6))
        while ((int(answer) != scale) if exercice == "lecture" else(answer != random_number)):
            if exercice == "audio":
                if answer == "":
                    print("Réécoutez.")
                    make_audio(random_number)
                else:
                    get_error = True
                    answer = input("Faux ! De quel nombre s'agit-il ? {}".format(scale if exercice == "ecriture" else random_number if exercice == "lecture" else "").ljust(50) + f"{count}/{how_much}\n".ljust(6))
            else:
                get_error = True
                answer = input("Faux ! De quel nombre s'agit-il ? {}".format(scale if exercice == "ecriture" else random_number if exercice == "lecture" else "").ljust(50) + f"{count}/{how_much}\n".ljust(6))
        if not get_error:
            count_good += 1
        else:
            count_error += 1
        print(f"{scale} : {random_number}")
        sleep(2)
    call_stat_session(count_good, count_error, how_much)
    again = input("Voulez-vous recommencer ? \n \t - Oui \n \t - Non \n")
    match again:
        case "oui": train_nombre(exercice)
        case _: main()


# function that convert numerical number to kanji
def generate_number_kanji(number):
    
    # Liste de chiffres en kanji
    kanji_units = ["万", "千", "百", "十", ""]
    kanji_numbers = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]

    # Convertir le nombre en kanji
    kanji_representation = ""
    num_str = str(number).zfill(5)  # Formatage avec des zéros pour obtenir 5 chiffres

    for i, digit in enumerate(num_str):
        digit = int(digit)
        if digit > 0:
            kanji_representation += kanji_numbers[digit] + kanji_units[i]
            
    return kanji_representation


# function that convert kanji to numerical number
def number_kanji_to_numerical(kanji_string):
    # Liste des chiffres en kanji japonais
    kanji_numbers = {
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
        '五': 5, '六': 6, '七': 7, '八': 8, '九': 9
    }

    # Initialisation des variables
    total = ""

    for char in kanji_string:
        for i in range(len(kanji_numbers)):
            if char == list(kanji_numbers.keys())[i]:
                total += str(list(kanji_numbers.values())[i])

    return total

   
# function that modify score in the csv's
def modify_score(alphabet, isUp, kana):
    df = pd.read_csv(f"{alphabet}.csv")
    if isUp:
        df.loc[kana[0][-1], 'score'] -=  2
        if df.loc[kana[0][-1], 'score'] < 1:
            df.loc[kana[0][-1], 'score'] = 1            
    else:
        df.loc[kana[0][-1], 'score'] += 5
    df.to_csv(f"{alphabet}.csv", index=False)
    

# function that modify taux in the csv's
def modify_taux(alphabet, jlpt):
    if alphabet == "kanji":
        jlpt = jlpt.split() if len(jlpt) > 1 else list(jlpt)
        for i in range(len(jlpt)):
            jlpt[i] = int(jlpt[i])
    df = pd.read_csv(f"{alphabet}.csv")
    modify_probabilities = probability(f"{alphabet}", jlpt)
    for j in range(len(df)):
        if alphabet == "kanji":
            if df.loc[j, 'JLPT'] == jlpt:
                df.loc[j, 'taux'] = modify_probabilities[2][j]
        else:
            df.loc[j, 'taux'] = modify_probabilities[2][j]
    df.to_csv(f"{alphabet}.csv", index=False)


# function that select a kana or a kanji with probability
def probability(alphabet, jlpt):
    df = pd.read_csv(f"{alphabet}.csv")
    coeff = 2.75
    if jlpt != "":
        jlpt = jlpt.split() if len(jlpt) > 1 else list(jlpt)
        for i in range(len(jlpt)):
            jlpt[i] = int(jlpt[i])
    data, score, = [], []
    for j in range(len(df)):
        if jlpt != "":
            if df.loc[j, 'JLPT'] in jlpt:
                kanji = df.loc[j, alphabet]
                onyomi = df.loc[j, 'onyomi']
                if alphabet == "kanji":
                    kunyomi = df.loc[j, 'kunyomi']
                    meaning = df.loc[j, 'meaning']
                data.append([kanji, onyomi, kunyomi, meaning, j] if alphabet == "kanji" else [kanji, onyomi, j])
                score.append(df.loc[j, 'score'])
        else:
            kanji = df.loc[j, alphabet]
            onyomi = str(df.loc[j, 'onyomi']).split()
            if alphabet == "kanji":
                kunyomi = df.loc[j, 'kunyomi'].split()
                meaning = df.loc[j, 'meaning']
            data.append([kanji, onyomi, kunyomi, meaning, j] if alphabet == "kanji" else [kanji, onyomi, j])
            score.append(df.loc[j, 'score'])
    #print(data)        
    total, weight = 0, []
    for i in range(len(data)):
        total += ceil(score[i]*coeff)
        weight.append(ceil(score[i]*coeff))
    selected_data = choices(data, ((ceil(score[i]*coeff))/total for i in range(len(score))))[0]
    
    list_of_droprate = []
    for i in range(len(data)):
        list_of_droprate.append((round((weight[i]/total)*100,3)))
    
    # return a list of tuple [kanji, romaji, (francais), i] and a list of the score of each data
    return selected_data, score, list_of_droprate
    
    
     
# function that calls stats at the end of the current session     
def call_stat_session(count_good, count_error, how_much):
    system('cls')
    print(f"Nombre validés  ✅ : {count_good}")
    print(f"Nombre ratés    ❌ : {count_error}")
    print(f"Taux de réussite📈 : {round((count_good/how_much)*100, 1)}%")
   
 
# add several data in kanji csv 
def add_kanjis_csv():
    stop, data_to_insert, score, taux, jlpt = False, [], 10, 0.0, "N5"
    while not stop:
        system('cls')
        add = input("Entrez le kanji, le romaji et sa traduction sous la forme : kanji romaji traduction\n")
        if add == "":
            stop = True
        if not stop:
            if len(add.split()) == 3:
                data_to_insert.append(add.split())
                print("Data added to csv.")
                sleep(1)
            else:
                print("Mauvais format.")
                sleep(1)
    for data in data_to_insert:
        with open("kanji.csv", "a", encoding="UTF-8", newline='') as f:
            writer = csv.writer(f)
            add_data = []
            results = pd.read_csv('kanji.csv')
            id = len(results) + 1
            add_data.append(id)
            add_data.append(data[0])
            add_data.append(data[1])
            add_data.append(data[2])
            add_data.append(score)
            add_data.append(taux)
            add_data.append(jlpt)
            writer.writerow(add_data)
    probability("kanji",False, None, jlpt="")
    main()


# write all kana in csv
def reset_scores_taux(alphabet, score=9):
    df = pd.read_csv(f"{alphabet}.csv")
    counter5, counter4, counter3, counter2 = 0, 0, 0, 0
    for i in range(len(df)):
        match df.loc[i, 'JLPT']:
            case 5.0: counter5 += 1
            case 4.0: counter4 += 1
            case 3.0: counter3 += 1
            case 2.0: counter2 += 1
    
    for i in range(len(df)):
        df.loc[i, 'score'] = score
        if alphabet != "kanji":
            df.loc[i, 'taux'] = round(100/len(df), 3)
        else:
            match df.loc[i, 'JLPT']:
                case 5.0: df.loc[i, 'taux'] = round(100/counter5, 3)
                case 4.0: df.loc[i, 'taux'] = round(100/counter4, 3)
                case 3.0: df.loc[i, 'taux'] = round(100/counter3, 3)
                case 2.0: df.loc[i, 'taux'] = round(100/counter2, 3)
    df.to_csv(f"{alphabet}.csv", index=False)
    print("Data reseted successfully.")
    sleep(1)
    main()
 
    
# get the current stats of kanas / kanjis
def get_current_stat(alphabet):
    system('cls')
    total = 0.0
    df = pd.read_csv(f"{alphabet}.csv")
    dictionnaire = {}
    for i in range(len(df)):
        kanji = df.loc[i, alphabet]
        taux = df.loc[i, 'taux']
        dictionnaire[kanji] = taux
        total += taux

    print("")
    colomne = "".ljust(8)
    for i in range(5):
        colomne += f"{i+1}".ljust(16)
    print(colomne)
    
    for i in range(ceil(len(df)/5)):   
        stat = f"{i+1}-".ljust(4)
        n_items = list(islice(dictionnaire.items(), 5*i, 5*(i+1)))
        for j in range(len(n_items)):
            stat += f"{n_items[j][0]}:{n_items[j][1]}%".ljust(15)
        print(stat)
    input("\n")
    main()
    
if __name__ == "__main__":
    main()
