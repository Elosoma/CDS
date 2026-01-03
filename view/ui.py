import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QGroupBox, QFormLayout, QSpinBox
)
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
        QWidget, QVBoxLayout, QFormLayout, QLineEdit, QTextEdit,
        QSpinBox, QDoubleSpinBox, QCheckBox, QRadioButton,
        QComboBox, QDateEdit, QSlider, QProgressBar,
        QPushButton, QGroupBox, QHBoxLayout
    )
from PyQt6.QtCore import Qt, QDate

from view.api_explorer.content_explorer import content_list


class GestorRol(QMainWindow):
    def __init__(self, api):
        super().__init__()
        self.setWindowTitle("CDS")
        self.setMinimumSize(900, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(self.tab_inicio(), "Inicio")
        self.tabs.addTab(self.tab_personaje(), "Personajes")
        self.tabs.addTab(self.tab_campaña(), "Campañas")
        self.tabs.addTab(content_list(api), "Contenido")
        self.tabs.addTab(self.tab_rulebooks(), "Libros de reglas")
        
        

    # ------------------ TAB 1: INICIO ------------------
    def tab_inicio(self):
        tab = QWidget()
        layout = QVBoxLayout()

        titulo = QLabel("Selección de Contenido")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")

        botones = QHBoxLayout()
        for texto in ["Razas", "Clases", "Personajes", "Campañas"]:
            botones.addWidget(QPushButton(texto))

        layout.addWidget(titulo)
        layout.addLayout(botones)
        layout.addStretch()

        tab.setLayout(layout)
        return tab
    
    def tab_rulebooks(self):
        tab = QWidget()
        layout = QVBoxLayout()

        titulo = QLabel("Selección de Contenido")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")

        botones = QVBoxLayout()

        btn_razas = QPushButton("Razas")
        btn_clases = QPushButton("Clases")
        btn_personajes = QPushButton("Personajes")
        btn_campañas = QPushButton("Campañas")

        # Conexiones
        btn_razas.clicked.connect(lambda: self.tabs.setCurrentIndex(0))
        btn_clases.clicked.connect(lambda: self.tabs.setCurrentIndex(1))
        btn_personajes.clicked.connect(lambda: self.tabs.setCurrentIndex(2))
        btn_campañas.clicked.connect(lambda: self.tabs.setCurrentIndex(3))

        for btn in [btn_razas, btn_clases, btn_personajes, btn_campañas]:
            botones.addWidget(btn)

        for texto in ["ability-scores", "alignments", "backgrounds", "conditions", "damage-types", "equipment", "equipment-categories", "feats", "features", "languages", "magic-items", "magic-schools", "proficiencies", "races", "rule-sections", "rules", "skills", "spells", "subclasses", "subraces", "traits", "weapon-properties"]:
            botones.addWidget(QPushButton(texto))

        
        layout.addWidget(titulo)
        layout.addLayout(botones)
        layout.addStretch()

        tab.setLayout(layout)
        return tab

    # ------------------ TAB 2: LISTA ------------------
    def tab_lista(self):
        tab = QWidget()
        layout = QHBoxLayout()

        lista = QListWidget()
        lista.addItems([
            "Guerrero", "Mago", "Pícaro", "Clérigo",
            "Bárbaro", "Paladín", "Explorador"
        ])

        detalle = QLabel(
            "Selecciona una clase para ver su descripción.\n\n"
            "Ejemplo:\n"
            "Guerrero: Combatiente especializado en armas y armaduras."
        )
        detalle.setWordWrap(True)

        layout.addWidget(lista, 1)
        layout.addWidget(detalle, 2)

        tab.setLayout(layout)
        return tab

    # ------------------ TAB 3: PERSONAJE ------------------
    def tab_personaje(self):
        tab = QWidget()
        layout = QVBoxLayout()

        info = QLabel("Elena la Vagabunda – Nivel 6 (Maga)")
        info.setStyleSheet("font-size: 16px; font-weight: bold;")

        stats = QGroupBox("Estadísticas")
        form = QFormLayout()

        for stat, value in [
            ("Fuerza", 10),
            ("Destreza", 18),
            ("Constitución", 14),
            ("Inteligencia", 12),
            ("Sabiduría", 11),
            ("Carisma", 14),
        ]:
            spin = QSpinBox()
            spin.setValue(value)
            spin.setMaximum(30)
            form.addRow(stat, spin)

        stats.setLayout(form)

        layout.addWidget(info)
        layout.addWidget(stats)
        layout.addStretch()

        tab.setLayout(layout)
        return tab

    # ------------------ TAB 4: CAMPAÑA ------------------
    def tab_campaña(self):
        tab = QWidget()
        layout = QHBoxLayout()

        personajes = QListWidget()
        personajes.addItems([
            "Aranil (Mago)",
            "Thorn (Guerrero)",
            "Elena (Pícara)",
            "Korgan (Clérigo)"
        ])

        recursos = QGroupBox("Recursos de la Campaña")
        form = QFormLayout()

        vida = QSpinBox()
        vida.setMaximum(999)
        vida.setValue(58)

        hechizos = QSpinBox()
        hechizos.setMaximum(99)
        hechizos.setValue(7)

        form.addRow("Vida del grupo", vida)
        form.addRow("Hechizos disponibles", hechizos)

        recursos.setLayout(form)

        layout.addWidget(personajes, 1)
        layout.addWidget(recursos, 1)

        tab.setLayout(layout)
        return tab
    