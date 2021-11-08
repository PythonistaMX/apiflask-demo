from apiflask import APIFlask
from models import db, Alumno
from blueprints import abc_alumnos

app = APIFlask(__name__)

app.config.from_pyfile("settings.py")

db.init_app(app)
    
@app.before_first_request
def crea_base():
    db.create_all()
    with open("data/alumnos.txt", "rt") as f:
        alumnos = eval(f.read())
        for alumno in alumnos:
            db.session.add(Alumno(**alumno))
        db.session.commit()


app.register_blueprint(abc_alumnos, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)