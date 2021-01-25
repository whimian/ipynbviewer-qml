import QtQuick 2.12
// import QtQuick.Window 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.3
import QtQuick.Controls.Material 2.12
import QtWebView 1.1


ApplicationWindow {
    id: window
    title: "IPYNB Viewer"
    width: 1000
    height: 800
    visible: true
    //SET FLAGS
    // flags: Qt.WindowCloseButonHint | Qt.WindowMinimizeButtonHint //| Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint

    // menuBar
    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: fileDialog.open();
            }
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();
            }
        }
        Menu {
            title: qsTr("Help")
            MenuItem {
                text: qsTr("About")
                onTriggered: aboutDialog.open();
            }
        }
    }


    // Column {
    //     anchors.centerIn: parent

    //     RadioButton { text: qsTr("Small") }
    //     RadioButton { text: qsTr("Medium");  checked: true }
    //     RadioButton { text: qsTr("Large") }
    // }
    ColumnLayout{
        spacing: 2
        anchors.fill: parent
        WebView {
            id: webview
            url: "file:///./index.html"
            Layout.alignment: Qt.AlignCenter

            Layout.fillWidth: true
            Layout.fillHeight: true

            onLoadingChanged: {
                var url_string = String(url)

                if (url_string.endsWith("ipynb")) {
                    webview.loadHtml(con.getUrl(url))
                }
            }
        }
    }

    FileDialog {
        id: fileDialog
        title: "Please choose a file"

        // path: ""

        folder: shortcuts.home
        onAccepted: {
            // console.log("You chose: " + fileDialog.fileUrls)
            // webview.url = webview.loadHTML(con.getUrl(fileDialog.fileUrls))
            webview.loadHtml(con.getUrl(fileDialog.fileUrls))
            // fileDialog.path = fileDialog.fileUrls
            // console.log(fileDialog.path)
            // Qt.quit()
        }
        onRejected: {
            // console.log("Canceled")
            // Qt.quit()
        }
        // Component.onCompleted: visible = true
    }

    MessageDialog {
        id: aboutDialog
        title: "About"
        text: " IPYNBViewer"
        informativeText: qsTr("Created by Yu Hao\nE-mail: yuhao89@live.cn\n\nA jupyter notebook (.ipynb) file viewer created with nbconvert, pyside2 ,and QML")
        icon: StandardIcon.Information
        onAccepted: {
            // console.log("And of course you could only agree.")
            // Qt.quit()
        }
        // Component.onCompleted: visible = true
    }

}


