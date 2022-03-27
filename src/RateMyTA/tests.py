from django.test import TestCase
from .forms import SearchForm, SignupForm, TaRequestForm
from .forms import LoginForm, NewReviewForm

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

# #Luis
# class signupTests(TestCase):
#     #testing
#     def test_signupPage(self):

#     def test_validSignup(self):

#     def test_invalidSignupUserExists(self):

#     def test_invalidSignupIncompleteForm(self):

#     def test_invalidSignupEmailFormatError(self):  

# #John
# class viewSearchResults(TestCase):

#     def test_searchResultsPage(self):

#     def test_viewNoResults(self):

#     def test_viewOneResult(self):

#     def test_viewMultipleResults(self):

# #Adam
# class viewReviewResults(TestCase):

#     def test_reviewResultsPage(self):

#     def test_viewOneReview(self):

#     def test_viewNoReviews(self):

#     def test_viewMultipleReviews(self):

# #Leave for now
# class writeNewReview(TestCase):

#     def test_newReviewPage(self):

#     def test_newReviewFormNotComplete(self):

#     def test_newReviewValid(self):

# #Kenny
# class requestNewTa(TestCase):

#     def test_newTAPage(self):

#     def test_newTAFormNotComplete(self):

#     def test_newTAValid(self):