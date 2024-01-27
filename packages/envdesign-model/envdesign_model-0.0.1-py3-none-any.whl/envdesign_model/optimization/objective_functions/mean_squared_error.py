# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from copy import deepcopy
from envdesign_model.optimization.optimization_utils import sort_tuple


class MSE:
    def __init__(self, target_values, weight, normalize):
        self.target_values = target_values
        self.weight = weight
        self.normalize = normalize
        if self.normalize:
            self.target_values = self.normalize_values(target_values)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        elif self.target_values != other.target_values:
            return False
        elif self.weight != other.weight:
            return False
        elif self.normalize != other.normalize:
            return False
        return True

    def __str__(self):
        return 'MSE object - target values: '\
            + f'{self.target_values}, weight: {self.weight}, '\
            + f'normalize values: {self.normalize}'

    def normalize_values(self, values_dict):
        normalized_dict = dict()
        values_sum = sum(values_dict.values())
        # to prevent divide by 0 errors
        norm_const = 1 if values_sum == 0 else values_sum
        for key, value in values_dict.items():
            normalized_dict[key] = value / norm_const
        return normalized_dict

    def compute(self, true_values_dict, default_value=0):
        # reconcile dictionaries
        target_values_dict, true_values_dict = self.reconcile_dicts(
            true_values_dict, default_value)
        
        # normalize values
        if self.normalize:
            target_values_dict = self.normalize_values(target_values_dict)
            true_values_dict = self.normalize_values(true_values_dict)

        # compute mean squared error
        mse = 0
        for target_key, target_val in target_values_dict.items():
            true_val = true_values_dict[target_key]
            mse += ((true_val - target_val) ** 2) / len(
                target_values_dict)
        return mse * self.weight

    def reconcile_dicts(self, true_values_dict, default_value):
        # if default value is None, check that key sets are equal
        target_values_dict = deepcopy(self.target_values)
        if default_value is None:
            if true_values_dict.keys() != target_values_dict.keys():
                raise Exception(
                    'Dictionary of target values and dictionary '
                    + 'of true values have different key sets')
        else:
            # add keys in true values dictionary that are not present in 
            # target values dictionary
            for key in true_values_dict.keys():
                if key not in target_values_dict.keys():
                    target_values_dict[key] = default_value
            # add keys in target values dictionary that are not present in
            # true values dictionary
            for key in target_values_dict.keys():
                if key not in true_values_dict.keys():
                    true_values_dict[key] = default_value
        if self.normalize:
            target_values_dict = self.normalize_values(
                target_values_dict)
            true_values_dict = self.normalize_values(
                true_values_dict)
        return target_values_dict, true_values_dict


class DimensionMSE(MSE):
    def __init__(self, target_values, weight=1, normalize=True):
        super().__init__(target_values, weight, normalize)


def _process_values_dict(values):
    # sort keys in target values dictionary, take sums of values with
    # the same key
    new_values = dict()
    for key, value in values.items():
        new_key = sort_tuple(key)
        if new_key in new_values.keys():
            new_value = new_values[new_key] + value
        else:
            new_value = value
        new_values[new_key] = new_value
    return new_values


class RelationshipMSE(MSE):
    def __init__(self, target_values, weight=1, normalize=True):
        new_target_values = _process_values_dict(target_values)
        super().__init__(new_target_values, weight, normalize)

    def compute(self, true_values, default_value=0):
        new_true_values = _process_values_dict(true_values)
        return super().compute(new_true_values, default_value)


class CombinationMSE(MSE):
    def __init__(self, target_values, normalize=True):
        new_target_values = _process_values_dict(target_values)
        super().__init__(new_target_values, 1, normalize)

    def compute(self, true_values, default_value=0):
        new_true_values = _process_values_dict(true_values)
        return super().compute(new_true_values, default_value)
