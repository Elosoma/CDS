from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem, QHBoxLayout, QLineEdit
)

from model import DatabaseManager


class CampaignList(QWidget):
    def __init__(self, db:DatabaseManager, parent):
        super().__init__()
        self.db = db
        self.parent_tab = parent

        layout = QVBoxLayout()
        layouth = QHBoxLayout()
        widget = QWidget()

        # Buscador
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("🔎 Buscar nombre...")
        layouth.addWidget(self.buscador)

        # Nueva campaña
        self.new_btn = QPushButton("➕ New campaign")
        self.new_btn.clicked.connect(lambda: self.parent_tab.show_form())
        self.new_btn.setMinimumSize(225, 30)
        self.new_btn.setMaximumSize(250, 40)
        layouth.addWidget(self.new_btn)

        widget.setLayout(layouth)
        layout.addWidget(widget)

        # Lista de campañas
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.open_campaign)
        layout.addWidget(self.list)

        self.buscador.textChanged.connect(self.search_bar)
        self.setLayout(layout)

    def __get_list(self):
        return self.db.get_user_campaigns(self.parent_tab.user)

    def search_bar(self, texto):
        texto = texto.lower()
        filtrados = [
            nombre for nombre in self.__get_list()
            if texto in nombre.name.lower()
        ]
        self.refresh(filtrados)

    def refresh(self, campaigns=0):
        '''Limpia la lista y la refresca con datos actualizados.'''
        self.list.clear()
        if campaigns == 0: campaigns = self.__get_list()

        for c in campaigns:
            item = QListWidgetItem(c.name)
            item.setData(Qt.ItemDataRole.UserRole, c.object_id)
            self.list.addItem(item)

    def open_campaign(self, item):
        campaign_id = item.data(Qt.ItemDataRole.UserRole)
        self.parent_tab.show_detail(campaign_id)
