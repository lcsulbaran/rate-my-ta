from django.test import TestCase
from .forms import SearchForm, SignupForm, TaRequestForm
from .forms import LoginForm, NewReviewForm
from django.contrib.auth.models import User


#Harry
class loginTests(TestCase):

    def test_loginPage(self):
    # testing
    def test_invalidLoginUserDoesNotExist(self):

    def test_validLogin(self):

    def test_incompleteLoginFormNotFilled(self):

#Luis
class signupTests(TestCase):
    #testing
    def test_signupPage(self):

    def test_validSignup(self):

    def test_invalidSignupUserExists(self):

    def test_invalidSignupIncompleteForm(self):

    def test_invalidSignupEmailFormatError(self):  

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

Adam
class viewReviewResults(TestCase):

    def test_reviewResultsPage(self):

    def test_viewOneReview(self):

    def test_viewNoReviews(self):

    def test_viewMultipleReviews(self):


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

    def test_newTAFormNotComplete(self):

    def test_newTAValid(self):