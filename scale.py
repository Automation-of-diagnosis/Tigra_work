from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    try:
        title='Оценка тяжести состояния пациента'
        scale='Введите показатели:'
        return render_template ('index.html', page_title=title, scale=scale)
    except (IndexError, TypeError):
        return False

if __name__=='__main__':
    app.run(debug=True)