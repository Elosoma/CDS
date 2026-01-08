from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QTextEdit, 
    QPushButton, QFormLayout, QMessageBox
)

from model import DatabaseManager, Campaigns


class CampaignForm(QWidget):
    def __init__(self, db:DatabaseManager, parent):
        super().__init__()
        self.db = db
        self.parent_tab = parent
        self.campaign_id = None

        self.name = QLineEdit()
        self.desc = QTextEdit()

        self.save_btn = QPushButton("💾 Guardar")
        self.cancel_btn = QPushButton("Cancelar")

        self.save_btn.clicked.connect(self.save)
        self.cancel_btn.clicked.connect(self.parent_tab.show_list)

        layout = QFormLayout()
        layout.addRow("Nombre:", self.name)
        layout.addRow("Descripción:", self.desc)
        layout.addRow(self.save_btn, self.cancel_btn)

        self.setLayout(layout)

    def load_campaign(self, campaign_id=None):
        self.campaign_id = campaign_id
        if campaign_id:
            c = self.db.get_campaign(campaign_id)[0]
            self.name.setText(c.name)
            self.desc.setPlainText(c.description or "")
            return

        self.name.clear()
        self.desc.clear()
        
    def save(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío")
            return

        if self.campaign_id is None:
            self.db.add_campaign(
                Campaigns(
                    user_id=self.parent_tab.user,
                    name=self.name.text(),
                    description=self.desc.toPlainText()
                )
            )
        else:
            self.db.update_campaigns(
                Campaigns(
                    name=self.name.text(),
                    description=self.desc.toPlainText(),
                    user_id=self.parent_tab.user,
                    object_id=self.campaign_id
                )
            )

        self.parent_tab.show_list()
