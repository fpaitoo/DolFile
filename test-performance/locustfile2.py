from locust import task, run_single_user
from locust import FastHttpUser


class lfile(FastHttpUser):
    host = "http://0.0.0.0:8000"
    default_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "0.0.0.0:8000",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/",
            headers={
                "Cache-Control": "max-age=0",
                "Cookie": "session=eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiZTBiZTk5M2Q3MzJmYjVkNjgyMzc1NmJiN2ZiMTlhMGJkNDkxOTA2YiJ9.Y680ew.G8K4ufO2ZKahUGVYj5TyGgniU9c",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login/",
            headers={
                "Cache-Control": "max-age=0",
                "Content-Length": "33",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "session=eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiZTBiZTk5M2Q3MzJmYjVkNjgyMzc1NmJiN2ZiMTlhMGJkNDkxOTA2YiJ9.Y680ew.G8K4ufO2ZKahUGVYj5TyGgniU9c",
                "Origin": "http://0.0.0.0:8000",
                "Referer": "http://0.0.0.0:8000/",
            },
            data="username=admin&password=letMePass",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/dashboard/",
            headers={
                "Cache-Control": "max-age=0",
                "Cookie": "session=.eJwljkuKAzEMBe_i9Swky3JbuUwjSzIJAzPQnaxC7h6F7N4HinqWfR1xXsvlfjzip-w3L5fC3oSMiaMPdkUcKmzNbYMg1ohal9hqtmpzDZfmIxZpJdWmFpWASRJhoNRNP7dwBsUkDvMhFRHBmIUpNu5tIYFFJ6ghWlLkccbxtcGsdh5rv___xl8OATOS7hvVNdn7qJSIObc1URRm2qNAn-X1Bl7mP94.Y7B6LA.3GNOzr_qJ1FffpP0tLfSgfkaToU",
                "Referer": "http://0.0.0.0:8000/",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/logout/",
            headers={
                "Cookie": "session=.eJwljkuKAzEMBe_i9Swky3JbuUwjSzIJAzPQnaxC7h6F7N4HinqWfR1xXsvlfjzip-w3L5fC3oSMiaMPdkUcKmzNbYMg1ohal9hqtmpzDZfmIxZpJdWmFpWASRJhoNRNP7dwBsUkDvMhFRHBmIUpNu5tIYFFJ6ghWlLkccbxtcGsdh5rv___xl8OATOS7hvVNdn7qJSIObc1URRm2qNAn-X1Bl7mP94.Y7B6LA.3GNOzr_qJ1FffpP0tLfSgfkaToU",
                "Referer": "http://0.0.0.0:8000/dashboard/",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/login/",
            headers={
                "Cookie": "session=eyJjc3JmX3Rva2VuIjoiZTBiZTk5M2Q3MzJmYjVkNjgyMzc1NmJiN2ZiMTlhMGJkNDkxOTA2YiJ9.Y7B6UA.TTBO1GYuf3I9ekK75NUW0BBOXmA",
                "Referer": "http://0.0.0.0:8000/dashboard/",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(lfile)
