from translate import Translator

def main():
    text_translate = input("Digite o texto que deseja traduzir: ")
    target_language = input("Digite o idioma de destino(por exemplo, 'en' para inglês): ")

    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text_translate)

    print(f"Texto traduzido: ")
    print(translated_text)


if __name__ == "__main__":
    main()






