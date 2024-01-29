"""
Test basic functionality of classifiers.py
"""
import PIL.Image
import numpy as np
import torch

from transfer_learning_vision_classifiers import classifiers


def test_trivial_classifier(tmp_path):
    torch.manual_seed(0)

    # Instantiate a trivial classifier and save it
    trivial_classifier = classifiers.TransferLearningVisionClassifier(
        "trivial", ["cat", "dog"], False
    )
    save_path = tmp_path / "test.pth"
    trivial_classifier.save_model(save_path)

    # Now load this classifier again.
    trivial_classifier_loaded = classifiers.TransferLearningVisionClassifier(
        "trivial", ["cat", "dog"], True, save_path
    )

    # Check that the linear layers are equal (the 2nd element in the Sequential).
    assert torch.equal(
        trivial_classifier.model.layers[1].weight,
        trivial_classifier_loaded.model.layers[1].weight,
    )


def test_predict():
    torch.manual_seed(0)

    # Instantiate a trivial classifier.
    trivial_classifier = classifiers.TransferLearningVisionClassifier(
        "trivial", ["A380", "Boeing 747", "DC-8"], False
    )

    # Make a random image.
    np.random.seed(0)
    img = PIL.Image.fromarray(np.uint8(255 * np.random.rand(300, 300, 3)))

    # Now make a prediction.
    pred = trivial_classifier.predict(img, custom_predict_transform=None)

    # Get the prediction probability for A380 and check it matches.
    pred_prob_A380_expected = 0.2670742869377136
    pred_prob_A380 = pred[0]["A380"]
    assert np.isclose(pred_prob_A380_expected, pred_prob_A380)
