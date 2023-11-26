def print_full_name(first, last):
    # Formatting the output string using the provided first and last names
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
