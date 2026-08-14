# Python Playwright Automation Framework

Python-based web automation framework using **Playwright, Pytest, Page Object Model (POM), API testing, and network interception**.

The project demonstrates UI automation combined with API-driven test setup and backend response interception for validating real-world web application scenarios.

## Tech Stack

* **Python**
* **Playwright**
* **Pytest**
* **Pytest Playwright**
* **API Testing**
* **Page Object Model (POM)**

## Framework Structure

```text
pythonPlaywrightFramework/
│
├── pageObject/
│   ├── LoginPage.py
│   ├── HomePage.py
│   ├── OrdersHistoryPage.py
│   └── OrderSummaryPage.py
│
├── utilities/
│   ├── apiBase.py
│   └── networkRoutes.py
│
├── testCases/
│   ├── test_web_api.py
│   └── test_interceptingNetworking.py
│
├── testData/
│   └── userCredentials.json
│
├── feature/
│   └── orders.feature
│
└── conftest.py
```

## Key Features

* Playwright UI automation with Pytest
* Page Object Model
* Cross-browser support for Chromium and Firefox
* API-based test data/setup
* Network request interception and response mocking
* Parameterized tests
* Reusable fixtures through `conftest.py`
* Positive and negative test scenarios

## Test Scenarios

### API + UI Validation

Creates an order through the API and verifies the order through the web UI.

```text
API
 ↓
Create Order
 ↓
Login
 ↓
Orders History
 ↓
Select Order
 ↓
Verify Order Summary
```

### Network Interception

Intercepts backend API responses to validate frontend behavior for:

* No orders returned
* Unauthorized order access

```text
Browser
   ↓
Intercept API Request
   ↓
Mock / Modify Response
   ↓
Verify UI Behavior
```

## Setup

Install the required dependencies:

```bash
pip install pytest pytest-playwright
playwright install
```

Configure test credentials using a secure local configuration or environment variables.

## Run Tests

Run the complete test suite:

```bash
pytest
```

Run with a specific browser:

```bash
pytest --browser_name=chrome
```

or:

```bash
pytest --browser_name=firefox
```

## Project Focus

This project focuses on demonstrating practical Playwright automation concepts beyond basic UI testing, including:

* UI automation
* API integration
* Network interception
* Test data management
* Page Object Model
* Pytest fixtures and parameterization

## Future Improvements

* Improve configuration and environment management
* Move credentials to environment variables
* Add stronger assertions and reporting
* Add CI/CD with GitHub Actions
* Expand cross-browser coverage
* Improve test data management

## Author

**Kavin**

Software QA Engineer / SDET

[GitHub](https://github.com/kavin-crypto)
