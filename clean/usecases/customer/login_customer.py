class LoginCustomerUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, email, password):
        customer = self.repository.find_by_email(email)
        if not customer or customer.password != password:
            raise Exception("Invalid credentials")
        return customer
