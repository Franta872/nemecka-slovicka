import random
import difflib
import vocabulary_selector as vc
from htmlStyleLite import *

#! question_type, cz, cz_visi, de, de_gender, de_gender_visi, de_visi, description = vc.choose_word()
#print(question_type, cz, de, de_gender, de_visi, description, sep="\n")    

#print(("němčina: " + de_visi) if description is None else f"němčina ({description}): " + de_visi  if question_type == "de" else "čeština: "+cz_visi)
def word_getter(question_type, cz_visi, de_visi, description):
    if description is None and question_type == "de":
        return "němčina: " + bold(de_visi)
    elif description is not None and question_type == "de":
        return f"němčina ({description}): " + bold(de_visi)
    elif question_type == "cz":
        return "čeština: " + bold(cz_visi)

def answer_checker(answer_gender, answer, question_type, cz, cz_visi, de, de_gender, de_gender_visi, de_visi):
    correct_asnwer = True
    # gender
    show_answer = False
    result_gender = None
    if question_type != "de" and de_gender != None:
        if answer_gender.lower() == de_gender:
            result_gender = random.choice(["správně!", "dobře!", "velmi dobře!"])
        elif answer_gender == "":
            result_gender = f"{random.choice(['špatně, nic jsi nenapsal. Mel být', '... asi špatně, nic jsi nezadal. Mel být'])} {de_gender_visi}"
            correct_asnwer = False
        else:
            result_gender = f"{random.choice(['špatně! Měl být', 'nesprávně! Měl být'])} {de_gender_visi}"
            show_answer = True
            correct_asnwer = False


    # rest of the word
    lang_var = de if question_type != "de" else cz
    similarity = max(difflib.SequenceMatcher(None, answer.lower(), (de[x] if question_type != "de" else cz[x]).lower()).ratio() for x in range(len(de)))

    if answer in lang_var:
        result = random.choice(["správně!", "výborně!", "dokonalé!"])
    elif "" == answer:
        result = random.choice(["špatně, nic jsi nenapsal.", "... nic jsi nenapsal", "... nic = chyba"])
        correct_asnwer = False
    elif answer.lower() in [x.lower() for x in lang_var]:
        result = random.choice(["správně, ale velikost písmen dělá problémy |:", "asi jo, ale ta velikost písmen."])
        show_answer = True
    elif remove_diacritics(answer) in [remove_diacritics(x) for x in lang_var]:
        result = random.choice(["asi ještě správně, ale diakritika dělá problémy.", "asi dobře, ale ta diakritika."])
        show_answer = True
    elif remove_diacritics(answer.lower()) in [remove_diacritics(x.lower()) for x in lang_var]:
        result = random.choice(["špatně, je tu problém ve velikosti písmen a ani diakritika tam není.", "špatně. problém = neexistující diakritika a správná velikost písmen."])
        show_answer = True
        correct_asnwer = False
    elif similarity >= 0.87:
        result = random.choice(["spíše správně, ale je tam gramatická chyba.", "asi správně, ale je tam malá chyba."])
        show_answer = True
    elif 0.75 <= similarity < 0.87:
        result = random.choice(["spíše špatně, ale je to podobné výsledku.", "asi špatně, ale je to podobné."])
        show_answer = True
        correct_asnwer = False
    else:
        result = random.choice(["prostě špatně!", "špatně!", "hrozně!", "nesprávně!"])
        show_answer = True
        correct_asnwer = False

    #cz_visi, de_visi = map(lambda y: bold(color(underline(y) if question_type == f"{y=}".split("_")[0] else y, "red")), [cz_visi, de_visi])
    cz_visi = bold(underline(cz_visi) if question_type != "cz" else cz_visi)
    de_visi = bold(underline(de_visi) if question_type != "de" else de_visi)

    return result_gender, result, show_answer, cz_visi, de_visi, correct_asnwer

########
#if result_gender is not None:
#    print(f"Rod je {result_gender}")
#print(f"{random.choice(['Slovíčko je', 'Tentokrát to je', 'Je to'])} {result}")
#print(f"Tvá odpověď: {answer_gender if de_gender is not None else ''} {answer}\n" if show_answer else "")
#print(f"Slovo německy:  {de_visi}\nSlovo česky:    {cz_visi}\n")
########