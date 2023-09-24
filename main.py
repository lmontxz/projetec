from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'FUNCIONA2'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes')
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', clientes=data)

@app.route('/login', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO clientes (nome, email) VALUES (%s, %s)', (nome, email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/perfil')
def perfil():
    return render_template('perfil.html', titulo='Perfil Profissional')
@app.route('/agendamento')
def agen():
    return render_template('agendamento.html', titulo='Agende sua Consulta')


@app.route('/navegar')
def navegar():
    return render_template('navegar.html', titulo='Perfis recomendados')


@app.route('/psicanalistas')
def psicanalistas():
    return render_template('psicanalistas.html', titulo='Psicanalistas Disponíveis')


@app.route('/psicologos')
def psicologos():
    return render_template('psicologos.html', titulo='Psicólogos Disponíveis')


@app.route('/psiquiatras')
def psiquiatras():
    return render_template('psiquiatras.html', titulo='Psiquiatras Disponíveis')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre Nós')


@app.route('/proximas')
def proximas():
    return render_template('proximas.html', titulo='Historico de Consultas')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=100)
