from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Desenvolvedor Web',
    'localidade': 'São Paulo',
    'salario': 'R$ 3.500,00'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Python',
    'localidade': 'São Paulo',
    'salario': 'R$ 4.500,00'
}, {
    'id': 3,
    'titulo': 'Desenvolvedor Java',
    'localidade': 'São Paulo',
    'salario': 'R$ 5.500,00'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor JavaScript',
    'localidade': 'São Paulo',
    'salario': 'R$ 6.500,00'
}, {
    'id': 5,
    'titulo': 'Desenvolvedor C#',
    'localidade': 'São Paulo',
    'salario': 'R$ 7.500,00'
}]


@app.route('/')
def hello():
  return render_template("home.html", vagas=VAGAS)


@app.route('/vagas')
def listar_vagas():
  return jsonify(VAGAS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
