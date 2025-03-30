## **Web Automation with pytest**

This project is an automation test suite built using **Python** and **Selenium** for the **OrangeHRM** application. The suite is designed to perform end-to-end testing of the login functionality and to ensure that the core functionality of the web application works as expected. The tests are written using **pytest** and are structured to be easily extensible for future test cases.

## Video

https://github.com/user-attachments/assets/5f4d70d0-446c-4afe-b873-8b05ab81f2fe

## **Technologies Used**
- **Python 3.x**
- **Selenium WebDriver** for browser automation
- **pytest** for running the tests and managing test cases
- **pytest-html** for generating HTML reports
- **Firefox WebDriver** for testing in a Firefox browser

---

## Test Scenarios

### **Test Scenario 1: Login with Valid Credentials**
1. **Test Objective**: Verify that the user can successfully log in with valid credentials.
2. **Test Steps**:
    1. Navigate to the OrangeHRM login page.
    2. Enter the username (`Admin`).
    3. Enter the password (`admin123`).
    4. Click the login button.
3. **Expected Result**: The user is redirected to the dashboard page and the URL should contain the keyword "dashboard".

---

### How to Run Tests

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests using pytest:
    ```bash
    pytest --html=report.html
    ```

3. After the tests run, an HTML report will be generated in the `report.html` file.

## Screenshot (Report)

![image](https://github.com/user-attachments/assets/f8f26019-9af8-44d5-9374-e98b200b1f90)

