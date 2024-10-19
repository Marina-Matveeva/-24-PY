# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44*1024*1024
number_of_pages = 100
number_of_lines = 50
number_of_char = 25
total_char = number_of_char*number_of_lines*number_of_pages
total_bytes = total_char*4
number_of_books = int(volume // total_bytes)
print("Количество книг, помещающихся на дискету:", number_of_books)