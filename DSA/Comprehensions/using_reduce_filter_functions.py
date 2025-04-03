from functools import reduce


employees_dict = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 28, "salary": 55000},
    {"name": "David", "age": 24, "salary": 70000}
]

sum_of_squares = reduce(lambda x, y: x + y, [emp["salary"] ** 2 for emp in filter(lambda item: item["age"] > 26, employees_dict)], 0)


print("Sum of squares of salaries:", sum_of_squares)
