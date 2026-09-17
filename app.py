from bottle import route, static_file, run, template, view

@route('/')
@view('home')
def home():
    return {}

@route('/about')
@view('about')
def about():
    return {}

@route('/contact')
@view('contact')
def contact():
    return {}

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, reloader=True, debug=True)
print("Server is running at http://localhost:8080")