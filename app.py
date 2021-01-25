# from PySide6.QtWidgets import QApplication
# from PySide6.QtQuick import QQuickView
# from PySide6.QtCore import QUrl
import sys
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from PySide2 import QtWidgets, QtQuick, QtCore, QtGui, QtQml, QtWebEngine

from style_rc import *

class WebView(QtCore.QObject):
    @QtCore.Slot(str, result=str)
    def getUrl(self, url):
        filename = QtCore.QUrl(url).toLocalFile()
        notebook = nbformat.read(Path(filename), as_version=4)
        html_exporter = HTMLExporter()
        # html_exporter.template_name = 'lab'
        (body, resources) = html_exporter.from_notebook_node(notebook)
        # self.webView.setHtml(body)
        return body


if __name__ == "__main__":

    # sys.argv += ['--style', 'material']

    app = QtWidgets.QApplication(sys.argv)
    QtWebEngine.QtWebEngine.initialize()

    app.setWindowIcon(QtGui.QIcon("./favicon.png"))

    # app.ApplicationWindow.WebView.intialize()
    engine = QtQml.QQmlApplicationEngine()

    view = WebView()

    context = engine.rootContext()
    context.setContextProperty("con", view)

    engine.load("qml/app.qml")

    # view = QtQuick.QQuickView()
    # url = QtCore.QUrl("qml/app.qml")
    # engine.show()
    # view.setSource(url)

    # view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)

    # view.show()
    # app.exec_()

    # Instance of the Python object
    # bridge = Bridge()

    # # Expose the Python object to QML
    # context = engine.rootContext()
    # context.setContextProperty("con", bridge)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
