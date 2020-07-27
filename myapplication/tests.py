from django.test import TestCase,SimpleTestCase
from django.test import RequestFactory
from . views import index,about

# Create your tests here.

class TestTemplates(SimpleTestCase):

    #this method is short but runs for long

    # def test_index_html_template(self):
    #     index=self.client.get('/')

    #     self.assertTemplateUsed(index,'myapplication/index.html')


    #shorter alternative
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

    

    #about_page
    def test_about_html_template(self):
        request_factory=RequestFactory()

        request=request_factory.get('/about/')

        request.session={}

        response=about(request)

        self.assertContains(response,"<h1>About Page</h1>")







