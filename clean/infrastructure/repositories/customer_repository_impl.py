from framework.bookstore.models import CustomerModel
from domain.entities.customer import Customer

class DjangoCustomerRepository:
    def create(self, name, email, password):
        customer = CustomerModel.objects.create(
            name=name,
            email=email,
            password=password
        )
        return Customer(
            customer.id,
            customer.name,
            customer.email,
            customer.password
        )

    def get_by_id(self, customer_id):
        c = CustomerModel.objects.get(id=customer_id)
        return Customer(c.id, c.name, c.email, c.password)
