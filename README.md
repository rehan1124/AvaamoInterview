# AvaamoInterview

* Clone the GitHub repo
* Navigate to directory/project and run command `python -m venv venv` for creating virtual environment, activate
  using `venv\Scripts\activate`
* Once virtual env is activated, install project dependencies by executing command `pip install -r requirements.txt`
* For running the tests, run `pytest -v -s`. Wait for test run to finish by itself.
* Generate Allure-reports using command `allure serve Reports` after test run finishes.
* Drill down to any test and on the right-side you will see screenshots attached for each and every step. This is done
  using decorators in `pages` directory page-object model classes.