from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'segredo123'  # Necessário para sessão
Bootstrap(app)

# Fake DB de usuários (login e senha)

usuarios = {
    'admin': '1234',
    'joao': 'senha',
    'maria': 'teste'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        module = request.form['module']

        if username in usuarios and usuarios[username] == password:
            session['user'] = username
            if module == 'financeiro':
                return redirect(url_for('financeiro'))
            elif module == 'estoque':
                return redirect(url_for('estoque'))
            elif module == 'orcamentos':
                return redirect(url_for('orcamentos'))
            else:
                flash("Módulo inválido.")
        else:
            flash("Usuário ou senha incorretos.")
    return render_template('login.html')

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/orcamentos')
def orcamentos():
    return render_template('orcamentos.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
