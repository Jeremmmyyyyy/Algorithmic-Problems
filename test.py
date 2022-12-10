list_of_tuples = [(5, 'Alice'), (10, 'Bob'), (15, 'Carl'), (20, 'Dean'), (21, 'Dean')]

# 👇️ [(0, (5, 'Alice')), (1, (10, 'Bob')), (2, (15, 'Carl')), (3, (20, 'Dean'))]
print(list(enumerate(list_of_tuples)))

# ✅ get list of all indices of tuples that match the condition

result = [
    idx for idx, tup in enumerate(list_of_tuples) if tup[1] == 'F'
]
print(result)  # 👉️ [2]

result = [
    idx for idx, tup in enumerate(list_of_tuples) if tup[1] == 'Dean'
]

print(result)  # 👉️ [2]
