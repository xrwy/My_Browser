import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar_
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self,)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigateHome)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigateToUrl)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.updateUrl)
    
    def navigateHome(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigateToUrl(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)

QApplication.setApplicationName('My Simple Browser')
window = MainWindow()
app.exec_()