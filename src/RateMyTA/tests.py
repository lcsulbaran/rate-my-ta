from django.test import TestCase
from .forms import SearchForm, SignupForm, TaRequestForm
from .forms import LoginForm, NewReviewForm, TaRequestForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate

# additional test cases are included in the seleniumTests folder
# the additional test cases are for demonstrating the flow between web pages

class loginTests(TestCase):

    # test that the login page is successfully rendered
    def test_loginPage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    # 
    def test_invalidLoginUserDoesNotExist(self):
        newUser = User.objects.create_user('harry', 'harry@email.com', 'pa$$word')
        user = authenticate(username = 'jaxson', password = 'pa$$word')
        self.assertEqual(user, None)

    # 
    def test_validLogin(self):
        newUser = User.objects.create_user('harry', 'harry@email.com', 'pa$$word')
        user = authenticate(username = 'harry', password = 'pa$$word')
        self.assertNotEqual(user, None)
        
    # 
    def test_incompleteLoginFormNotFilled(self):
        incompleteForm = LoginForm(data={
            'username': '',
            'password': ''
        })
        self.assertFalse(incompleteForm.is_valid())

        
class signupTests(TestCase):

     def test_signupPage(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

     def test_validSignup(self):
        response = self.client.post(reverse('signup'), {'name': 'testuser', 'email': 'test@email.com', 'password': 'pass123'}, format='text/html')
        self.assertEqual(response.status_code, 302)

     def test_invalidSignupUserExists(self):
        User.objects.create_user(username = 'testuser', email = 'test@email.com', password = 'hello123')
        response = self.client.post(reverse('signup'), {'name': 'testuser', 'email': 'test@email.com', 'password': 'pass123'},format='text/html')
        self.client.get('/signup/', follow = True)

     def test_invalidSignupIncompleteForm(self):
        form = SignupForm(data={
            'name': '',
            'email': '',
            'password': ''
         })
        self.assertFalse(form.is_valid())

        
class viewSearchResults(TestCase):

    # Tests that the search page returned is valid
    def test_searchPage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Tests that the search from is valid
    def test_validSearchForm(self):
        form = SearchForm(data={
            'searchQuery': 'John Appleseed'
        })
        self.assertTrue(form.is_valid())

        
class writeNewReview(TestCase):

    # Tests that the search page returned is valid
    def test_newReviewPage(self):      
        User.objects.create_user(username='testuser', email='test@mail.com', password='hello123')
        self.client.login(username='testuser', password='hello123')
        response = self.client.get('/new-review/')
        self.assertEqual(response.status_code, 200)

    # Tests to ensure that a form cannot be valid if it is incomplete
    def test_newReviewFormNotComplete(self):
        form = NewReviewForm(data={
            'courseCode': 'SENG 401',
            'title': 'Test Review',
            'body': 'Excellent TA...'
        })
        self.assertFalse(form.is_valid())

    # Tests to ensure that a completed form is valid
    def test_newReviewValid(self):
        form = NewReviewForm(data={
            'courseCode': 'SENG 401',
            'title': 'Test Review',
            'body': 'Excellent TA!',
            'rating': '10',
            'taID': '12345'
        })
        self.assertTrue(form.is_valid())


class requestNewTa(TestCase):

    def test_newTAPage(self):
        User.objects.create_user(username='testuser', email='test@mail.com', password='hello123')
        self.client.login(username='testuser', password='hello123')
        response = self.client.get('/ta-request/')
        self.assertEqual(response.status_code, 200)

    def test_newTAFormNotComplete(self):
        form = TaRequestForm(data={
            'name' : 'mike'
        })
        self.assertFalse(form.is_valid())

    def test_newTAValid(self):
        form = TaRequestForm(data={
            'name' : 'mike',
            'school': 'test school'
        })
        self.assertTrue(form.is_valid())
