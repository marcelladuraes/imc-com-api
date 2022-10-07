from sre_constants import SRE_FLAG_UNICODE
from flask import Flask, request
app = Flask(__name__)
# http://127.0.0.1:5000/teste/1
@app.route('/teste/1', methods=['GET', 'POST'])
def teste_dados_formulario_html():
    if request.method == 'POST':
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        imc = peso/(altura**2)
        situacao = ''
        if imc < 18.5:
            situacao = 'Abaixo do peso'
        elif imc >= 18.6 and imc <= 24.9:
            situacao = 'Peso ideal (parabéns)'
        elif imc >= 25 and imc <= 29.9:
            situacao = 'Levemente acima do peso'
        elif imc >= 30 and imc <= 34.9:
            situacao = 'Obesidade grau I'
        elif imc >= 35 and imc <= 39.9:
            situacao = 'Obesidade grau II (severa)'
        else: 
            situacao = 'Obesidade III (mórbida)'

        return '''
                <h1>Peso: {} kg</h1>
                <h1>Altura: {} m</h1>
                <h2>IMC: {}</h2>
                <h2>Situação: {}</h2>
                '''.format(peso, altura, imc, situacao,)

    return '''
            <form method="POST">
            <div><label>Informe a altura(m): <input type="number" step="0.01" id="totalAmt"
            name="altura"></label></div>
            <div><label>Informe o peso(kg): <input type="number" step="0.01" id="totalAmt"
            name="peso"></label></div>
            <input type="submit" value="Enviar">
            </form>'''
if __name__ == '__main__':
    app.run(debug = True, port = 5000)