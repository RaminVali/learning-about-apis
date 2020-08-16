import requests
# Create a dictionary of headers containing our Authorization header.

headers = {"Authorization": "token fe5ae7c975f358a9652351383a6b0c59fe64a6dd"}


# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/RaminVali", headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
print(response.json())

orgs = response.json()


# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
payload = {"name": "learning-about-apis"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = response.status_code
