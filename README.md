# Weekly Comic Bulletin
A python script that scrapes and e-mails the comic books that will come out that week. A quick script I wrote to familiarize myself with scripts, Python and web scraping. The script can be automatized by scheduling a cron job. I have yet to test the automation, but the code works when you trigger it manually. In the future I plan to add the mail addresses with a config file instead of hard coding them into the script, and maybe work on some cosmetic changes on the final mail. The script scrapes the releases from comics.org. The final mail sent currently looks like this:

![Screenshot_20241203_030609](https://github.com/user-attachments/assets/a57f8e02-422e-4e01-ac7f-0c2bd8baccfb)

Changelog:
  The script now gets all the mail & SMTP data from a json file instead of having everything hard coded. You need mailConfig.json with the correct info in it to run the script. (03-12-24)
