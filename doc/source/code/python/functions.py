def print_names():
    """Print names."""
    print('Reinout')
    print('Harry')


def print_name(name):
    """Print(the name passed as argument."""
    print(name)


def print_default_name(name='Reinout'):
    """Print(the name (default is Reinout)."""
    print(name)


# You call them like this:
print_names()
print_name('Harry')
print_default_name()
print_default_name('Harry')
