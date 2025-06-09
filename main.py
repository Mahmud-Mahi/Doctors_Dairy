from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QButtonGroup
from PySide6.QtGui import QShortcut, QKeySequence, QIcon
from app import Ui_MainWindow
import os
from PySide6 import QtCore, QtWidgets
from datetime import datetime
import json
from about_us import AboutDialog  # Assuming you have an about_us.py file with the AboutDialog class

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Doctor's Diary")
        self.setWindowIcon(QIcon("Doctors_dairy/report.png"))
        self.setBaseSize(1200, 800)
        self.setMinimumSize(1150, 600)
        self.show()
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.actionSave.triggered.connect(self.save_file)
        save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        save_shortcut.activated.connect(self.save_file)
        self.actionNew.triggered.connect(self.new_form)
        new_shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        new_shortcut.activated.connect(self.new_form)
        patient_ID = " " + self.patient_id()
        self.id_lineEdit.setText(patient_ID)
        self.actionOpen.triggered.connect(self.open_file)
        open_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        open_shortcut.activated.connect(self.open_file)
        self.actionClose.triggered.connect(self.close_form)
        close_shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        close_shortcut.activated.connect(self.close_form)
        self.actionQuit.triggered.connect(self.quit)
        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(self.quit)
        self.actionAbout_Us.triggered.connect(self.show_about_dialog)
        self.setStyleSheet("""
            QLineEdit:focus, QTextEdit:focus, QRadioButton:focus, QCheckBox:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {
                border: 2px solid #0078D7;  /* Blue border */
                border-radius: 4px;
            }
        """)
        self.avarice_buttonGroup = QButtonGroup(self)
        self.avarice_buttonGroup.addButton(self.yes_radioButton)
        self.avarice_buttonGroup.addButton(self.no_radioButton)

        self.religious_btngroup = QButtonGroup(self)
        self.religious_btngroup.addButton(self.yes2_radioButton)
        self.religious_btngroup.addButton(self.no2_radioButton)

        self.gender_buttonGroup = QButtonGroup(self)
        self.gender_buttonGroup.addButton(self.male_radiobtn)
        self.gender_buttonGroup.addButton(self.female_radiobtn)

    def quit(self):
        self.close()

    def patient_id(self):
        today = datetime.now()
        prefix = today.strftime("%d%m") # e.g. 2505
        
        #count existing files for today
        directory = "records"
        if not os.path.exists(directory):
            os.makedirs(directory)

        count = sum(1 for filename in os.listdir("records") if filename.startswith(prefix)) + 1
        
        # create patient ID
        return f"{prefix}{count:03d}"

    def save_file(self):
        file_name = self.id_lineEdit.text().strip()
        data ={}

        # Example for LineEdits
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
           data[line_edit.objectName()] = line_edit.text().strip()
        
        # Example for TextEdits
        for text_edit in self.findChildren(QtWidgets.QTextEdit):
            data[text_edit.objectName()] = text_edit.toPlainText().strip()
        
        # Example for ComboBoxes
        for combo_box in self.findChildren(QtWidgets.QComboBox):
            data[combo_box.objectName()] = combo_box.currentText().strip()
        
        # Example for SpinBoxes
        for spin_box in self.findChildren(QtWidgets.QSpinBox):
            data[spin_box.objectName()] = str(spin_box.value()).strip()
        
        # Example for DateEdits
        for date_edit in self.findChildren(QtWidgets.QDateEdit):
            data[date_edit.objectName()] = date_edit.date().toString(QtCore.Qt.ISODate)
        
        # Example for RadioButtons
        for radio_button in self.findChildren(QtWidgets.QRadioButton):
            data[radio_button.objectName()] = radio_button.isChecked()
        
        # Example for CheckBoxes
        for check_box in self.findChildren(QtWidgets.QCheckBox):
            data[check_box.objectName()] = check_box.isChecked()
            
        with open(f"records/{file_name}.json", "w") as file:
            json.dump(data, file, indent=4)
        self.statusbar.showMessage("Form saved successfully.", 3000)
        
    def load_file(self, file_path):
        if not os.path.exists(file_path):
            self.statusbar.showMessage("File not found.", 3000)
            return
        
        with open(file_path, "r") as file:
            data = json.load(file)
        
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            if line_edit.objectName() in data:
                line_edit.setText(data[line_edit.objectName()])
        
        for text_edit in self.findChildren(QtWidgets.QTextEdit):
            if text_edit.objectName() in data:
                text_edit.setPlainText(data[text_edit.objectName()])
        
        for combo_box in self.findChildren(QtWidgets.QComboBox):
            if combo_box.objectName() in data:
                index = combo_box.findText(data[combo_box.objectName()])
                if index != -1:
                    combo_box.setCurrentIndex(index)
        
        for spin_box in self.findChildren(QtWidgets.QSpinBox):
            if spin_box.objectName() in data:
                spin_box.setValue(int(data[spin_box.objectName()]))
        
        for date_edit in self.findChildren(QtWidgets.QDateEdit):
            if date_edit.objectName() in data:
                date_edit.setDate(QtCore.QDate.fromString(data[date_edit.objectName()], QtCore.Qt.ISODate))
        
        for radio_button in self.findChildren(QtWidgets.QRadioButton):
            if radio_button.objectName() in data:
                radio_button.setChecked(data[radio_button.objectName()])
        
        for check_box in self.findChildren(QtWidgets.QCheckBox):
            if check_box.objectName() in data:
                check_box.setChecked(data[check_box.objectName()])
        
        self.statusbar.showMessage("Form loaded successfully.", 3000)
    
    def open_file(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        file_dialog.setDirectory("records")
        file_dialog.setWindowTitle("Record Files")
        file_dialog.setNameFilter("JSON files (*.json)")
        file_dialog.setViewMode(QtWidgets.QFileDialog.List)
        
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                self.load_file(file_path)

    def clear_form(self):
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QtWidgets.QLineEdit):
                widget.clear()
            elif isinstance(widget, QtWidgets.QTextEdit):
                widget.clear()
            elif isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentIndex(0)
            elif isinstance(widget, QtWidgets.QSpinBox):
                widget.setValue(0)
            elif isinstance(widget, QtWidgets.QDateEdit):
                widget.setDate(QtCore.QDate.currentDate())
            elif isinstance(widget, QtWidgets.QRadioButton):
                widget.setChecked(False)
            elif isinstance(widget, QtWidgets.QCheckBox):
                widget.setChecked(False)
    
    def is_form_filled(self):
        for line_edit in self.findChildren(QtWidgets.QLineEdit):
            if isinstance(line_edit.parent(), QtWidgets.QAbstractSpinBox):
                continue
            elif line_edit.objectName() == "observation_lineEdit":
                continue
            elif line_edit.objectName() == "id_lineEdit":
                continue
            elif line_edit.text().strip():
                #print(f"Filled LineEdit: {line_edit.objectName()} → {line_edit.text()}")
                return True
        return False

    def new_form(self):
        if self.is_form_filled():
            message = QtWidgets.QMessageBox.warning(self, "New Form", "Do you want to save the current form before creating a new one?", QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
            #message.setDefaultButton(QtWidgets.QMessageBox.Save)

            # Show the message box
            
            if message == QtWidgets.QMessageBox.Save:
                self.save_file()
                self.clear_form()
                self.id_lineEdit.setText(self.patient_id())
            elif message == QtWidgets.QMessageBox.Discard:
                self.clear_form()
                self.id_lineEdit.setText(self.patient_id())
            else:
                pass
    def close_form(self):
        check_file = "records/" + self.id_lineEdit.text().strip() + ".json"
        if not os.path.exists(check_file):
            if self.is_form_filled():
                message = QtWidgets.QMessageBox.warning(self, "Close Form", "Do you want to save the current form before closing?", QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
                if message == QtWidgets.QMessageBox.Save:
                    self.save_file()
                    self.statusbar.showMessage("Form saved successfully.", 3000)
                    self.clear_form()
                    self.id_lineEdit.setText(self.patient_id())
                    
                elif message == QtWidgets.QMessageBox.Discard:
                    self.clear_form()
                    self.id_lineEdit.setText(self.patient_id())
                    
                else:
                    pass
            else:
                self.open_file()
        else:
            self.clear_form()
            self.id_lineEdit.setText(self.patient_id())
            self.statusbar.showMessage("Form closed.", 3000)

    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = UserInterface()
    app.exec()

