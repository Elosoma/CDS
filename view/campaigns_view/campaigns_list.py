from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem
)
from model import DatabaseManager


class CampaignList(QWidget):
    def __init__(self, db:DatabaseManager, parent):
        super().__init__()
        self.db = db
        self.parent_tab = parent

        self.list = QListWidget()
        self.new_btn = QPushButton("➕ New campaign")

        self.list.itemDoubleClicked.connect(self.open_campaign)
        self.new_btn.clicked.connect(lambda: self.parent_tab.show_form())

        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.new_btn)
        self.setLayout(layout)

    def refresh(self):
        self.list.clear()
        campaigns = self.db.get_user_campaigns(self.parent_tab.user)

        for c in campaigns:
            item = QListWidgetItem(c.name)
            item.setData(Qt.ItemDataRole.UserRole, c.object_id)
            self.list.addItem(item)

    def open_campaign(self, item):
        campaign_id = item.data(Qt.ItemDataRole.UserRole)
        self.parent_tab.show_detail(campaign_id)
