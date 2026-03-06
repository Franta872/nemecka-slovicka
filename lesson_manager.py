from pathlib import Path
import json

from pprint import pprint

class LessonManager:
    def __init__(self, path: str = "lessons") -> None:
        self.lessons_folder = Path(path)

    def get_available_lessons(self) -> list:
        return [file.stem for file in self.lessons_folder.glob("*.json")]
    
    def load_lessons(self, lessons) -> list:
        loaded_lessons = dict()
        for lesson in lessons:
            loaded_lessons.update(json.loads((self.lessons_folder/f"{lesson}.json").read_text(encoding="utf-8")))
        self.lessons = []
        for strana in loaded_lessons.values():
            for slovo in strana:
                self.lessons.append(slovo)
        self.lessons_copy = self.lessons.copy()
        return self.lessons
    
    def lessons_copy_remove(self, removed_word) -> None:
        self.lessons_copy.remove(removed_word)

        if not self.lessons_copy:
            self.lessons_copy = self.lessons.copy()

if __name__ == "__main__":
    LessonMan = LessonManager()
    LessonMan.load_lessons(LessonMan.get_available_lessons())
    pprint(LessonMan.lessons, indent=4)
