class Errors(Exception):
    pass


class InstantiateCSVError(Errors):
    def __init__(self, *args):
        self.message = args[0] if args else 'InstantiateCSVError: items.csv поврежден'

    def __str__(self):
        return f'{self.message}'
