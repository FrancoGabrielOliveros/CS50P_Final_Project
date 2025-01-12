import pytest
from unittest.mock import patch
from project import add_plant, delete_plant, edit_plant, update_nourishment, purchase_fertilizer, nourish_plant, data_reset
from project import Plant, Fertilizer, Log


def test_add_plant():
    plant_dictionary = {}
    log_dictionary = {}

    with patch("builtins.input", side_effect=["Sunflower", "OUTDOOR"]):
        add_plant(plant_dictionary, log_dictionary)
    assert plant_dictionary["P0"].name == "Sunflower"
    assert plant_dictionary["P0"].storage == "OUTDOOR"

    with patch("builtins.input", side_effect=["Bouganvilla", "INDOOR"]):
        add_plant(plant_dictionary, log_dictionary)
    assert plant_dictionary["P1"].name == "Bouganvilla"
    assert plant_dictionary["P1"].storage == "INDOOR"
    
    with patch("builtins.input", side_effect=["sAnTaN", "INDOOR"]):
        add_plant(plant_dictionary, log_dictionary)

    with patch("builtins.input", side_effect=["Tulip", "outdoor"]):
        add_plant(plant_dictionary, log_dictionary)
    assert "P3" not in plant_dictionary

    with patch("builtins.input", side_effect=["Sunflower", "OUTDOOR"]):
        add_plant(plant_dictionary, log_dictionary)
    assert "P3" not in plant_dictionary

def test_delete_plant():
    plant_dictionary = {}
    log_dictionary = {}

    with patch("builtins.input", side_effect=["P1"]):
        delete_plant(plant_dictionary, log_dictionary)
    assert "P1" not in plant_dictionary

def test_edit_plant():
    plant_dictionary = {"P2": Plant("sAnTaN", "INDOOR")}
    log_dictionary = {}

    with patch("builtins.input", side_effect=["P2", "Santan", "OUTDOOR"]):
        edit_plant(plant_dictionary, log_dictionary)
    assert plant_dictionary["P2"].name != "sAnTaN"
    assert plant_dictionary["P2"].name == "Santan"
    assert plant_dictionary["P2"].storage != "INDOOR"
    assert plant_dictionary["P2"].storage == "OUTDOOR"
    
def test_update_nourishment():
    plant_dictionary = {"P0": Plant("Sunflower", "OUTDOOR"), "P2": Plant("Bouganvilla", "INDOOR")}

    with patch("builtins.input", side_effect=["P0", "Urea", "15"]):
        update_nourishment(plant_dictionary)
    assert plant_dictionary["P0"].fertilizer == "Urea"
    assert plant_dictionary["P0"].amount == 15

    with patch("builtins.input", side_effect=["P2", "Nitrogen", "10"]):
        update_nourishment(plant_dictionary)
    assert plant_dictionary["P2"].fertilizer == "Nitrogen"
    assert plant_dictionary["P2"].amount == 10

def test_purchase_fertilizer():
    fertilizer_dictionary = {}
    log_dictionary = {}

    with patch("builtins.input", side_effect=["Urea", "30", "Mr. Cooper"]):
        purchase_fertilizer(fertilizer_dictionary, log_dictionary)
    assert fertilizer_dictionary["F0"].name == "Urea"
    assert fertilizer_dictionary["F0"].stock == 30
    assert fertilizer_dictionary["F0"].supplier == "Mr. Cooper"

    with patch("builtins.input", side_effect=["Nitrogen", "5", "Ms. Anna"]):
        purchase_fertilizer(fertilizer_dictionary, log_dictionary)
    assert fertilizer_dictionary["F1"].name == "Nitrogen"
    assert fertilizer_dictionary["F1"].stock == 5
    assert fertilizer_dictionary["F1"].supplier == "Ms. Anna"

def test_nourish_plant():
    plant_dictionary = {"P0": Plant("Sunflower", "OUTDOOR", "Urea", "15"), "P2": Plant("Bouganvilla", "INDOOR", "Nitrogen", "10")}
    fertilizer_dictionary = {"F0": Fertilizer("Urea", 30, "Mr. Cooper"), "F1": Fertilizer("Nitrogen", 5, "Ms. Anna")}
    log_dictionary = {}

    with patch("builtins.input", side_effect=["P0"]):
        nourish_plant(plant_dictionary, fertilizer_dictionary, log_dictionary)
    assert fertilizer_dictionary["F0"].stock == 15

    with patch("builtins.input", side_effect=["P2"]):
        nourish_plant(plant_dictionary, fertilizer_dictionary, log_dictionary)
    assert fertilizer_dictionary["F1"].stock == 5

def test_data_reset():
    plant_dictionary = {"P0": Plant("Sunflower", "OUTDOOR", "Urea", "15"), "P2": Plant("Bouganvilla", "INDOOR", "Nitrogen", "10")}
    fertilizer_dictionary = {"F0": Fertilizer("Urea", 30, "Mr. Cooper"), "F1": Fertilizer("Nitrogen", 5, "Ms. Anna")}
    log_dictionary = {"L0": Log("2025-01-10","add_plant", "P0","NA"), 
                      "L1": Log("2025-01-10","add_plant", "P1","NA"), 
                      "L2": Log("2025-01-10","add_plant","P2","NA"), 
                      "L3": Log("2025-01-10","delete_plant","P1","NA"), 
                      "L4": Log("2025-01-10","purchase_fertilizer","NA","F0"), 
                      "L5": Log("2025-01-10","purchase_fertilizer","NA","F1"), 
                      "L6": Log("2025-01-10","nourish_plant","P0","F0")}
                      
    with patch("builtins.input", side_effect=["y"]):
        data_reset(plant_dictionary, log_dictionary, fertilizer_dictionary)
    assert plant_dictionary == {}
    assert fertilizer_dictionary == {}
    assert log_dictionary == {}


pytest.main()