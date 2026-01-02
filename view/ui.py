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


class GestorRol(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CDS")
        self.setMinimumSize(900, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(self.tab_inicio(), "Inicio")
        self.tabs.addTab(self.tab_personaje(), "Personajes")
        self.tabs.addTab(self.tab_campaña(), "Campañas")
        self.tabs.addTab(self.tab_lista(), "Contenido")
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
    

    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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



    def tab_formulario(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # ---------- DATOS GENERALES ----------
        datos = QGroupBox("Datos Generales")
        form = QFormLayout()

        nombre = QLineEdit()
        nombre.setPlaceholderText("Nombre del personaje / campaña")

        descripcion = QTextEdit()
        descripcion.setPlaceholderText("Descripción larga...")

        nivel = QSpinBox()
        nivel.setRange(1, 20)

        oro = QDoubleSpinBox()
        oro.setRange(0, 9999)
        oro.setDecimals(2)

        activo = QCheckBox("Activo / Disponible")

        clase = QComboBox()
        clase.addItems(["Guerrero", "Mago", "Pícaro", "Clérigo"])

        fecha_creacion = QDateEdit()
        fecha_creacion.setDate(QDate.currentDate())
        fecha_creacion.setCalendarPopup(True)

        form.addRow("Nombre:", nombre)
        form.addRow("Descripción:", descripcion)
        form.addRow("Nivel:", nivel)
        form.addRow("Oro:", oro)
        form.addRow("Clase:", clase)
        form.addRow("Fecha creación:", fecha_creacion)
        form.addRow("", activo)

        datos.setLayout(form)

        # ---------- OPCIONES ----------
        opciones = QGroupBox("Opciones")
        opciones_layout = QVBoxLayout()

        rb1 = QRadioButton("Jugador")
        rb2 = QRadioButton("PNJ")
        rb1.setChecked(True)

        opciones_layout.addWidget(rb1)
        opciones_layout.addWidget(rb2)

        opciones.setLayout(opciones_layout)

        # ---------- VALORES ----------
        valores = QGroupBox("Valores")
        valores_layout = QFormLayout()

        dificultad = QSlider(Qt.Orientation.Horizontal)
        dificultad.setRange(1, 10)

        progreso = QProgressBar()
        progreso.setValue(60)

        # Sincronizar slider con barra
        dificultad.valueChanged.connect(progreso.setValue)

        valores_layout.addRow("Dificultad:", dificultad)
        valores_layout.addRow("Progreso:", progreso)

        valores.setLayout(valores_layout)

        # ---------- BOTONES ----------
        botones = QHBoxLayout()
        btn_guardar = QPushButton("Guardar")
        btn_cancelar = QPushButton("Cancelar")

        botones.addStretch()
        botones.addWidget(btn_guardar)
        botones.addWidget(btn_cancelar)

        # ---------- ENSAMBLAJE ----------
        layout.addWidget(datos)
        layout.addWidget(opciones)
        layout.addWidget(valores)
        layout.addLayout(botones)

        tab.setLayout(layout)
        return tab

    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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
    
    # ------------------ TAB 4: CAMPAÑA ------------------

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestorRol()
    window.show()
    sys.exit(app.exec())
