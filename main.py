from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
