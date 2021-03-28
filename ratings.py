"""Restaurant rating lister."""

def add_new_restaurant_rating():

    new_restaurant_name = input("What's the restaurant's name you want to rate?")
    new_restaurant_rate = input(f"What's the rating of {new_restaurant_name}?")

    ratings_by_restaurant[new_restaurant_name] = new_restaurant_rate

def create_restaurant_rating_dict(filename):
    """Returns dictionary relating restaurant name and its rating."""

    #read file  
    restaurant_ratings = open(filename)
 
    #loop through file, every line find the rating
    for line in restaurant_ratings:
        line = line.strip()
        rating = line[-1:]
        restaurant_name = line[:-2]
        ratings_by_restaurant[restaurant_name] = rating
    return ratings_by_restaurant

ratings_by_restaurant = {}

restaurant_ratings_dict = create_restaurant_rating_dict("scores.txt")

sorted_list_of_restaurants = sorted(restaurant_ratings_dict)

def alpha_print_restaurants_and_ratings():
    for restaurant in sorted_list_of_restaurants:
        print(f"{restaurant} is rated at {restaurant_ratings_dict[restaurant]}.")



# print(ratings_by_restaurant)
# print(f"this {restaurant_name}  has a rating of {rating}")
#store ratings in a dictionary

#dictionary: key: restaurant name ; value: rating

#produce list of ratings, by alphabetical order by restaurant

#sort key, print values

