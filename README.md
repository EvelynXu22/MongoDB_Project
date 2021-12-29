# DatabseFinalProject
Each paper has the following information that need to be stored:
• Title: a string. A paper can only have one title, and you can assume it is unique.
• Authors: a paper can have many authors. Each author should have the following information
stored
o Lastname
o Firstname
o Affiliation:thenameofhis/heremployer(acompanyoraschool,youdon’thaveto
store the type of the affiliation). Notice that each author may change employers, so for each person, you need to record the start and end date for each employer that employ him/her. You should further assume the following:
▪ Eachauthorcanhaveonlyatmostoneemployeratanygiventime
▪ Itispossiblethatanauthorisunemployedforsomeperiod
o Noticethatifthepaperhavemorethanoneauthor,theorderoftheauthorsneedtobe
recorded.
• Publication: Where the paper is published. There are two types
o Conferences:youneedtorecordthefollowinginfo ▪ Nameoftheconference
▪ The number of times it is held (e.g., 1st, 17th, etc.) ▪ Theyearthatisheld
▪ The location that it is held (just a string is fine)
o Journal:youneedtorecordthefollowinginfo
▪ Thenameofthejournal
▪ Theyearandmonthwherethepaperispublished
▪ Some(butnotall)journalhaveavolumenumberassociatedwithit(justastring
is fine, some volume # have complicated format that you don’t have to worry
about in this project)
• Some optional information about each paper
o URLwherethepapercanbedownload
o Pagenumber(ifitispublishedaspartofabook/magazine)(stringisfine)

Data Entry:
The system will provide a GUI for the user to input papers. It may be necessary to provide places for users to input other info (such as authors, publications etc.). It should ensure the consistency of data (to the best of ability – for instance, you should assume paper title, conference name, journal name to be unique. However, many authors may have the same name).
Query
You should implement the following queries via your GUI.
• The program should get the name of a paper and return all relevant info for each paper
• The program should get the name of an author (just the name), and list of the papers for that
author.
• The program should get the name of a publication, and a year range, and list of papers that is
published within that range.
