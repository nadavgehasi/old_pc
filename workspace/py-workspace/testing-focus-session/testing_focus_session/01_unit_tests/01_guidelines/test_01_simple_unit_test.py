"""
Simple Unit-Test
* Using name pattern: test_action_name__state_under_test__expected_behavior
* Splitting to A3: Arrange, Act, Assert
* Wrap acting part with triple # to make it easier to find
"""
from datetime import datetime

from code_resources import extract_year


def test_extract_year__got_datetime_with_year_2020__should_return_2020():
    expected_year = 2020

    ###
    actual_year = extract_year(datetime(expected_year, 2, 10))
    ###

    assert actual_year == expected_year
