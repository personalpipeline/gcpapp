from google.auth import default

try:
    credentials, project = default()
    if credentials and project:
        print(f"Successfully retrieved Application Default Credentials for project: {project}")
        print(f"Credential type: {type(credentials)}")
        # You can optionally print some credential details (be cautious with sensitive info)
        # print(f"Credential info: {credentials.info}")
    else:
        print("Failed to retrieve Application Default Credentials.")
        print("Make sure you have run 'gcloud auth application-default login'.")
except Exception as e:
    print(f"An error occurred while retrieving ADC: {e}")
    print("Make sure your Google Cloud CLI is installed and you have logged in.")