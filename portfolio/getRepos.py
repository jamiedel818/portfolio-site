#!/usr/bin/env python3
'''
    Small library of functions dedicated to gathering Github project information.
'''
import requests
import json

'''
    Request all public repositories from a Github account.
    Return Json blob of repository information.
'''
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

'''
    Parse the repository information we are interested in.
    Return list of repository dictionaries
'''
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
