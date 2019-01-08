desserts = ["ice cream", "cookies"]

desserts.sort()

print(desserts)

print(desserts.index("ice cream"))

food = desserts[:]

food.extend(["broccoli", "turnips"])

print(desserts)
print(food)

food.remove("cookies")
print(food[0:2])

breakfast = "cookies, cookies, cookies".split(", ")
print(breakfast)
