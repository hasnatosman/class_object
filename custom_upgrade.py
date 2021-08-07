class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def upgrade_membership(self, new_member):
        self.membership_type = new_member


customer1 = Customer('Hasnat', 'Gold')
print(customer1.name, customer1.membership_type)


customer1.upgrade_membership('Silver')
print(customer1.name, customer1.membership_type)


