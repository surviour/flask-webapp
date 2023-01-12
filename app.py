# run this in "flask"(name of virtual enviourment) virtual enviourment
# minimal web app code copied from google
from flask import Flask, render_template, request,redirect
# request module was import to use the form in post mode
#redirect module is used to send the user to a particular page on performing a particular action 
# for database creation and connection with webapp
from flask_sqlalchemy import SQLAlchemy
# this module provide us with the current date-time of system when an object is created
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(600))
    date_Created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        # use to print the python objects
        return f"{self.sno} - {self.date_Created}"


# this are endpoint(pages) of our web app
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


# this is how we make routes to new pages in our web app(website)
@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title = request.form["title"]
        desc = request.form["desc"]
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)

if __name__ == "__main__":
    app.run(debug=True, port=7860)
    # app.run(debug=True,port=7860) used to run our app
    # debug=True means open app in debugging mode so that we can see the errors if occurs
    # port=7860(optional) in this we are expicitly changing the port from default to our choice
