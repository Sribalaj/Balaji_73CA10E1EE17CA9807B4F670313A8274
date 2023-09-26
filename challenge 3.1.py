def linear_search_product(products, target):

    indices = []

    for i in range(len(products)):

        if products[i] == target:

            indices.append(i)

    return indices



# Get the list of products from the user

products = input("Enter the list of products (separated by commas): ").split(",")



# Get the target product from the user

target = input("Enter the target product name: ")



# Call the linear_search_product function

indices = linear_search_product(products, target)



# Print the result

if indices:

    print("Indices of occurrences:", indices)

else:

    print("The product was not found in the list.")