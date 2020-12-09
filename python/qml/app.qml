import QtQuick 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12

ApplicationWindow {
    title: qsTr("Print to console")
    visible: true
	minimumWidth: 400
	minimumHeight: 100
    flags: Qt.Dialog

	ColumnLayout {
		anchors.fill: parent
		spacing: 2
		TextField {
			Layout.fillWidth: true
			id: message
			placeholderText: "Some message"
            focus: true
		}
		Button {
			Layout.alignment: Qt.AlignHCenter
			text: "Print"
            onClicked: backend.create(message.text)
		}
	}
}
