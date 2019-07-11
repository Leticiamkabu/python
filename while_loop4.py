def event():
    fn = int( input ("Enter first number"))
    sn = int( input ("Enter second number"))

    even_number = []

    for number in range(fn,sn):
      if number % 2 ==0:
         even_number.append(number)

    return even_number

def reverse_event():
    even_numbers = event()
    even_numbers.reverse()
    return even_numbers

reverses = reverse_event()
print(reverses)
