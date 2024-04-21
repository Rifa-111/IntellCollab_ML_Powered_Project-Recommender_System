import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    
    # Ensure that the index page returns a 200 status code
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
    
    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Login' in response.data)
    
    # Ensure that the login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', 
                               data=dict(username="test_user", password="test_password"), 
                               follow_redirects=True)
        self.assertIn(b'Welcome', response.data)
    
    # Ensure that the login behaves correctly given incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', 
                               data=dict(username="wrong_user", password="wrong_password"), 
                               follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)
    
    # Add more test cases as needed...
    
if __name__ == '__main__':
    unittest.main()





















''' import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    
    
    # Ensure that the index page returns a 200 status code
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
    
    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Login' in response.data)
    
    # Ensure that the login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', 
                               data=dict(username="test_user", password="test_password"), 
                               follow_redirects=True)
        self.assertIn(b'Welcome', response.data)
    
    # Ensure that the login behaves correctly given incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', 
                               data=dict(username="wrong_user", password="wrong_password"), 
                               follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)
    
    # Add more test cases as needed...
    
if __name__ == '__main__':
    unittest.main()
 '''