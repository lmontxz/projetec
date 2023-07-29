from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
  
@app.route('/agendamento')
def agen():
  return render_template('agendamento.html', titulo= 'Agende sua Consulta')

@app.route('/login')
def login():
  return render_template('login.html', titulo= 'Login')

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

app.run(debug = True, host='0.0.0.0', port=100)
