from flask import Blueprint, render_template, request, session


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('search.html')

@main.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    return render_template('search.html', query=query)
@main.route('/logado')

def logado():
    username = session.get('username')  
    return render_template('logado.html', username=username)

