class Node:
    def __init__(self, nim, nama):
        self.nim = nim  
        self.nama = nama  
        self.next = None  
        self.prev = None  

class DoubleLinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.length = 0

    def append(self, nim, nama):
        new_node = Node(nim, nama)  
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail  
            self.tail = new_node  
        self.length += 1  

    def pop(self):
        if self.length == 0:  
            return None
        temp = self.tail 
        if self.length == 1:  
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev  
            self.tail.next = None
        self.length -= 1 
        return temp.nim, temp.nama 

    def prepend(self, nim, nama):
        new_node = Node(nim, nama)  
        if self.length == 0:  
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node  
            self.head = new_node  
        self.length += 1 

    def insert(self, index, nim, nama):
        if index < 0 or index > self.length:  
            return False
        if index == 0:  
            return self.prepend(nim, nama)
        if index == self.length: 
            return self.append(nim, nama)

        new_node = Node(nim, nama)  
        temp = self.head
        for _ in range(index - 1):  
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length: 
            return None
        if index == 0:  
            removed_node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.length -= 1
            return removed_node.nim, removed_node.nama
        if index == self.length - 1: 
            return self.pop()

        temp = self.head
        for _ in range(index): 
            temp = temp.next

        temp.prev.next = temp.next
        if temp.next:  
            temp.next.prev = temp.prev
        self.length -= 1
        return temp.nim, temp.nama

    def print_list(self):
        temp = self.head
        while temp: 
            print(f"NIM: {temp.nim}, Nama: {temp.nama}")
            temp = temp.next

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append("2101", "Septia")
dll.append("2102", "Lutviana")
dll.append("2103", "Margarita")
dll.append("2404", "Celyesta")

# Menampilkan list awal setelah di append
print("Setelah Append/")
dll.print_list()

# Penghapusan di data terakhir
dll.pop()
print("\nSetelah Pop:")
dll.print_list()

# Menambahkan data baru di awal list
dll.prepend("2000", "Intan")
print("\nSetelah Prepend:")
dll.print_list()

# Menyisipkan data baru pada posisi tertentu
dll.insert(1, "2205", "Lintang")
print("\nSetelah Insert:")
dll.print_list()

# Menghapus data pada posisi tertentu
dll.remove(1)
print("\nSetelah Remove:")
dll.print_list()
