import requests
import json

SECRET_API_KEY = ''

Google_Search_Robot_ID = '' # Input required is search_term and max_results_no -> {"inputParameters": {"originUrl" : "Soccer", "Organic Result_limit": 5}}
Reddit_Search_Robot_ID = '' # Input required is reddit_subreddit and max_results_no -> {"inputParameters": {"originUrl" : "https://www.reddit.com/user/OfficialSGExams/", "Posts_limit": 5}}
Country_Trends_Robot_ID = '' # Input required is uppercase country abbreviation like US, CA and UK -> {"inputParameters": {"originUrl" : "SG"}}
Google_Scholars_Robot_ID = '' # Input required is search_term and max_results_no -> {"inputParameters": {"search_keyword" : "Blockchain", "articles_list_limit": 5}}

def get_all_robots(SECRET_API_KEY):
    Token = 'Bearer ' + SECRET_API_KEY

    headers = {"Authorization": Token}

    url = "https://api.browse.ai/v2/robots"

    response = requests.request("GET", url, headers=headers)

    json_string = response.text

    data = json.loads(json_string)

    print(json.dumps(data, indent=4)) # JSON Prettify
