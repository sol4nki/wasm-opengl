import os 


# for i in range(9):
#     try:
#         os.mkdir(f"PHASE-{i}")
#         print(f"'PHASE-{i}' created.")
#     except FileExistsError:
#         print(f"'PHASE-{i}' already created.")

for i in range(9):
    file_path = f"./PHASE-{i}/README.md"
    with open(file_path, "w") as file:
        file.write(f" ")
        print(f"Created {file_path}")



