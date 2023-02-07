# GDSC Event Attendance Tool

Welcome to the Attendance Tool repository!

As GDSC Leads, we were facing the challenge of individuals attending events but not properly marking their attendance. To address this issue, we have developed a tool using the Selenium library in Python that allows us to easily add attendees by inputting their first and last names, as well as their email addresses.

## Demo Video


https://user-images.githubusercontent.com/99554708/210218861-d57c2c5d-d534-4c0b-8ed5-c12a47ae7324.mp4



## Setup

To use the Attendance Tool, you will need the following:

1. The link to the event where you have the "Add Attendee" button. (line 20)
2. Add CSV file with the following columns: `First_name`, `Last_name`, `Email`. Make sure to delete the top row (i.e. the column names) from the file - refer to file.csv to understand the format. (line 31)
3. Check if everything is working properly, (check whether the data is correctly being inputted in the fields, it would cancel after writing the names)

## Feature Update
- Fixed the issue "Browser not working" issue
- Uncomment lines 64 - 66 if you want the bot to add Checkin of that particular attendee
- If the email exists already, it cancels and skips that name
- continues from 1 plus incorrect entry
- If for whatever reason, the system fails, or delays is because of bad internet. The Bot would cater to it


## Usage

To use the Attendance Tool, simply run the Python script and follow the prompts. The tool will guide you through the process of adding attendees to the event.

We hope that this tool will be helpful for others facing similar challenges. Thank you for visiting. Don't forget to 🌟**Star** the repo, and show your LOVE. 👏
