#  Project: MongoDB based paper search system
Each paper has the following information that need to be stored:
- Title: a string. A paper can only have one title, and you can assume it is unique.
- Authors: a paper can have many authors. Each author should have the following information
stored
- Lastname
- Firstname
- Affiliation:thenameofhis/heremployer(acompanyoraschool,youdon’thaveto
store the type of the affiliation). Notice that each author may change employers, so for each person, you need to record the start and end date for each employer that employ him/her. You should further assume the following:
- Each author can have only at most one employer at any given time
- It is possible that an author is unemployed for some period
- Notice that if the paper have more than one author,the order of the authors need to be
recorded.
- Publication: Where the paper is published. There are two types
- Conferences:youneedtorecordthefollowinginfo ▪ Nameoftheconference
- The number of times it is held (e.g., 1st, 17th, etc.) ▪ Theyearthatisheld
- The location that it is held (just a string is fine)
- Journal:youneedtorecordthefollowinginfo
- Thenameofthejournal
- Theyearandmonthwherethepaperispublished
- Some(but not all)journal have a volume number as sociated with it(just a string is fine, some volume # have complicated format that you don’t have to worry
about in this project)
- Some optional information about each paper
- URLwherethepapercanbedownload
- Pagenumber(ifitispublishedaspartofabook/magazine)(stringisfine)

Data Entry:
The system will provide a GUI for the user to input papers. It may be necessary to provide places for users to input other info (such as authors, publications etc.). It should ensure the consistency of data (to the best of ability – for instance, you should assume paper title, conference name, journal name to be unique. However, many authors may have the same name).
Query
You should implement the following queries via your GUI.
• The program should get the name of a paper and return all relevant info for each paper
• The program should get the name of an author (just the name), and list of the papers for that
author.
• The program should get the name of a publication, and a year range, and list of papers that is
published within that range.
