my_book = (2002, '파이썬', 200)
print(my_book)
print(type(my_book))

your_book = [2002, '파이썬', 200]
print(your_book)
print(type(your_book))

year, title, size = your_book
print(year)
print(title)
print(size)

print('-'*50)
print(your_book[0])
print(your_book[1])
print(your_book[2])

print('-'*50)
print(your_book[-1])
print(your_book[-2])
print(your_book[-3])


#기존 데이터 변경
your_book[0] = 2025
print(your_book)

#추가도 가능
your_book.append('파이썬 프로그래밍')
print(your_book)

#특정 위치에 추가하고 싶다면//
your_book.insert(1, '프로그래밍 과목')
print(your_book)

#삭제
if '파이썬2' in your_book: #error 없이 출력 안 됨
 your_book.remove('파이썬')
print(your_book)