from django.test import TestCase
from .forms import SearchForm, SignupForm, TaRequestForm
from .forms import LoginForm, NewReviewForm, TaRequestForm
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


#Harry
class loginTests(TestCase):

    # done
    def test_loginPage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    # this might not be valid, could use selenium
    def test_invalidLoginUserDoesNotExist(self):
        newUser = User.objects.create_user('harry', 'harry@email.com', 'pa$$word')
        user = authenticate(username = 'jaxson', password = 'pa$$word')
        self.assertEqual(user, None)

    # this might not be valid, could use selenium
    def test_validLogin(self):
        newUser = User.objects.create_user('harry', 'harry@email.com', 'pa$$word')
        user = authenticate(username = 'harry', password = 'pa$$word')
        self.assertNotEqual(user, None)
        
    # done
    def test_incompleteLoginFormNotFilled(self):
        incompleteForm = LoginForm(data={
            'username': '',
            'password': ''
        })
        self.assertFalse(incompleteForm.is_valid())


# class signupTests(TestCase):
#     #testing
#     def test_signupPage(self):

#     def test_validSignup(self):

#     def test_invalidSignupUserExists(self):

#     def test_invalidSignupIncompleteForm(self):

#     def test_invalidSignupEmailFormatError(self):  

#John
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

    # The rest of the test cases are in Selenium. These include:
        # test_viewNoResults()
        # test_viewValidResults()

# Adam
# class viewReviewResults(TestCase):

#     def test_reviewResultsPage(self):

#     def test_viewOneReview(self):

#     def test_viewNoReviews(self):

#     def test_viewMultipleReviews(self):


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

#Kenny
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

