x = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
opposite = {}

for key in x:
    value = x[key]
    opposite[value] = key

print("Original Dictionary:", x)
print("Opposite Mapping:", opposite)