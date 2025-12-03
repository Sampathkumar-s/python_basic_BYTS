import os
FILENAME = "stress_factor1.csv"
if os.path.exists(FILENAME):
    os.remove(FILENAME)
    print(f"The file {FILENAME} exists and has been removed.")
else:
    print(f"The file {FILENAME} does not exist.")
    
