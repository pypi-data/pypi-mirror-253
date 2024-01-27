# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from envdesign_model.envdesign_model_main import run_envdesign_model


def test_envdesign_model():
    SCOPE_DFS = [
        None,
        pd.DataFrame({
            'Property': [
                'Hardware',
                'Hardware'
            ],
            'Value': [
                'HW1',
                'HW2'
            ],
            'Status': [
                'Include',
                'Include'
            ]
        }),
        pd.DataFrame({
            'Property': [
                'Virtual_Machine'
            ],
            'Value': [
                'VM2'
            ],
            'Status': [
                'Exclude'
            ]
        }),
        pd.DataFrame({
            'Property': [
                'Hardware',
                'Hardware',
                'Workload'
            ],
            'Value': [
                'HW1',
                'HW2',
                'WL4'
            ],
            'Status': [
                'Include',
                'Include',
                'Exclude'
            ]
        })
    ]
    dimension_dicts = [
        {
            'name': 'Hardware',
            'value': 'Hardware_Model',
            'df': pd.DataFrame({
                'Hardware_Model': [
                    'HW1',
                    'HW2',
                    'HW3',
                    'HW4'
                ],
                'Score': [
                    0.25,
                    0.25,
                    0.25,
                    0.25
                ]
            })
        },
        {
            'name': 'Hypervisor',
            'value': 'HyperV',
            'df': pd.DataFrame({
                'HyperV': [
                    'HV1',
                    'HV2',
                ],
                'Score': [
                    1,
                    1
                ]
            })
        },
        {
            'name': 'Virtual_Machine',
            'value': 'Vm_Type',
            'df': pd.DataFrame({
                'Vm_Type': [
                    'VM1',
                    'VM2',
                    'VM3'
                ],
                'Score': [
                    0.25,
                    0.5,
                    0.25
                ]
            })
        },
        {
            'name': 'Workload',
            'value': 'Workload',
            'df': pd.DataFrame({
                'Workload': [
                    'WL1',
                    'WL2',
                    'WL3',
                    'WL4'
                ],
                'Score': [
                    1,
                    1,
                    1,
                    1
                ]
            })
        }
    ]
    relationships_df = pd.DataFrame([
        # HW - VM relationships
        {
            'Dimension1': 'Virtual_Machine',
            'Value1': 'VM1',
            'Dimension2': 'Hardware',
            'Value2': 'HW1',
            'Score': 1,
            'RelationshipMetaData': [{'name': 'Many_To_One', 'value': 6}]
        },
        {
            'Dimension1': 'Hardware',
            'Value1': 'HW2',
            'Dimension2': 'Virtual_Machine',
            'Value2': 'VM2',
            'Score': 1,
            'RelationshipMetaData': [{'name': 'One_To_Many', 'value': 9}]
        },
        {
            'Dimension1': 'Virtual_Machine',
            'Value1': 'VM2',
            'Dimension2': 'Hardware',
            'Value2': 'HW3',
            'Score': 1,
            'RelationshipMetaData': [{'name': 'Many_To_One', 'value': 9}]
        },
        {
            'Dimension1': 'Hardware',
            'Value1': 'HW4',
            'Dimension2': 'Virtual_Machine',
            'Value2': 'VM3',
            'Score': 1,
            'RelationshipMetaData': [{'name': 'One_To_Many', 'value': 6}]
        },
        # VM - Workload relationships
        {
            'Dimension1': 'Workload',
            'Value1': 'WL1',
            'Dimension2': 'Virtual_Machine',
            'Value2': 'VM1',
            'Score': 1,
            'RelationshipMetaData': [{'name': 'Many_To_One', 'value': 2}]
        },
        {
            'Dimension1': 'Virtual_Machine',
            'Value1': 'VM2',
            'Dimension2': 'Workload',
            'Value2': 'WL2',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Virtual_Machine',
            'Value1': 'VM2',
            'Dimension2': 'Workload',
            'Value2': 'WL3',
            'Score': 1,
            'RelationshipMetaData': [{'name': 'One_To_Many', 'value': 3}]
        },
        {
            'Dimension1': 'Virtual_Machine',
            'Value1': 'VM3',
            'Dimension2': 'Workload',
            'Value2': 'WL4',
            'Score': 1,
            'RelationshipMetaData': []
        },
        # HW - Workload relationships
        {
            'Dimension1': 'Hardware',
            'Value1': 'HW1',
            'Dimension2': 'Workload',
            'Value2': 'WL1',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hardware',
            'Value1': 'HW2',
            'Dimension2': 'Workload',
            'Value2': 'WL2',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hardware',
            'Value1': 'HW3',
            'Dimension2': 'Workload',
            'Value2': 'WL3',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hardware',
            'Value1': 'HW4',
            'Dimension2': 'Workload',
            'Value2': 'WL4',
            'Score': 1,
            'RelationshipMetaData': []
        },
        # Hypervisor - HW relationships
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV2',
            'Dimension2': 'Hardware',
            'Value2': 'HW1',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': '<ANY>',
            'Dimension2': 'Hardware',
            'Value2': 'HW2',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': '<ANY>',
            'Dimension2': 'Hardware',
            'Value2': 'HW3',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': '<ANY>',
            'Dimension2': 'Hardware',
            'Value2': 'HW4',
            'Score': 1,
            'RelationshipMetaData': []
        },
        # Hypervisor - VM relationships
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV2',
            'Dimension2': 'Virtual_Machine',
            'Value2': 'VM1',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV1',
            'Dimension2': 'Virtual_Machine',
            'Value2': 'VM2',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV1',
            'Dimension2': 'Virtual_Machine',
            'Value2': 'VM3',
            'Score': 1,
            'RelationshipMetaData': []
        },
        # Hypervisor - WL relationships
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV2',
            'Dimension2': 'Workload',
            'Value2': 'WL1',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV1',
            'Dimension2': 'Workload',
            'Value2': 'WL2',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': '<ANY>',
            'Dimension2': 'Workload',
            'Value2': 'WL3',
            'Score': 1,
            'RelationshipMetaData': []
        },
        {
            'Dimension1': 'Hypervisor',
            'Value1': 'HV1',
            'Dimension2': 'Workload',
            'Value2': 'WL4',
            'Score': 1,
            'RelationshipMetaData': []
        },
    ])
    num_groups = 100
    obj_func_dim = {
        'type': 'dimension',
        'specifics': [
            {
                'name': 'Hardware',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.3,
            },
            {
                'name': 'Hypervisor',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.1,
            },
            {
                'name': 'Virtual_Machine',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.3,
            },
            {
                'name': 'Workload',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.3,
            }
        ]
    }
    obj_func_rel = {
        'type': 'relationship',
        'specifics': [
            {
                'dimension1': 'Hardware',
                'dimension2': 'Virtual_Machine',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.10,
            },
            {
                'dimension1': 'Hardware',
                'dimension2': 'Workload',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.10,
            },
            {
                'dimension1': 'Hardware',
                'dimension2': 'Hypervisor',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.10,
            },
            {
                'dimension1': 'Virtual_Machine',
                'dimension2': 'Workload',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.10,
            },
            {
                'dimension1': 'Virtual_Machine',
                'dimension2': 'Hypervisor',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.10,
            },
            {
                'dimension1': 'Workload',
                'dimension2': 'Hypervisor',
                'objective_function': 'mse',
                'metric': 'Score',
                'weight': 0.10,
            }
        ]
    }
    obj_func_comb = {
        'type': 'combination',
        'specifics': [{
            'combinations': [
                {
                    'combination': [
                        {
                            'dimension': 'Hardware',
                            'value': 'HW1'
                        },
                        {
                            'dimension': 'Hypervisor',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Virtual_Machine',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Workload',
                            'value': '<ANY>'
                        },
                    ],
                    'metric_values': [
                        {
                            'name': 'Score',
                            'value': 1
                        }
                    ]
                },
                {
                    'combination': [
                        {
                            'dimension': 'Hardware',
                            'value': 'HW2'
                        },
                        {
                            'dimension': 'Hypervisor',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Virtual_Machine',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Workload',
                            'value': '<ANY>'
                        },
                    ],
                    'metric_values': [
                        {
                            'name': 'Score',
                            'value': 1
                        }
                    ]
                },
                {
                    'combination': [
                        {
                            'dimension': 'Hardware',
                            'value': 'HW3'
                        },
                        {
                            'dimension': 'Hypervisor',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Virtual_Machine',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Workload',
                            'value': '<ANY>'
                        },
                    ],
                    'metric_values': [
                        {
                            'name': 'Score',
                            'value': 1
                        }
                    ]
                },
                {
                    'combination': [
                        {
                            'dimension': 'Hardware',
                            'value': 'HW4'
                        },
                        {
                            'dimension': 'Hypervisor',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Virtual_Machine',
                            'value': '<ANY>'
                        },
                        {
                            'dimension': 'Workload',
                            'value': '<ANY>'
                        },
                    ],
                    'metric_values': [
                        {
                            'name': 'Score',
                            'value': 1
                        }
                    ]
                },
            ],
            'metric': 'Score',
            'objective_function': 'mse'
        }]
    }
    # input is validated, graph is created and validated, schedules are
    # created using each optimization strategy, each output (schedules)
    # is postprocessed and validated
    TEST_CASES = [
        (dimension_dicts, relationships_df, num_groups, obj_func_dim),
        (dimension_dicts, relationships_df, num_groups, obj_func_rel),
        (dimension_dicts, relationships_df, num_groups, obj_func_comb)
    ]
    OPTMIZATION_STRATEGY_CHOICES = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
    for test_case in TEST_CASES:
        dimension_dicts, relationships_df, num_groups,\
            objective_function = test_case
        for scope_df in SCOPE_DFS:
            for opt_strategy in OPTMIZATION_STRATEGY_CHOICES:
                run_envdesign_model(
                    dimension_dicts, relationships_df, num_groups,
                    objective_function, scope_df, max_dim_size=10,
                    opt_strategy=opt_strategy, opt_time_limit=8,
                    group_tag='Node', cont_train=False)
