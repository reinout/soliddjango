# Partial copy from https://github.com/django/django/blob/master/docs/_ext/djangodocs.py
# Goal: to get the 'setting' intersphinx references to work.

def setup(app):
    app.add_crossref_type(
        directivename = "setting",
        rolename = "setting",
        indextemplate = "pair: %s; setting",
    )
