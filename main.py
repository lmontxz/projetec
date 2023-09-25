from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'af'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM login')
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', login=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO login (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/agendamento')
def agen():
  return render_template('agendamento.html', titulo='Agende sua Consulta')


@app.route('/perfil')
def perfil():
  return render_template('perfil.html', titulo= 'Perfil Profissional')

@app.route('/navegar')
def navegar():
  return render_template('navegar.html', titulo= 'Perfis recomendados')

@app.route('/psicanalistas')
def psicanalistas():
  return render_template('psicanalistas.html', titulo= 'Psicanalistas Disponíveis')

@app.route('/psicologos')
def psicologos():
  return render_template('psicologos.html', titulo= 'Psicólogos Disponíveis')

@app.route('/psiquiatras')
def psiquiatras():
  return render_template('psiquiatras.html', titulo= 'Psiquiatras Disponíveis')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html', titulo= 'Sobre Nós')

@app.route('/proximas')
def proximas():
  return render_template('proximas.html', titulo= 'Historico de Consultas')

app.run(debug = True, host='0.0.0.0', port=100)
