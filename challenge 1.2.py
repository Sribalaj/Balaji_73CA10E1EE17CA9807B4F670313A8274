years = []
num_years = int(input("Enter the number of years: "))

# Get the years from the user
for i in range(num_years):
    year = int(input("Enter a year: "))
    years.append(year)

# Check if the years are leap years
for year in years:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")