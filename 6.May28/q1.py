people = []


def my_function(name, age):
    for i in range(8):
        j = {}
        j.update({"name": name[i]})
        j.update({"age": age[i]})
        people.append(j)
    print(people)


names = ["alan", "john", "tania", "ahmad", "ali", "muddassar", "raheel", "hamza"]
ages = [12, 13, 14, 15, 17, 16, 13, 13]
my_function(names, ages)
