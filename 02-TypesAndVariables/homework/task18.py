from cmath import sqrt


a = int(input('first side is (cm) ')) 
b = int(input('second side is (cm) '))
c = int(input('third side is (cm) '))

semi = (a + b + c)/2
area = sqrt(semi*(semi-a)*(semi-b)*(semi-c))

print(f"area is {area} cm2")