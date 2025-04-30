import requests
from bs4 import BeautifulSoup

COURSE_URL = "https://auasonis.jenzabarcloud.com/GENSRsC.cfm"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                  "AppleWebKit/537.36 (KHTML, like Gecko) " 
                  "Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_courses():
    response = requests.get(COURSE_URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    courses = []

    if table:
        rows = table.find_all("tr")[1:]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 4:
                course_name = cols[0].text.strip()
                section = cols[1].text.strip()
                session = cols[2].text.strip()
                credits = cols[3].text.strip()
                instructor = cols[5].text.strip()
                course_time = cols[6].text.strip()
                location = cols[11].text.strip()

                courses.append({
                    "course_name": course_name,
                    "section": section,
                    "session": session,
                    "credits": credits,
                    "instructor": instructor,
                    "course_time": course_time,
                    "location": location,
                })

    return courses
