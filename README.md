# OrangeHRM test automation
by Maciej Sz.


This repo contains a simple script presenting how to use Selenium Webdriver (with Python) to go through [OrangeHRM demo website]('https://opensource-demo.orangehrmlive.com').

### Requirements
- Google Chrome
- chromedriver
- Python 3.6+

### Configuration
1. Add path of chromedriver's directory to PATH environmental variable:
```commandline
export PATH=$PATH:path/to/your/chromedriver/directory
```
2. Create Python virtual environment and activate it
```commandline
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages
```commandline
python3 -m pip install -r requirements.txt
```

### Test Scenarios
#### Scenario 1
```
a. Navigate to the test site in a browser
b. Try to login with any random username and password
c. Validate that the Invalid Credentials message is correctly displayed
```

#### Scenario 2
```
a. Navigate to the test site
b. Capture the Username and Password mentioned in the test screen
c. Use them and log in
d. Validate that upon successful login, you are able to see the logged in user (displayed at top right corner)
e. Print the Name of the user in the report

additional points:
f. Go to Buzz page
h. Write a new post
i. Validate if it's shown properly
```

### How to run
All test cases
```commandline
pytest tests -v --html=report.html --log-cli-level=info
```

You can also specify which part of test cases you would like to run, by adding `-m` param. For example, the command below will trigger tests marked as `happy` (happy path)

```commandline
pytest tests -v --html=report.html --log-cli-level=info -m happy
```

Available markers:
```text
    unhappy:    unhappy-path test cases
    happy:      happy-path test cases
    login:      test cases related to login process
    buzz:       test cases related to Buzz feeds
```

### What could be done more?

Of course, we could make full test coverage for this test CRUD :) Apart from that, there are 3 topics, which could be improved at this stage.

#### Selectors
Mostly, I was able to make stable XPath selectors (generic ones, not static). However, as you may see in `login_page.py`, there are 2 selectors, which are basing on parent's XPath. To improve the stability of the test framework and fluency of work, we should ask a dev team for better selectors (f.e. some additional attribute in searched elements).

#### Requirements
During developing this test framework, I had to base my actions on my experience and exploratory tests. There is one thing, which concerns me - difference between user name from dropdown and user name from Buzz post. In some cases, the dropdown shows f.e. `Michael Brown` and the Buzz feed shows `Michael J Brown`. Lack of requirements forced me to disable user name assertions in Buzz page.

#### Injecting API token in browser's console
For now, all test cases are preceded by `setup_method`, which processes login to OrangeHRM on frontend side. To save a time, we could try to inject a token from API to browser's memory (cookie or local storage).
I make a try in `playground/login_inject_check.py`. Something failed here, because frontend does not react to injected token. It's good to discuss it with a dev team.

Why is it useful? For bigger amount of test cases, every saved second sum to notable period of time saved.