from PyQt6.QtWidgets import (
    QTabWidget, QFormLayout, QLineEdit, 
    QPushButton, QWidget, QMessageBox, QLabel
)

from model import DatabaseManager, DnDAPI, Users
from view.home_view import HomeWidget
from view.characters_view import CharacterTab
from view.campaigns_view import CampaignWidget
from view.contenet_view import ContentWidget
from view.rulebooks_view import RulebooksWidget


class ViewWidget(QWidget):
    '''Layout central de la aplicación, cuenta con unos tabuladores que permite alternar entre las pestañas de la app.'''
    def __init__(self, parent):
        super().__init__()
        self.parent_tab = parent
        self.db = DatabaseManager()
        self.build_ui()

    def build_ui(self):
        '''Construlle la interfaz del formulario de inicio de sesión'''
        self.parent_tab.resize(400, 400)
        layout = QFormLayout()

        # Mail del usuario.
        self.mail = QLineEdit()
        self.mail_label = QLabel("Mail: ")
        layout.addRow(self.mail_label, self.mail)

        # Contraseña del usuario.
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Botón mostrar / ocultar
        self.btn_toggle = QPushButton("👁")
        self.btn_toggle.setCheckable(True)
        self.btn_toggle.setFixedWidth(40)
        self.btn_toggle.clicked.connect(self.toggle_password)

        layout.addRow(self.btn_toggle, self.password)

        # Botón login.
        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.login_check)
        layout.addRow(self.btn_login)

        # Botón registrar.
        self.btn_change = QPushButton("Sign in")
        self.btn_change.clicked.connect(self.toggle_layout)
        layout.addRow(self.btn_change)


        '''Construlle la interfaz del formulario de registro'''
        # Nobre del usuario.
        self.username = QLineEdit()
        self.username_label = QLabel("Username: ")
        layout.addRow(self.username_label, self.username)

        # Mail del usuario.
        self.mailin = QLineEdit()
        self.mailin_label = QLabel("Mail: ")
        layout.addRow(self.mailin_label, self.mailin)

        # Contraseña del usuario.
        self.passwordin = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Botón mostrar / ocultar
        self.btn_togglein = QPushButton("👁")
        self.btn_togglein.setCheckable(True)
        self.btn_togglein.setFixedWidth(40)
        self.btn_togglein.clicked.connect(self.toggle_password)

        layout.addRow(self.btn_togglein, self.passwordin)

        # Botón login.
        self.btn_signup = QPushButton("Sign in")
        self.btn_signup.clicked.connect(self.signin_check)
        layout.addRow(self.btn_signup)

        # Botón registrar.
        self.btn_logup = QPushButton("Login")
        self.btn_logup.clicked.connect(self.toggle_layout)
        layout.addRow(self.btn_logup)

        self.toggle_layout()
        self.setLayout(layout)

    def toggle_password(self, checked):
        if checked:
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
            return
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

    def toggle_layout(self):
        if self.mail.isVisible():
            self.parent_tab.setWindowTitle("CDS - Sign in")
            self.mail.setVisible(False)
            self.mail_label.setVisible(False)
            self.password.setVisible(False)
            self.btn_toggle.setVisible(False)
            self.btn_login.setVisible(False)
            self.btn_change.setVisible(False)

            self.username.setVisible(True)
            self.username_label.setVisible(True)
            self.mailin.setVisible(True)
            self.mailin_label.setVisible(True)
            self.passwordin.setVisible(True)
            self.btn_togglein.setVisible(True)
            self.btn_signup.setVisible(True)
            self.btn_logup.setVisible(True)
            self.passwordin.setEchoMode(QLineEdit.EchoMode.Password)
            return
        
        self.parent_tab.setWindowTitle("CDS - Login")
        self.mail.setVisible(True)
        self.mail_label.setVisible(True)
        self.password.setVisible(True)
        self.btn_toggle.setVisible(True)
        self.btn_login.setVisible(True)
        self.btn_change.setVisible(True)

        self.username.setVisible(False)
        self.username_label.setVisible(False)
        self.mailin.setVisible(False)
        self.mailin_label.setVisible(False)
        self.passwordin.setVisible(False)
        self.btn_togglein.setVisible(False)
        self.btn_signup.setVisible(False)
        self.btn_logup.setVisible(False)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
    

    def login_check(self):
        mail = self.mail.text()
        password = self.password.text()

        if mail == '':
            QMessageBox.warning(self, "Error", "Mail can't be blank")
            return
        
        if password == '':
            QMessageBox.warning(self, "Error", "Password can't be blank")
            return

        users = self.db.get_all_users()
        user = next((obj for obj in users if obj.mail == mail), None)

        if user is None:
            QMessageBox.warning(self, "Error", "Incorrect user")
            return
        
        if user.password != password:
            QMessageBox.warning(self, "Error", "Incorrect password")
            return

        self.loged(user.object_id)

    def signin_check(self):
        username = self.username.text()
        mail = self.mailin.text()
        password = self.passwordin.text()

        if username == '':
            QMessageBox.warning(self, "Error", "Username can't be blank")
            return

        if mail == '':
            QMessageBox.warning(self, "Error", "Mail can't be blank")
            return
        
        if password == '':
            QMessageBox.warning(self, "Error", "Password can't be blank")
            return
        
        try:
            self.db.add_user(Users(
                username=username,
                mail=mail,
                password=password
            ))

            users = self.db.get_all_users()
            self.loged(users[-1].object_id)
        except:
            QMessageBox.warning(self, "Error", "User error")

    def toggle_password(self, checked):
        if checked:
            self.password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.passwordin.setEchoMode(QLineEdit.EchoMode.Normal)
            return
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordin.setEchoMode(QLineEdit.EchoMode.Password)
 
    def loged(self, user_id):
        view_widget = UserView(user_id)
        self.parent_tab.setWindowTitle("CDS")
        self.parent_tab.setCentralWidget(view_widget)
        self.parent_tab.resize(1000, 750)

class UserView(QTabWidget):
    def __init__(self, current_user = 1):
        super().__init__()
        api = DnDAPI()
        db = DatabaseManager()

        self.addTab(HomeWidget(), "Home")
        self.addTab(CharacterTab(db,api, current_user), "Characters")
        self.addTab(CampaignWidget(db, current_user), "Campaigns")
        self.addTab(ContentWidget(api), "Content")
        self.addTab(RulebooksWidget(db, current_user), "Rulebooks")  
