from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QLabel, QTextEdit, QSpinBox,
    QPushButton, QListWidget, QMessageBox, 
    QVBoxLayout, QListWidgetItem, QInputDialog, 
    QFormLayout, QHBoxLayout
)

from model import DatabaseManager


class CampaignDetail(QWidget):
    def __init__(self, db:DatabaseManager, parent):
        super().__init__()
        self.db = db
        self.parent_tab = parent
        self.campaign_id = None
        self.selected_character_id = None

        # Arriba, titulo y desc
        layout = QVBoxLayout()
        self.title = QLabel()
        self.desc = QTextEdit()
        self.desc.setReadOnly(True)
        layout.addWidget(self.title)
        layout.addWidget(self.desc)
        layout.addWidget(QLabel("Campaign Characters:"))
        layout.addStretch()

        # Lista y detalles, medio
        widget = QWidget()
        layouth = QHBoxLayout()

        self.char_list = QListWidget()
        self.char_list.itemClicked.connect(self.load_character_data)
        layouth.addWidget(self.char_list)
        layouth.addStretch()

        self.hp = QSpinBox()
        self.hp.setRange(0, 99999)
        self.notes = QTextEdit()

        self.save_btn = QPushButton("💾 Save info")
        self.remove_btn = QPushButton("❌ Delete from campaign")
        self.save_btn.clicked.connect(self.save_character_data)
        self.remove_btn.clicked.connect(self.remove_character)

        editform = QFormLayout()
        editform.addRow("Actual HP:", self.hp)
        editform.addRow("Notes:", self.notes)
        editform.addRow(self.save_btn)
        editform.addRow(self.remove_btn)
        layouth.addLayout(editform)

        widget.setLayout(layouth)
        layout.addWidget(widget)

        # Abajo, botones guardar salir etc
        self.add_btn = QPushButton("➕ Add character")
        self.edit_btn = QPushButton("✏️ Edit campaign")
        self.del_btn = QPushButton("🗑️ Delete Campaign")
        self.back_btn = QPushButton("⬅️ Back")

        self.add_btn.clicked.connect(self.add_character)
        self.edit_btn.clicked.connect(lambda: self.parent_tab.show_form(self.campaign_id))
        self.del_btn.clicked.connect(self.delete_campaign)
        self.back_btn.clicked.connect(self.parent_tab.show_list)

        layout.addWidget(self.add_btn)
        layout.addWidget(self.edit_btn)
        layout.addWidget(self.del_btn)
        layout.addWidget(self.back_btn)
        
        self.setLayout(layout)

    def load_character_data(self, item):
        '''Carga la información del personaje seleccionado'''
        data = item.data(Qt.ItemDataRole.UserRole)
        self.selected_character_id = data

        char = self.db.get_campaign_character(
            self.campaign_id, data
        )

        self.hp.setValue(char.health_points)
        self.notes.setPlainText(char.notes or "")

    def save_character_data(self):
        '''Almacena los cambios en la información del personaje seleccionado'''
        if self.selected_character_id is None:
            return

        self.db.update_campaign_character(
            self.campaign_id,
            self.selected_character_id,
            self.hp.value(),
            self.notes.toPlainText()
        )

    def remove_character(self):
        '''Elimina el personaje selecionado de la campaña'''
        if self.selected_character_id is None:
            return

        reply = QMessageBox.question(
            self,
            "Delete character",
            "Are you sure you want to delete this character from the campaign?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_campaign_character(
                self.campaign_id,
                self.selected_character_id
            )
            self.refresh_characters()

    def refresh_characters(self):
        '''Refresca la lista de personajes'''
        self.char_list.clear()
        chars = self.db.get_campaign_characters(self.campaign_id)

        for ch in chars:
            char = self.db.get_character(ch.character_id)
            item = QListWidgetItem(f"{char.name}")
            item.setData(Qt.ItemDataRole.UserRole, ch.character_id)
            self.char_list.addItem(item)

    def load_campaign(self, campaign_id):
        '''Carga la campaña y refresca la lista de personajes'''
        self.campaign_id = campaign_id
        campaign = self.db.get_campaign(campaign_id)[0]

        self.title.setText(campaign.name)
        self.desc.setPlainText(campaign.description or "")

        self.refresh_characters()

    def add_character(self):
        '''Desplega una pestaña para añadir personajes nuevos'''
        characters = self.db.get_user_characters(self.parent_tab.user)

        names = [c.name for c in characters]
        name, ok = QInputDialog.getItem(
            self, "Add character", "Character:", names, 0, False
        )

        if ok:
            c = next(c for c in characters if c.name == name)
            self.db.add_campaign_character(
                self.campaign_id, c.object_id, c.hit_points, ""
            )
            self.refresh_characters()

    def delete_campaign(self):
        '''Borra la camapaña actual'''
        reply = QMessageBox.question(
            self,
            "Delete campaign",
            "Are you sure you want to delete this campaign?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_campaign(self.campaign_id)
            self.parent_tab.show_list()
