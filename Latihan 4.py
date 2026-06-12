import os
import shutil

if not os.path.exists("arsip"):
    os.mkdir("arsip")

if os.path.exists("data_mahasiswa.txt"):
    shutil.move("data_mahasiswa.txt", "arsip/data_mahasiswa.txt")
    print("File berhasil dipindahkan ke folder arsip.")
else:
    print("File data_mahasiswa.txt tidak ditemukan.")
