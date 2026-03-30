import json

JSON_PATH = "config/config.json"
FILES_PATH = "files_data/"

successfully_substituted = False

def substitution_config():
    with open(JSON_PATH, "r") as f:
        words_json = ""

        config = json.load(f)
        for j in range(len(config["subst"])) :
            words_json += config["subst"][j] + ";"
            
    return words_json

def substitute_drive(words_json):
    words = []
    with open(FILES_PATH + "teste 2.txt", "r") as f:
        content = f.read()
        
        for line in content.splitlines():
            words += line.strip().split("\n")

    for i in range(len(words)):
        words[i] = words[i].replace(words[i][:4], words_json)
    
    return words

def export_back(words):
    with open(FILES_PATH + "teste 2.txt", "w") as f:
        for word in words:
            f.write(word + "\n")

def main_subst():

    words_json_config = ""

    print("Substitute file drive in path")
    print(30 * "=")
    print("Gathering data from config file...")
    try:
        words_json_config = substitution_config()

        if words_json_config == "":
            print("No substitution data found.")
            return successfully_substituted
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return successfully_substituted
    
    print("Config data gathered successfully")
    print(30 * "-")
    print("Substituing file drive in path")
    print("Gathering changed data...")

    try:
        final_subst = substitute_drive(words_json_config)
        
        if final_subst == "":
            print("No data found.")
            return successfully_substituted
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return successfully_substituted
    
    print("Changed data gathered successfully")
    print(30 * "-")
    print("Exporting data back to file...")

    export_back(final_subst)

    print("Data exported successfully")
    
    print(". . .")

    return successfully_substituted == True


if __name__ == "__main__":
    main_subst()