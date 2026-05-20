# Python Selenium PyTest Framework

A Selenium automation framework built with Python, PyTest, and the Page Object Model (POM) design pattern. Tests are written against the [OrangeHRM demo application](https://opensource-demo.orangehrmlive.com).

## Project Structure
python-selenium-pytest-framework/
├── config/
│   └── config.py          # Central configuration (URL, browser, wait times)
├── pages/
│   ├── LoginPage.py        # Login page actions
│   ├── LogoutPage.py       # Logout page actions
│   ├── PIMPage.py          # PIM module page actions
│   └── SearchEmployee.py   # Search employee page actions
├── tests/
│   ├── conftest.py         # PyTest fixtures (driver setup and teardown)
│   ├── test_login.py       # Login test cases
│   ├── test_logout.py      # Logout test cases
│   ├── test_PIM.py         # PIM module test cases
│   └── test_searchEmployee.py  # Search employee test cases
├── .gitignore
├── pytest.ini
└── README.md

## Tech Stack

- Python 3.x
- Selenium WebDriver
- PyTest
- WebDriver Manager
- Page Object Model (POM)

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/sanjayvelan24/python-selenium-pytest-framework.git
cd python-selenium-pytest-framework
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install selenium pytest webdriver-manager
```

## Running Tests

Run all tests:
```bash
pytest -v
```

Run a specific test file:
```bash
pytest tests/test_login.py -v
```

## Configuration

All configuration is managed in `config/config.py`:
- `BASE_URL` — application URL
- `BROWSER` — browser to use
- `IMPLICIT_WAIT` — global wait time in seconds
