from source.subst_drive import main_subst


def main():
    print(30 * "=")
    print("1 - Replace file drive")
    print("2 - Create local db")
    print("3 - Export to MySQL")
    print("4 - Configuration")
    print(30 * "=")
    
    choice = input("Enter your choice: ")
    choice = str(choice)

    match choice:
        case "1":
            subst = main_subst()
            if subst:
                print("File drive substituted succesfully")
        case "2":
            pass
            

if __name__ == "__main__":
    main()