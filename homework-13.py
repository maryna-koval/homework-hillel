n = int(input("Enter amount of files: "))
file_permissions = {}
for i in range(n):
    user_input = input("Enter name of files and permissions (example, 'file.txt R W X'): ")
    input_parts = user_input.split()
    file, *permissions = input_parts
    file_permissions[file] = [perm.lower() for perm in permissions]
m = int(input("Enter amount of requests: "))
queries = []
files = []
for i in range(m):
    query, file = input("Enter your request (example, 'read file.txt'): ").split()
    queries.append(query.lower())
    files.append(file.lower())
for i in range(m):
    query = queries[i]
    file = files[i]
    permissions = file_permissions.get(file, [])
    if query == "read" and "r" in permissions or query == 'write' and "w" in permissions \
            or query == "execute" and "x" in permissions:
        print("OK")
    else:
        print("Access denied")
