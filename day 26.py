import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contoh Aplikasi PyQt')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel('Selamat datang di PyQt!', self)
        self.label.setStyleSheet('font-size: 18pt;')

        self.button = QPushButton('Klik Saya', self)
        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addStretch(1)

        self.setLayout(layout)

    def on_button_click(self):
        self.label.setText('Tombol telah diklik!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
