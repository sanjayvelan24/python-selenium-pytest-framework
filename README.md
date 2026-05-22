# Python Selenium PyTest Framework

A Selenium automation framework built with Python, PyTest, and the Page Object Model (POM) design pattern. Tests are written against the [OrangeHRM demo application](https://opensource-demo.orangehrmlive.com).

## Project Structure
python-selenium-pytest-framework/
├── config/
│   └── config.py
├── pages/
│   ├── LoginPage.py
│   ├── LogoutPage.py
│   ├── PIMPage.py
│   └── SearchEmployee.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_PIM.py
│   └── test_searchEmployee.py
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
pip install -r requirements.txt
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
