from PyQt6.QtWidgets import QMainWindow, QTabWidget

from model.api_2014 import DnDAPI
from model.user_db import DatabaseManager

from view.home_view import HomeWidget
from view.characters.character_tab import CharacterTab
from view.campaigns_view.campaigns_tab import CampaignWidget
from view.contenet_view.content_widget import ContentWidget
from view.rulebooks_view import RulebooksWidget


class ViewWidget(QMainWindow):
    '''Layout central de la aplicación, cuenta con unos tabuladores que permite alternar entre las pestañas de la app.'''
    def __init__(self):
        super().__init__()
        api = DnDAPI()
        db = DatabaseManager()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(HomeWidget(), "Home")
        #self.tabs.addTab(CharacterTab(db,api, 1), "Characters")
        self.tabs.addTab(CampaignWidget(db, 1), "Campaigns")
        #self.tabs.addTab(ContentWidget(api), "Content")
        self.tabs.addTab(RulebooksWidget(db, 1), "Rulebooks")
