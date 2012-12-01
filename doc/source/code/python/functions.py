def print_names():
    """Print names."""
    print('Reinout')
    print('Maurits')


def print_name(name):
    """Print(the name passed as argument."""
    print(name)


def print_default_name(name='Reinout'):
    """Print(the name (default is Reinout)."""
    print(name)


# You call them like this:
print_names()  # Prints Reinout and Maurits.
print_name('Maurits')  # Prints Maurits.
print_default_name()  # Prints Reinout.
print_default_name('Maurits')  # Prints Maurits.
