from googletians import Translator

def translate_english_to_kannada(words):
    translator = Translator()

    translations = []
    for word in words:
        translation = translator.translate(word, dest='kn').text
        translations.append(translation)

    return translations

def main():
    input_sentence = input("Enter a sentence or words in English: ")
    english_words = input_sentence.split()  # Split input into a list of words

    kannada_translations = translate_english_to_kannada(english_words)

    for english_word, kannada_word in zip(english_words, kannada_translations):
        print(f'{english_word} → {kannada_word}')

if _name_ == "_main_":
    main()