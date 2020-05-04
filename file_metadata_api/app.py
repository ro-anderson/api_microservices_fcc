from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def render_form():
    if request.method == 'POST':
        for _, file in request.files.items():
            downloaded_file = file.read()
            return { "name": file.filename, "size": len(downloaded_file) }
    return render_template('form.html')

#requests -> o que vem client api1, api2, api3 
#responses -> resposta pro client

app.run
