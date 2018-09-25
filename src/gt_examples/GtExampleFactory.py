from .GtExample import GtExample
from .GtExampleGroup import GtExampleGroup


class GtExampleFactory:
    @classmethod
    def examples_in(cls, a_class):
        factory = cls()
        example_methods = factory.example_methods_in(a_class)
        return GtExampleGroup([GtExample(a_class, each_method) for each_method in example_methods])

    @classmethod
    def examples_in_all(cls, the_classes):
        all_examples = []
        factory = cls()
        for a_class in the_classes:
            each_class_example_methods = factory.example_methods_in(a_class)
            for each_example_method in each_class_example_methods:
                all_examples.append(GtExample(a_class, each_example_method))

        return GtExampleGroup(all_examples)

    def all_methods_in(self, a_class):
        return [getattr(a_class, func) for func in dir(a_class) if callable(getattr(a_class, func)) and not func.startswith("__")]

    def example_methods_in(self,a_class):
        all_methods = self.all_methods_in(a_class)
        return [each_method for each_method in all_methods if hasattr(each_method, "_is_example")]
