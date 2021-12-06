
from locust import HttpUser, TaskSet, task, between, constant
import os

class UserBehavior(TaskSet):
    @task(1)
    def login(self):

        l = os.environ['LOCUST_PARAM'].split(';')
        tmp = map(lambda s:s.split('='), l)
        param = dict(tmp)

        self.client.post(os.environ['LOCUST_TARGET_PATH'], param)

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(1)

