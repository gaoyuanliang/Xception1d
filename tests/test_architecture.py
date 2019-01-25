from unittest import TestCase
import torch
from torch import nn

import numpy as np

from src.architecture import XceptionArchitecture1d


class TestXceptionArchitecture1d(TestCase):
    def setUp(self):
        self.n_classes = 32
        self.batch_size = 16
        self.x = torch.rand(self.batch_size, 1, 16000)
        self.y = torch.from_numpy(np.random.choice(range(self.n_classes), self.batch_size))
        self.model = XceptionArchitecture1d(n_classes=self.n_classes)

    def tearDown(self):
        pass

    def test_forward_pass_shape(self):
        y_hat = self.model.forward(self.x)
        self.assertEqual(y_hat.shape, (self.batch_size, self.n_classes))

    def test_loss(self):
        loss = self.model.calculate_loss(self.x, self.y)
        self.assertGreater(loss, 0)

    def test_gradient_check(self):
        loss_0 = self.model.step(self.x, self.y)
        loss_1 = self.model.calculate_loss(self.x, self.y)
        self.assertGreater(loss_0, loss_1)