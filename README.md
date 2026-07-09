# learn-python

## July 8, 2026
For Loop: List
```
dogs = ["Bulldog", "Beagle", "Poodle", "Labrador"]

for dog in dogs: 
    print(dog)
```
`dog` is storing a variable from the list

For Loop: Numbers
`range()` - generate series of numbers
```
for value in range(1, 5): 
    print(value)

1
2
3
4
```
to create a list use `list()`
```
numbers = list(range(1, 6))
print(numbers)
[1, 2, 3, 4, 5]
```

simple stat function
`min()`, `max()`, `sum()`

list comprehension
```
squares = [value**2 for value in range(1, 11)]
print(squares)
[1, 4, 9. 16, 25, 36, 49, 64, 81, 100]
```

Slice
```
players = ['a', 'b', 'c', 'd', 'e']
print(players[0:3])
['a', 'b', 'c']
```

you can also copy list by 
```
my_foods = [pizza, flafel, carrot cake]
friend_foods = my_foods[:]
```
this will show exact same list
and we can manipulate each of the lists separately. 

## July 7, 2026
string manipulation
- .strip(): strips the whitespace 
- .title() 
- .upper() and .lower()

List manipulation
- .append(): adds the end of the list
- .insert(index, new element): adds the new element by specifying the index
- del: if you know the position of the item from the list
- .pop(): removes last element in a list
- .pop(index): removes item in a list at any poistion 
**** when you want to delete an item from a list and not use that item in any way, use `del`
**** when you wan to use an item as you remove it, use `pop()` mthod
- .remove(): you don't know the position, but you know the item

Organizaing a list
- .sort(): alphabetical order. sort permanant 
- .sorted(): maintains original list, but temporarily 
- .reverse(): reverse the orignal order
- len(list): identify number of items in list