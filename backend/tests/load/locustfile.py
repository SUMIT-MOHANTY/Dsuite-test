from locust import HttpUser, task, between

class CalculatorUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def calculate(self):
        self.client.post("/calculate", data={
            'num1': 100,
            'num2': 200,
            'operation': 'add'
        })

    @task(1)
    def home_page(self):
        self.client.get("/")
