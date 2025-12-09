from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value, number_of_parts, sum_of_the_parts",
    [
        (8, 2, 8),
        (11, 3, 11)
    ],
    ids=[
        "value: 8, number_of_parts: 2",
        "value: 11, number_of_parts: 3"
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int,
    sum_of_the_parts: int
) -> None:
    assert (
        sum(split_integer(value, number_of_parts)) == sum_of_the_parts
    ), f"Sum of all parts should be equal to {sum_of_the_parts}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    pass


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    pass


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    pass


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    pass
