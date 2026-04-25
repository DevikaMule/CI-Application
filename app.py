from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
<title>DevOps CI App</title>
<style>
body {
    font-family: Arial;
    background: linear-gradient(to right, #667eea, #764ba2);
    text-align: center;
    color: white;
}
.box {
    background: white;
    color: black;
    width: 400px;
    margin: 80px auto;
    padding: 20px;
    border-radius: 10px;
}
input {
    padding: 10px;
    width: 80%;
}
button {
    padding: 10px;
    margin-top: 10px;
}
</style>
</head>
<body>
<div class="box">
<h2>🚀 CI Demo App</h2>
<form method="POST">
<input type="text" name="name" placeholder="Enter your name">
<br>
<button type="submit">Submit</button>
</form>
{% if name %}
<h3>Hello {{name}}</h3>
{% endif %}
</div>
</body>
</html>
'''

@app.route('/', methods=['GET','POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template_string(HTML, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)