# GDSC Event Attendance Tool

Welcome to the Attendance Tool repository!

As GDSC Leads, we were facing the challenge of individuals attending events but not properly marking their attendance. To address this issue, we have developed a tool using the Selenium library in Python that allows us to easily add attendees by inputting their first and last name, as well as their email address.

## Setup

To use the Attendance Tool, you will need the following:

1. The file path to your Chrome profile. This can typically be found at: `C:\\Users\\[YOUR USERNAME]\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1` (line 14)
2. The link to the event where you have the "Add Attendee" button. (line 20)
3. Add CSV file with the following columns: `First_name`, `Last_name`, `Email`. Make sure to delete the top row (i.e. the column names) from the file - refer to file.csv to understand the format. (line 31)
4. Check if everytihng is working properly, (check whether the data is correctly being inputted in the fields, it would cancel after writing the names)
5. Uncomment the send_btn code at line 52-53, and delete line 49-50

## Usage

To use the Attendance Tool, simply run the Python script and follow the prompts. The tool will guide you through the process of adding attendees to the event.

If you are still having trouble, hit me up.

We hope that this tool will be helpful for others facing similar challenges, and we appreciate your support by giving this repository a star. Thank you for your consideration.
