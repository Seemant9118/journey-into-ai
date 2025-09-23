# __name__ tells how a Python file is being used.
# if __name__ == "__main__": runs code only when the file is executed directly, not when imported.
# Useful for:
# Writing reusable modules.
# Keeping test/demo code inside the same file.
# Defining entry points for apps.

# Thus, this behaviour is used to check whether the module is run
# directly or imported to another file.

def main():
    print("This code runs when the file is executed directly.")
if __name__ == "__main__":
    main()