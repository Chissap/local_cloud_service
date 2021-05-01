import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, 
                                QVBoxLayout, QWidget)
from PyQt5.QtCore import QProcess, QTimer, QEventLoop

import time

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Worker_bot_folder v.1.0")

        self.p = None

        self.btn = QPushButton("Copy folder")
        self.btn.setToolTip("<h4>The program copies whole folder once</h4>")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):

        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("python", ['projekti_kansio\worker_bot_folder.py'])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("latin-1")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("latin-1")
        self.message(stdout)

    def handle_state(self, state):
        states = {   
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None        


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec_()

#TODO: / #FIXME:
# how to make gui run code slower

# import user imput from worker_bot.py into gui to assign copy path

#TODO:
# make another button to run the code that copies the whole dir