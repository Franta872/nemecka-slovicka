# toto je program, který vytvoří JSON pro další program
import json
import pyperclip #pip install pyperclip

nazev_strany = f"strana_{input('Jaké je číslo strany?: ')}"
print(nazev_strany)
words_list = []
word_dict = {}

while True:
    gender = input("Zadejte rod slova: ").strip().lower()
    if gender == "":
        gender = None
    de = input("Zadejte německé slova: ")
    de = de.split(";")
    cz = input("Zadejte české slova: ")
    cz = cz.split(";")
    description = input("Zadejte popis slova: ").strip()
    if description == "":
        description = None
    word_dict.update({"cz": cz})
    word_dict.update({"de": de})
    word_dict.update({"gender": gender})
    word_dict.update({"description": description})
    words_list.append(word_dict.copy())
    word_dict.clear()
    print(de, cz, gender, description)
    if input("Chceš pokračovat? (ne pro ne): ").strip().lower() in ["ne", "n", "no", "nein"]:
        break

json_text = json.dumps({nazev_strany: words_list}, ensure_ascii=False, indent=2)
pyperclip.copy(json_text)
print(json_text)