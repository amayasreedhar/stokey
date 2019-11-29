
from flask import Flask,render_template
app = Flask(__name__)






@app.route('/')
def hello_world():
    return 'Hello World!'

    @app.route('/log')
    def log():
        return render_template('login.html')




        if __name__ == '__main__':
            app.run(debug=True, port=5500)


