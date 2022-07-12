# PyTest
Tasks for test automation for educational courses  
The /Calculator directory contains files for task 19.2.3
<ul>
<li>Calculator.py contains the main logic of the program</li>
<li>first_test.py contains several tests for Calculator.py</li>
</ul> 
The /API directory contains files for task 19.7.2
<ul>
<li>settings.py contains valid test data</li>
<li>api.py contains an interface for interacting with the application</li>
<li>/tests directory contains files: test_pet_good.py with some positive and test_pet_bad.py with some negative tests</li>
</ul> 
The api library is written in a class. The base_url variable is used when generating the url for the request.
Methods have a subgeneric description.
Tests check the work of methods using the api library.

Bug has been detected in the GET-request for the site's API-login: the user login with any username and password.

The /test_selenium directory contains file for task 25.5.1
<ul>
<li>test_petfriend.py contains several tests using 'find_elements', 'WebDriverWait' and 'implicitly_wait' from selenium</li>
</ul> 

