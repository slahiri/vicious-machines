import urllib.request


class AppTest:
    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen('http://localhost:5000/')
        self.assertEqual(response.code, 200)
