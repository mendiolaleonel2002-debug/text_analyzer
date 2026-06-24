from analyzer.text_analyzer import(
    count_words,
    count_characters,
    count_paragraphs,
    count_sentences,
    longest_paragraph,
    longest_word,
    longest_sentences
)

text = """
Hola mundo. Este texto es para analizar un programa.

Esta es una prueba.

Esto es un parrafo.
"""

print("Palabras: ", count_words(text))
print("Caracteres: ", count_characters(text))
print("Parrafos: ", count_paragraphs(text))
print("Oraciones: ", count_sentences(text))
print("Palabra mas larga: ", longest_word(text))
print("Oracion mas larga: ", longest_sentences(text))
print("Parrafo mas largo: ", longest_paragraph(text))