# import json
import random
#from pathlib import Path
# import sys
# import os
from htmlStyleLite import *
import lesson_manager as lm

#def resource_path(relative_path):
#   if hasattr(sys, "_MEIPASS"):
#       return os.path.join(sys._MEIPASS, relative_path)
#   return os.path.join(os.path.abspath("."), relative_path)
#
#with open(resource_path("lekce_2.3.json"), "r", encoding="utf-8") as f:
#   lekce = json.load(f)

#       print(json.dumps(lekce["strana_77"], indent=4, ensure_ascii=False))

#with open(f"{Path(__file__).parent}/vocabulary.json", "r", encoding="utf-8") as f:
#    lekce = json.load(f)
#lessons = []
#for strana in loaded_lessons.values():
#    for slovo in strana:
#        lessons.append(slovo)

def choose_word(LessonMan):
    question_type = random.choice(["cz", "de"])

    word = random.choice(LessonMan.lessons_copy)
    LessonMan.lessons_copy_remove(word)

    cz = word.get("cz")
    cz_visi = bold(", ".join(cz))
    de_visi = []
    de_gender = word.get("gender")
    de = word.get("de")
    if de_gender == "der":
        de_gender_visi = color(de_gender, "blue")
    elif de_gender == "die":
        de_gender_visi = color(de_gender, "red")
    elif de_gender == "das":
        de_gender_visi = color(de_gender, "green")
    else:
        de_gender_visi = None
    if de_gender is None:
        for item in de:
            de_visi.append(item)
    else:
        for x in range(len(word.get("de"))):
            de_visi.append(f"{de_gender_visi} {bold((word.get('de'))[x])}")
    de_visi = bold(", ".join(de_visi))
    description = word.get("description")

    return question_type, cz, cz_visi, de, de_gender, de_gender_visi, de_visi, description