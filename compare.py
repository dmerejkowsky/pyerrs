import subprocess

print("Comparing error messages between 2 and 3")
out2 = subprocess.check_output(["python2", "pyerrs.py"]).splitlines()
out3 = subprocess.check_output(["python3", "pyerrs.py"]).splitlines()

print("Here are differences (2 first)")
print()
for line2, line3 in zip(out2, out3):
    if line2 != line3:
        print(line2.decode("utf-8"))
        print(line3.decode("utf-8"))
        print()
