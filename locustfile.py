from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def health_check(self):
        self.client.get("/health")

    @task(2)
    def create_ticket(self):
        self.client.post("/tickets/", json={
            "concert_name": "Concert A",
            "user_name": "User1",
            "status": "available"
        })

    @task(2)
    def read_tickets(self):
        self.client.get("/tickets/")

    @task(1)
    def read_ticket(self):
        # Supongamos que el ID 1 existe
        self.client.get("/tickets/1")

    @task(1)
    def update_ticket(self):
        # Supongamos que el ID 1 existe
        self.client.put("/tickets/1", json={
            "concert_name": "Concert A Updated",
            "user_name": "User1",
            "status": "reserved"
        })

    @task(1)
    def delete_ticket(self):
        # Supongamos que el ID 1 existe
        self.client.delete("/tickets/2")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Tiempo de espera entre tareas