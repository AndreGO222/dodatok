import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from random import shuffle

class DuolingoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Duolingo')
        self.setGeometry(100, 100, 400, 200)

        self.word_label = QLabel('Слово:', self)
        self.word_entry = QLineEdit(self)

        self.trans_label = QLabel('Перевід:', self)
        self.trans_entry = QLineEdit(self)

        self.check_button = QPushButton('Перевірити', self)
        self.check_button.clicked.connect(self.checkTranslation)

        self.next_button = QPushButton('Наступне слово', self)
        self.next_button.clicked.connect(self.nextWord)

        vbox = QVBoxLayout()
        vbox.addWidget(self.word_label)
        vbox.addWidget(self.word_entry)
        vbox.addWidget(self.trans_label)
        vbox.addWidget(self.trans_entry)

        hbox = QHBoxLayout()
        hbox.addWidget(self.check_button)
        hbox.addWidget(self.next_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.show()

        self.words = {'apple': 'яблуко', 'banana': 'банан', 'cat': 'кіт', 'dog': 'собака'}
        self.current_word = None
        self.nextWord()

    def nextWord(self):
        self.current_word, translation = self.words.popitem()
        self.word_entry.setText(self.current_word)
        self.trans_entry.clear()

    def checkTranslation(self):
        translation = self.trans_entry.text().strip()
        if translation == self.words[self.current_word]:
            self.trans_label.setText('Правильно!')
        else:
            self.trans_label.setText('Неправильно!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DuolingoApp()
    sys.exit(app.exec_())