from gt_examples import (GtExample, example, Assert)


class Haba:
    @example
    def foo(self):
        return 'foo'

    @example
    def bar(self):
        return 'bar'


class GtExampleExamples:
    @example
    def foo_example(self):
        foo = GtExample(Haba, Haba.foo)
        Assert.equals(foo.get_class(), Haba)
        Assert.equals(foo.get_name(), 'foo')
        Assert.equals(foo.get_method(), Haba.foo)
        return foo

    @example
    def bar_example(self):
        bar = GtExample(Haba, Haba.bar)
        Assert.equals(bar.get_class(), Haba)
        Assert.equals(bar.get_name(), 'bar')
        Assert.equals(bar.get_method(), Haba.bar)
        return bar

    @example
    def examples_equality(self):
        foo = self.foo_example()
        bar = self.bar_example()
        Assert.not_equals(foo, bar)
        return foo == bar