from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget
)

from view.campaigns_view.campaigns_list import CampaignList
from view.campaigns_view.campaigns_detail import CampaignDetail
from view.campaigns_view.campaigns_form import CampaignForm


class CampaignWidget(QWidget):
    def __init__(self, db, current_user=1):
        super().__init__()
        self.db = db
        self.user = current_user

        self.stack = QStackedWidget()

        self.list_view = CampaignList(db, self)
        self.detail_view = CampaignDetail(db, self)
        self.form_view = CampaignForm(db, self)

        self.stack.addWidget(self.list_view)
        self.stack.addWidget(self.detail_view)
        self.stack.addWidget(self.form_view)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.show_list()

    def show_list(self):
        self.list_view.refresh()
        self.stack.setCurrentWidget(self.list_view)

    def show_detail(self, campaign_id):
        self.detail_view.load_campaign(campaign_id)
        self.stack.setCurrentWidget(self.detail_view)

    def show_form(self, campaign_id=None):
        self.form_view.load_campaign(campaign_id)
        self.stack.setCurrentWidget(self.form_view)
