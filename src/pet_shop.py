# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    if cash > 0:
         pet_shop["admin"]["total_cash"] += cash    
    else:
        cash = cash * -1
        pet_shop["admin"]["total_cash"] -= cash
    

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num_pets_sold):
    pet_shop["admin"]["pets_sold"] += num_pets_sold 
    

def get_stock_count(pet_shop):
    return len(pet_shop["pets"]) 


def get_pets_by_breed(pet_shop, breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(breed)
    return found_breed
  

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash_to_remove):
    customer_cash = get_customer_cash(customers)
    cash_left = customer_cash - cash_to_remove
    customers["cash"] = cash_left

def get_customer_pet_count(customers):
    return len(customers["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    

def customer_can_afford_pet(customer, new_pet):
    cash = get_customer_cash(customer)
    if cash >= new_pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, pet, customer):
    customer_cash = get_customer_cash(customer)
    if pet:
        if customer_cash >= pet["price"]:
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(pet_shop, pet) 
            cash_to_remove = pet["price"]
            remove_customer_cash(customer, cash_to_remove )  
            num_pets_sold = 1 
            increase_pets_sold(pet_shop, num_pets_sold)
            add_or_remove_cash(pet_shop, cash_to_remove)



