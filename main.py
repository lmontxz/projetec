from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('projetec.html')
  
@app.route('/agendamento')
def agen():
  return render_template('agendamento.html', titulo= 'Agende sua Consulta')

@app.route('/login')
def login():
  return render_template('login.html', titulo= 'Login')

@app.route('/perfil')
def perfil():
  return render_template('perfil.html', titulo= 'Perfis recomendados')

@app.route('/navegar')
def navegar():
  return render_template('navegar.html', titulo= 'Perfis recomendados')

app.run(debug = True, host='0.0.0.0', port=100)
