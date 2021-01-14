import requests
from bs4 import BeautifulSoup
import schedule
from configparser import ConfigParser
import time


def get_latest_cones_from_noaa(base_url, resource):
    page = requests.get(base_url + resource)
    soup = BeautifulSoup(page.content, 'html.parser')
    resources = find_all_cones_of_uncertainty_resources(soup)
    return resources


def find_all_cones_of_uncertainty_resources(soup):
    resources = []
    for a in soup.findAll('a'):
        if a.get_text() == 'Cone':
            resources.append(a.get('href'))
    return resources


def job():
    config = ConfigParser()
    config.read('config.ini')
    noaa_base_url = config.get('main', 'noaa_url')
    noaa_resource = config.get('main', 'noaa_resource')
    storm_tracker_api = config.get('main', 'storm_tracker_url')
    resources = get_latest_cones_from_noaa(noaa_base_url, noaa_resource)
    payload = {'storms': resources}    
    response = requests.post(storm_tracker_api,json=payload)
    print(response)


if __name__ == "__main__":
    # schedule.every().day.at("09:00").do(job)
    schedule.every(30).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)