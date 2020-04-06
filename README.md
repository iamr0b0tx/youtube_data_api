# youtube_data_api
To fetch data from youtube using the youtube_analytics_report.query api. This project has the code sample (in python) to pull data from the api. The code sample can be edited to suit needs like [dimensions](https://developers.google.com/youtube/analytics/dimensions) and [metrics](https://developers.google.com/youtube/analytics/metrics). There is also and __EXE__ available for windows users to pull core metrics and dimensions from youtube api. All tou need is to set up the credentials as explained below.

Check here to find out more [Youtube API docs](https://developers.google.com/youtube/reporting/v1/code_samples/python#retrieve_daily_channel_statistics)


## Setting up your Project
Before running this sample locally for the first time, you need to set up authorization credentials for your project:

1. Create or select a project in the Google API Console.
2. Enable the YouTube Analytics API for your project.
3. At the top of the Credentials page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
4. On the Credentials page, click the Create credentials button and select Oauth client ID.
5. Select the application type Other, enter the name "YouTube Analytics API Quickstart", and click the Create button.
6. Click OK to dismiss the resulting dialog.
7. Click the file_download (Download JSON) button to the right of the client ID.
8. Move the downloaded file to your working directory.

### Execution

### Running executable
* double click ytapi.exe to run the application

### Prerequisites (for running code sample)

*   Python 2.6 or greater(get here: https://python.org/downloads)

*   The pip package management tool

*   The Google APIs Client Library for Python:
    ```
    pip install --upgrade google-api-python-client
    ```
*   The google-auth, google-auth-oauthlib, and google-auth-httplib2 for user authorization.
    ```
    pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
    ```

### Testing
Now, you are ready to actually test the sample:
1. Copy the code sample below to your working directory.
In the sample, update the value of the CLIENT_SECRETS_FILE variable to match the location of the file that you downloaded after setting up your authorization credentials.

2. Run the sample code in a terminal window:.
    ```
    python ytapi.py
    ```

3. Go through the authorization flow. The auth flow might automatically load in your browser, or you might need to copy the auth URL into a browser window. At the end of the authorization flow, if necessary, paste the authorization code displayed in the browser into your terminal window and click [return].

4. The API query executes and the JSON response is written as an output.json and csv file.