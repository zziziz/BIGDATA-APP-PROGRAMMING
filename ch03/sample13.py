my_book = (2002, '파이썬', 200)

your_book = [2002, '파이썬', 200]


#other_book = [your_book[0], your_book[1], your_book[2], your_book[3]]
other_book = your_book[0:4]
print(my_book)
print(your_book)

other_book[0] = 2025

print(other_book)
print(your_book)

print(id(my_book))
print(id(your_book))#yourbook = otherbook의 주소는 같음
print(id(other_book))


new_book = your_book[1:3]
print(new_book)

new_book2 = my_book[1:3]
print(new_book2)