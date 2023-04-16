import requests
from ics import Calendar
from io import StringIO


def download_ical(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def read_ical(ical_data):
    calendar = Calendar(ical_data)
    return calendar


if __name__ == "__main__":
    url = "https://www.meetup.com/ThaiPy-Bangkok-Python-Meetup/events/ical/"
    ical_data = download_ical(url)
    calendar = read_ical(ical_data)

    for event in calendar.events:
        print("Event Name:", event.name)
        print("Event Begin:", event.begin)
        print("Event End:", event.end)
        print("Event Description:", event.description)
        print("------------")
