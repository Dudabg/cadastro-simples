from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos (inicialmente vazia)
produtos = []

# Rota para a página inicial (listagem de produtos)
@app.route('/')
def index():
    # Ordena os produtos por valor (do menor para o maior)
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('index.html', produtos=produtos_ordenados)

# Rota para o formulário de cadastro de produtos
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        disponivel = request.form.get('disponivel', False) == 'sim'

        # Adiciona o produto à lista
        produtos.append({'nome': nome, 'descricao': descricao, 'valor': valor, 'disponivel': disponivel})

        # Redireciona para a página inicial (listagem de produtos)
        return redirect(url_for('index'))

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)
