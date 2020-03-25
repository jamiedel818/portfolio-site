#!/usr/bin/env python3
import requests
import json

def getData():
    r = requests.get("https://api.github.com/users/jamiedel818/repos")
    #TEST 404 LINK --> r = requests.get("https://httpbin.org/delete")
    try:
        r.raise_for_status()
        print("INFO: Data recieved from API")
        data = r.json()
        return data

    except Exception as e:
        print("ERROR:", e)
        data = {
            'name': "Data Not Found",
            'author': "Data Not Found",
            'date': "Data Not Found",
            'description': "Data Not Found",
            'url': "Data Not Found"
        }
        return data

def handleData():
    data = getData()
    repos = []

    for repo in data:
        project = {}
        project['name'] = repo['name']
        project['author'] = 'jamiedel818'
        project['date'] = repo['updated_at']
        project['description'] = repo['description']
        project['url'] = repo['html_url']
        repos.append(project)
    return repos

def main():
    print(json.dumps(handleData(), indent=2))

if __name__ == "__main__":
    main()

## TODO: Need to add excpetion handling to this and write to file? if exception fails read from local file
## TODO: Add some logging to when was written or if it failed
## TODO: ADD webhooks from github
