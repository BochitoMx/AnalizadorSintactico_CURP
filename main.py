from flask import Flask, render_template, request, jsonify
from lexer import lexico
from parser import sintactico

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    curp = request.form['curp']
    lex_analysis = lexico(curp)
    syntactic_validation = sintactico(curp)
    return jsonify({
        'lexical_analysis': lex_analysis,
        'syntactic_validation': syntactic_validation
    })

if __name__ == '__main__':
    app.run(debug=True)
