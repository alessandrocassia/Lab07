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
        #print("DEBUG: connessione generi creata - cursore creato")

        query = """
                SELECT DISTINCT `genere`
                FROM libro
                """
        cursore.execute(query)
        #print("DEBUG: query generi eseguita")

        lista_generi = []
        for genere in cursore:
            lista_generi.append(genere[0])
        #print("DEBUG: libri aggiunti alla lista generi)")

        cursore.close()
        cnx.close()

        return lista_generi

    def restituisci_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        cursore = cnx.cursor()

        query = """
                SELECT `id`, `titolo` ,`autore`, `genere`, `anno_pubblicazione`, `id_biblioteca`
                FROM libro
                    WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
                    AND genere = COALESCE(%s, genere)
                """

        cursore.execute(query, (biblioteca, genere))

        libri_filtrati = []
        for record in cursore:
            libro = Libro(record[0], record[1], record[2], record[3], record[4], record[5])
            libri_filtrati.append(libro)

        cursore.close()
        cnx.close()

        return libri_filtrati