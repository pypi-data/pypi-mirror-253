import dataclasses
import logging
import typing
import torch
import torchmetrics.functional.classification
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Evaluate predictions results using torchmetrics classification metrics for multilabel classification problems.

    The following metrics are supported:
    - accuracy
    - average_precision
    - f1_score
    - precision
    - recall

    The metrics are macro-averaged, i.e. they are computed for each class and then averaged over the classes.

    Inputs:
        num_classes (int): The number of classes.
        predictions (Tensor): The logits of the predictions. The shape of the Tensor is (N, num_classes). Either predictions or predictions_list must be provided.
        predictions_list (List[Tensor]): The class indices of the predictions. The shape of each Tensor is (N, ).
        targets (LongTensor): The class indices of the targets. The shape of each Tensor is (N, ) or (N, num_classes). Either targets or targets_list must be provided.
        targets_list (List[LongTensor]): The class indices of the targets. The shape of each Tensor is (N, ).
    """

    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        num_classes: int
        predictions: typing.Optional[torch.Tensor] = None  # Shape (N, num_classes)
        predictions_list: typing.Optional[typing.List[torch.Tensor]] = None
        targets: typing.Optional[torch.Tensor] = None  # Shape (N, num_classes)
        targets_list: typing.Optional[typing.List[torch.Tensor]] = None

    @dataclasses.dataclass
    class Outputs:
        accuracy: float = 0.0
        average_precision: float = 0.0
        f1_score: float = 0.0
        precision: float = 0.0
        recall: float = 0.0

    def execute(self, inputs):
        if inputs.predictions is None and inputs.predictions_list is None:
            raise ValueError("predictions or predictions_list must be provided")
        if inputs.predictions is not None and inputs.predictions_list is not None:
            raise ValueError("only one of predictions or predictions_list must be provided")
        if inputs.targets is None and inputs.targets_list is None:
            raise ValueError("targets or targets_list must be provided")
        if inputs.targets is not None and inputs.targets_list is not None:
            raise ValueError("only one of targets or targets_list must be provided")

        if inputs.predictions_list is not None and not all(not torch.is_floating_point(prediction) for prediction in inputs.predictions_list):
            raise ValueError("predictions_list must not be float.")

        predictions = inputs.predictions
        targets = inputs.targets

        if predictions is None:
            predictions = self._multi_hot(inputs.predictions_list, inputs.num_classes).to(torch.float32)

        if targets is None:
            targets = self._multi_hot(inputs.targets_list, inputs.num_classes)
        elif targets.ndim == 1:
            targets = torch.nn.functional.one_hot(targets, num_classes=inputs.num_classes)

        if len(predictions) != len(targets):
            raise ValueError(f"predictions and targets must have the same length, got {len(predictions)} and {len(targets)}")

        # If the predictions are int then we assume they are class indices and we need to convert them to one-hot vectors
        if predictions.ndim == 1 and not torch.is_floating_point(predictions):
            predictions = torch.nn.functional.one_hot(inputs.predictions, num_classes=inputs.num_classes)

        if torch.is_floating_point(targets):
            raise ValueError("targets must be int")

        assert predictions.ndim == 2 and predictions.shape[1] == inputs.num_classes, f"predictions must have shape (N, {inputs.num_classes}), got {predictions.shape}"
        assert targets.ndim == 2 and targets.shape[1] == inputs.num_classes, f"targets must have shape (N, {inputs.num_classes}), got {targets.shape}"

        accuracy = float(torchmetrics.functional.classification.multilabel_accuracy(predictions, targets, num_labels=inputs.num_classes))
        average_precision = float(torchmetrics.functional.classification.multilabel_average_precision(predictions, targets, num_labels=inputs.num_classes))
        f1_score = float(torchmetrics.functional.classification.multilabel_f1_score(predictions, targets, num_labels=inputs.num_classes))
        precision = float(torchmetrics.functional.classification.multilabel_precision(predictions, targets, num_labels=inputs.num_classes))
        recall = float(torchmetrics.functional.classification.multilabel_recall(predictions, targets, num_labels=inputs.num_classes))

        logger.info(f"accuracy: {accuracy}, average_precision: {average_precision}, f1_score: {f1_score}, precision: {precision}, recall: {recall}")

        return self.Outputs(accuracy=accuracy, average_precision=average_precision, f1_score=f1_score, precision=precision, recall=recall)

    @staticmethod
    def _multi_hot(predictions_list, num_classes):
        predictions = torch.zeros((len(predictions_list), num_classes), dtype=torch.int64)
        for i, prediction in enumerate(predictions_list):
            predictions[i, prediction] = 1
        return predictions
