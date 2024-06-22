from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    '../oauth_credential.json',
    scopes=["<https://www.googleapis.com/auth/youtube>"])

credential = flow.run_local_server()

token = credential.to_json()

print(token)
