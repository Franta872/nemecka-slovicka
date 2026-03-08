# toto je program, který vytvoří JSON pro další program
import json
import pyperclip #pip install pyperclip

cislo_strany = ""
while not cislo_strany.isdigit():
    cislo_strany = input("Jaké je číslo strany?: ").strip()
nazev_strany = f"strana_{cislo_strany}"
print(nazev_strany)
words_list = []
word_dict = {}

while True:
    gender = None
    while not (gender == "" or gender in ["der", "die", "das"]):
        gender = input("Zadejte rod slova: ").strip().lower()
    if gender == "":
        gender = None
    de = input("Zadejte německé slova: ").strip()
    de = de.split(";")
    cz = input("Zadejte české slova: ").strip()
    cz = cz.split(";")
    description = input("Zadejte popis slova: ").strip()
    if description == "":
        description = None
    word_dict.update({"gender": gender})
    word_dict.update({"de": de})
    word_dict.update({"cz": cz})
    word_dict.update({"description": description})
    words_list.append(word_dict.copy())
    word_dict.clear()
    print(gender, de, cz, description)
    if input("Chceš pokračovat? (ne pro ne): ").strip().lower() in ["ne", "n", "no", "nein"]:
        break

json_text = json.dumps({nazev_strany: words_list}, ensure_ascii=False, indent=2)
pyperclip.copy(json_text)
print(json_text)