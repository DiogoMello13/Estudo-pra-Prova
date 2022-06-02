from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Dados(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  numeros = db.Column(db.String)
  posicao = db.Column(db.String)
  caracter = db.Column(db.String)


@app.route('/')
def index():
    new_dados = Dados.query.all()
    return render_template('index.html', new_dados = new_dados)

@app.route('/add', methods=['POST'])
def add():
  name = request.form.get('name')
  numeros = request.form.get('numeros')
  posicao = request.form.get('posicao')
  caracter = request.form.get('caracter')

  new_dados = Dados(
    name=name, numeros=numeros, posicao=posicao, caracter=caracter
  )
  db.session.add(new_dados)
  db.session.commit()
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  new_dados = Dados.query.filter_by(id=id).first()
  db.session.delete(new_dados)
  db.session.commit()
  return redirect ('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  name = request.form.get('name')
  numeros = request.form.get('numeros')
  posicao = request.form.get('posicao')
  caracter = request.form.get('caracter')
  new_dados = Dados.query.filter_by(id=id).first()
  new_dados.name = name
  new_dados.numeros = numeros
  new_dados.posicao = posicao
  new_dados.caracter = caracter
  db.session.commit()
  return redirect('/')


if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=81)