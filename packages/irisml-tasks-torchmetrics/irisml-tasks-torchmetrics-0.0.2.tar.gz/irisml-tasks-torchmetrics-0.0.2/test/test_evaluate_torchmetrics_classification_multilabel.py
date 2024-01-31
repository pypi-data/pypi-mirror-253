import unittest
import torch
from irisml.tasks.evaluate_torchmetrics_classification_multilabel import Task


class TestEvaluateTorchmetricsClassificationMultilabel(unittest.TestCase):
    def test_class_id_predictions(self):
        predictions = [torch.tensor([0]), torch.tensor([0]), torch.tensor([2]), torch.tensor([3])]
        targets = [torch.tensor([0]), torch.tensor([1]), torch.tensor([2]), torch.tensor([3])]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions_list=predictions, targets_list=targets, num_classes=4))

        self.assertEqual(outputs.accuracy, 0.875)
        self.assertEqual(outputs.average_precision, 0.6875)
        self.assertAlmostEqual(outputs.f1_score, 0.66666666)
        self.assertEqual(outputs.precision, 0.625)
        self.assertEqual(outputs.recall, 0.75)

    def test_logits_predictions(self):
        predictions = torch.nn.functional.one_hot(torch.tensor([0, 0, 2, 3])).to(torch.float32)
        targets = [torch.tensor([0]), torch.tensor([1]), torch.tensor([2]), torch.tensor([3])]
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions=predictions, targets_list=targets, num_classes=4))

        self.assertEqual(outputs.accuracy, 0.875)
        self.assertEqual(outputs.average_precision, 0.6875)
        self.assertAlmostEqual(outputs.f1_score, 0.66666666)
        self.assertEqual(outputs.precision, 0.625)
        self.assertEqual(outputs.recall, 0.75)
