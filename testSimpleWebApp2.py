import unittest

from simpleWebApp2 import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.data.decode()
        assert "You can do the following:" in html
    
    def test_viewMap(self):
        response = self.client.get("/viewMap")
        assert response.status_code == 200
        html = response.data.decode()
        assert "This is the view map page" in html

if __name__ == "__main__":
    unittest.main()