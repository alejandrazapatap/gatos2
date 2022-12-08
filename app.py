from flask import Flask, render_template
from views import views
from flask_sqlalchemy import SQLAlchemy
import sqlite3



#register of views
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sitio.db'

#cursor to query to db
db = SQLAlchemy(app)

app.register_blueprint(views, url_prefix="/views")

@app.route("/query")
def query():
    con=sqlite3.connect("database/sitio.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM project")
    data=cur.fetchall()
    con.close()
    return render_template('query.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

