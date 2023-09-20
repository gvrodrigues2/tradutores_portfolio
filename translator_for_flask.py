from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_text = request.form['source_text']
        target_language = request.form['target_language']

        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(source_text)

        return render_template('index.html', translated_text=translated_text, source_text=source_text,
                               target_language=target_language)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
