'''
string = input("Введите строку: ")
string = string.lower().replace(" ","")
st = string[::-1]

print(st == string)


# Задание 2

names:list[str] = []
s:list[str] = input('').split()

for name in s:
    if name.isalpha():
        names.append(name.capitalize())
print(sorted(names))


# Задание 3
ages_str:list[str] = input("")

ages = [int(s.split()[0]) for s in ages_str]

print("Максимальный:", max(ages))
print("Минимальный:", min(ages))
print("Средний:", sum(ages) / len(ages))


# Задание 4

s = input("")

for ch in sorted(set(s), key = s.count):
    print(ch, s.count(ch))


# Задание 5
def input_str():
    return input()

numbers = list(map(int, input_str().split()))

def f(s):
    count = 0
    for i in s:
        if i >=0 :
            count+=1
    return count

print(f(numbers)) 
'''

# Задание 6

def sum_of_digits(text: str) -> int:
    return sum(list(map(lambda x: int(x), filter(lambda x: x.isdigit(), text))))

# Задание 7
class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self) -> str:
        return f"{self.name}: {self.price}р, {self.quantity}шт"

class Warehouse:
    def __init__(self) -> None:
        self.products = []
    
    def add(self, name: str, price: float, quantity: int) -> None:
        self.products.append(Product(name, price, quantity))
    
    def remove(self, name: str) -> None:
        self.products = list(filter(lambda p: p.name != name, self.products))
    
    def edit(self, name: str, price: float = None, quantity: int = None) -> None:
        product = next(filter(lambda p: p.name == name, self.products), None)
        if product:
            if price is not None: product.price = price
            if quantity is not None: product.quantity = quantity
    
    def show_alphabetical(self) -> list[Product]:
        return sorted(self.products, key=lambda p: p.name)
    
    def show_by_price(self, ascending: bool = True) -> list[Product]:
        return sorted(self.products, key=lambda p: p.price, reverse=not ascending)
    
    def search(self, name: str) -> list[Product]:
        return list(filter(lambda p: name.lower() in p.name.lower(), self.products))


if __name__ == "__main__":
    print(sum_of_digits("Вчера мне было 17 годиков, а сегодня мне уже 18 лет!"))
    print(sum_of_digits("Эта строка совсем-совсем без цифр..."))

    warehouse = Warehouse()
    warehouse.add("Яблоки", 100, 50)
    warehouse.add("Бананы", 80, 30)
    warehouse.add("Апельсины", 120, 40)

    warehouse.edit("Яблоки", price=110)
    warehouse.remove("Бананы")

    print(warehouse.show_alphabetical())
    print(warehouse.show_by_price(ascending=True))
    print(warehouse.search("ябл"))
