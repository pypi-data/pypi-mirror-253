# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.utils import get_logger


class OptimizationStrategy():
    def __init__(self, opt_params, logger=None):
        self.opt_params = opt_params
        if logger is None:
            self.logger = get_logger()
        else:
            self.logger = logger

    def process():
        raise NotImplementedError('OptimizationStrategy instance must have '
                                  + 'process() method implemented by '
                                  + 'subclass')
