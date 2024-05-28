# README

## Instantiate environment

```bash
python3.10 -m venv .testing
source .testing/bin/activate
pip install -r requirements.txt
```

Also need JSON authorization file from Google Cloud Platform.

## Getting Google Authentication information

Creating a Google Cloud Service Account:

1. Go to the Google Cloud Console: Open your web browser and navigate to the Google Cloud Console.
1. Create a new project: Click on the project drop-down and select `New Project`, then fill in the `Project name` field and click `Create`.
1. Enable the Google Sheets API: Navigate to `APIs & Services > Library`, search for `Google Sheets API` and click on it. In the Google Sheets API page, click `Enable`.
1. Create credentials: Navigate to `APIs & Services > Credentials`, click `Create Credentials` and select `Service account`. Fill in the `Service account name` and `Service account description` fields and click `Create`.
1. Grant this service account access to project: In the `Role` field, select `Project > Editor` (or `Project > Viewer`). Click `Continue`.
1. Create key: In the `Service account` details page, click `Add Key`, then `Create new key`. Select `JSON` as the key type and click `Create`. Your JSON key file will be downloaded.
1. Share your Google Spreadsheet: Open your Google Spreadsheet, click on `Share`, and paste the `client_email` from the JSON key file (or the `Details` page). Click `Done`.


Convert the JSON key to a string, to be used in Github Actions:

```bash
jq -c . <path-to-json-key-file>
```



Add the string as a secret in GitHub:

-  Go to your GitHub repository and click on `Settings`.
-   Click on `Secrets` in the left sidebar.
-   Click on `New repository secret`.
-   Enter a name for the secret in the `Name` field. This will be the name of the environment variable that holds the JSON contents.
-   Paste the string you copied into the `Value` field.
-   Click on `Add secret`.



