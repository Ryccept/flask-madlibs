from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "idk"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page_madlibs():
    prompts_list = story.prompts
    return render_template('madlibs.html', prompts=prompts_list)

@app.route('/story')
def story_page_madlibs():
    story_content = story.generate(request.args)
    return render_template('madlibsanswers.html', story=story_content)