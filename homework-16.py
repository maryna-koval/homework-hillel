import pickle
import json
data = [
    {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'},
    {'key4': 'val4', 'key5': 'val5', 'key6': 'val6'},
    {'key7': 'val7', 'key8': 'val8', 'key9': 'val9'}
]
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
# Завдання 2
def combine_dict(A, B):
    C = A.copy()
    for key, value in B.items():
        if key in C:
            if isinstance(C[key], list):
                C[key].append(value)
            else:
                C[key] = [C[key], value]
        else:
            C[key] = value

    return C
A = {'key': 1, 'key1': 4}
B = {'key1': 2}
C = combine_dict(A, B)
with open('result.json', 'w') as k:
    json.dump(C, k)
