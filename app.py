from bottle import Bottle, route, static_file, run, template, view

app = Bottle()

@app.route('/')
@app.view('home')
def home():
    return {}

@app.route('/truthvsmyth')
@app.view('truthvsmyth')
def truthvsmyth():
    return {}

@app.route('/nzissues')
@app.view('nzissues')
def nzissues():
    return {}

@app.route('/impacts')
@app.view('impacts')
def impacts():
    return {}

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)), debug=False)
        
    