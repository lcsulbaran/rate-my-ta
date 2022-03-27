from django.test import TestCase
from .forms import SearchForm, SignupForm, TaRequestForm
from .forms import LoginForm, NewReviewForm


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

    def test_searchResultsPage(self):

    def test_viewNoResults(self):

    def test_viewOneResult(self):

    def test_viewMultipleResults(self):

#Adam
class viewReviewResults(TestCase):

    def test_reviewResultsPage(self):

    def test_viewOneReview(self):

    def test_viewNoReviews(self):

    def test_viewMultipleReviews(self):

#Leave for now
class writeNewReview(TestCase):

    def test_newReviewPage(self):

    def test_newReviewFormNotComplete(self):

    def test_newReviewValid(self):

#Kenny
class requestNewTa(TestCase):

    def test_newTAPage(self):

    def test_newTAFormNotComplete(self):

    def test_newTAValid(self):