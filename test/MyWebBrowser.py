# Importer les modules nécessaires
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QEvent, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QLineEdit

# Définition des couleurs
color = {
    'MAIN': '#3A3276',
    'LIGHT': '#847EB1',
    'MIDDLE': '#5B5393',
    'DARK': '#201858',
    'FULL DARK': '#0E083B',
}

# Définition de la classe principale du navigateur
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuration de la fenêtre principale
        self.setWindowTitle('Arc Browser')
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.setGeometry(452, 36, 900, 650)
        self.setMinimumSize(900, 650)
        self.setMaximumSize(900, 650)
        
        # Installation de l'event filter pour la transparence
        QApplication.instance().installEventFilter(self)
        
        # Configuration de la fenêtre pour rester au premier plan et opacité à 100%
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(1.0)
        self.is_fullscreen = False  # Variable pour suivre l'état du plein écran
        
        # Configuration du style de la fenêtre
        self.setStyleSheet(f"background-color: {color['MAIN']}")
        
        self.blue_frame = QFrame(self)
        self.blue_frame.setGeometry(218, 2, 680, 646)
        self.blue_frame.setStyleSheet("background-color: #619399; border-radius: 7px; border : 1px solid black")
        self.blue_frame.setVisible(True)  # Visible par défaut
        
        layout = QVBoxLayout(self.blue_frame)
        layout.setContentsMargins(0, 0, 0, 0)  # Supprime les marges du layout
        
        nested_frame = QFrame(self.blue_frame)
        nested_frame.setStyleSheet("background-color: transparent; border-radius: 6px;")  # Coins arrondis
        nested_layout = QVBoxLayout(nested_frame)
        nested_layout.setContentsMargins(1, 1, 1, 1)
        
        self.navigateur = QWebEngineView(nested_frame)
        self.navigateur.setUrl(QUrl('https://www.google.com'))
        nested_layout.addWidget(self.navigateur)
        
        layout.addWidget(nested_frame)
        
        self.is_fullscreen = False
        
        """
        # Création de la frame bleue
        self.blue_frame = QFrame(self)
        self.blue_frame.setGeometry(218, 2, 680, 646)
        self.blue_frame.setStyleSheet(f"background-color: {color['MIDDLE']}; border-radius: 7px; border: 1px solid black")
        self.blue_frame.setVisible(True)  # Visible par défaut
        
        # Création du layout pour la frame bleue
        layout = QVBoxLayout(self.blue_frame)
        layout.setContentsMargins(0, 0, 0, 0)  # Supprime les marges du layout
        
        # Création de la frame interne pour le navigateur web
        nested_frame = QFrame(self.blue_frame)
        nested_frame.setStyleSheet("background-color: transparent; border-radius: 7px;")  # Coins arrondis
        nested_layout = QVBoxLayout(nested_frame)
        nested_layout.setContentsMargins(0, 0, 0, 0)
        
        # Initialisation du composant du navigateur web
        self.navigateur = QWebEngineView(nested_frame)
        self.navigateur.setUrl(QUrl('https://www.duckduckgo.com'))
        nested_layout.addWidget(self.navigateur)
        self.navigateur.urlChanged.connect(self.update_url)
        
        # Ajout de la frame interne au layout
        layout.addWidget(nested_frame)
        """
        # Configuration de la barre d'adresse
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.search)
        self.url_bar.setGeometry(4, 650-6-20 , 210, 20)  # Position et taille de la barre d'adresse
        self.url_bar.setStyleSheet(
            f"border-radius: 2px; background-color: {color['DARK']}; color: {color['LIGHT']}; font: 11pt monospace;"
        )
        
        # Connexion des signaux pour la mise à jour de la barre d'adresse
        self.url_bar.textChanged.connect(self.update_partial_url)
        self.url_bar.editingFinished.connect(self.update_full_url)
        
        self.partial_url = ''  # Garder une copie du texte partiel de la barre d'adresse
        
    # Méthode pour filtrer les événements de l'application
    def eventFilter(self, obj, event):
        if event.type() == QEvent.ApplicationDeactivate:
            self.setWindowOpacity(0.85)  # Passage à 85% d'opacité lorsque l'application passe au second plan
        if event.type() == QEvent.ApplicationActivate:
            self.setWindowOpacity(1)
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_G:
                self.toggle_fullscreen()
        return super().eventFilter(obj, event)
    
    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.blue_frame.setGeometry(218, 2, 680, 646)
            self.url_bar.setVisible(True)
            self.is_fullscreen = False
        else:
            self.blue_frame.setGeometry(0, 0, self.width(), self.height())
            self.url_bar.setVisible(False)
            self.is_fullscreen = True

    # Méthode pour mettre à jour le texte partiel dans la barre d'adresse
    def update_partial_url(self, text):
        self.partial_url = text  # Mettre à jour le texte partiel
        
        if self.url_bar.hasFocus():
            self.url_bar.setText(self.partial_url[-35:])  # Afficher les derniers caractères
        else:
            self.url_bar.setText(self.partial_url)  # Afficher le texte complet
    
    # Méthode pour mettre à jour le texte complet dans la barre d'adresse
    def update_full_url(self):
        if not self.url_bar.hasFocus():
            self.url_bar.setText(self.partial_url)
    
    # Méthode pour effectuer une recherche en utilisant la barre d'adresse
    def search(self):
        url = self.url_bar.text()
        self.navigateur.setUrl(QUrl(f'https://{url}'))
    
    # Méthode pour mettre à jour l'URL dans la barre d'adresse lorsque la page change
    def update_url(self, url):
        self.url_bar.setText(url.toString())

# Point d'entrée du programme
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
