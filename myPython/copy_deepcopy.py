import copy

# original list containing a nested list
org_list = [1, 2, [3, 4]]

# shallow copy
shallow_copy_list = copy.copy(org_list)

# deep copy
deep_copy_list = copy.deepcopy(org_list)

print(f"Original: {org_list}")
print(f"Shallow Copy: {shallow_copy_list}")
print(f"Deep Copy: {deep_copy_list}")

shallow_copy_list[2][0] = 99

print("\nAfter modifying Shallow copy's nested list:")
print(f"Original: {org_list}")
print(f"Shallow Copy: {shallow_copy_list}")

deep_copy_list[2][1] = 88

print("\nAfter modifying Deep copy's nested list:")
print(f"Original: {org_list}")
print(f"Deep Copy: {deep_copy_list}")

# print original list again.
print("print the original again: ")
print("-----------------")
print(org_list[0])
print(org_list[1])
print(org_list[2][0])    # this is same as shallow_copy_list[2][0]?
print(org_list[2][1])    # this is same as deep_copy_list[2][2]?
print("-----------------")
print("Try the shallow copy list and deep copy list: ")
print(shallow_copy_list[2][0]) # this is same as shallow_copy_list[2][0]?
print(deep_copy_list[2][1])    # this is same as deep_copy_list[2][2]?
