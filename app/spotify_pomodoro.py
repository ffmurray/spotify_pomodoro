import tekore as tk

## Authorization
# set client ID and secret
client_id = '330de5fda11346ed8fe1c9e683471877'
client_secret = '616969349565471587934d59077bce2f'
redirect_uri = 'http://localhost' #TODO figure out uri....
#
app_token = tk.request_client_token(client_id, client_secret)
spotify = tk.Spotify(app_token)

user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)

