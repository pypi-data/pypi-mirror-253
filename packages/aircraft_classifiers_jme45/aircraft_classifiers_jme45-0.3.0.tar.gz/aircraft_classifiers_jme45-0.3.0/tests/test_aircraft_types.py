"""
Test aircraft types, in particular the function for implementing the target transform
"""

from aircraft_classifiers_jme45 import aircraft_types as act


def test_TEST_subset():
    assert act.AIRCRAFT_SUBSETS["TEST"] == ["A380", "Boeing 747", "DC-8"]


def test_target_transform():
    target_transform = act.TargetTransform("TEST")

    # The aircraft here are "A380", "Boeing 747", "DC-8". Get the index for each of
    # them and check that these match to 0, 1, 2.
    for i, aircraft_name in enumerate(act.AIRCRAFT_SUBSETS["TEST"]):
        idx_in_full_set = act.AIRCRAFT_SUBSETS["ALL_AIRCRAFT"].index(aircraft_name)
        assert target_transform(idx_in_full_set) == i
