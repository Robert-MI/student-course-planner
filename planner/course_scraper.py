import requests
from bs4 import BeautifulSoup
import re

COURSE_URL = "https://auasonis.jenzabarcloud.com/GENSRsC.cfm"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_courses(major_prefix=""):
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
                raw_course_name = cols[0].get_text(strip=True) if len(cols) > 0 else ""
                section = cols[1].get_text(strip=True) if len(cols) > 1 else ""
                session = cols[2].get_text(strip=True) if len(cols) > 2 else ""
                credits = cols[3].get_text(strip=True) if len(cols) > 3 else ""
                instructor = cols[5].get_text(strip=True) if len(cols) > 5 else ""
                course_time = cols[6].get_text(strip=True) if len(cols) > 6 else ""
                location = cols[11].get_text(strip=True) if len(cols) > 11 else ""

                # Check for prerequisite tag
                has_prerequisite = "(Prerequisite)" in raw_course_name

                # Remove "(Prerequisite)" and extract course code
                cleaned_name = raw_course_name.replace("(Prerequisite)", "").strip()
                match = re.search(r"\(([A-Z]{2,4}\d{3,4})\)", cleaned_name)
                course_code = match.group(1) if match else ""

                # Clean course title by removing course code in parentheses
                course_title = re.sub(r"\s*\([A-Z]{2,4}\d{3,4}\)\s*", "", cleaned_name).strip()

                # Filter by major prefix
                if major_prefix and not course_code.startswith(major_prefix):
                    continue

                courses.append({
                    "course_name": raw_course_name,
                    "course_code": course_code,
                    "course_title": course_title,
                    "section": section,
                    "session": session,
                    "credits": credits,
                    "instructor": instructor,
                    "course_time": course_time,
                    "location": location,
                    "has_prerequisite": has_prerequisite
                })

    return courses
