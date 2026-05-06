import requests
import webbrowser

# 🔑 Add your API key
API_KEY =  "8dec4fe3cemsh040a8754f8e7965p1c0e7bjsn75744017c317"

query = input("Enter your skills: ")

url = "https://jsearch.p.rapidapi.com/search"

querystring = {
    "query": query + " internship fresher india",
    "page": "1",
    "num_pages": "1"
}

headers = {
    "X-RapidAPI-Key":  "8dec4fe3cemsh040a8754f8e7965p1c0e7bjsn75744017c317",
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

html_content = """
<html>
<head>
    <title>Internship Results</title>
</head>
<body>
    <h1>🔥 Internship Results</h1>
"""

count = 1

if 'data' in data:
    for job in data['data']:

        title = job.get('job_title', '').lower()

        if not ('intern' in title or 'internship' in title or 'trainee' in title):
            continue

        role = job.get('job_title', 'Not Available').split(" in ")[0]

        location = (
            job.get('job_city') or
            job.get('job_state') or
            job.get('job_country') or
            "Not Available"
        )

        salary = job.get('job_salary') or "Check Apply Link"

        link = job.get('job_apply_link')
        if not link:
            continue

        html_content += f"""
        <div style="border:1px solid black; padding:10px; margin:10px;">
            <h3>{role}</h3>
            <p><b>Company:</b> {job.get('employer_name')}</p>
            <p><b>Location:</b> {location}</p>
            <p><b>Stipend:</b> {salary}</p>
            <a href="{link}" target="_blank">👉 Apply Now</a>
        </div>
        """

        count += 1
        if count > 5:
            break

html_content += "</body></html>"

# Save HTML file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# 🔥 Open in browser
webbrowser.open("output.html")