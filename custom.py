class Customer:
    def __init__(self, name, member_ship):
        self.name = name
        self.member = member_ship


customer1 = Customer('Hasnat', 'Gold')
print(customer1.name, customer1.member)

customer2 = Customer('Tarek', 'Silver')
print(customer2.name, customer2.member)


