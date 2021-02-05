"""
Using Parametrization
"""
from datetime import datetime

from parametrization import Parametrization

from code_resources import extract_year


@Parametrization.autodetect_parameters()
@Parametrization.default_parameters(
    expected_year=2020
)
@Parametrization.case(
    name='got_datetime_with_year_2020__should_return_2020',
    value_to_extract_year_from=datetime(2020, 2, 10),
)
@Parametrization.case(
    name='got_number_2019__should_return_2019',
    value_to_extract_year_from=2019,
    expected_year=2019,
)
@Parametrization.autodetect_parameters()
@Parametrization.case(name='s', a=2)
@Parametrization.case(name='s', a=3)
def test_extract_year(value_to_extract_year_from, expected_year, a):
    ###
    actual_year = extract_year(value_to_extract_year_from)
    ###
    assert actual_year == expected_year
