import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
import subprocess

class App(QWidget):
    global api_key_label
    global novel_path_label
    global chapter_label
    global lang_label
    def __init__(self):
        super().__init__()
        self.title = 'novel'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        api_key_label = QLabel('API Key')
        novel_path_label = QLabel('novel path')
        chapter_label = QLabel('number of chapters')
        lang_label = QLabel('Language')
        
        api_key_edit = QLineEdit()
        novel_path_edit = QLineEdit()
        chapter_edit = QLineEdit()
        lang_edit = QLineEdit()
        
        grid.addWidget(api_key_label, 1, 0)
        grid.addWidget(api_key_edit, 1, 1)

        grid.addWidget(novel_path_label, 2, 0)
        grid.addWidget(novel_path_edit, 2, 1)

        grid.addWidget(chapter_label, 3, 0)
        grid.addWidget(chapter_edit, 3, 1)
        
        grid.addWidget(lang_label, 4, 0)
        grid.addWidget(lang_edit, 4, 1)

        submit_button = QPushButton('submit')
        submit_button.clicked.connect(lambda: self.submit(api_key_edit.text(),novel_path_edit.text(),chapter_edit.text(),lang_edit.text()))
        grid.addWidget(submit_button, 5, 0)

        self.show()

    def submit(self, api_key,novel_path_edit,chapter_edit,lang_edit):
        subprocess.call(['python', 'xiou.py', api_key,novel_path_edit,chapter_edit,lang_edit])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())