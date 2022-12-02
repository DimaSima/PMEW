import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QMenu, QToolBar

from PyQt5.QtCore import Qt


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.x = 100
        self.y = 100
        self.width = 1100
        self.height = 810
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setStyleSheet("background:rgb(255,255,255)")
        self.setWindowTitle('Projekt - Planer')

        self.createMenuBar()

        WindowLayout = QVBoxLayout()
        self.setLayout(WindowLayout)

    def createMenuBar(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)

        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")

    def createToolBars(self):
        fileToolBar = self.addToolBar("File")
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = Window()
    win.show()
    sys.exit(app.exec_())