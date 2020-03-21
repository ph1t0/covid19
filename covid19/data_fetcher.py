import re
import sys
import os
import urllib.request
import json


def file_download(output_dir, file_data):
    try:
        urllib.request.urlretrieve(file_data["download_url"], os.path.join(output_dir, file_data["name"]))
    except KeyboardInterrupt:
        print("Interrupted: CTRL+C")
        sys.exit(0)


def dir_list(output_dir, data):
    IGNORE = ['README.md', ".gitignore"]
    for item in data:
        if isinstance(item, dict) and item["type"] == "dir":
            data_dir = request(item["url"])
            dir_list(output_dir, data_dir)
        else:
            if isinstance(item, dict) and item["type"] == "file":
                if item["name"] not in IGNORE:
                    file_download(output_dir, item)
            pass


def request(api_url):
    try:
        response = urllib.request.urlretrieve(api_url)
    except KeyboardInterrupt:
        print("Interrupted: CTRL+C")
        sys.exit(0)

    with open(response[0], "r") as f:
        data = json.load(f)

    return data


def create_api_url(url):
    re_branch = re.compile("/(tree|blob)/(.+?)/")
    branch = re_branch.search(url)
    download_dir = url[branch.end():]
    api_url = (url[:branch.start()].replace("github.com", "api.github.com/repos", 1) +
              "/contents/" + download_dir + "?ref=" + branch.group(2))

    return api_url


def download_files(output_dir, url):
    github_api_url = create_api_url(url)
    data = request(github_api_url)
    dir_list(output_dir, data)
