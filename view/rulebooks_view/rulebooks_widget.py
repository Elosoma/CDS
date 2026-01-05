from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QScrollArea, QTextEdit
)

from model.user_db import DatabaseManager


class RulebooksWidget(QWidget):
    '''Muestra contenido en bruto de la base de datos local de los libros de reglas'''
    def __init__(self, db:DatabaseManager):
        super().__init__()
        self.db = db
        layout = QVBoxLayout()

        titulo = QLabel("Rulebooks secctions")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(titulo)

        # Bloque de contenido, botones y detalles.
        widget = QWidget()
        hlayout = QHBoxLayout()

        btn_scroll = QScrollArea()
        btn_list = QVBoxLayout()
        btn_widget = QWidget()
        rulebooks = {
            "Ability Scores": ("ability_scores"), 
            "Alignments": ("alignments"), 
            "Backgrounds": ("backgrounds"), 
            "Conditions": ("conditions"),
            "Damage Types": ("damage_types"),
            "Equipment": ("equipment"),
            "Equipment_categories": ("equipment_categories"),
            "Feats": ("feats"),
            "Features": ("features"),
            "Languages": ("languages"),
            "Magic Items": ("magic_items"),
            "Magic Schools": ("magic_schools"),
            "Proficiencies": ("proficiencies"),
            "Races": ("races"),
            "Rule Sections": ("rule_sections"),
            "Rules": ("rules"),
            "Skills": ("skills"),
            "Spells": ("spells"),
            "Subclasses": ("subclasses"),
            "Subraces": ("subraces"),
            "Traits": ("traits"),
            "Weapon Properties": ("weapon_properties"),
        }

        self.detail = QTextEdit()
        for name, (index) in rulebooks.items():
            boton = QPushButton(name)
            boton.clicked.connect(lambda: self.change_detail(index))
            btn_list.addWidget(boton)
        btn_widget.setLayout(btn_list)
        btn_scroll.setWidget(btn_widget)
        hlayout.addWidget(btn_scroll, 1)

        hlayout.addWidget(self.detail, 2)
        widget.setLayout(hlayout)
        layout.addWidget(widget)
        self.setLayout(layout)

    def change_detail(self, index: str):
        rulebooks = self.db.get_all_rulebooks()
        if rulebooks is []:
            self.detail.clear()
            return

        lines = []

        for rulebook in rulebooks:
            value = getattr(rulebook, index, None)
            if value:
                lines.append(str(value))

        self.detail.setPlainText("\n\n".join(lines))
