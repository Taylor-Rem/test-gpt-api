from flask import Flask, render_template, request
from chat_model import generate_message

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response_text = generate_message(user_input)
    return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
    app.run(debug=True)