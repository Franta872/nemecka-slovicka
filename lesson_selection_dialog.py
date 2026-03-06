from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QCheckBox,
    QDialog,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt

class lessonSelectionDialog(QDialog):
    def __init__(self, lesson_manager):
        super().__init__()
        
        self.lesson_manager = lesson_manager
        self.setWindowTitle("Výběr lekcí")
        self.setWindowIcon(QIcon(r"icon.ico"))
        self.setMinimumSize(280, 500)

        self.selected_lessons = []

        self.main_layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        self.checkboxes = []

        for lesson in self.lesson_manager.get_available_lessons():
            checkbox = QCheckBox(lesson)
            self.scroll_layout.addWidget(checkbox)
            checkbox.setStyleSheet("font-size: 25px;"
                                   "margin: 10px;")
            self.checkboxes.append(checkbox)

        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

        self.main_layout.addWidget(self.scroll_area)

        self.ok_button = QPushButton("Potvrdit")
        self.ok_button.setStyleSheet("font-size: 24px;"
                                     "background-color: hsl(256, 87%, 37%);"
                                     "border: 3px solid hsl(256, 87%, 10%);"
                                     "border-radius: 13px;"
                                     "font-weight: bold;")
        self.ok_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ok_button.clicked.connect(self.accept_selection)
        self.main_layout.addWidget(self.ok_button)

    def accept_selection(self):
        self.selected_lessons = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        if not self.selected_lessons:
            QMessageBox.critical(None, "Chyba!", "Nevybral jsi nic. Vyber něco!")
        else:
            self.accept()