from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QButtonGroup
from PySide6.QtGui import QShortcut, QKeySequence, QIcon, QAction
from main_gui import Ui_MainWindow
import os
from PySide6 import QtCore, QtWidgets
from datetime import datetime
import json
from about_us import AboutDialog 
from EditWindow import edit_window 
from config_manager import update_config, load_config, DEFAULT_CONFIG

class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Doctor's Diary")
        self.setMinimumSize(950, 300)
        self.show()
        self.load_custom_labels()
        self.dateEdit.setDisplayFormat("dd MMMM yyyy")
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        self.actionSave.triggered.connect(self.save_file)
        self.actionSave.setShortcut(QKeySequence("Ctrl+S"))

        self.actionNew.triggered.connect(self.new_form)
        self.actionNew.setShortcut(QKeySequence("Ctrl+N"))

        patient_ID = " " + self.patient_id()
        self.id_lineEdit.setText(patient_ID)

        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpen.setShortcut(QKeySequence("Ctrl+O"))

        self.actionClose.triggered.connect(self.close_form)
        self.actionClose.setShortcut(QKeySequence("Ctrl+W"))
        self.actionQuit.triggered.connect(self.quit)

        self.actionQuit.setShortcut(QKeySequence("Ctrl+Q"))
        
        self.actionCut.triggered.connect(self.cut_text)
        self.actionCut.setShortcut(QKeySequence("Ctrl+X"))
        
        self.actionCopy.triggered.connect(self.copy_text)
        self.actionCopy.setShortcut(QKeySequence("Ctrl+C"))
        
        self.actionPaste.triggered.connect(self.paste_text)
        self.actionPaste.setShortcut(QKeySequence("Ctrl+V"))

        self.actionUndo.triggered.connect(self.undo_action)
        self.actionUndo.setShortcut(QKeySequence("Ctrl+Z"))

        self.actionRedo.triggered.connect(self.redo_action)
        self.actionRedo.setShortcut(QKeySequence("Ctrl+Y"))

        theme = load_config().get("theme", "system")
        self.get_theme(theme)
        self.actionDark_Mode.triggered.connect(lambda: self.apply_theme("dark"))
        self.actionLight_Mode.triggered.connect(lambda: self.apply_theme("light"))
        self.actionSystem.triggered.connect(lambda: self.apply_theme("system"))

        self.actionReset_to_Defaults.triggered.connect(self.reset_to_defaults)

        self.actionAbout_Us.triggered.connect(self.show_about_dialog)
        self.actionAbout_Us.setShortcut(QKeySequence("F2"))

        self.actionEdit_Form.triggered.connect(self.edit_form)

        # Button Groups for Radio Buttons
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

        if self.is_form_filled():
            if not os.path.exists("records"):
                os.makedirs("records")

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
        else:
            self.statusbar.showMessage("Form is empty. Please fill in the required fields.", 3000)
        
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
                if isinstance(widget.parent(), QtWidgets.QDateEdit):
                    continue
                elif widget.objectName() == "id_lineEdit":
                    widget.setText(self.patient_id())
                    continue
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
            if line_edit.objectName() == "observation_lineEdit":
                continue
            elif line_edit.objectName() == "id_lineEdit":
                continue
            elif line_edit.text().strip():
                #print(f"Filled LineEdit: {line_edit.objectName()} → {line_edit.text()}")
                return True
        return False
    
    def is_form_saved(self):
        file_name = self.id_lineEdit.text().strip()
        file_path = f"records/{file_name}.json"
        return os.path.exists(file_path)

    def new_form(self):
        if self.is_form_filled() and not self.is_form_saved():
            message = QtWidgets.QMessageBox.warning(self, "New Form", "Do you want to save the current form before creating a new one?", QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
            #message.setDefaultButton(QtWidgets.QMessageBox.Save)

            # Show the message box
            if message == QtWidgets.QMessageBox.Save:
                self.save_file()
                self.clear_form()
                
            elif message == QtWidgets.QMessageBox.Discard:
                self.clear_form()
            else:
                self.statusbar.showMessage("Form is already empty.", 3000)
                return
        else:
            self.clear_form()
        
    def close_form(self):
        check_file = "records/" + self.id_lineEdit.text().strip() + ".json"
        if not os.path.exists(check_file):
            if self.is_form_filled():
                message = QtWidgets.QMessageBox.warning(self, "Close Form", "Do you want to save the current form before closing?", QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
                if message == QtWidgets.QMessageBox.Save:
                    self.save_file()
                    self.statusbar.showMessage("Form saved successfully.", 3000)
                    self.clear_form()
                    
                elif message == QtWidgets.QMessageBox.Discard:
                    self.clear_form()
                    
                else:
                    pass
            else:
                self.new_form()
        else:
            self.clear_form()
            
            self.statusbar.showMessage("Form closed.", 3000)

    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def cut_text(self):
        widget = self.focusWidget()
        if isinstance(widget, QtWidgets.QLineEdit) or isinstance(widget, QtWidgets.QTextEdit):
            text = widget.text() if isinstance(widget, QtWidgets.QLineEdit) else widget.toPlainText()
            if text != "":
                QApplication.clipboard().setText(text)
                widget.clear()
                self.statusbar.showMessage("Text cut to clipboard.", 3000)
    
    def copy_text(self):
        widget = self.focusWidget()
        if isinstance(widget, QtWidgets.QLineEdit) or isinstance(widget, QtWidgets.QTextEdit):
            text = widget.text() if isinstance(widget, QtWidgets.QLineEdit) else widget.toPlainText()
            if text != "":
                QApplication.clipboard().setText(text)   
                self.statusbar.showMessage("Text copied to clipboard.", 3000)
    
    def paste_text(self):
        widget = self.focusWidget()
        clipboard_text = QApplication.clipboard().text()
        if isinstance(widget, QtWidgets.QLineEdit) or isinstance(widget, QtWidgets.QTextEdit):
            widget.setText(clipboard_text) if isinstance(widget, QtWidgets.QLineEdit) else widget.setPlainText(clipboard_text)
            self.statusbar.showMessage("Text pasted from clipboard.", 3000)
    
    def undo_action(self):
        widget = self.focusWidget()
        if isinstance(widget, QtWidgets.QLineEdit) or isinstance(widget, QtWidgets.QTextEdit):
            widget.undo()
    
    def redo_action(self):
        widget = self.focusWidget()
        if isinstance(widget, QtWidgets.QLineEdit) or isinstance(widget, QtWidgets.QTextEdit):
            widget.redo()
    
    def get_theme(self, mode):
        if mode == "dark":
            # Apply dark theme styles
            self.setStyleSheet("""
                 QWidget {
                    background-color: #121212;
                    color: #f0f0f0;
                 }
                QLineEdit, QTextEdit, QComboBox, QSpinBox, QDateEdit {
                    background-color: #1e1e1e;
                    color: #FFFFFF;
                    border: 1px solid #555555;
                }
                QRadioButton, QCheckBox {
                    color: #FFFFFF;
                    background-color: #1e1e1e;
                }
                QMenuBar, QMenu, QToolBar {
                    background-color: #303030;
                    border: 2px solid #555555;
                }
                QLineEdit:focus, QTextEdit:focus, QRadioButton:focus, QCheckBox:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {
                    border: 2px solid #0078D7;  /* Blue border */
                    border-radius: 4px;
                }
            """)
        elif mode == "light":
            # Apply light theme styles
            self.setStyleSheet("""
                QWidget {
                    background-color: #f5f5f5;
                    color: #000000;
                }
                QLineEdit, QTextEdit, QComboBox, QSpinBox, QDateEdit, QRadioButton, QCheckBox {
                    background-color: #E8E8E8;
                    color: #000000;
                    border: 1px solid #CCCCCC;
                }
                QMenuBar, QMenu, QToolBar {
                    background-color: #E0E0E0;
                    border: 2px solid #CCCCCC;
                }
                QLineEdit:focus, QTextEdit:focus, QRadioButton:focus, QCheckBox:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {
                    border: 2px solid #0078D7;  /* Blue border */
                    border-radius: 4px;
                }
            """)
        elif mode == "system":
            # Apply system default styles
            self.setStyleSheet("""
                QLineEdit:focus, QTextEdit:focus, QRadioButton:focus, QCheckBox:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {
                    border: 2px solid #0078D7;  /* Blue border */
                    border-radius: 4px;
                }
            """)  # Use the system default style
    
    def save_user_theme(self, mode):
        update_config("theme", mode)
        print(f"Theme '{mode}' saved to configuration.")
    
    def apply_theme(self, mode):
        self.get_theme(mode)
        self.save_user_theme(mode)
        
    def edit_form(self):
        editor = edit_window(self)
        editor.exec()
    
    def load_custom_labels(self):
        config = load_config()
        custom_labels = config.get("labels", {})
        for label in self.findChildren(QtWidgets.QLabel):
            if label.objectName() in custom_labels:
                label.setText(custom_labels[label.objectName()])
            else:
                label.setText(label.text())
    
    def reset_to_defaults(self):
        # Save the default configuration
        update_config("labels", DEFAULT_CONFIG["labels"])
        self.load_custom_labels()

        #Apply the default theme
        self.apply_theme("system")
        self.statusbar.showMessage("Configuration reset to defaults.", 3000)




if __name__ == "__main__":
    app = QApplication([])
    window = UserInterface()
    app.exec()

