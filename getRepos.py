#!/usr/bin/env python3
import requests
import json
#r = requests.get("https://api.github.com/users/jamiedel818/repos")
def writeData(data):
    with open('backup.json', 'w+') as outfile:
        json.dump(data, outfile)

def readData():
    with open('backup.json') as file:
        data = json.load(file)
    return data

def getData():
    r = requests.get("https://api.github.com/users/jamiedel818/repos")
    #TEST 404 LINK --> r = requests.get("https://httpbin.org/delete")
    try:
        r.raise_for_status()
        print("INFO: Data recieved from API")
        data = r.json()
        writeData(data)
        return data

    except Exception as e:
        print('INFO: Loading from backup file.')
        data = readData()
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
