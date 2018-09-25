class GtExampleDependency:
    def __init__(self,gt_example):
        self.gt_example = gt_example
        self.parent_dependencies = []
        self.child_dependencies = []

    def add_parent(self, parent_dependency):
        self.parents().append(parent_dependency)

    def add_child(self, child_dependency):
        self.children().append(child_dependency)

    def parents(self):
        return self.parent_dependencies

    def children(self):
        return self.child_dependencies
