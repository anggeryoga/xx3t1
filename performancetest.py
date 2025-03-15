"""
Author: XX3T1
Deskripsi: Menguji performa website dengan Locust.
"""

from locust import HttpUser, task, between

class LoadTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_endpoint(self):
        self.client.get("/")

print("🔥 Jalankan dengan: locust -f performancetest.py --host=http://example.com")
