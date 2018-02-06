• Write a Python script (with REST requests embedded) called “load.py”. The script will do two things:
o Convert the given csv file into JSON format and store it in Firebase. You may need Python “requests” package as described in the lecture.
o Create an inverted index for the event attribute of the menus. For this, you need to parse the content of event attribute and extracts unique tokens (which are defined as a sequence of alphabetic characters) among the values of all attributes.
For example, “[DINNER]” has only one token “DINNER” (or “dinner” if you decide to lower case it), while “FRUHSTUCK/BREAKFAST;” has two tokens.
You then create an index in Firebase to record, for each token, the list of ids of menus which contain the token.
For example:
{"index": {
"breakfast": [12463, 12470, ...]
...
}
which says “breakfast” appears in menu 12463, 12470, …
Execution format:
o python load.py menu-200.csv
• [40 points] Write a Python script called “search.py”. The script takes a list of keywords (which may contain multiple tokens) and return a list of ids of menus whose event field contains any keywords in the list. The search needs to be executed using the data stored in your Firebase database. Note that the search is NOT case-sensitive. For example,
o python search.py “dinner breakfast”
should return the ids of menus that contain dinner (and DINNER), breakfast, or both.


1. The load python file takes a user argument which would be the address of the CSV file and upload it to the Googles's Firebase Database.
2. It will create a new Database by using inverted indexes.
3. Search python file will return indexes of events like breakfast etc by taking these events as a user argument. 

The aim of the project is to just understand the basics of cloud databases. 