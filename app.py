from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "itssecret"

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    """Return Homepage/question form"""
    questions = story.prompts

    return render_template("homepage.html", questions = questions)



@app.route('/story')
def story_page():
    """returns story with answers filled in"""
    text = story.generate(request.args)

    return render_template("story.html", text = text)

