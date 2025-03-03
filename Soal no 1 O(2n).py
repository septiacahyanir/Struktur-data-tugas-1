def print_items(n):
    # Loop pertama (O(n)), mulai dari 0
    for i in range(n):
        print(f"item pertama: {i}")  

    # Loop kedua (O(n)), tanpa penambahan
    for i in range(n):
        print(f"item kedua: {i}")  

# Memanggil fungsi dengan n = 5
print_items(4)
