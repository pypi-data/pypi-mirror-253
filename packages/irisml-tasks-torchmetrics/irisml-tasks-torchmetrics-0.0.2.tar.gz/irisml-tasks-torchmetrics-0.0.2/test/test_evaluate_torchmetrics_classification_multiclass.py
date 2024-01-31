import unittest
import torch
from irisml.tasks.evaluate_torchmetrics_classification_multiclass import Task


class TestEvaluateTorchmetricsClassificationMulticlass(unittest.TestCase):
    def test_class_id_predictions(self):
        predictions = torch.tensor([0, 0, 2, 3])
        targets = torch.tensor([0, 1, 2, 3])
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions, targets, 4))

        self.assertEqual(outputs.accuracy, 0.75)
        self.assertEqual(outputs.average_precision, 0.6875)
        self.assertEqual(outputs.calibration_error, 0.25)
        self.assertAlmostEqual(outputs.f1_score, 0.66666666)
        self.assertEqual(outputs.precision, 0.625)
        self.assertEqual(outputs.recall, 0.75)

    def test_logits_predictions(self):
        predictions = torch.nn.functional.one_hot(torch.tensor([0, 0, 2, 3])).to(torch.float32)
        targets = torch.tensor([0, 1, 2, 3])
        outputs = Task(Task.Config()).execute(Task.Inputs(predictions, targets, 4))

        self.assertEqual(outputs.accuracy, 0.75)
        self.assertEqual(outputs.average_precision, 0.6875)
        self.assertEqual(outputs.calibration_error, 0.25)
        self.assertAlmostEqual(outputs.f1_score, 0.66666666)
        self.assertEqual(outputs.precision, 0.625)
        self.assertEqual(outputs.recall, 0.75)
