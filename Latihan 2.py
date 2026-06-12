with open("data_mahasiswa.txt", "r") as file:
    data = file.readlines()

for i, nama in enumerate(data, start=1):
    print(f"{i}. {nama.strip()}")
