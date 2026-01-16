class ViewCartUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, customer_id):
        return self.repo.get_by_customer(customer_id)
