from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<title>Greeting App</title>
<h1>Enter your name</h1>
<form method="POST">
    <input type="text" name="name">
    <input type="submit" value="Greet">
</form>
{% if greeting %}
    <h2>{{ greeting }}</h2>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def greet():
    greeting = None
    if request.method == 'POST':
        name = request.form['name']
        greeting = f"Hello, {name}!"
    return render_template_string(HTML_TEMPLATE, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
