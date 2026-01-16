# Apple Watch Sleep Data Parser
Apple Health doesn't store sleep data separately from other health data. This script parses all of the data and creates a sleep dataset.

## You're going to need to install lxml and pandas
If you prefer another XML parser, that probably works too.

## Getting Apple Watch data
Go to the Health app on your iPhone, press your profile picture in the top right corner, scroll down and press Export All Health Data.
Put export.zip onto your computer and unzip it. Look for export.xml and put that in the project repository.

## SOURCE variable in the script
Get rid of my name and put your name. The source has a weird apostrophe and an \xa0 so leave those.

## Run the script
and you should get sleep_clean.csv. I analyzed it with ChatGPT, you can analyze it how you wish.


