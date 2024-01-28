import unittest
import math
import numpy as np
from EDCR_pipeline import run_EDCR_pipeline, load_priors
from vit_pipeline import get_and_print_metrics

class Test_before_edcr(unittest.TestCase):

    def setUp(self):
        fine_prediction = np.load("src/metacognitive_error_detection_and_correction_v2/combined_results/vit_b_16_BCE_test_fine_pred_lr0.0001_e19.npy")
        coarse_prediction = np.load("src/metacognitive_error_detection_and_correction_v2/combined_results/vit_b_16_BCE_test_coarse_pred_lr0.0001_e19.npy")
        self.test_fine_accuracy, \
        self.test_coarse_accuracy = get_and_print_metrics(fine_prediction,
                                                       coarse_prediction,
                                                       loss="BCE",
                                                       model_name="vit_b_16",
                                                       lr=1e-04)

    def test_fine_accuracy(self):
        self.assertTrue(math.fabs(self.test_fine_accuracy - 68.97 / 100) < 0.5, 'The accuracy for fine grain is wrong.')

    def test_coarse_accuracy(self):
        self.assertTrue(math.fabs(self.test_coarse_accuracy - 84.27 / 100) < 0.5, 'The accuracy for coarse grain is wrong.')

    
if __name__ == '__main__':
    unittest.main()