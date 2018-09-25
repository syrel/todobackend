class GtExampleGroup:
    def __init__(self,gt_examples):
        self.gt_examples = gt_examples

    def examples(self):
        return self.gt_examples

    def run(self):
        print('Running examples...')
        for each_example in self.examples():
            result = each_example.run()
            print(' ',each_example.get_name(), ' => ', result)
