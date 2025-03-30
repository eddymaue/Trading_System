import sys, json, os
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Qt
from QT_MKQtxtbox_UI import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.PushButton.clicked.connect(self.on_close)
        self.oldPos = None
        self.load_position()

    def load_position(self):
        if os.path.exists('QT_MKQtxtbox_pos.json'):
            with open('QT_MKQtxtbox_pos.json', 'r') as f:
                pos = json.load(f)
                self.move(pos['x'], pos['y'])

    def save_position(self):
        pos = {'x': self.x(), 'y': self.y()}
        with open('QT_MKQtxtbox_pos.json', 'w') as f:
            json.dump(pos, f)

    def on_close(self):
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setText("Fermeture en cours...")
        msg.exec()
        self.save_position()
        subprocess.Popen(['python', 'MonScript.py', 'SourisAction.txt'])
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.oldPos = None

    def on_text_changed(self):
        symbol = self.ui.textEdit.toPlainText().strip().upper()
        if symbol:
            print(f"Nouveau symbole: {symbol}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())