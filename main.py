from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class HtmlPyqt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HtmlPyqt")
        self.centralWidget = QWidget(self)
        self.lay = QVBoxLayout(self.centralWidget)

        self.html_view = QWebEngineView() # this is the root line :)
        self.lay.addWidget(self.html_view)

        with open('index.html','r') as i:
            html = i.read()
            self.html_view.setHTML(html)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = HtmlPyqt()

    sys.exit(app.exec_())
    

