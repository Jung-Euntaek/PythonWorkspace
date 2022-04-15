from item import Item
# from phone import Phone

# Item.instantiate_from_csv()

# print(Item.all)

item1 = Item("MyItem", 750)
item1._name = "OtherItem"

print(item1._name)
item1.read_only_name = "AAA" # read_only_name 은 property 이므로 변경 불가

item1.send_email()