# Message on change fetches data from a website, and notifies the user when the data has changed.
# Copyright (C) 2024  Rūdolfs Driķis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys
import threading

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QStackedWidget, QWidget
from message_on_change.gui import Ui_MainWindow as Ui_File1
from message_on_change.status import Ui_InfoWindow as Ui_File2
import message_on_change.fetch_logic
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.stacked_widget = QStackedWidget(self)

        # Create instances of the compiled UI classes
        self.ui_file1 = Ui_File1()
        self.ui_file2 = Ui_File2()

        # Set up UI from file1
        self.ui_file1.setupUi(self)
        self.stacked_widget.addWidget(self.ui_file1.centralwidget)

        # Hide the custom delay input box and add the switch visibility function
        self.ui_file1.spinBox.hide()
        self.ui_file1.spinBox.setEnabled(True)
        self.ui_file1.checkBox_2.clicked.connect(self.toggle_widget_visibility)

        # Custom file input box toggle
        self.ui_file1.pushButton_2.hide()
        self.ui_file1.lineEdit_2.hide()
        self.ui_file1.checkBox.clicked.connect(self.toggle_file_select_visibility)

        # file select logic
        self.ui_file1.pushButton_2.clicked.connect(self.openFile)

        # call the main function
        self.ui_file1.pushButton.clicked.connect(self.startProcess)

        # Set up UI from file2
        self.ui_file2.setupUi(self)
        self.stacked_widget.addWidget(self.ui_file2.centralwidget)

        self.current_index = 0

        # self.switch_button = QPushButton('Switch Layout', self)
        # self.switch_button.clicked.connect(self.switch_layout)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        # self.layout.addWidget(self.switch_button)
        self.layout.addWidget(self.stacked_widget)
        self.layout.addStretch(1)  # Add stretch to push the button to the top

        # Initially, show the first layout
        self.stacked_widget.setCurrentIndex(0)

    def switch_layout(self):
        self.current_index = (self.current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(self.current_index)

    def getOptions(self):
        # options to pass
        return {
            'url': self.ui_file1.lineEdit.text(),
            'customFile': self.ui_file1.checkBox.isChecked(),
            'customFilePath': self.ui_file1.lineEdit_2.text(),
            'separateFile': self.ui_file1.checkBox_3.isChecked(),
            'customDelay': self.ui_file1.checkBox_2.isChecked(),
            'customDelayValue': self.ui_file1.spinBox.value()
        }

    def toggle_widget_visibility(self):
        # Show or hide the widget based on the checkbox state
        if self.ui_file1.checkBox_2.isChecked():
            self.ui_file1.spinBox.show()
        else:
            self.ui_file1.spinBox.hide()

    def toggle_file_select_visibility(self):
        if self.ui_file1.checkBox.isChecked():
            self.ui_file1.pushButton_2.show()
            self.ui_file1.lineEdit_2.show()
        else:
            self.ui_file1.pushButton_2.hide()
            self.ui_file1.lineEdit_2.hide()

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Sound File", "", "(*.wav *.mp3);;All Files (*)",
                                                   options=options)

        self.ui_file1.lineEdit_2.setText(file_path)

    def startProcess(self, options):
        print('process started')
        options = self.getOptions()
        proc = threading.Thread(target=message_on_change.fetch_logic.main, kwargs={
            'url': options['url'],
            'delay': options['customDelayValue'],
            'change_sound': options['customFilePath']
        })

        try:
            proc.start()
            self.switch_layout()

        except:
            print('specify needed arguments')


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
