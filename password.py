import random
import string

class Password:

    def __init__(self, length = 12, strong = 'medium'):

        text = ''
        chars = {
            'min': string.digits,
            'vey_low': string.hexdigits,
            'low': string.ascii_lowercase,
            'medium': ''.join([string.ascii_lowercase, string.digits]),
            'high': string.ascii_letters,
            'very_high':  ''.join([string.ascii_letters, string.digits]),
            'max': ''.join([string.ascii_letters, string.digits, string.punctuation]),
        }

        while len(text) < length: text += random.choice(chars[strong])

        self.password = text

    def __str__(self):

        return self.password
