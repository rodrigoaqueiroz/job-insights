from src.sorting import sort_by

criteria = ["min_salary", "max_salary", "date_posted"]

jobs = [
        {"min_salary": 44587, "max_salary": 82162,
            "date_posted": "2020-05-08"},
        {"min_salary": 46298, "max_salary": 55893,
            "date_posted": "2020-05-01"},
        {"min_salary": 94715, "max_salary": 103279,
            "date_posted": "2020-05-05"},
        ]
mock_min_salary = [
        {"min_salary": 44587, "max_salary": 82162,
            "date_posted": "2020-05-08"},
        {"min_salary": 46298, "max_salary": 55893,
            "date_posted": "2020-05-01"},
        {"min_salary": 94715, "max_salary": 103279,
            "date_posted": "2020-05-05"},
        ]
mock_max_salary = [
        {"min_salary": 94715, "max_salary": 103279,
            "date_posted": "2020-05-05"},
        {"min_salary": 44587, "max_salary": 82162,
            "date_posted": "2020-05-08"},
        {"min_salary": 46298, "max_salary": 55893,
            "date_posted": "2020-05-01"},
        ]
mock_date_posted = [
        {"min_salary": 44587, "max_salary": 82162,
            "date_posted": "2020-05-08"},
        {"min_salary": 94715, "max_salary": 103279,
            "date_posted": "2020-05-05"},
        {"min_salary": 46298, "max_salary": 55893,
            "date_posted": "2020-05-01"},
        ]

function_mappings = {
    "min_salary": mock_min_salary,
    "max_salary": mock_max_salary,
    "date_posted": mock_date_posted,
}
# Referência:
# https://stackoverflow.com/questions/7719466/
# i-have-a-string-whose-content-is-a-function-name-how-to-refer-to-the-correspond


def test_sort_by_criteria():
    for test in criteria:
        sort_by(jobs, test)
        assert jobs == function_mappings[test]

# other way to do.
# def test_sort_by_criteria():
#     for test in criteria:
#         sort_by(jobs, test)
#         assert jobs == eval(f'mock_{test}')
