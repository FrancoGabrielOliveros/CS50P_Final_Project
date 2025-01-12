# GARDEN LOGGING SYSTEM

Link to [video demo](https://youtu.be/7pOoO755qbw).

## Description:

This program functions as a **Garden Logging System** which takes records and data regarding garden information such as **plants** and **fertilizers**. The program requires the user to do the inputs regarding
plant and fertilizer data (and its related information), while automatically writing logs which contains the **date** and the **actions** made by the user. All the data in turn are saved in a _CSV file_ such that all the inputs made by the user do not disappear unless intentionally deleted.

To manipulate and handle the data, the program places the information in three main classes, **Plant**, **Fertilizer**, and **Log** class; which are all cointained in their corresponding dictionaries and can
be accessed using _automatically made unique IDs_.

## Objects/ Classes

### Plant

Object **Plant** can be accesed in a dictionary using its corresponding **Plant ID**, and contains **Plant Name**, **Plant Storage** (INDOOR/OUTDOOR), **Fertilizer**, **Amount** (amount of fertilizer needed
by the plant per nourish).

### Fertilizer

Object **Fertilizer** can be accesed in a dictionary using its corresponding **Fertilizer ID**, and contains **Fertilizer Name**, **Stock**, **Supplier** (latest).

### Log

Object **Log** can be accesed in a dictionary using its corresponding **Log ID**, and contains **Plant ID** (related to action), **Fertilizer ID** (related to action), **Date** (when the action was made),
**Action** (add_plant/ delete_plant/ edit_plant/ purchase_fertilizer/ nourish_plant).

## Functions

### Main Menu

![](/Images/main_menu.png)

1. **Data Restore**
    - Automatically runs after starting the program.
    - Using the csv module, data in the _data.csv_ file are read and placed inside the program's dictionaries.
2. **Plant Section**
    - Can be accesed by typing input **'1'**.
3. **Fertilizer Section**
    - Can be accessed by typing input **'2'**
4. **Log Section**
    - Can be accessed by typing input **'3'**.
5. **Save and Exit**
    - Can be accessed by typing input **'0'**.
    - Fetches all the data in the current dictionary and writes them in the _data.csv_ file using the csv module.
6. **Exit Without Saving**
    - Can be accessed by typing input **'-'**.
    - Exits out of the program without changing the _data.csv_ file.

### Plant Section

![](/Images/plant_section.png)

1. **Add Plant**
    - Can be accessed by typing input **'1'**.
    - Asks for _plant name_ and _plant storage_ (INDOOR/ OUTDOOR).
    - Automatically creates a unique _Plant ID_ and places the new _Plant_ object in a dictionary.
    - Updates the log dictionary.
2. **Delete Plant**
    - Can be accessed by typing input **'2'**.
    - Asks for the _Plant ID_ of the plant you want to remove from the dictionary.
    - Updates the log dictionary.
3. **View Plants**
    - Can be accessed by typing input **'3'**.
    - Prints out all the _Plant_ objects and related information such as _Plant ID_, _name_, _storage_, _fertilizer_, and _amount_ in a neat tabular format.
4. **Edit Plant**
    - Can be accessed by typing input **'4'**.
    - Asks for the _Plant ID_ of the plant you want to edit, then the new name and storage to replace the previous one.
    - Updates the log dictionary.
5. **Update Nourishment**
    - Can be accessed by typing input **'5'**.
    - Asks for the _Plant ID_ of the plant nourishment you want to update.
    - Requires the user to input _fertilizer name_ and the _amount_ needed by the plant per nourish.
6. **Nourish Plant**
    - Can be accessed by typing input **'6'**.
    - Asks for the _Plant ID_ of the plant you want to nourish.
    - Using the fertilizer of the accessed _Plant_ object, it tries to find the corresponding fertilizer in the _Fertilizer Dictionary_ and checks whether there is enough stock.
    - If there is enough stock, the plant will be nourished and the stock will be reduced depending on the amount needed by the plant.
    - Updates the log dictionary.
7. **Return to Main Menu**
    - Can be accessed by typing input **'0'**.

### Fertilizer Section

![](/Images/fertilizer_section.png)

1. **Purchase Fertilizer**
    - Can be accessed by typing input **'1'**.
    - Asks for _fertilzer name_, _stock_, and _supplier_.
    - Automatically creates a unique _Fertilizer ID_ and places the new _Fertilizer_ object in a dictionary.
    - In a case that the fertilizer already exists, the stock purchase will only be added to the current stock.
    - Updates the log dictionary.
2. **View Fertilizers**
    - Can be accessed by typing input **'2'**.
    - Prints out all the _Fertilizer_ objects and related information such as _Fertilizer ID_, _name_, _stock_, and _supplier_ in a neat tabular format.
3. **View Affected Plants**
    - Can be accessed by typing input **'3'**.
    - Asks for _Fertilizer ID_ of the fertilizer whose affected plants you want to see.
    - Seeks the _Plant Dictionary_ for plants which requires the accessed fertilizer and prints them in a neat tabular format.
4. **Return to Main Menu**
    - Can be accessed by typing input **'0'**.

### Log Section

![](/Images/log_section.png)

1. **View All Entries**
    - Can be accessed by typing input **'1'**.
    - Prints out all the _Log_ objects and related information such as _Log ID_, _Plant ID_ (related to action), _Fertilizer ID_ (related to action), _date_ (in which the action was made), and _action_ (done by the user) in a neat tabular format.
2. **View Transactions Per Action**
    - Can be accessed by typing input **'2'**.
    - Asks user to choose an action (add_plant/ delete_plant/ edit_plant/ purchase_fertilizer/ nourish_plant) and displays logs with such action.
3. **Data Reset**
    - Can be accessed by typing input **'3'**.
    - Removes all the contents and objects from the _Plant Dictionary_, _Fertilizer Dictionary_, and _Log Dictionary_.
4. **Return To Main Menu**
    - Can be accessed by typing input **'0'**.

## TODO

### Installation

Download the repository through Clone Repository.

    git clone https://github.com/FrancoGabrielOliveros/CS50P_Final_Project.git

Use pip to install needed libraries.

    pip install -r requirements.txt

### Usage

Run the program by using python.

    python project.py

Test the program using python, pytest, and unittest. The _test_project.py_ file runs the pytest inside the python program.

    python test_project.py

After running the program, navigating the functions can be seen in the [functions](#functions) section.
