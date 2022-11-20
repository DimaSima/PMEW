import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QStackedWidget, QWidget



class Window(QWidget):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.x = 100
        self.y = 100
        self.width = 1300
        self.height = 910
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setStyleSheet("background:rgb(255,255,255)")
        self.setWindowTitle('Fahrzeugbuchungs - Tool')


        WindowLayout = QVBoxLayout()
        self.setLayout(WindowLayout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = Window()
    win.show()
    sys.exit(app.exec_())