class Author(object):
    subject = 'Anything'

    def __init__(self, name):
        self.name = name

    def info(self):
        """Print author's name and subject."""
        print(self.name + ' writes about ' + self.subject)


class DjangoBookAuthor(Author):
    subject = 'Django'


# You use them like this:
author = Author('Rianne')
author2 = DjangoBookAuthor('Reinout')
author.info()
# Outputs 'Rianne writes about Anything'.
author2.info()
# Outputs 'Reinout writes about Django'.
print(author2.name)
# Outputs 'Reinout'.
