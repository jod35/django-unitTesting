from django.test import TestCase,SimpleTestCase
from django.test import RequestFactory
from . views import index,about
# from django.shortcuts import render_to_response
from django.contrib.auth.models import User

# Create your tests here.
###################################
#######test overall application####
###################################
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
            Testing for 1+1 =2
        """

        self.assertEqual(1+1,2)

##############################################
########testing template functionality########
##############################################
class TestTemplates(SimpleTestCase):

    #this method is short but runs for long

    # def test_index_html_template(self):
    #     index=self.client.get('/')

    #     self.assertTemplateUsed(index,'myapplication/index.html')


    #longer alternative because it tests for only one thing
    #index page
    def test_index_html_template2(self):
        request_factory=RequestFactory() #helps us to create mock request objects for testing

        #we create the request

        request=request_factory.get('/') #this gets '/' route

        request.session={} # associate the request with a session

        #we create our response which is simply a call to our view function

        response=index(request)

        #to verify
        self.assertContains(response,"<title>Test App</title>") # this passes 

    

    # about_page
    def test_about_html_template(self):
        request_factory=RequestFactory()

        request=request_factory.get('/about/')

        request.session={}

        response=about(request)

        self.assertContains(response,"<h1>About Page</h1>")

    def test_about_template(self):
        about=self.client.get('/about/')


        self.assertTemplateUsed(about,'myapplication/about.html')


    #verify whether the view returns the correct HTML
    # def test_returns_exact_html(self):
    #     index=self.client.get('/about')

    #     self.assertEqual(index.content,render_to_response('myapplication/about.html').content)



# Testing status code (if valid view functions)

################################################
#############Testing Views######################
################################################
class TestStatusCodes(TestCase):
    def test_index_view_status_code(self):
        index_view=self.client.get('/')

        self.assertEqual(index_view.status_code,200)
        #verify whether the index view returns a status code of 200
    

    def test_about_view_status_code(self):
        about_view=self.client.get('/about/')

        self.assertEqual(about_view.status_code,200)




#######################################
########Testing Database Models########
#######################################

class TestModel(TestCase):
    def test_user_creation(self):
        #create a user instance and save it in the db
        User(username="jojo",email='jojo@test.com',is_superuser=True).save()

        users_in_db=User.objects.all() #query for all users in the test db


        self.assertEqual(users_in_db.count(),1) #verify number of entries in db
