import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QMessageBox, QTabWidget, QLineEdit
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        self.removeTab(index)

    def add_tab(self, widget, title):
        self.addTab(widget, title)

class CustomTitleBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)  # Устанавливаем высоту заголовочной панели
        self.setObjectName("titleBar")  # Устанавливаем объектное имя для стилизации

        # Создаем метку для отображения названия программы
        self.title_label = QtWidgets.QLabel("Simple Steam V8", alignment=QtCore.Qt.AlignCenter)  # Выравниваем текст по центру
        self.title_label.setObjectName("titleLabel")  # Устанавливаем объектное имя для стилизации

        # Создаем кнопку для закрытия программы
        self.close_button = QtWidgets.QPushButton("×")
        self.close_button.setObjectName("closeButton")  # Устанавливаем объектное имя для стилизации
        self.close_button.setFixedSize(30, 30)
        self.close_button.clicked.connect(self.parent().close)  # Подключаем сигнал clicked к методу close родительского окна

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addStretch()  # Растягиваем пространство между названием и кнопкой закрытия
        layout.addWidget(self.close_button)  # Добавляем кнопку закрытия в заголовочную панель
        layout.setContentsMargins(5, 0, 5, 0)  # Устанавливаем внешние отступы слева и справа
        self.setLayout(layout)

        # Применяем стили к заголовочной панели
        self.setStyleSheet("""
            #titleBar {
                background-color: #0D0D0D;
            }
            #titleLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            #closeButton {
                background-color: transparent;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
            }
            #closeButton:hover {
                background-color: #FF5733;
            }
        """)

        # Добавляем функциональность перетаскивания окна
        self.mouse_pos = None
        self.mouse_pressed = False
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mouse_pos = event.globalPos() - self.parent().pos()
            self.mouse_pressed = True

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            if self.mouse_pos:
                self.parent().move(event.globalPos() - self.mouse_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mouse_pressed = False
            self.mouse_pos = None


    def launch_steam(self):
        steam_path = r"C:\Program Files (x86)\Steam\steam.exe"
        if os.path.exists(steam_path):
            os.startfile(steam_path)
        else:
            QMessageBox.critical(self, "Ошибка", "Steam не найден.")

class SteamGamePorter(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Steam V8")
        self.setGeometry(100, 100, 1024, 600)
        self.setStyleSheet("background-color: #212121; color: #FFFFFF;")

                        # Убираем заголовочную панель
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)

        # Добавляем кастомную заголовочную панель
        self.title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.title_bar)

        # Остальной код приложения
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.font_style = QtGui.QFont("Roboto", 14, QtGui.QFont.Bold)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)


        self.font_style = QtGui.QFont("Roboto", 14, QtGui.QFont.Bold)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.installed_games_label = QtWidgets.QLabel("Установленные игры:")
        self.installed_games_label.setFont(self.font_style)
        self.main_layout.addWidget(self.installed_games_label)

        self.installed_games_list = QtWidgets.QListWidget(self)
        self.installed_games_list.setFont(self.font_style)
        self.installed_games_list.setStyleSheet("background-color: #212121; color: #FFFFFF;")
        self.installed_games_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.installed_games_list.itemClicked.connect(self.on_game_select)
        self.main_layout.addWidget(self.installed_games_list)

        self.options_layout = QtWidgets.QHBoxLayout()
        self.launch_options_label = QtWidgets.QLabel("Параметры запуска:")
        self.launch_options_label.setFont(self.font_style)
        self.options_layout.addWidget(self.launch_options_label)

        self.launch_options_entry = QtWidgets.QLineEdit()
        self.launch_options_entry.setFont(self.font_style)
        self.options_layout.addWidget(self.launch_options_entry)
        self.options_layout.addStretch()

        self.main_layout.addLayout(self.options_layout)

        self.button_layout = QtWidgets.QHBoxLayout()

        self.launch_button = QtWidgets.QPushButton("Запустить")
        self.launch_button.setStyleSheet("background-color: #2ecc71; color: #FFFFFF;")
        self.launch_button.setFont(self.font_style)
        self.launch_button.clicked.connect(self.launch_game)
        self.launch_button.setFixedSize(200, 50)
        self.button_layout.addWidget(self.launch_button)

        self.remove_button = QtWidgets.QPushButton("Удалить")
        self.remove_button.setStyleSheet("background-color: #e74c3c; color: #FFFFFF;")
        self.remove_button.setFont(self.font_style)
        self.remove_button.clicked.connect(self.remove_game)
        self.remove_button.setFixedSize(200, 50)
        self.button_layout.addWidget(self.remove_button)

        self.refresh_button = QtWidgets.QPushButton("Обновить")
        self.refresh_button.setStyleSheet("background-color: #9300ff; color: #FFFFFF;")
        self.refresh_button.setFont(self.font_style)
        self.refresh_button.clicked.connect(self.scan_games)
        self.refresh_button.setFixedSize(200, 50)
        self.button_layout.addWidget(self.refresh_button)

        self.open_location_button = QtWidgets.QPushButton("Расположение")
        self.open_location_button.setStyleSheet("background-color: #3498db; color: #FFFFFF;")
        self.open_location_button.setFont(self.font_style)
        self.open_location_button.clicked.connect(self.open_game_location)
        self.open_location_button.setFixedSize(200, 50)
        self.button_layout.addWidget(self.open_location_button)

        self.main_layout.addLayout(self.button_layout)

        self.author_label = QtWidgets.QLabel("By ReTrojan")
        self.author_label.setFont(self.font_style)
        self.author_label.setStyleSheet("background-color: #212121; color: #FFFFFF;")
        self.author_label.setAlignment(QtCore.Qt.AlignRight)
        self.main_layout.addWidget(self.author_label)


        self.scan_games()

    def scan_games(self):
        self.installed_games_list.clear()  # Очистка списка перед обновлением
        steam_path = r"C:\Program Files (x86)\Steam\steamapps\common"
        if os.path.exists(steam_path):
            installed_games = os.listdir(steam_path)
            for game in installed_games:
                item = QtWidgets.QListWidgetItem(game)
                self.installed_games_list.addItem(item)

    def launch_game(self):
        selected_item = self.installed_games_list.currentItem()
        if selected_item:
            selected_game = selected_item.text()
            steam_id = self.get_steam_id(selected_game)
            if steam_id:
                steam_url = f"steam://run/{steam_id}"
                if self.launch_options_entry.text():
                    steam_url += " " + self.launch_options_entry.text()
                QtGui.QDesktopServices.openUrl(QtCore.QUrl(steam_url))
            else:
                print("ID игры Steam не найден.")

    def remove_game(self):
        selected_item = self.installed_games_list.currentItem()
        if selected_item:
            selected_game = selected_item.text()
            confirmation = QMessageBox.question(self, "Подтверждение", f"Вы уверены, что хотите удалить игру '{selected_game}'?",
                                                 QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                game_path = os.path.join(r"C:\Program Files (x86)\Steam\steamapps\common", selected_game)
                try:
                    os.system(f'rd /s /q "{game_path}"')
                    self.installed_games_list.takeItem(self.installed_games_list.row(selected_item))
                    QMessageBox.information(self, "Успех", f"Игра '{selected_game}' успешно удалена.")
                except Exception as e:
                    QMessageBox.critical(self, "Ошибка", f"Не удалось удалить игру '{selected_game}': {str(e)}")

    def open_game_location(self):
        selected_item = self.installed_games_list.currentItem()
        if selected_item:
            selected_game = selected_item.text()
            game_path = os.path.join(r"C:\Program Files (x86)\Steam\steamapps\common", selected_game)
            os.startfile(game_path)  # Открытие расположения игры

    def get_steam_id(self, game_name):
        steam_apps_path = r"C:\Program Files (x86)\Steam\steamapps"
        if os.path.exists(steam_apps_path):
            for foldername in os.listdir(steam_apps_path):
                if foldername.startswith("appmanifest"):
                    file_path = os.path.join(steam_apps_path, foldername)
                    with open(file_path, 'r', encoding="utf-8") as f:
                        content = f.read()
                        if game_name.lower() in content.lower():
                            return foldername.split("_")[1]

    def on_game_select(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SteamGamePorter()
    window.show()
    sys.exit(app.exec_())