from flask import Flask

app = Flask(__name__)

def template(value, id=None):
    content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        {value}
    </head>
    <body>
    
    </body>
    </html>
    '''
    return content

@app.route('/')
def main():
    return template('<h1><a href="/">WEB</a></h1>hello world~')


app.run(port=5000)