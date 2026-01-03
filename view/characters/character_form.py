from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QSpinBox

class CharacterForm(QWidget):
    def __init__(self, controller, parent):
        super().__init__()
        self.controller = controller
        self.parent_tab = parent
        self.character_id = None

        self.name = QLineEdit()
        self.race = QComboBox()
        self.clazz = QComboBox()
        self.level = QSpinBox()

        self.save_btn = QPushButton("💾 Guardar")
        self.cancel_btn = QPushButton("❌ Cancelar")

        self.save_btn.clicked.connect(self.save)
        self.cancel_btn.clicked.connect(self.parent_tab.show_list)

        layout = QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.race)
        layout.addWidget(self.clazz)
        layout.addWidget(self.level)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.cancel_btn)
        self.setLayout(layout)

    def load_character(self, character_id=None):
        self.character_id = character_id

        self.race.clear()
        self.clazz.clear()

        for r in self.controller.get_races():
            self.race.addItem(r["name"], r["index"])

        for c in self.controller.get_classes():
            self.clazz.addItem(c["name"], c["index"])

        if character_id:
            c = self.controller.get_character(character_id)
            self.name.setText(c.name)
            self.level.setValue(c.level)

    def save(self):
        data = {
            "name": self.name.text(),
            "race_index": self.race.currentData(),
            "class_index": self.clazz.currentData(),
            "level": self.level.value()
        }

        if self.character_id:
            self.controller.update_character(self.character_id, data)
        else:
            self.controller.create_character(data)

        self.parent_tab.show_list()
