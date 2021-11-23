import os
import glob

os.system("find . -name '*.csv.gz' -print0 | xargs -0 -n1 gzip -d")

list_of_files = glob.glob('*.csv')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

new_name1 = input("File Name: ")

new_name = new_name1 + ".csv"

os.rename(latest_file, new_name)

print("Saved the file")