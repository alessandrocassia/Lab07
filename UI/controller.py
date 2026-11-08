import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_biblioteca_dropdown(self):
        dd_biblioteca = self._view.dropdown_biblioteca
        dd_biblioteca.options.append(ft.DropdownOption(key = "Nessun filtro", text = "Nessun filtro"))

        biblioteche = self._model.get_biblioteche() #prendo tutte le biblioteche dal database

        for biblioteca in biblioteche:
            dd_biblioteca.options.append(ft.DropdownOption(key = str(biblioteca.id), text = biblioteca.nome))

        print("opzioni biblioteche aggiunte")
        self._view.update()

    def popola_genere_dropdown(self):
        dd_genere = self._view.dropdown_genere
        dd_genere.options.append(ft.DropdownOption(key = "Nessun filtro", text = "Nessun filtro"))

        generi = self._model.get_generi()
        for genere in generi:
            dd_genere.options.append(ft.DropdownOption(key = genere, text = genere))

        print("opzioni generi aggiunte")
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
