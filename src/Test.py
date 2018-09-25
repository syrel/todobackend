from models import (TaskExamples)

from gt_examples import (example, GtExampleFactory, GtExampleExamples, Assert)

GtExampleFactory.examples_in_all((TaskExamples, GtExampleExamples)).run()