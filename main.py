from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<string:text>')
def index(text):
    return render_template("base.html", title=text)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    lists = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
             "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот джронов"]
    return render_template("list_prof.html", profs=lists, types=type_list)


@app.route('/auto_answer')
def answer():
    person = {'surname': 'Рётся', 'name': 'Эрно', 'education': 'Основное общее',
              'profession': 'в процессе получения', 'sex': 'М', 'motivation': 'Нету',
              'ready': 'False'}
    return render_template("auto_answer.html", title="Анкета", person=person,
                           css=url_for('static', filename='css/anwser_style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
