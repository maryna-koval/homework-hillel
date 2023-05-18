n = int(input("Enter amount of files: "))
file_permissions = {}
for i in range(n):
    user_input = input("Enter name of files and permissions (example, 'file.txt R W X'): ")
    input_parts = user_input.split()
    file = input_parts[0]
    permissions = input_parts[1:]
    file_permissions[file] = permissions
m = int(input("Enter amount of requests: "))
queries = []
files = []
for i in range(m):
    query, file = input("Enter your request (example, 'read file.txt'): ").split()
    queries.append(query)
    files.append(file)
for i in range(m):
    query = queries[i]
    file = files[i]
    if file in file_permissions:
        permissions = file_permissions[file]
        if query == "read" and "R" in permissions:
            print("OK")
        elif query == "write" and "W" in permissions:
            print("OK")
        elif query == "execute" and "X" in permissions:
            print("OK")
        else:
            print("Access denied")
    else:
        print("Access denied")
