import sys
import os
#Agregar la ruta del paquete
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzer.text_analyzer import (
    count_words,
    count_characters,
    count_sentences,
    longest_word
)

def test_count_words():
    text = "Hola mundo"
    assert count_words(text) == 1

def test_count_characters():
    text = "Hola"
    assert count_characters(text) == 4

def test_count_sentences():
    text = "Hola mundo. Esto es una prueba."
    assert count_sentences(text) == 2

def test_longest_word():
    text = "Hola mundo de programacion"
    assert longest_word(text) == "programacion"

if __name__ == '__main__':
    print("Ejecutando tests...")
    test_count_words()
    test_count_characters()
    test_count_sentences()
    test_longest_word()
    print("Todos los tests se ejecutaron correctamente")