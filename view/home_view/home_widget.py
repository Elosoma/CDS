from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea
)


class HomeWidget(QScrollArea):
    '''Pestaña de inicio, incluye un label con el nombre de la app y una imagen con su logo.'''
    def __init__(self):
        super().__init__()
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel()
        pixmap = QPixmap('utils/log.png')
        pixmap = pixmap.scaled(580, 580, Qt.AspectRatioMode.KeepAspectRatio)

        result_pixmap = QPixmap(pixmap.size())
        result_pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(result_pixmap)
        painter.setOpacity(0.75)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        label.setPixmap(result_pixmap)
        layout.addWidget(label)
        
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layout)
        self.setWidget(widget)
