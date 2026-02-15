employees = {
    "John": 30000,
    "Emma": 35000,
    "Alex": 40000
}

employees["David"] = 28000
employees["Emma"] = 38000
del employees["John"]

for name in employees:
    print(name, ":", employees[name])
