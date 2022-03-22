from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    unique_job_types = []
    for job in file:
        unique_job_types.append(job["job_type"])
    return set(unique_job_types)


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    file = read(path)
    unique_industries = []
    for industry in file:
        if industry["industry"]:
            unique_industries.append(industry["industry"])
    return set(unique_industries)


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)
    return filtered_industries


def get_max_salary(path):
    file = read(path)
    max_salary = []
    for salary in file:
        if salary["max_salary"].isdigit():
            max_salary.append(float(salary["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    file = read(path)
    min_salary = []
    for salary in file:
        if salary["min_salary"].isdigit():
            min_salary.append(float(salary["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    try:
        if job["min_salary"] <= int(salary) <= job["max_salary"]:
            return True
        elif job["min_salary"] > job["max_salary"]:
            raise ValueError
        else:
            return False
    except(TypeError, KeyError):
        raise ValueError


# referência: para o 'raise' (a forma python de mandar um throw)
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
# referência para o erro 'do not use bare except'
# https://www.flake8rules.com/rules/E722.html


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
