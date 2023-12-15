# Receive the names of eight clients and store them in a vector. In a second vector, store the number of DVDs rented in 2011 for each of the eight clients.
# For every ten rentals, the client is entitled to a free rental.
# Display the names of all clients with the number of free rentals they are entitled to.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

clients = []
rentals = []

# Receive names and number of DVDs rented in 2011
for i in range(8):
    name = input(f"Enter the name of client {i+1}: ")
    dvd_rented = int(input(f"Enter the number of DVDs rented in 2011 by {name}: "))
    clients.append(name)
    rentals.append(dvd_rented)

# Display the names of clients with the number of free rentals they are entitled to
print("\nClients with the number of free rentals:")
for i in range(8):
    free_rentals = rentals[i] // 10  # Calculate the number of free rentals based on every ten rentals
    print(f"{clients[i]} is entitled to {free_rentals} free rentals.")
