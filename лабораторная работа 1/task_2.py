num_pages = 100
num_string = 50
num_char = 25
byte_in_char = 4
memory_diskette = 1.44

memory_diskette_in_byte = memory_diskette * 1024 * 1024
num_char_in_book = num_pages * num_string * num_char

size_book = num_char_in_book * byte_in_char

num_book = memory_diskette_in_byte // size_book
num_book = int(num_book)
print("Количество книг, помещающихся на дискету:", num_book)
