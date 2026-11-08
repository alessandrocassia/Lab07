from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def restituisci_generi(self):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor()
        print("DEBUG: connessione generi creata - cursore creato")

        query = """
                SELECT DISTINCT `genere`
                FROM libro
                """
        cursore.execute(query)
        print("DEBUG: query generi eseguita")

        lista_generi = []
        for genere in cursore:
            lista_generi.append(genere[0])
        print("DEBUG: libri aggiunti alla lista generi)")

        cursore.close()
        cnx.close()

        return lista_generi
