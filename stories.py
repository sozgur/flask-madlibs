"""Madlibs Stories."""
from collections import OrderedDict

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, storyId, title, words, text):
        """Create story with words and template text."""
        self.storyId = storyId 
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

class StoryList:
    stories = OrderedDict()

    # def __init__(self):
    #     self.stories = OrderedDict()
    @classmethod
    def createStory(cls, title, words_list, text):
        keys = list(cls.stories.keys())
        key = keys[-1] + 1 if len(keys) > 0 else 1

        story = Story(key, title, words_list, text)
        cls.stories[key] = story

# Here's a story to get you started

StoryList.createStory("Long Ago", ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
StoryList.createStory("Unbelievable",["noun", "adverb", "plural_noun"], """ A woman, wanting to surprise her {noun} for {adverb} {plural_noun}, got him something completely unbelievable.""")

stories = StoryList.stories
