from locust import task, HttpUser, between


class WebsiteUser(HttpUser):
    host = "https://votinghubgh.com"
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/categories/60/0")
