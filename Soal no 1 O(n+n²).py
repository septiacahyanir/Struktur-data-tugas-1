def print_items(n):
    # Bagian O(n)
    for i in range(n):
        print(f"Item O(n): {i}")  

    # Bagian O(n²)
    for i in range(n):
        for j in range(n):
            print(f"Item O(n²): {i}, {j}")  
            
# Memanggil fungsi dengan n = 4
print_items(4)
