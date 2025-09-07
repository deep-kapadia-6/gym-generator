import numpy as np
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QImage


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(375, 300, 1200, 300)
        self.setWindowTitle("Gym")
        self.setToolTip("Gym")
        self.setWindowIcon(QIcon("static/dumbbell.ico"))
        self.setCentralWidget(Color('light blue'))

        self.initUI()
    
    def initUI(self):
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText(" Generate Routine")
        self.btn_save.setToolTip("Generate Routine")
        self.btn_save.setIcon(QIcon("static/dumbbell.ico"))
        self.btn_save.setFont(QFont("Arial", weight=QFont.Bold, pointSize=11))
        self.btn_save.move(500, 50)
        self.btn_save.resize(200, 75)
        self.btn_save.clicked.connect(self.clicked)

        self.lbl_result = QtWidgets.QLabel("Routine:", self)
        self.lbl_result.setFont(QFont("Arial", weight=QFont.Bold, pointSize=9))
        self.lbl_result.move(175, 175)
        self.lbl_result.resize(200, 50)

    def week(self):
        # Define exercise lists
        self.chest1 = ['Barbell bench press', 'Incline bench press']
        self.chest2 = ['Flat dumbbell press', 'Incline dumbbell press', 'Cable flys', 'Pushups']
        self.back1 = ['Lat pulldown', 'Weighted pullups']
        self.back2 = ['Seated row', 'Bent over row', 'Lat pushdowns', 'Face pulls']
        self.shoulder1 = ['Barbell shoulder press']
        self.shoulder2 = ['Dumbbell shoulder press', 'Lateral raises', 'Single arm leaning in raise', 'Cable crossover']
        self.quads1 = ['Back squat', 'Front squat']
        self.quads2 = ['Leg press', 'Split squats', 'Lunges']
        self.glutes = ['Hip thrusts', 'Deadlift', 'Glute ham raise', 'Romanian deadlift', 'Sled push']
        self.quads_rf = ['Leg extensions']
        self.hamstrings = ['Seated/prone leg curl']
        self.calves = ['Standing calf raise', 'Seated calf raise', 'Leg press calf raise']

        # Randomly select exercises for Upper1
        self.Upper1 = []
    
        self.c1u1 = np.random.choice(self.chest1)
        self.Upper1.append(self.c1u1)
        self.chest1.remove(self.c1u1)
        self.b1u1 = np.random.choice(self.back1)
        self.Upper1.append(self.b1u1)
        self.back1.remove(self.b1u1)
        self.s1u1 = np.random.choice(self.shoulder1)
        self.Upper1.append(self.s1u1)
        self.c2u1 = np.random.choice(self.chest2)
        self.Upper1.append(self.c2u1)
        self.chest2.remove(self.c2u1)
        self.b2u1 = np.random.choice(self.back2)
        self.Upper1.append(self.b2u1)
        self.back2.remove(self.b2u1)
        self.s2u1 = np.random.choice(self.shoulder2)
        self.Upper1.append(self.s2u1)
        self.shoulder2.remove(self.s2u1)
    
        # Randomly select exercises for Legs1
        self.Legs1 = []
        for exercise_list in [self.calves, self.quads1, self.quads2, self.glutes, self.quads_rf, self.hamstrings]:
            exercise = np.random.choice(exercise_list)
            self.Legs1.append(exercise)
          
        # Randomly select exercises for Upper2 (Not same as Upper1)
        self.Upper2 = []
        self.c1u2 = np.random.choice(self.chest1)
        self.Upper2.append(self.c1u2)
        self.b1u2 = np.random.choice(self.back1)
        self.Upper2.append(self.b1u2)
        self.s1u2 = np.random.choice(self.shoulder1)
        self.Upper2.append(self.s1u2)
        self.c2u2 = np.random.choice(self.chest2)
        self.Upper2.append(self.c2u2)
        self.b2u2 = np.random.choice(self.back2)
        self.Upper2.append(self.b2u2)
        self.s2u2 = np.random.choice(self.shoulder2)
        self.Upper2.append(self.s2u2)

        self.upper1_str = ', '.join(self.Upper1)
        self.legs1_str = ', '.join(self.Legs1)
        self.upper2_str = ', '.join(self.Upper2)
        
        # Return the formatted string
        return f"Upper1: {self.upper1_str}\nLegs1: {self.legs1_str}\nUpper2: {self.upper2_str}"

    def clicked(self):
        new_text = self.week()
        self.lbl_result.setText("Routine:\n" + new_text)
        self.lbl_result.adjustSize()

def window():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("static/dumbbell.ico"))
    win = my_window()
    win.show()
    sys.exit(app.exec_())
        
window()