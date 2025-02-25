import os

filepath = os.getenv("FILEPATH", "/home/python/test_file")

try:
    with open(filepath, "r") as f:
        content = f.read()
 
        print(f"✅ Successfully read file at {filepath}!\n---\n{content}\n---")
except FileNotFoundError:
    print(f"❌ Error: File '{filepath}' not found!")
except Exception as e:
    print(f"❌ Error while reading file: {e}")
