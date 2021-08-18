from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories


app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

app.config['SECRET_KEY'] = "asdfasdfsdafdsfdasfaf"
debug = DebugToolbarExtension(app)


@app.route('/', methods=['GET', 'POST'])
def chose_story():
    """Choose story from list and generate the story to ask words. """
    if request.method == 'POST':
        storyId = int(request.form['story_id'])
        return render_template('story_form.html', stories = stories.values(), story = stories[storyId])
    else:
        return render_template('story_form.html', stories = stories.values(), story=None)


@app.route('/story')
def story():
    """Show story"""
    storyId = int(request.args["story_id"])
    story = stories[storyId]
    story_text = story.generate(request.args)

    return render_template('story.html', story=story_text)

