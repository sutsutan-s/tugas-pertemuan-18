import os

if os.path.exists("log.txt"):
    print("Isi log.txt:")
    with open("log.txt", "r") as file:
        print(file.read())
else:
    with open("log.txt", "w") as file:
        file.write("Log dimulai")

    print("File log.txt berhasil dibuat.")
