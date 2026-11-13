# FitMan account setup

FitMan defaults to local mode. It opens the existing single-user database at `data/fitman.db`. Account mode uses a separate database for each signed-in user. Existing local profiles and logs stay in the local database.

1. Install dependencies with `python -m pip install -r requirements.txt`.
2. Register FitMan with your OpenID Connect provider. Allow the exact callback URL that users will reach, including the port for local testing.
3. Copy `.streamlit/secrets.example.toml` to `.streamlit/secrets.toml` and fill in the credentials, callback URL, and a random cookie secret. Keep this file private.
4. Start Streamlit in account mode:

```powershell
$env:FITMAN_MODE = "accounts"
.\venv\Scripts\python.exe -m streamlit run app.py --server.port 8501
```

For phone browser access, deploy in account mode over HTTPS with a persistent, backed-up `data/` volume. The phone and desktop browsers must use the same deployment and identity provider to see the same saved history. Native mobile clients will need an API before they can use these accounts.
