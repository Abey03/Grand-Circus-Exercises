# First part of lab
def apt_search1(city: str, max_rent: int, min_beds: int, pets_allowed: bool):
    if pets_allowed:
        welcome_statement = (f"""Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedrooms,
that allow pets, all within a budget of ${max_rent} per month.""")
    else:
        welcome_statement = (f"""Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedrooms,
all within a budget of {max_rent} per month.""")

    return welcome_statement


# Second part of lab
def apt_search2(city, max_rent, min_beds=3, pets_allowed=False):
    if pets_allowed:
        return f"""Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedrooms,
           that allow pets, all within a budget of {max_rent} per month."""
    else:
        return f"""Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedrooms,
                   all within a budget of {max_rent} per month."""

# Third part of lab/Results
print("Lambda Function results:")
add_100 = lambda x : x + 100
print(add_100(50))

squared = lambda x : x ** 2
print(squared(4))

concatenate = lambda x : "-" + x
print(concatenate("Hello"))

divide = lambda x : x // 3
print(divide(6))


# First part results
print("First part results:")
print(apt_search1("Atlanta", 500, 3, True))
print(apt_search2("Atlanta", 500))

# Second part results
print("Second part results:")
print(apt_search2(city="Detroit", max_rent=5000))
print(apt_search2(city="Detroit", max_rent=5000, min_beds=3))
print(apt_search2(city="Detroit", max_rent=5000, pets_allowed=True))


