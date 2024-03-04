# AvaamoInterview

### Following is the structure of project

| Folder / Directory | Purpose                                                             |
|--------------------|---------------------------------------------------------------------|
| envconfig          | Holds `config.ini` file for configuration related things            |
| pages              | Base class + Page-object classes                                    |
| Reports            | Allure report is generated here                                     |
| tests              | Automated tests are stored in this package                          |
| utils              | Utilities such as reading config file or excel file are stored here |
| app_exceptions     | Custom exceptions are defined here                                  |
| README_IMAGES      | README file specific images                                         |

### To get started, go step-by-step as mentioned below

* Clone the GitHub repo
* Navigate to directory/project and run command `python -m venv venv` for creating virtual environment, activate
  using `venv\Scripts\activate`
* Once virtual env is activated, install project dependencies by executing command `pip install -r requirements.txt`
* For running the tests, run `pytest -v -s`. Wait for test run to finish by itself.
* Generate Allure-reports using command `allure serve Reports` after test run finishes.

![AllTestPassedReport.png](README_IMAGES%2FAllTestPassedReport.png)

* Drill down to any test and on the right-side you will see screenshots attached for each and every step. This is done
  using decorators in `pages` directory page-object model classes.

![ScreenshotForEveryStep.png](README_IMAGES%2FScreenshotForEveryStep.png)

![ScreenshotForEveryStep2.png](README_IMAGES%2FScreenshotForEveryStep2.png)

* Framework also supports adding pytest markers `pytest -m smoke` or `pytest -m regression`. As of now, you can use
  tags `smoke` and `regression` for test classification purpose.
* If any of the step fails, framework will automatically capture failing step screenshot using
  fixture `capture_screenshot`, which can then be viewed in teardown section with screenshot name `FailedStep`.

![FailingTest.png](README_IMAGES%2FFailingTest.png)

![FailingTestScreenshot.png](README_IMAGES%2FFailingTestScreenshot.png)

![FailingTestScreenshot2.png](README_IMAGES%2FFailingTestScreenshot2.png)
