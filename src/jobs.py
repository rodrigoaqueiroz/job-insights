from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        data = list(csv.DictReader(file, delimiter=",", quotechar='"'))
    return data


# if __name__ == "__main__":
#     path = './src/jobs.csv'
#     for argument in read(path):
#         # print(read(path))
