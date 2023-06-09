# Web Automation Example using Python

This is a Python Selenium project for automating user login in a web application.


## Prerequisites

* Python 3.x
* Chrome or Firefox browser
* Selenium
* webdriver-manager 
* behave (for the BDD Features)

You can install the required packages by running the following command:
```
pip install -r requirements.txt

```

## Running the Tests

To run the LoginTestCase.py file, use the following command:
```
python LoginTestCase.py

```

Note: Before running the test case, make sure that the webdriver executable file for the browser you are using is in the project
If not, you can add it.

## Running the BDD tests

Tu run the LoginTestCase.feature, use the following command:
```
behave feature/LoginTestCase.feature
```