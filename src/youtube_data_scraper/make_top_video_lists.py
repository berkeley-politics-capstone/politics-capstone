import os
import googleapiclient.discovery
import googleapiclient.errors
from time import gmtime, strftime
import json
import csv
from glob import iglob
import pandas as pd


def main(candidates_file="candidate_names.txt", loops=2, api_key="../../keys/youtube_v3_api.key"):
    candidates = list(csv.reader(open(candidates_file), delimiter=','))

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    youtube_api_key = open(api_key, mode="r").readline()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=youtube_api_key)

    now = strftime("%Y-%m-%d", gmtime())
    print("Getting data from YouTube API")
    try:
        for candidate in candidates:
            print("Candidate", candidate, "querying.")
            directory = "../../data/Youtube/Lists_of_Videos/{}/{}".format(candidate[0], now)
            os.makedirs(directory, exist_ok=True)

            page_token = ""
            for i in range(loops):
                part = "Part-{}".format(str(i).zfill(3))
                request = youtube.search().list(
                    part="id",
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
    except googleapiclient.errors.HttpError as e:
        print(e)
    finally:
        # compile results to list even if API is down
        print("compiling video list...")
        DATA_DIRECTORY = "../../data/Youtube/Lists_of_Videos/"
        rootdir_glob = DATA_DIRECTORY + '**/*'
        file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]
        data = []
        for file in file_list:
            with open(file, 'r') as f:
                j = json.load(f)
                for i in range(50):
                    data.append((j["items"][i]['id']['videoId']
                                 , file.split("/")[5]
                                 , file.split("/")[6]
                                 , i + 1
                                 ))
        df = pd.DataFrame(data, columns=('videoId', 'candidate', 'day_observed', 'rank'))
        df.to_csv('../../data/Youtube/list_of_videos.csv', header=True, index=False)


if __name__ == "__main__":
    main()
