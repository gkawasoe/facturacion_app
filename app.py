from PySide2.QtWidgets import QApplication
from controllers.pantalla_principal_window import PantallaPrincipalVentana

if __name__ == "__main__":
    app = QApplication()
    window = PantallaPrincipalVentana()
    window.show()

    app.exec_()