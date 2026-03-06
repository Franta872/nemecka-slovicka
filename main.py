import vocabulary_selector as vc
import checker
import lesson_manager as lm

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                            QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton,
                            QSizePolicy, QButtonGroup, QLineEdit)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

LessonMan = lm.LessonManager("lessons")
lessons = LessonMan.load_lessons(LessonMan.get_available_lessons())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Německá slovíčka")
        self.setGeometry(500, 300, 750, 400)
        self.setWindowIcon(QIcon(r"icon.ico"))
        self.phase = 0
        self.points = {"correct": 0, "wrong": 0}
        self.drawUI()
        self.distributor()

    def drawUI(self):
        # creating widgets
        self.mainText = QLabel("Text", self)
        self.results = QLabel("<span style='color: lime;'>Correct: 0</span>"
                              "<br>"
                              "<span style='color: red;'>Wrong: 0</span>", self)
        self.mainInput = QLineEdit(self)
        self.mainButton = QPushButton("Zkontrolovat", self)
        self.hideButton = QPushButton("Skrýt", self)
        # editing widgets
        self.mainButton.pressed.connect(self.distributor)
        self.mainInput.returnPressed.connect(self.distributor)
        self.hideButton.clicked.connect(self.hideResultsText)
        
        self.hideButton.setMinimumWidth(62)
        self.hideButton.setMinimumHeight(20)
        self.mainButton.setObjectName("mainButton")
        self.hideButton.setObjectName("hideButton")
        self.mainInput.setObjectName("mainInput")

        self.setStyleSheet("""
        QPushButton#mainButton{
            background-color: hsl(256, 87%, 37%);
            border: 4px solid hsl(256, 87%, 10%);
            border-radius: 23px;
            font-weight: bold;
        }
        QPushButton#mainButton:hover, QPushButton#hideButton:hover{
            background-color: hsl(256, 87%, 30%);
        }
        QPushButton#hideButton {
            background-color: hsl(256, 87%, 37%);
            border: 1.5px solid hsl(256, 87%, 10%);
            border-radius: 5px;
        }
        QLineEdit#mainInput{
            background-color: hsl(256, 87%, 20%);
            border: 4px solid hsl(256, 87%, 10%);
            border-radius: 23px;
        }
        """)

        self.results.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for widget in [self.mainText, self.results, self.mainInput, self.mainButton]:
            widget.setStyleSheet("font-size: 30px;")

            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # layouts and etc...
        self.gridLayout = QGridLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.central_widget)
        
        # adding wigets to layout
        self.gridLayout.addWidget(self.hideButton, 0, 1, Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addWidget(self.mainText, 1, 0)
        self.gridLayout.addWidget(self.results, 1, 1)
        self.gridLayout.addWidget(self.mainInput, 2, 0)
        self.gridLayout.addWidget(self.mainButton, 2, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)

    def distributor(self):
        match self.phase:
            case 0:
                self.phase = 1
                self.input()
            case 1:
                self.phase = 0
                self.output()

    def input(self):
        question_type, cz, cz_visi, de, de_gender, de_gender_visi, de_visi, description = vc.choose_word(LessonMan)
        self.vars = {
            "question_type": question_type,
            "cz": cz,
            "cz_visi": cz_visi,
            "de": de,
            "de_gender": de_gender,
            "de_gender_visi": de_gender_visi,
            "de_visi": de_visi,
            "description": description
        }
        self.mainText.setText(checker.word_getter(question_type, cz_visi, de_visi, description))
        self.mainInput.clear()
        self.mainButton.setText("Zkontrolovat")

    def output(self):
        if self.vars["question_type"] == "cz" and \
            not self.vars['de_gender'] is None and \
            len(self.mainInput.text().split(" ", 1)) >= 2:
            gender_answer, word_answer = self.mainInput.text().split(" ", 1)
        else:
            gender_answer, word_answer = "", self.mainInput.text()
        
        output = checker.answer_checker(gender_answer, word_answer,
                               self.vars["question_type"], self.vars["cz"], self.vars["cz_visi"], self.vars["de"], 
                                self.vars["de_gender"], self.vars["de_gender_visi"], self.vars["de_visi"])
        self.mainText.setText(f'{f"Rod: {output[0]}<br>" if not output[0] is None else ""}'
                              f'{"" if output[0] is None else f"Slovo: "}{output[1]}<br>'
                              f'{f"Tvá odpověď: {self.mainInput.text()}<br>" if output[2] else ""}'
                              f"Čeština: {output[3]}<br>"
                              f"Němčina: {output[4]}")
                              #f"<br>de_gender: {self.vars['de_gender']}"
                              #f"<br>Question type: {self.vars['question_type']}")
        if output[5]:
            self.points.update({"correct": self.points["correct"]+1})
        elif not output[5]:
            self.points.update({"wrong": self.points["wrong"]+1})
        self.results.setText(f"<span style='color: lime;'>Correct: {self.points['correct']}</span>"
                              "<br>"
                              f"<span style='color: red;'>Wrong: {self.points['wrong']}</span>")
        self.mainInput.clear()
        self.mainButton.setText("Pokračovat")
    
    def hideResultsText(self):
        self.results.setVisible(not self.results.isVisible())
        self.hideButton.setText("Skrýt" if self.results.isVisible() else "Zobrazit")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()