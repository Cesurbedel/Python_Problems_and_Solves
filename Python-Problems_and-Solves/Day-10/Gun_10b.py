# List of supported commands
supported = ["Lights off", "Lock the door", "Open the door", "Make coffee", "Shut down"]

# Taking input command
command = input()

# Checking if the input command is supported
if command in supported:
    print("OK")
else:
    print("Unknown")
