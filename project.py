import csv
from datetime import date
from tabulate import tabulate


class Plant:
    def __init__(self, name: str, storage: str, fertilizer="", amount=""):
        self.name = name
        self.storage = storage
        self.fertilizer = fertilizer
        if amount == "":
            self.amount = amount
        else:
            self.amount = int(amount)

    def return_list(self):
        return [self.name, self.storage, self.fertilizer, self.amount]

class Fertilizer:
    def __init__(self, name: str, stock: int, supplier: str):
        self.name = name
        if stock == "":
            self.stock = stock
        else:
            self.stock = int(stock)
        self.supplier = supplier

    def return_list(self):
        return [self.name, self.stock, self.supplier]

class Log:
    def __init__(self, date: str, action: str, plant_id="NA", fertilizer_id="NA"):
        self.plant_id = plant_id
        self.fertilizer_id = fertilizer_id
        self.date = date
        self.action = action

    def return_list(self):
        return [self.plant_id, self.fertilizer_id, self.date, self.action]
    

def main_menu() -> str:
    main_menu = {"Main Menu": ["[1] Plant Section", "[2] Fertilizer Section", "[3] Log Section", "[0] Save and Exit", "[-] Exit Without Saving"]}
    print()
    print(tabulate(main_menu, headers="keys", tablefmt="rounded_outline"))

    while True:
        x = input("Enter choice: ").strip()
        if x in ["1", "2", "3", "0", "-"]:
            return x


def plant_section() -> str:
    plant_menu = {"Plant Section": ["[1] Add Plant", "[2] Delete Plant", "[3] View Plants", "[4] Edit Plant", "[5] Update Nourishment", "[6] Nourish Plant", "[0] Return to Main Menu"]}
    print()
    print(tabulate(plant_menu, headers="keys", tablefmt="rounded_outline"))

    while True:
        x = input("Enter choice: ").strip()
        if x in ["1", "2", "3", "3", "4", "5", "6", "0"]:
            return x


def fertilizer_section() -> str:
    fertilizer_menu = {"Fertilizer Section": ["[1] Purchase Fertilizer", "[2] View Fertilizers", "[3] View Affected Plants", "[0] Return to Main Menu"]}
    print()
    print(tabulate(fertilizer_menu, headers="keys", tablefmt="rounded_outline"))

    while True:
        x = input("Enter choice: ").strip()
        if x in ["1", "2", "3", "0"]:
            return x
        

def log_section() -> str:
    log_menu = {"Log Section": ["[1] View All Entries", "[2] View Transactions Per Action", "[3] Data Reset", "[0] Return to Main Menu"]}
    print()
    print(tabulate(log_menu, headers="keys", tablefmt="rounded_outline"))

    while True:
        x = input("Enter choice: ").strip()
        if x in ["1", "2", "3", "0"]:
            return x


def id_create(reference: dict, letter: str) -> str:
    num = 0
    while True:
        if letter + str(num) in reference:
            num += 1
        else:
            return letter + str(num)


def view_plants(plant_dictionary: dict):
    plants = []
    for key, value in plant_dictionary.items():
        plant_info = value.return_list()    
        plant_info.insert(0, key)
        plants.append(plant_info)

    print()
    print(tabulate(plants, headers=["Plant ID", "Name", "Storage", "Fertilizer", "Required Amount"], tablefmt="rounded_outline"))


def add_plant(plant_dictionary: dict, log_dictionary: dict):
    names = [value.name.lower() for value in plant_dictionary.values()]
    name = input("Enter plant name: ").strip()
    if name.lower() in names:
        print(":Name already in use.")
        return 

    storage = input("Enter plant storage [INDOOR/OUTDOOR]: ").strip()
    if storage not in ["INDOOR", "OUTDOOR"]:
        print(":Please enter a valid option.")
        return 

    plant = Plant(name, storage)
    plant_ID = id_create(plant_dictionary, "P")
    plant_dictionary[plant_ID] = plant

    log = Log(str(date.today()), "add_plant", plant_id=plant_ID)
    log_dictionary[id_create(log_dictionary, "L")] = log


def delete_plant(plant_dictionary: dict, log_dictionary: dict):
    view_plants(plant_dictionary)
    plant_ID = input("Enter ID of plant to be deleted: ").strip()
    if plant_ID not in plant_dictionary:
        print(":Enter valid ID.")
        return

    del plant_dictionary[plant_ID]

    log = Log(str(date.today()), "delete_plant", plant_id=plant_ID)
    log_dictionary[id_create(log_dictionary, "L")] = log


def edit_plant(plant_dictionary:dict, log_dictionary: dict):
    view_plants(plant_dictionary)
    plant_ID = input("Enter ID of plant to be edited: ").strip()
    if plant_ID not in plant_dictionary:
        print(":Enter valid ID.")
        return
    
    names = [value.name for value in plant_dictionary.values()]
    name = input("Enter new plant name: ").strip()
    if name in names:
        print(":Name already in use.")
        return 

    storage = input("Enter plant storage [INDOOR/OUTDOOR]: ").strip()
    if storage not in ["INDOOR", "OUTDOOR"]:
        print(":Please enter a valid option.")
        return

    plant_dictionary[plant_ID].name = name
    plant_dictionary[plant_ID].storage = storage

    log = Log(str(date.today()), "edit_plant", plant_id=plant_ID)
    log_dictionary[id_create(log_dictionary, "L")] = log


def update_nourishment(plant_dictionary: dict):
    view_plants(plant_dictionary)
    plant_ID = input("Enter ID of plant nourishment to be updated: ").strip()
    if plant_ID not in plant_dictionary:
        print(":Enter valid ID.")
        return
    
    plant_dictionary[plant_ID].fertilizer = input("Enter fertilizer name: ").strip()
    try:
        plant_dictionary[plant_ID].amount = int(input("Enter fertilizer amount required by plant: ").strip())
    except ValueError:
        print(":Please enter an integer.")


def nourish_plant(plant_dictionary: dict, fertilizer_dictionary: dict, log_dictionary: dict):
    if not plant_dictionary:
        print(":No plants have been added yet.")
        return
    elif not fertilizer_dictionary:
        print(":No fertilizer have been added yet.")
        return

    view_plants(plant_dictionary)
    plant_ID = input("Enter ID of plant you wnat to nourish: ").strip()
    if plant_ID not in plant_dictionary:
        print(":Please enter valid ID.")
        return

    fertilizer_ID = None
    for key, value in fertilizer_dictionary.items():
        if plant_dictionary[plant_ID].fertilizer == value.name:
            fertilizer_ID = key

    if not fertilizer_ID:
        print(":Not enough stock.")
        return
    elif fertilizer_dictionary[fertilizer_ID].stock - plant_dictionary[plant_ID].amount < 0:
        print(":Not enough stock.")
        return
    else:
        print(":Plant successfully nourished.")
        fertilizer_dictionary[fertilizer_ID].stock -= plant_dictionary[plant_ID].amount

    log = Log(str(date.today()), "nourish_plant", plant_id=plant_ID, fertilizer_id=fertilizer_ID)
    log_dictionary[id_create(log_dictionary, "L")] = log


def purchase_fertilizer(fertilizer_dictionary: dict, log_dictionary: dict):
    name = input("Enter fertilizer name: ").strip()
    fertilizer_ID = None
    for key, value in fertilizer_dictionary.items():
        if name.lower() == value.name.lower():
            fertilizer_ID = key
    
    try:
        stock = int(input("Enter amount purchased: ").strip())
    except ValueError:
        print(":Please enter and integer.")
        return
    supplier = input("Enter supplier name: ").strip()

    if fertilizer_ID:
        fertilizer_dictionary[fertilizer_ID].stock += stock
        fertilizer_dictionary[fertilizer_ID].supplier = supplier    
    else:
        fertilizer = Fertilizer(name, stock, supplier)
        fertilizer_ID = id_create(fertilizer_dictionary, "F")
        fertilizer_dictionary[fertilizer_ID] = fertilizer

    log = Log(str(date.today()), "purchase_fertilizer", fertilizer_id=fertilizer_ID)
    log_dictionary[id_create(log_dictionary, "L")] = log


def view_fertilizers(fertilizer_dictionary: dict):
    fertilizers = []
    for key, value in fertilizer_dictionary.items():
        fertilizer_info = value.return_list()    
        fertilizer_info.insert(0, key)
        fertilizers.append(fertilizer_info)

    print()
    print(tabulate(fertilizers, headers=["Fertilizer ID", "Name", "Stock", "Supplier"], tablefmt="rounded_outline"))


def affected_plants(plant_dictionary: dict, fertilizer_dictionary: dict):
    view_fertilizers(fertilizer_dictionary)
    fertilizer_ID = input("Enter ID of fertilizer whose affected plants you want to view: ").strip()
    if fertilizer_ID not in fertilizer_dictionary:
        print(":Enter valid ID.")
        return

    affected_plants = []
    for value in plant_dictionary.values():
        if value.fertilizer == fertilizer_dictionary[fertilizer_ID].name:
            affected_plants.append([value.name])

    print()
    print(tabulate(affected_plants, headers=[f"{fertilizer_dictionary[fertilizer_ID].name} Affected Plants"], tablefmt="rounded_outline"))


def view_entries(log_dictionary: dict):
    logs = []
    for key, value in log_dictionary.items():
        log_info = value.return_list()    
        log_info.insert(0, key)
        logs.append(log_info)

    print()
    print(tabulate(logs, headers=["Log ID", "Plant ID", "Fertilizer ID", "Date", "Action"], tablefmt="rounded_outline"))


def entries_per_action(log_dictionary: dict):
    entries_menu = {"Actions": ["[1] add_plant", "[2] delete_plant", "[3] edit_plant", "[4] purchase_fertilizer", "[5] nourish_plant"]}
    print()
    print(tabulate(entries_menu, headers="keys", tablefmt="rounded_outline"))

    x = input("Enter choice: ").strip()
    if x not in ["1", "2", "3", "4", "5"]:
        print(":Please enter valid option")
        return
    
    match x:
        case "1":
            add_plant = [[key, value.plant_id, value.fertilizer_id, value.date, value.action] for key,value in log_dictionary.items() if value.action == "add_plant"]
            print()
            print(tabulate(add_plant, headers=["Add Plant", "", "", "", ""], tablefmt="rounded_outline"))

        case "2":
            delete_plant = [[key, value.plant_id, value.fertilizer_id, value.date, value.action] for key,value in log_dictionary.items() if value.action == "delete_plant"]
            print()
            print(tabulate(delete_plant, headers=["Delete Plant", "", "", "", ""], tablefmt="rounded_outline"))

        case "3":
            edit_plant = [[key, value.plant_id, value.fertilizer_id, value.date, value.action] for key,value in log_dictionary.items() if value.action == "edit_plant"]
            print()
            print(tabulate(edit_plant, headers=["Edit Plant", "", "", "", ""], tablefmt="rounded_outline"))

        case "4":
            purchase_fertilizer = [[key, value.plant_id, value.fertilizer_id, value.date, value.action] for key,value in log_dictionary.items() if value.action == "purchase_fertilizer"]
            print()
            print(tabulate(purchase_fertilizer, headers=["Purchase Fertilizer", "", "", "", ""], tablefmt="rounded_outline"))

        case "5":
            nourish_plant = [[key, value.plant_id, value.fertilizer_id, value.date, value.action] for key,value in log_dictionary.items() if value.action == "nourish_plant"]
            print()
            print(tabulate(nourish_plant, headers=["Nourish Plant", "", "", "", ""], tablefmt="rounded_outline"))


def data_reset(plant_dictionary: dict, fertilizer_dictionary: dict, log_dictionary: dict):
    x = input("Are you sure you want to delete all the data? [y/n] ")
    if x not in ["y", "n"]:
        return
    match x:
        case "y":
            plant_dictionary.clear()
            fertilizer_dictionary.clear()
            log_dictionary.clear()
        case "n":
            return


def data_save(plant_dictionary: dict, fertilizer_dictionary: dict, log_dictionary: dict):
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for key, value in plant_dictionary.items():
            writer.writerow([key, value.name, value.storage, value.fertilizer, value.amount])
        for key, value in fertilizer_dictionary.items():
            writer.writerow([key, value.name, value.stock, value.supplier])
        for key, value in log_dictionary.items():
            writer.writerow([key, value.plant_id, value.fertilizer_id, value.date, value.action])


def data_restore (plant_dictionary: dict, fertilizer_dictionary: dict, log_dictionary: dict):
    with open("data.csv") as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0][0] == "P":
                plant_dictionary[line[0]] = Plant(line[1], line[2], line[3], (line[4])) 
            elif line[0][0] == "F":
                fertilizer_dictionary[line[0]] = Fertilizer(line[1], line[2], line[3]) 
            elif line[0][0] == "L":
                log_dictionary[line[0]] = Log(line[3], line[4], plant_id=line[1], fertilizer_id=line[2]) 


def main():
    plant_dictionary = {}
    fertilizer_dictionary = {}
    log_dictionary = {}
    data_restore(plant_dictionary, fertilizer_dictionary, log_dictionary)

    while True:
        choice = main_menu()
        match choice:
            case "1":
                while True:
                    action = plant_section()
                    match action:
                        case "1":
                            add_plant(plant_dictionary, log_dictionary)
                        case "2":
                            delete_plant(plant_dictionary, log_dictionary)
                        case "3":
                            view_plants(plant_dictionary)
                        case "4":
                            edit_plant(plant_dictionary, log_dictionary)        
                        case "5":
                            update_nourishment(plant_dictionary)
                        case "6":
                            nourish_plant(plant_dictionary, fertilizer_dictionary, log_dictionary)
                        case "0":
                            break
            case "2":
                while True:
                    action = fertilizer_section()
                    match action:
                        case "1":
                            purchase_fertilizer(fertilizer_dictionary, log_dictionary)
                        case "2":
                            view_fertilizers(fertilizer_dictionary)
                        case "3":
                            affected_plants(plant_dictionary, fertilizer_dictionary)        
                        case "0":
                            break
            case "3":
                while True:
                    action = log_section()
                    match action:
                        case "1":
                            view_entries(log_dictionary)
                        case "2":
                            entries_per_action(log_dictionary)
                        case "3":
                            data_reset(plant_dictionary, fertilizer_dictionary, log_dictionary)        
                        case "0":
                            break
            case "0":
                data_save(plant_dictionary, fertilizer_dictionary, log_dictionary)        
                break
            case "-":
                break


if __name__ == "__main__":
    main()