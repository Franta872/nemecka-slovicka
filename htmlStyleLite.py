import unicodedata

def remove_diacritics(text):
    normalized = unicodedata.normalize("NFD", text)
    return "".join(
        char for char in normalized
        if unicodedata.category(char) != "Mn"
    )
def bold(text: str):
    return "<b>"+text+"</b>"
def underline(text: str):
    return "<u>"+text+"</u>"
def color(text: str, color: str):
    return f"<span style='color: {color}'>"+text+"</span>"