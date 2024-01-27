# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE, CombinationMSE
from copy import deepcopy
from tests.utils import check_exception


MOCK_VALUES_DIM_MSE = [
    {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25},
    {0: 0.2, 1: 0.3, 2: 0.2, 3: 0.3},
    {0: 0.3, 1: 0.3, 2: 0.4},
    {0: 0, 1: 0, 2: 0},
]
MOCK_VALUES_REL_MSE = [
    {(2, 4): 0.5, (3, 5): 0.5},
    {(2, 4): 0.4, (2, 5): 0.2, (3, 5): 0.4},
    {(2, 4): 0, (3, 5): 0},
]
MOCK_VALUES_COMB_MSE = [
    {(0, 2, 4): 0.5, (1, 3, 5): 0.5},
    {(0, 2, 4): 0.3, (1, 3, 5): 0.3, (1, 3, 4): 0.4},
    {(0, 2, 4): 0, (1, 3, 5): 0, (1, 3, 4): 0}
]
MOCK_DIMENSION_MSES = [
    DimensionMSE(MOCK_VALUES_DIM_MSE[0], 0.5, True),
    DimensionMSE(MOCK_VALUES_DIM_MSE[1], 1, False),
    DimensionMSE(MOCK_VALUES_DIM_MSE[3], 1, True),
]
MOCK_RELATIONSHIP_MSES = [
    RelationshipMSE(MOCK_VALUES_REL_MSE[0], 0.5, True),
    RelationshipMSE(MOCK_VALUES_REL_MSE[1], 1, False),
    RelationshipMSE(MOCK_VALUES_REL_MSE[2], 1, True)
]
MOCK_COMBINATION_MSES = [
    CombinationMSE(MOCK_VALUES_COMB_MSE[0], True),
    CombinationMSE(MOCK_VALUES_COMB_MSE[1], False),
    CombinationMSE(MOCK_VALUES_COMB_MSE[2], True)
]


def test_mse_equality():
    # test case: tuple(DimensionMSE object, DimensionMSE object, boolean for
    # equality)
    TEST_CASES = [
        (MOCK_DIMENSION_MSES[0], deepcopy(MOCK_DIMENSION_MSES[0]), True),
        (MOCK_DIMENSION_MSES[0], MOCK_DIMENSION_MSES[1], False),
        (MOCK_RELATIONSHIP_MSES[0], deepcopy(MOCK_RELATIONSHIP_MSES[0]), True),
        (MOCK_RELATIONSHIP_MSES[0], MOCK_RELATIONSHIP_MSES[1], False),
        (MOCK_COMBINATION_MSES[0], deepcopy(MOCK_COMBINATION_MSES[0]), True),
        (MOCK_COMBINATION_MSES[0], MOCK_COMBINATION_MSES[1], False)
    ]
    for test_case in TEST_CASES:
        dim_mse1, dim_mse2, equal = test_case
        assert (dim_mse1 == dim_mse2) == equal, 'Incorrect value for '\
            + f'{dim_mse1} == {dim_mse2}. Expected: {equal}, Actual: '\
            + f'{dim_mse1 == dim_mse2}'


def test_normalize():
    # test case: tuple(targets, expected normalized targets)
    TEST_CASES = [
        (MOCK_VALUES_DIM_MSE[0], MOCK_VALUES_DIM_MSE[0]),
        ({0: 2, 1: 3, 2: 2, 3: 3}, MOCK_VALUES_DIM_MSE[1]),
        (MOCK_VALUES_REL_MSE[0], MOCK_VALUES_REL_MSE[0]),
        ({(2, 4): 4, (2, 5): 2, (3, 5): 4}, MOCK_VALUES_REL_MSE[1]),
        (MOCK_VALUES_COMB_MSE[0], MOCK_VALUES_COMB_MSE[0]),
        ({(0, 2, 4): 3, (1, 3, 5): 3, (1, 3, 4): 4}, MOCK_VALUES_COMB_MSE[1])
    ]
    for test_case in TEST_CASES:
        targets, normalized_targets = test_case
        dim_mse = DimensionMSE(targets, normalize=True)
        assert dim_mse.target_values == normalized_targets, 'Incorrect '\
            + 'normalization of target values. Expected: '\
            + f'{normalized_targets}, Actual: {dim_mse.target_values}'


def test_reconcile_dicts():
    # test case: tuple(MSE object, true values dict, default value)
    TEST_CASES = [
        (MOCK_DIMENSION_MSES[0], {0: 0.25, 1: 0.25, 2: 0.25}, 0),
        (MOCK_DIMENSION_MSES[1], {0: 0.2, 1: 0.3, 2: 0.2, 4: 0.3}, 0),
        (MOCK_RELATIONSHIP_MSES[0], {(2, 4): 0.5, (3, 5): 0.5, (1, 4): 1}, 0),
        (MOCK_RELATIONSHIP_MSES[1], {(2, 4): 0.4, (2, 5): 0.2}, 0),
        (MOCK_COMBINATION_MSES[0],
         {(0, 2, 4): 0.3, (1, 3, 5): 0.3, (1, 3, 4): 0.4}, 0),
        (MOCK_COMBINATION_MSES[1], {(0, 2, 4): 0.5, (1, 3, 5): 0.5}, 0)
    ]
    for case in TEST_CASES:
        mse_obj, true_values_dict, default_value = case
        orig_target_keys = set(mse_obj.target_values.keys())
        orig_true_keys = set(true_values_dict.keys())
        target_values, true_values = mse_obj.reconcile_dicts(
            true_values_dict, default_value)
        new_target_keys = set(target_values.keys())
        new_true_keys = set(true_values.keys())

        # check that keys of each dictionary are preserved
        if isinstance(mse_obj, RelationshipMSE):
            sorted_orig_target_keys = set(map(lambda k: tuple(sorted(k)),
                                            orig_target_keys))
            assert len(
                sorted_orig_target_keys.difference(new_target_keys)) == 0,\
                'Original key of target value dictionary not preserved in '\
                + 'reconciled target values dictionary'
            sorted_orig_true_keys = set(map(lambda k: tuple(sorted(k)),
                                            orig_target_keys))
            assert len(
                sorted_orig_true_keys.difference(new_true_keys)) == 0,\
                'Original key of true value dictionary not preserved in '\
                + 'reconciled true values dictionary'

        # check that key sets are equal
        assert new_target_keys == new_true_keys,\
            'Key sets of target and true values dictionaries after '\
            + 'reconciliation are not equal. Target keys: '\
            + f'{new_target_keys}. True keys: {new_true_keys}'
    
        # check default values for keys in target values dict but not in
        # true values dict
        for target_key in orig_target_keys:
            # get original and new target keys
            orig_target_key = target_key
            if type(target_key) is tuple:
                new_target_key = tuple(sorted(target_key))
            else:
                new_target_key = target_key
            assert new_target_key in new_target_keys, f'Key {new_target_key}'\
                + ' not present in true values dictionary'

            orig_key_present = orig_target_key in orig_true_keys
            new_key_present = new_target_key in orig_true_keys
            if not orig_key_present and not new_key_present:
                assert new_target_key in new_true_keys, 'Key '\
                    + f'{new_target_key} present in target values '\
                    + f'dictionary but not present in true values '\
                    + 'dictionary'
                assert true_values[new_target_key] == default_value, 'Value '\
                    + f'for key {new_target_key} in true values dictionary '\
                    + f'expected to be default value {default_value}, '\
                    + f'instead it is {true_values[new_target_key]}'
        
        # check default values for keys in true values dict but not in
        # target values dict
        for true_key in orig_true_keys:
            # get original and new true keys
            orig_true_key = true_key
            if type(true_key) is tuple:
                new_true_key = tuple(sorted(true_key))
            else:
                new_true_key = true_key
            assert new_true_key in new_true_keys, f'Key {new_true_key}'\
                + ' not present in true values dictionary'
            
            orig_key_present = orig_true_key in orig_target_keys
            new_key_present = new_true_key in orig_target_keys
            if not orig_key_present and not new_key_present:
                assert new_true_key in target_values.keys(), 'Key '\
                    + f'{new_true_key} present in true values '\
                    + 'dictionary but not present in target values '\
                    + 'dictionary'
                assert target_values[new_true_key] == default_value, 'Value '\
                    + f'for key {new_true_key} in target values dictionary '\
                    + f'expected to be default value {default_value}, '\
                    + f'instead it is {target_values[new_true_key]}'


def test_compute():
    # test case tuple(MSE object, default value, expected MSE)
    PASS_CASES = [
        (MOCK_DIMENSION_MSES[0], MOCK_VALUES_DIM_MSE[0], 0, 0),
        (MOCK_DIMENSION_MSES[0], MOCK_VALUES_DIM_MSE[1], 0, 0.00125),
        (MOCK_RELATIONSHIP_MSES[0], MOCK_VALUES_REL_MSE[0], 0, 0),
        (MOCK_RELATIONSHIP_MSES[1], MOCK_VALUES_REL_MSE[0], 0, 0.02),
        (MOCK_COMBINATION_MSES[0], MOCK_VALUES_COMB_MSE[0], 0, 0),
        (MOCK_COMBINATION_MSES[0], MOCK_VALUES_COMB_MSE[1], 0, 0.08),
        (MOCK_DIMENSION_MSES[2], MOCK_VALUES_DIM_MSE[1], 0, 0.065),
        (MOCK_RELATIONSHIP_MSES[2], MOCK_VALUES_REL_MSE[0], 0, 0.25),
        (MOCK_COMBINATION_MSES[2], MOCK_VALUES_COMB_MSE[0], 0, 0.16667),
    ]
    FAIL_CASES = [
        (MOCK_DIMENSION_MSES[1], MOCK_VALUES_DIM_MSE[2], None, 0.14
         # expect Exception because no default value provided and dict
         # keys differ between target values dict and true values dict
         ),
        (MOCK_RELATIONSHIP_MSES[0], MOCK_VALUES_REL_MSE[1], None, 0.02
         # expect Exception because no default value provided and dict
         # keys differ between target values dict and true values dict
         ),
        (MOCK_COMBINATION_MSES[0], MOCK_VALUES_COMB_MSE[1], None, 0.08
         # expect Exception because no default value provided and dict
         # keys differ between target values dict and true values dict
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            try:
                mse_obj, true_values, default_val, expected_mse = test_case
                mse = mse_obj.compute(true_values, default_val)
                threshold = 1e-4
                assert abs(mse - expected_mse) < threshold, 'Incorrect '\
                    + 'computed MSE value. Expected: value within '\
                    + f'{threshold} of {expected_mse}. Actual: {mse}'
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)
