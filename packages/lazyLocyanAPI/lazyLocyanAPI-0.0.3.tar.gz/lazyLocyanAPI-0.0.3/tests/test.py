import unittest
from lazyLoCyanAPI.LoCyanAPI import LoCyanAPI


class TestAPI(unittest.TestCase):
    api = LoCyanAPI()

    def test_list_proxy(self):
        print(f"(list)token: {self.api.login_token}, username: {self.api.username}")
        print(self.api.get_user_proxies())

    def test_login(self):
        test = self.api.login("MojaveHao", "haojunjie2009")
        print(f"login: {test},token: {self.api.login_token}, username: {self.api.username}")
        info = self.api.get_user_info()
        print(f"user info:{info}")


if __name__ == '__main__':
    unittest.main()
