from lib.Space import Space

class Object(Space):
    def __init__(self, name='Unknown'):
        super().__init__()
        self.name = name
        self._char = 'O'
