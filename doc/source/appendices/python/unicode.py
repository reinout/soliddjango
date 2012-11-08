# -*- coding: utf-8 -*-

# Use this file's encoding to type in the actual e+" character.
unicode_string = u"The Dutch word for seas is zeeën"
print unicode_string

# Alternative is to use unicode codes. ë is U+00EB in unicode.
# In Python, that is \xeb .
# START_HIGHLIGHT
unicode_string = u"The Dutch word for seas is zee\xebn"
# END_HIGHLIGHT
print unicode_string
