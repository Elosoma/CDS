from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QTabWidget, QFormLayout, QLineEdit, 
    QPushButton, QWidget, QMessageBox,
    QLabel, QVBoxLayout, QHBoxLayout
)

from model import DatabaseManager, DnDAPI, Users
from view.home_view import HomeWidget
from view.characters_view import CharacterTab
from view.campaigns_view import CampaignWidget
from view.contenet_view import ContentWidget
'''


from view.rulebooks_view import RulebooksWidget'''

class ViewWidget(QWidget):
    '''Layout central de la aplicación, cuenta con unos tabuladores que permite alternar entre las pestañas de la app.'''
    def __init__(self, parent):
        super().__init__()
        self.parent_tab = parent
        self.db = DatabaseManager()
        self.api = DnDAPI()

        self.build_ui()

    def build_ui(self):
        layout = QFormLayout()
    
        '''Construlle la interfaz del formulario de inicio de sesión'''
        # Mail del usuario.
        self.mail = QLineEdit()
        self.mail.setMaximumSize(250, 30)
        self.mail_label = QLabel(" Mail: ")
        self.mail_label.setObjectName("logo_inicio")
        self.mail_label.setFixedHeight(30)
        layout.addRow(self.mail_label, self.mail)

        # Contraseña del usuario y botón mostrar / ocultar.
        self.password = QLineEdit()
        self.password.setMaximumSize(250, 30)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_toggle = QPushButton("👁")
        self.btn_toggle.setCheckable(True)
        self.btn_toggle.setFixedWidth(40)
        self.btn_toggle.clicked.connect(self.toggle_password)
        layout.addRow(self.btn_toggle, self.password)

        # Botón login.
        self.btn_login = QPushButton("Login")
        self.btn_login.setMaximumSize(250, 100)
        self.btn_login.clicked.connect(self.login_check)
        layout.addRow(self.btn_login)

        # Botón registrar.
        self.btn_change = QPushButton("Sign in")
        self.btn_change.setMaximumSize(250, 100)
        self.btn_change.clicked.connect(self.toggle_layout)
        layout.addRow(self.btn_change)

        '''Construlle la interfaz del formulario de registro'''
        # Nobre del usuario.
        self.username = QLineEdit()
        self.username.setMaximumSize(250, 30)
        self.username_label = QLabel(" Username: ")
        self.username_label.setFixedHeight(30)
        layout.addRow(self.username_label, self.username)

        # Mail del usuario.
        self.mailin = QLineEdit()
        self.mailin.setMaximumSize(250, 30)
        self.mailin_label = QLabel(" Mail: ")
        self.mailin_label.setFixedHeight(30)
        layout.addRow(self.mailin_label, self.mailin)

        # Contraseña del usuario y botón mostrar / ocultar.
        self.passwordin = QLineEdit()
        self.passwordin.setMaximumSize(250, 30)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_togglein = QPushButton("👁")
        self.btn_togglein.setCheckable(True)
        self.btn_togglein.setFixedWidth(40)
        self.btn_togglein.clicked.connect(self.toggle_password)

        layout.addRow(self.btn_togglein, self.passwordin)

        # Botón login.
        self.btn_signup = QPushButton("Sign in")
        self.btn_signup.setMaximumSize(250, 100)
        self.btn_signup.clicked.connect(self.signin_check)
        layout.addRow(self.btn_signup)

        # Botón registrar.
        self.btn_logup = QPushButton("Login")
        self.btn_logup.setMaximumSize(250, 100)
        self.btn_logup.clicked.connect(self.toggle_layout)
        layout.addRow(self.btn_logup)

        self.toggle_layout()

        form_widget = QWidget()
        form_widget.setLayout(layout)
        form_widget.setFixedWidth(330)

        main_v = QVBoxLayout()
        main_h = QHBoxLayout()

        main_h.addStretch()
        main_h.addWidget(form_widget)
        main_h.addStretch()

        main_v.addStretch()
        main_v.addLayout(main_h)
        main_v.addStretch()

        self.setLayout(main_v)
        self.parent_tab.move(500,300)
        self.parent_tab.resize(400, 400)

    def toggle_layout(self):
        self.passwordin.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

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

    def login_check(self):
        mail_text = self.mail.text()
        password = self.password.text()

        if mail_text == '':
            QMessageBox.warning(self, "Error", "Mail can't be blank")
            return
        
        if password == '':
            QMessageBox.warning(self, "Error", "Password can't be blank")
            return

        users = self.db.get_all_users()
        user = next((obj for obj in users if obj.mail == mail_text), None)

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
                mail=mail,
                username=username,
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
        view_widget = UserView(self.api, self.db, self.parent_tab, user_id)
        self.parent_tab.setWindowTitle("CDS")
        self.parent_tab.setCentralWidget(view_widget)
        self.parent_tab.resize(1000, 750)


class UserView(QTabWidget):
    def __init__(self, api, db, parent, current_user = 1):
        super().__init__()
        self.parent_tab = parent

        self.addTab(HomeWidget(), "Home")
        self.addTab(CharacterTab(db,api, current_user), "Characters")
        self.addTab(CampaignWidget(db, current_user), "Campaigns")
        self.addTab(ContentWidget(api), "Content")
        self.addTab(QWidget(), "Log off")

        self.parent_tab.move(300,100)
        self.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        '''Salir de la app'''
        if index == 4:
            reply = QMessageBox.question(
                self,
                "Log out?",
                "Are you sure you want to log out?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.Yes:
                self.parent_tab.setCentralWidget(ViewWidget(self.parent_tab))
            else:
                self.setCurrentIndex(0)
