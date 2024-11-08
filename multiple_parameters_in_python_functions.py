dictionary = {
  7: "first",
  3: "second",
  4: "third",
  8: "fourth",
  9: "fifth",
}

my_list = [int(n) for n in input().split()]

for num in my_list:
    if num in dictionary:
        print(dictionary[num])
    else:
        print("Not found")