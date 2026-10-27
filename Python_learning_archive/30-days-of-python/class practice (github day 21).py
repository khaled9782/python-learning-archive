# class Person:
#     def __init__(self, fname, lname,  age, salary):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.salary = salary

#     def full_name(self):
#         return f"{self.fname} {self.lname}"


# p1 = Person("khaled", "Abdul", 20, 250)
# p1.salary = 300
# print(p1.salary)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        """" returns the number of items in the list"""
        return len(self.data)

    def sum(self):
        """" returns the sum of numbers in the list"""
        return sum(self.data)

    def min(self):
        """" returns the lowest number in the list"""
        return min(self.data)

    def max(self):
        """" returns the highest number in the list"""
        return max(self.data)

    def range(self):
        """" returns the range of the list"""
        return self.max() - self.min()

    def mean(self):
        """" returns the Mean of the list to the nearest integer"""
        return round(self.sum()/self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n//2
        if n % 2 == 0:
            return (sorted_data[mid-1]+sorted_data[mid])/2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = {}
        for value in self.data:
            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1
        max_freq = 0
        for v in freq:
            if freq[v] > max_freq:
                max_freq = freq[v]
        modes = []
        for value, count in freq.items():
            if count == max_freq:
                modes.append(value)
        if len(modes) == 1:
            return f"Mode: {modes[0]}, Count: {max_freq}"
        else:
            return f"Modes: {modes}, Count: {max_freq}"


stats = Statistics(ages)

print("Count:", Statistics.count(stats))
print("Sum:", Statistics.sum(stats))
print("Min:", Statistics.min(stats))
print("Max:", Statistics.max(stats))
print("Range:", Statistics.range(stats))
print("Mean:", Statistics.mean(stats))
print("Median:", Statistics.median(stats))
print("Mode:", Statistics.mode(stats))
