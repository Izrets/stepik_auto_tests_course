import selenium


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {}, got {actual_result}"
test_input_text(11, 1)