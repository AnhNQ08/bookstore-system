class RegisterCustomerUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, name, email, password):
        return self.repo.create(name, email, password)
