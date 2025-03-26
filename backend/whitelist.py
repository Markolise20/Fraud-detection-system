import re

# Test regex pattern
text = "Hello, my email is    pppty@d.com ."
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

match = re.search(pattern, text)
if match:
    print("Email found:", match.group())
else:
    print("No email found.")
