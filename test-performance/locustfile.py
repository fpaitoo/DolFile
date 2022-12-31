from locust import task, run_single_user
from locust import FastHttpUser


class filebank_locust(FastHttpUser):
    host = "http://127.0.0.1:8000"
    default_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "127.0.0.1:5000",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/login/",
            headers={
                "Cookie": "backendVersion=1.1.2.3249; localauth=localapi43e98ce38fbb1d1d:; isNotIncognito=true; _ga=GA1.1.966465648.1607208089; TawkConnectionTime=0; csrftoken=vi0meEfM2AjPIhlWlUbLzOUDecYe4L8G2qCokt0LutUzc1QI5RKybF9AaOdR18lk; session=.eJztkjEKgDAQBL9ybB18QF5hL0GOcDGB04iXLuTv5huC1RYz023HnpQti8FvHdTm4BQzPgQOqwqbkNaDykWtEsc4IbVcjO7pLAjD_d2nu-DmCR6xDJ9YTcYLnp-xlg.Y6dHjw.Q8u8hOjhtDGU2ntxURvEEgiOYSI",
                "Sec-Fetch-Site": "none",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/login/",
            headers={
                "Content-Length": "32",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "backendVersion=1.1.2.3249; localauth=localapi43e98ce38fbb1d1d:; isNotIncognito=true; _ga=GA1.1.966465648.1607208089; TawkConnectionTime=0; csrftoken=vi0meEfM2AjPIhlWlUbLzOUDecYe4L8G2qCokt0LutUzc1QI5RKybF9AaOdR18lk; session=.eJztkjEKgDAQBL9ybB18QF5hL0GOcDGB04iXLuTv5huC1RYz023HnpQti8FvHdTm4BQzPgQOqwqbkNaDykWtEsc4IbVcjO7pLAjD_d2nu-DmCR6xDJ9YTcYLnp-xlg.Y6dHjw.Q8u8hOjhtDGU2ntxURvEEgiOYSI",
                "Origin": "http://127.0.0.1:8000",
                "Referer": "http://127.0.0.1:8000/login/",
                "Sec-Fetch-Site": "same-origin",
            },
            data="username=admin&password=letMePass",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/dashboard/",
            headers={
                "Cookie": "backendVersion=1.1.2.3249; localauth=localapi43e98ce38fbb1d1d:; isNotIncognito=true; _ga=GA1.1.966465648.1607208089; TawkConnectionTime=0; csrftoken=vi0meEfM2AjPIhlWlUbLzOUDecYe4L8G2qCokt0LutUzc1QI5RKybF9AaOdR18lk; session=.eJztUsuKwzAM_BWjc1hsy0rtfMXel1KELDeB7LbEyan031fLfkWhJ42YB3OYB1zayn3WDtPXA9xuB761d74qDPC5Knd16-3qlh-33xyLGOn2eenubpoPOD-Ht--lfefBRrBpn2Hat0PtWypMQDUVFELSMVPlEDIXklTl5BWJVWNsRVqSFlNlrSXVrA05InNi0YiesFiEeMZR-I8uZICDJWapucQQgheiQqgnGlML6EVH9FELW_3L0XX7bxPg-Qu999tl.Y6dHwA.8CiLzVrXrBP7aCqvIwR8km6eUnU",
                "Referer": "http://127.0.0.1:8000/login/",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            # print(resp.text)
            pass


if __name__ == "__main__":
    run_single_user(filebank_locust)
