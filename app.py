from flask import Flask, render_template, redirect ,request,url_for
from wtforms import StringField, BooleanField
from wtforms.validators import Length, InputRequired
from flask_wtf import FlaskForm
from bson import ObjectId
from flask_pymongo import MongoClient
from flask_bootstrap import Bootstrap

# creates a Flask application, named app
app = Flask(__name__)
Bootstrap(app)
#calling client
client = MongoClient('mongodb://127.0.0.1:27017')
#database name
db = client.mydatabase
todos = db.todo
# for securing our content
app.config['SECRET_KEY'] = 'this_is_a_secret'

class Todo(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(max=100)])
    done = BooleanField("Done")

    '''def validate_name(form, field):
        if len(field.data) > 50:
            raise ValidationError('Name must be less than 50 characters')
'''

'''todos = [
        {
            'Title': 'Do TOC Assignment',
            'Done': False,
        }, {
            'Title': 'OOP Assignment',
            'Done': True,
        },
    ]'''
@app.route('/', methods = ['GET', 'POST'])      #for adding content in To-do-list
def home():
    form = Todo()
    if form.validate_on_submit():
        task = {
            'Title': form.title.data,
            'Done': form.done.data
        }
        todos.insert(task)
        return redirect("/")
    return render_template("home_page.html", todo_list=todos.find(), form=form) #rendering

@app.route("/delete/<string:index>")       #deleting content of the list
def delete(index):
    #todos.pop(index)
    todos.remove({'_id': ObjectId(index)})
    return redirect("/")

#def hello():
 #   myTodo = Todo()



#@app.route('info')
#def info():
 #   return render_template("info.html")

#@app.route('info2')
#def info2():
 #   return render_template("info2.html")

# run the application
if __name__ == "__main__":
    app.run(debug=True)

