'''Archivo ejecutable, actua como una raíz para imports y referencias'''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from view import ViewWidget


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.explorer = ViewWidget(self)
        self.setCentralWidget(self.explorer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e1e;
            border: 2px solid #8b5cf6;
        }
                      
        QWidget {
            font-family: Segoe UI;
            background: #2a2a2a;        
            font-size: 14px;
            color: #e5e7eb;
        }

        QTabWidget::pane {
            border: 1px solid #444;
            background: #2a2a2a;
        }

        QTabBar::tab {
            background: #333;
            padding: 8px;
            border-radius: 4px;
        }

        QTabBar::tab:selected {
            background: #8b5cf6;
            color: white;
        }

        QPushButton {
            background-color: #444;
            border: 1px solid #666;
            padding: 6px;
            border-radius: 4px;
        }

        QPushButton:hover {
            background-color: #555;
        }
    """)

    window = Application()
    window.show()
    sys.exit(app.exec())
