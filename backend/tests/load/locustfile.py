from locust import HttpUser, task, between
import random

# --------------------------------------------------------------------------
# Locust file to hit /calculate with realistic load.
# --------------------------------------------------------------------------

class CalculatorLoadTest(HttpUser):
    wait_time = between(0.5, 1.5)  # light human-emulation

    def on_start(self):
        # Warm-up fetch; not measured directly
        self.client.get("/", verify=False)

    @task(weight=20)
    def add(self):
        self._hit_calc("add", 1, 100)

    @task(weight=15)
    def subtract(self):
        self._hit_calc("subtract", 1, 100)

    @task(weight=15)
    def multiply(self):
        self._hit_calc("multiply", 0, 10)

    @task(weight=8)
    def divide(self):
        self._hit_calc("divide", 1, 50)

    def _hit_calc(self, op, lo, hi):
        payload = dict(
            num1=random.uniform(lo, hi),
            num2=random.uniform(lo, hi),
            operation=op,
        )
        with self.client.post(
            "/calculate", data=payload, verify=False, catch_response=True
        ) as resp:
            if resp.status_code != 200:
                resp.failure("Non-200 status")
                return
            try:
                js = resp.json()
                if not js.get("success"):
                    resp.failure(js.get("error"))
            except ValueError:
                resp.failure("Invalid JSON")
