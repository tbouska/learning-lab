numbers = range(1_000_000)
print(sum(n ** 2 for n in numbers))

# replaces the following list comprehension
print(sum([n ** 2 for n in numbers]))
