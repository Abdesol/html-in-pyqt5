import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import os
 
class htmlPyQt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HtmlPyQt")
        #self.resize(800, 600)

        self.centralwidget = QWidget()
        self.lay = QVBoxLayout(self.centralwidget)

        self.html_view = QWebEngineView()
        self.lay.addWidget(self.html_view)

        self.html_view.load(QUrl.fromLocalFile(os.path.abspath('my_portfolio/index.html')))
        self.setCentralWidget(self.centralwidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = htmlPyQt()
    mainwindow.show()
    sys.exit(app.exec_())

