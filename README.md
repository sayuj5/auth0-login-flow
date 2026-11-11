# Auth0 Login Flow with Flask

A simple web application demonstrating Auth0 authentication using Python and Flask.

## Features

- 🔐 Login with Auth0 Universal Login
- 👤 View user profile after authentication
- 🚪 Logout functionality
- 🔒 Protected routes
- 🌐 Built with Flask and Auth0 Python SDK

## Tech Stack

- **Python** with Flask framework
- **Auth0** for authentication
- **Auth0 Python SDK** (`auth0-server-python`)
- **python-dotenv** for environment variables

## Setup

### Prerequisites
- Python 3.8+
- An Auth0 account (free at [auth0.com](https://auth0.com))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sayuj5/auth0-login-flow.git
   cd auth0-login-flow
   ```

2. Install dependencies:
   ```bash
   pip install "auth0-server-python>=1.0.0b1,<2" "flask[async]" python-dotenv markupsafe
   ```

3. Create a `.env` file:
AUTH0_DOMAIN=your-domain.us.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
AUTH0_SECRET=64-character-random-string
APP_BASE_URL=http://localhost:5000
PORT=5000

4. Run the application:
   ```bash
   python app.py
   ```

5. Open `http://localhost:5000` in your browser

## Auth0 Configuration

In your Auth0 dashboard, set:
- **Allowed Callback URLs**: `http://localhost:5000/callback`
- **Allowed Logout URLs**: `http://localhost:5000`
- **Allowed Web Origins**: `http://localhost:5000`

## Project Structure

auth0-login-flow/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── .gitignore # Git ignore rules
└── README.md # Project documentation


## Built With

This project was built as part of **Global Hack Week: Builders Week** using GitHub Copilot to generate the initial codebase.
