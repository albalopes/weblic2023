from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/contato', defaults={'n': 'Contato Genérico', 't':'1111-2222'})
@app.route('/contato/<n>/<t>')
def contato(n, t):
    return render_template('contato.html', nome=n, tel=t)

@app.route('/dobro/<int:n>')
def dobro(n):
  resultado = n * 2
  dados = {'n': n, 
           'resultado': resultado
          }
  return render_template('dobro.html', dados=dados)

@app.route('/perfil', defaults={'usuario': 'anonimo'})
@app.route('/perfil/<usuario>')
def usuario(usuario):
  return render_template('perfil.html', usuario=usuario)


@app.route('/dados')
def dados():
  return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
  nome = request.form.get('nome')
  escola = request.form.get('escola') 
  estado = request.form.get('estado')
  formacao = request.form.get('formacao')
  modalidades = request.form.getlist('modalidades')
  
  return render_template('recebedados.html', nome=nome, escola=escola, estado=estado, formacao=formacao,modalidades=modalidades)


@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
  if idade >= 18:
    return 'Maior de idade'
  else:
    return 'Menor de idade'

@app.route('/situacaofinal/<float:nota>')
def situacaofinal(nota):
  situacao = ""
  if nota >= 6.0:
    situacao = "Aprovado"
  elif nota >= 3.0:
    situacao = "Em recuperação"
  else:
    situacao = "Reprovado"
  return render_template('situacaofinal.html', situacao=situacao)

@app.route('/acesso', methods=['GET'])
@app.route('/login', methods=['GET'])
def login():
  if request.method=="GET":
    return render_template('login.html')


@app.route('/login', methods=['POST'])
@app.route('/validalogin', methods=['POST'])
@app.route('/testelogin', methods=['POST'])
def verificalogin():
  login = request.form.get("login")
  senha = request.form.get("senha")
  if login == "admin" and senha=="12345":
    return render_template("arearestrita.html")
  else:
    return "Você não tem permissão de acessar essa página"


@app.route('/numero/<int:n>')
def numero(n):
  return render_template('numero.html', n=n)

@app.route('/rifa/<int:l>/<int:c>')
def rifa(l, c):
  return render_template('rifa.html', l=l, c=c)


'''
@app.route('/compras', methods=['GET'])
def escolheitens():
  return render_template('escolheritens.html')
'''  
@app.route('/compras')
def compras():
  itens = [
    {'nome':'Arroz', 'preco': 5.15} ,
    {'nome':'Farinha', 'preco': 5.60} ,
    {'nome':'Feijão', 'preco': 10.35} ,
  ]
  
  return render_template('compras.html', itens=itens)


@app.route('/disciplinas')
def disciplinas():
  materias = [
    {'nome': 'Desenvolvimento Web', 'professor': 'Alba Lopes', 'creditos': 4},
    {'nome': 'Sistemas Operacionais', 'professor': 'Wanderley', 'creditos': 4},
    {'nome': 'Libras', 'professor': 'Leandro', 'creditos': 2},
  ]

  return render_template('disciplinas.html', materias=materias)

@app.route('/galeria')
def galeria():
  imagens = [
    {'nome':'bart.png', 'legenda': 'Bart Simpson'},
    {'nome':'lisa.png', 'legenda': 'Lisa Simpson'},
    {'nome':'homer.png', 'legenda': 'Homer Simpson'},
  ]
  return render_template('galeria.html', imagens=imagens)




app.run(host='0.0.0.0', port=81, debug=True)

