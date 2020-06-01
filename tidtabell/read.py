from os import listdir, system

files = listdir(".")
for file in files:
    if "pdf" in file:
        parts = file.split(".")[0]
        system("pdftotext -table -margint 60 -marginb 25 " + file)
        system("iconv -f iso-8859-1 -t utf-8 " + parts + ".txt > " + parts + "u.txt ")
