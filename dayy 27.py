import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class PajakCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Kalkulator Pajak')
        self.setGeometry(100, 100, 300, 200)

        self.label_pendapatan = QLabel('Pendapatan Tahunan:', self)
        self.input_pendapatan = QLineEdit(self)

        self.button_hitung = QPushButton('Hitung Pajak', self)
        self.button_hitung.clicked.connect(self.hitung_pajak)

        self.label_hasil = QLabel('Hasil Pajak:', self)
        self.hasil_pajak = QLabel('', self)

        layout = QVBoxLayout()
        layout.addWidget(self.label_pendapatan)
        layout.addWidget(self.input_pendapatan)
        layout.addWidget(self.button_hitung)
        layout.addWidget(self.label_hasil)
        layout.addWidget(self.hasil_pajak)

        self.setLayout(layout)

    def hitung_pajak(self):
        try:
            pendapatan = float(self.input_pendapatan.text())
            if pendapatan < 0:
                raise ValueError
            pajak = self.hitung_pajak_berdasarkan_pendapatan(pendapatan)
            self.hasil_pajak.setText(f'Rp {pajak:,.2f}')
        except ValueError:
            QMessageBox.warning(self, 'Input Salah', 'Masukkan angka yang valid untuk pendapatan.')

    def hitung_pajak_berdasarkan_pendapatan(self, pendapatan):
        # Fungsi ini bisa disesuaikan sesuai peraturan perpajakan yang berlaku
        # Contoh sederhana:
        if pendapatan <= 50000000:
            return pendapatan * 0.05
        elif pendapatan <= 100000000:
            return pendapatan * 0.1
        else:
            return pendapatan * 0.15

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PajakCalculator()
    window.show()
    sys.exit(app.exec_())
