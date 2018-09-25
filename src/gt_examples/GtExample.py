class GtExample:
    def __init__(self,a_class, a_method):
        self.example_class = a_class
        self.example_decorated_method = a_method

    def get_class(self):
        return self.example_class

    def get_name(self):
        return self.get_original_method().__name__

    def get_method(self):
        return self.example_decorated_method

    def run(self):
        example_name = self.get_name()
        examples_instance = self.get_class()()
        return getattr(examples_instance, example_name)()

    def get_original_method(self):
        return self.example_decorated_method._original_method

    def __str__(self):
        return 'Example({})'.format(self.get_name())

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, GtExample):
            return self.example_class == other.example_class and self.get_name() == other.get_name()
        return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash((self.example_class, self.get_name()))
