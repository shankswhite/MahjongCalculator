from collections import defaultdict

# Given list of tuples
tuples_list = [(63,1), (63,4), (63,7), (64,1), (64,4), (64,7)]

# Convert list of tuples to dictionary format as requested
result_dict = defaultdict(list)
for k, v in tuples_list:
    result_dict[k].append(v)

# Convert defaultdict to regular dict if needed
result_dict = dict(result_dict)

print([1,2] + [3,4])
