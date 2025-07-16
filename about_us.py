from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QSizePolicy, QHBoxLayout, QWidget
from PySide6.QtGui import QMovie, QDesktopServices, QPainter, QPainterPath

from PySide6.QtCore import Qt, QUrl, QSize

class RoundedMovieLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.radius = 20  # Corner radius - adjust as needed
        
    def paintEvent(self, event):
        if self.movie() and self.movie().currentPixmap():
            # Create rounded clipping path
            path = QPainterPath()
            path.addRoundedRect(self.rect(), self.radius, self.radius)
            
            # Draw pixmap with rounded corners
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setClipPath(path)
            painter.drawPixmap(self.rect(), self.movie().currentPixmap())
            painter.end()
        else:
            super().paintEvent(event)

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Us")
        self.setFixedSize(650, 520)

        layout = QVBoxLayout()

        # App Logo
        logo = RoundedMovieLabel()
        movie = QMovie("Doctors_dairy/report.gif")  # Replace with your logo file path
        movie.setScaledSize(QSize(150, 150))
        logo.setMovie(movie)
        movie.start()
        logo.setFixedSize(150, 150)

        # Description Label
        name_label = QLabel("Doctor's Dairy")
        name_label.setStyleSheet("font-size: 25px; font-weight: bold;")
        desc_label = QLabel("A simple diary application for doctors to manage their patients' records.\nThe idea of Dr. Sheikh Rizwanur Rahman\nDeveloped by Mahmud Mahi.")
        others_label = QLabel("Version 1.0\n© 2025 All Rights Reserved.")
        desc_label.setStyleSheet("font-size: 18px;")
        others_label.setStyleSheet("font-size: 14px; color: gray;")
        others_label.setAlignment(Qt.AlignCenter)
        desc_label.setAlignment(Qt.AlignCenter)
        name_label.setAlignment(Qt.AlignCenter)

        # Contact Information
        contact_label = QLabel("For any inquiry or information, contact us")
        contact_label.setAlignment(Qt.AlignLeft)
        contact_label.setStyleSheet("font-size: 14px; color: gray; margin-left: 10px;")
        Dr_sheikh_label = QLabel()
        Dr_sheikh_label.setText("<i>Dr. Sheikh Rizwanur Rahman:</i> +8801328-976677 (call or WhatsApp)")
        Dr_sheikh_label.setAlignment(Qt.AlignLeft)
        Dr_sheikh_label.setStyleSheet("font-size: 17px; margin-left: 10px;")
        Dr_sheikh_label.setTextFormat(Qt.RichText)
        mahmud_label = QLabel()
        mahmud_label.setText("<i>Mahmud Mahi:</i> +8801308-518852 (call or WhatsApp)<br>"
            "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Email: <a href='mailto:mahmudurahmanmahi26@gmail.com'>mahmudurahmanmahi26@gmail.com</a>") 
        mahmud_label.setAlignment(Qt.AlignLeft)
        mahmud_label.setStyleSheet("font-size: 17px; margin-left: 10px;")
        mahmud_label.setTextFormat(Qt.RichText)
        mahmud_label.setOpenExternalLinks(True)

        github_link = QLabel()
        github_link.setText("To update or install the app " '<a href="https://github.com/Mahmud-Mahi/Doctors_Dairy">Visit My GitHub Repository</a>')
        github_link.setOpenExternalLinks(True)
        github_link.setAlignment(Qt.AlignLeft)
        github_link.setStyleSheet("font-size: 16px; margin-left: 10px; margin-top: 10px;")
        github_link.setTextFormat(Qt.RichText)


        logo_layout = QHBoxLayout()
        logo_layout.addStretch()
        logo_layout.addWidget(logo)
        logo_layout.addStretch()
        layout.addLayout(logo_layout)

        layout.addWidget(name_label)
        layout.addWidget(desc_label)
        layout.addWidget(others_label)
        layout.addStretch(1)
        layout.addWidget(contact_label)
        layout.addWidget(Dr_sheikh_label)
        layout.addWidget(mahmud_label)
        layout.addWidget(github_link)

        self.setLayout(layout)
