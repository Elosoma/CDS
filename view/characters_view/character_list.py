'''Pestaña, lista de personajes del usuario.'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,QListWidget, 
    QPushButton, QListWidgetItem
)

from model import DatabaseManager


class CharacterList(QWidget):
    '''Muestra la lista de personajes de un usuario y permite crear nuevos u acceder a la pestaña con sus datos.'''
    def __init__(self, db:DatabaseManager, parent):
        '''Crea la lista y el botón de creación de personaje.'''
        super().__init__()
        self.db = db
        self.parent_tab = parent

        self.list = QListWidget()
        self.new_btn = QPushButton("➕ New character")

        self.list.itemDoubleClicked.connect(self.open_character)
        self.new_btn.clicked.connect(self.new_character)

        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.new_btn)
        self.setLayout(layout)

    def filtrar_nombres(self, texto):
        texto = texto.lower()
        filtrados = [
            nombre for nombre in self.nombres
            if texto in nombre.lower()
        ]
        self.actualizar_label(filtrados)

    def refresh(self):
        '''Limpia la lista y la refresca con datos actualizados.'''
        self.list.clear()
        characters = self.db.get_user_characters(self.parent_tab.user)

        for c in characters:
            item = QListWidgetItem(
                f"{c.name} (Nivel {c.level} {c.class_index})"
            )
            item.setData(Qt.ItemDataRole.UserRole, c.object_id)
            self.list.addItem(item)

    def open_character(self, item:QListWidgetItem):
        '''Abre la pestaña con los detalles del personaje seleccionado.'''
        character_id = item.data(Qt.ItemDataRole.UserRole)
        self.parent_tab.show_detail(character_id)

    def new_character(self):
        '''Llama al metodo que cambia la pestaña al formulario de creación.'''
        self.parent_tab.show_form()



import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit
)

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Búsqueda de nombres")
        self.resize(300, 400)

        # Lista original de nombres
        self.nombres = [
            "Ana", "Andrés", "Beatriz", "Carlos",
            "Carmen", "Daniel", "David", "Elena",
            "Fernando", "Lucía", "María", "Pablo"
        ]

        # Widgets
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Buscar nombre...")

        self.label = QLabel()
        self.label.setWordWrap(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.buscador)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Mostrar lista inicial
        self.actualizar_label(self.nombres)

        # Conectar señal
        self.buscador.textChanged.connect(self.filtrar_nombres)

    def actualizar_label(self, lista):
        texto = "\n".join(lista)
        self.label.setText(texto)

    def filtrar_nombres(self, texto):
        texto = texto.lower()
        filtrados = [
            nombre for nombre in self.nombres
            if texto in nombre.lower()
        ]
        self.actualizar_label(filtrados)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())