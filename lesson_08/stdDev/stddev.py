
class Person:
    def __init__(self, name, age): 
        self._name = name
        self._age =age
    
    def get_age(self):
        return self._age
    
def std_dev(list_of_person_objects):
    total = 0
    for person in list_of_person_objects:
        total += person.get_age()
    mean_of_ages = total / len(list_of_person_objects)
    list_of_results = []
    for person in list_of_person_objects:
        new_results = (person.get_age() - mean_of_ages) ** 2
        list_of_results.append(new_results)
    total_mean = 0
    for result in list_of_results:
        total_mean += result
    variance = total_mean / len(list_of_results)
    std = variance ** 0.5
    return std

p1 = Person('donnie', 73)
p2 = Person('Natlie', 24)
p3 = Person('rey', 48)
person_list = [p1,p2,p3]
answer = std_dev(person_list)
print(answer)