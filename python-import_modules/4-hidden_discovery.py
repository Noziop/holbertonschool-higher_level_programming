import os
import imp

# Download the compiled module
os.system("curl -o /tmp/hidden_4.pyc https://example.com/hidden_4.pyc")

# Load the compiled module
module = imp.load_compiled("hidden_4", "/tmp/hidden_4.pyc")

# Get all the names defined in the module
names = dir(module)

# Print the names in alphabetical order
for name in sorted(names):
	if not name.startswith("__"):
		print(name)