import requests
from icalendar import Calendar
from urllib.parse import urlparse, urlunparse

def get_ical(url):
    # Convert webcal:// to https://
    parsed_url = urlparse(url)
    scheme = 'https' if parsed_url.scheme == 'webcal' else parsed_url.scheme
    url = urlunparse(parsed_url._replace(scheme=scheme))

    # Fetch iCal data
    response = requests.get(url)
    response.raise_for_status()

    # Parse iCal data
    cal = Calendar.from_ical(response.text)

    return cal

def main():
    url = 'webcal://www.meetup.com/ThaiPy-Bangkok-Python-Meetup/events/ical/'
    cal = get_ical(url)

    for component in cal.walk():
        if component.name == 'VEVENT':
            summary = component.get('summary')
            dtstart = component.get('dtstart').dt
            dtend = component.get('dtend').dt
            location = component.get('location')

            print(f'Event: {summary}')
            print(f'Start: {dtstart}')
            print(f'End: {dtend}')
            print(f'Location: {location}\n')

if __name__ == '__main__':
    main()
