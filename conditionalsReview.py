# Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".



# Implement the decision structure to advise on what to wear:
# If the weather is "sunny", recommend "wear sunglasses and a hat".
# If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
# If the weather is "cold", recommend "wear a warm coat and gloves".
# If the input doesn't match any category, inform the user with a message saying the input was not recognized.

#Next 
# Ask the user to input their age and location. Assume location to be either "urban" or "rural".
# Implement the eligibility checks using comparison and logical operators:
# Participants must be at least 18 years old.
# Participants must live in an "urban" area.
# Display a message indicating whether the user is eligible or not based on these conditions.


# weather = input("Whats the current weather? sunny, rainy, or cold? ")
# if weather == "sunny": 
#     print("wear sunglasses and a hat")

# if weather == "rainy":
#     print("carry an umbrella and wear waterproof boots")

# if weather == "cold":
#     print("wear a warm coat and gloves")

# age = int(input("How old are you? "))
# location = input("Where do you live?  (urban, rural): ")

# if age >=18 and location == "urban":
#     print("You are elegible to participation")
# else:
#     print("You are not elegible to participate. ")

age = int(input("How old are you? "))
citizenship_status = input("Are you a citizen? ")

if citizenship_status == "yes" and age >=18:
    print("You are elegible to vote")
else:
    print("Sorry, you are not elegible to vote")
