numbers = [23, 5, 89, 43, 12, 7]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("hamgiin ih too", max_value)
print("hamgiin baga too ", min_value)
