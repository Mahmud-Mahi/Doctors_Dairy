from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QButtonGroup, QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QScrollArea
from PySide6.QtCore import QRect
from PySide6.QtGui import QShortcut, QKeySequence, QIcon, QAction
from main_gui import Ui_MainWindow
from PySide6 import QtCore, QtWidgets
import os, json
from config_manager import load_config, update_config

class edit_window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Labels")
        self.resize(700, 600)
        self.inputs = {}

       # Main layout for the dialog
        main_layout = QVBoxLayout(self)

        # Scroll area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Container widget inside scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        # Find labels from parent and create editable fields
        for label in parent.findChildren(QLabel):
            name = label.objectName()
            if name and name != "":
                row = QHBoxLayout()
                row.addWidget(QLabel(f"{name}:"))
                input_field = QLineEdit(label.text())
                self.inputs[name] = input_field
                row.addWidget(input_field)
                scroll_layout.addLayout(row)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)

        main_layout.addWidget(scroll_area)

        # Save/Cancel buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addStretch()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)

        main_layout.addLayout(button_layout)

    def get_updated_labels(self):
        return {name: edit.text() for name, edit in self.inputs.items()}
    
    def accept(self):
        updated_labels = self.get_updated_labels()
        try:
            update_config("labels", updated_labels)  # Save the config
        except Exception as e:
            print(f"Error saving labels: {e}")
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to save label changes.")
        
        # Apply the changes in the parent window
        parent = self.parent()
        if parent:
            for name, new_text in updated_labels.items():
                label = parent.findChild(QLabel, name)
                if label:
                    label.setText(new_text)
        super().accept()
