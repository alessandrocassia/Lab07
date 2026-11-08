from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def restituisci_biblioteche(self):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor()
        #print("DEBUG: connessione biblioteche creata - cursore creato")

        query = ("""SELECT `id`, `nome`, `indirizzo`
                    FROM biblioteca""")
        cursore.execute(query)
        #print("DEBUG: query biblioteche eseguita")

        lista_biblioteche = []
        for record in cursore:
            biblioteca = Biblioteca(id = record[0], nome = record[1], indirizzo = record[2])
            lista_biblioteche.append(biblioteca)
        #print("DEBUG: biblioteche aggiunte alla lista biblioteche")

        cursore.close()
        cnx.close()

        return lista_biblioteche
