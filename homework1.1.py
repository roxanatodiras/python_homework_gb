'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
то треугольника с такими сторонами не существует. 
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
'''

a = int(input('please input the first side of the triangle: '))
b = int(input('please input the second side of the triangle: '))
c = int(input('please input the third side of the triangle: '))

if (a + b) < c or (a + c) < b or (b + c) < a:
    print("you can't have a triangle with such sides")
elif a == b == c:
    print("the triangle is equilateral")
elif  a == b  or a == c or c == b:
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")
    