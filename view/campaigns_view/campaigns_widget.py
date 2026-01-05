from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea
)


class CampaignsWidget(QScrollArea):
    '''Pestaña de inicio, incluye un label con el nombre de la app y una imagen con su logo.'''
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QVBoxLayout()

        titulo = QLabel("Character Dungeon Stats")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 40px; font-weight: bold;")
        layout.addWidget(titulo)

        label = QLabel()
        pixmap = QPixmap('utils/log.png')
        pixmap = pixmap.scaled(750, 750, Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
        layout.addWidget(label)
        
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layout)
        self.setWidget(widget)
