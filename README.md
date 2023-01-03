# GDSC Event Attendance Tool

Welcome to the Attendance Tool repository!

As GDSC Leads, we were facing the challenge of individuals attending events but not properly marking their attendance. To address this issue, we have developed a tool using the Selenium library in Python that allows us to easily add attendees by inputting their first and last name, as well as their email address.

## Demo Video


https://user-images.githubusercontent.com/99554708/210218861-d57c2c5d-d534-4c0b-8ed5-c12a47ae7324.mp4



## Setup

To use the Attendance Tool, you will need the following:

1. The file path to your Chrome profile. This can typically be found at: `C:\\Users\\[YOUR USERNAME]\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1` (line 14)
2. The link to the event where you have the "Add Attendee" button. (line 20)
3. Add CSV file with the following columns: `First_name`, `Last_name`, `Email`. Make sure to delete the top row (i.e. the column names) from the file - refer to file.csv to understand the format. (line 31)
4. Check if everytihng is working properly, (check whether the data is correctly being inputted in the fields, it would cancel after writing the names)
5. Uncomment the send_btn code at line 52-53, and delete line 49-50

## FAQs
- Sometimes, it opens up in another window: try closing all chrome tabs, and open the one you want it to run on.
- Other times, the link wouldn't redirect to your page: make sure to close all the chrome tabs before opening the script.

## Feature Update
- Uncomment line 64 - 66 if you want the bot to add Checkin of that particular attendee
- If the email existes already, it cancels and skips that name.
- continues from 1 plus incorrect entry
- If for whatever reason, the system fails, or delays because of bad internet. The Bot would cater for it.


## Usage

To use the Attendance Tool, simply run the Python script and follow the prompts. The tool will guide you through the process of adding attendees to the event.

We hope that this tool will be helpful for others facing similar challenges, and we appreciate your support by giving this repository a star. Thank you for your consideration.
