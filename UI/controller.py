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

        #print("opzioni biblioteche aggiunte")
        self._view.update()

    def popola_genere_dropdown(self):
        dd_genere = self._view.dropdown_genere
        dd_genere.options.append(ft.DropdownOption(key = "Nessun filtro", text = "Nessun filtro"))

        generi = self._model.get_generi()
        for genere in generi:
            dd_genere.options.append(ft.DropdownOption(key = genere, text = genere))

        #print("opzioni generi aggiunte")
        self._view.update()

    # CALLBACKS DROPDOWN
    def leggi_biblioteca(self, e):
        self.biblioteca_selezionata = e.control.value

        return self.biblioteca_selezionata

    def leggi_genere(self, e):
        self.genere_selezionato = e.control.value

        return self.genere_selezionato

    # AZIONE: MOSTRA LIBRI
    def handler_libri(self, e):
        self._view.clean()

        if self.biblioteca_selezionata == "Nessun filtro":
            self.biblioteca_selezionata = None

        if self.genere_selezionato == "Nessun filtro":
            self.genere_selezionato = None

        libri_filtrati = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if len(libri_filtrati) == 0:
            self._view.show_alert("Non è stato trovato alcun libro corrispondente ai filtri applicati")

        else:
            listview = self._view.listview
            for libro in libri_filtrati:
                testo_libro = ft.Text(str(libro))
                listview.controls.append(testo_libro)

        self._view.update()
        self._view.update()

