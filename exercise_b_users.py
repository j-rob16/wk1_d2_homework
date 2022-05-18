users = {
    "Jonathan": {
        "twitter": "jonnyt",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Stirling",
        "pets": [
            {
                "name": "fluffy",
                "species": "cat"
            },
            {
                "name": "fido",
                "species": "dog"
            },
            {
                "name": "spike",
                "species": "dog"
            }
        ]
    },
    "Erik": {
        "twitter": "eriksf",
        "lottery_numbers": [18, 34, 8, 11, 24],
        "home_town": "Linlithgow",
        "pets": [
            {
                "name": "nemo",
                "species": "fish"
            },
            {
                "name": "kevin",
                "species": "fish"
            },
            {
                "name": "spike",
                "species": "dog"
            },
            {
                "name": "rupert",
                "species": "parrot"
            }
        ]
    },
    "Avril": {
        "twitter": "bridgpally",
        "lottery_numbers": [12, 14, 33, 38, 9, 25],
        "home_town": "Dunbar",
        "pets": [
            {
                "name": "monty",
                "species": "snake"
            }
        ]
    }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jon_twitter_handle = users["Jonathan"]["twitter"]

# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]

# 3. Get the list of Erik's lottery numbers
erik_lottery_nums = users["Erik"]["lottery_numbers"]

# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]

# 5. Get the smallest of Erik's lottery numbers
erik_lottery_nums.sort()
print(erik_lottery_nums[0])

# 6. Return an list of Avril's lottery numbers that are even

# return..? not a function so left as a variable. 
avril_lottery_nums = users["Avril"]["lottery_numbers"]
avrils_even_nums = []
for num in avril_lottery_nums:
    if num % 2 == 0:
        avrils_even_nums.append(num)

# function to return the even numbers
# def avrils_evens():
#     avrils_even_nums = []
#     for num in avril_lottery_nums:
#         if num % 2 == 0:
#             avrils_even_nums.append(num)
#     return avrils_even_nums


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# insert in index pos. 1 to keep the order
erik_lottery_nums.insert(1, 7)

# 8. Change Erik's hometown to Edinburgh
erik_hometown = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"
eriks_dog = {
    "name": "fluffy",
    "species": "dog"
    }
users["Erik"]["pets"].append(eriks_dog)

# 10. Add another person to the users dictionary

bob = {
    "twitter": "shovel_bob",
    "lottery_numbers": [10, 13, 37, 32, 3, 24],
    "home_town": "Springfield",
    "pets": [
        {
            "name": "Tony",
            "species": "squirrel"
        }
    ]
}

users["Sideshow Bob"] = bob

# I fed everything in to the one print statement below to keep it clean
# print(users)