import os
import googleapiclient.discovery
import googleapiclient.errors
from time import gmtime, strftime
import json

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # turn into arguments
    candidate = ("Sanders", "\"bernie sanders\"")
    loops = 10

    now = strftime("%Y-%m-%d", gmtime())
    directory = "../../data/Youtube/Lists_of_Videos/{}/{}".format(candidate[0], now)
    os.makedirs(directory, exist_ok=True)

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    youtube_api_key = open("../../keys/youtube_v3_api.key", mode="r").readline()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=youtube_api_key)

    page_token = ""
    for i in range(loops):
        part = "Part-{}".format(str(i).zfill(3))
        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            q=candidate[1],
            publishedAfter="2019-01-01T00:00:00Z",
            type="video",
            pageToken=page_token
        )
        response = request.execute()
        with open("{}/{}.json".format(directory, part), 'w') as f:
            json.dump(response, f)

        page_token = response["nextPageToken"]


if __name__ == "__main__":
    main()
