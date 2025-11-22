from flask import flask,
from flask_mysqldb import flask_mysqldb

#create a flask object
app = Flask(__name__)

#connect to MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'employee_data'

mysql = MySQL (app)

#route the data from the front-end
@app.route('/', methods = ['GET', 'POST'])
def index():
    msg = "Data successfully sent!"
    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']
        cur = mysql.connection.cursor()


        cur.execute("INSERT INTO employee(name,age)VALUES(%s, %s)",(name,age))

        mysql.connection.commit()
        cur.close()

        msg = "Data inserted succesfully!"

    return render_template("index.html", msg = msg)
if __name__ == "__main__"
    app.run(debug = True)