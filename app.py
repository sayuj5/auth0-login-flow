import os
from functools import wraps
from urllib.parse import urlencode, quote_plus

from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from flask import Flask, redirect, render_template_string, session, url_for

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-me")

oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


def login_required(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("home"))
        return view_func(*args, **kwargs)

    return wrapped


@app.route("/")
def home():
    user = session.get("user")
    return render_template_string(
        """
        <h1>Auth0 Login Flow</h1>
        {% if user %}
          <p>Signed in as {{ user.get('name') or user.get('email') or user.get('sub') }}</p>
          <a href="{{ url_for('profile') }}">View Profile</a><br>
          <a href="{{ url_for('logout') }}">Logout</a>
        {% else %}
          <a href="{{ url_for('login') }}">Login with Auth0</a>
        {% endif %}
        """,
        user=user,
    )


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/callback")
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token.get("userinfo") or oauth.auth0.userinfo()
    return redirect(url_for("profile"))


@app.route("/profile")
@login_required
def profile():
    return render_template_string(
        """
        <h1>Profile</h1>
        <pre>{{ user | tojson(indent=2) }}</pre>
        <a href="{{ url_for('logout') }}">Logout</a>
        """,
        user=session["user"],
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + os.getenv("AUTH0_DOMAIN", "")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": os.getenv("AUTH0_CLIENT_ID", ""),
            },
            quote_via=quote_plus,
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
