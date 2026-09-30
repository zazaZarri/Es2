from libro import Libro
from biblioteca import Biblioteca

biblio = Biblioteca("Biblioteca")
l1 = Libro("2001", "Gemelle", 1955, "Mondadori", 328)
l2 = Libro("Il Signore degli Anelli", "Signor anello", 1954, "Lui", 1200)
l3 = Libro("Fahrenheit 451", "Pompieri", 1953, "Mondadori", 180)

biblio.aggiungi_libro(l1)
biblio.aggiungi_libro(l2)
biblio.aggiungi_libro(l3)

print(f"{biblio.nome}")
print(f"Totale libri presenti: {biblio.conta_libri()}\n")

print(f"Tempo stimato di lettura per '{l1.titolo}': {l1.reading_time()} minuti\n")

autore_cercato = "Orwell"
print(f"Ricerca libri per autore '{autore_cercato}':")
risultati = biblio.cerca_per_autore(autore_cercato)
for libro in risultati:
    print(libro)