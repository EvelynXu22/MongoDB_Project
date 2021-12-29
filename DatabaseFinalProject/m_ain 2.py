import brython
import pymongo
import datetime
from bson.objectid import ObjectId


class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.SMUKI
        self.publications = self.db.publications
        self.authors = self.db.authors
        self.paper = self.db.paper


print("1")

paper = [
    {
        'title': 'Database Management',
        'authors': [
            {
                'last_name': 'David',
                'first_name': 'Lin',
                'sort': 1
            },
            {
                'last_name': 'Yiwen',
                'first_name': 'Xu',
                'sort': 2
            }
        ],
        'publication': 'Jornal',
        'url': "http://sshshshsh"
    },
    {
        'title': 'MongoDB Textbook',
        'authors': [
            {
                'last_name': 'David',
                'first_name': 'Lin',
                'sort': 1
            },
            {
                'last_name': 'Yiwen',
                'first_name': 'Xu',
                'sort': 2
            }
        ],
        'publication': 'Jornal',
        'url': "http://sshshshsh"
    }
]

afflication1 = [
    {
        "emoployer": "A",
        "start_date": datetime.datetime(1990, 1, 1),
        "end_date": datetime.datetime(1991, 1, 1)
    },
    {
        "emoployer": "B",
        "start_date": datetime.datetime(2000, 1, 1),
        "end_date": datetime.datetime(2001, 1, 1)
    }
]

afflication2 = [
    {
        "emoployer": "C",
        "start_date": datetime.datetime(1990, 1, 1),
        "end_date": datetime.datetime(1992, 1, 1)
    },
    {
        "emoployer": "D",
        "start_date": datetime.datetime(2021, 1, 1),
        "end_date": datetime.datetime(2022, 1, 1)
    }
]


class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.SMUKI
        self.publications = self.db.publications
        self.authors = self.db.authors
        self.paper = self.db.paper

    def insertConferenceToPublications(self, name, times, location, year):
        conference = {
            "name": name,
            "times": times,
            "location": location,
            "time": datetime.datetime(year, 1, 1)  # Year Only
        }

        publicationId = self.publications.insert(conference)
        return publicationId

    def insertJournalToPublications(self, name, associated_volume, year, month):
        journal = {
            "name": name,
            "associated_volume": associated_volume,
            "time": datetime.datetime(year, month, 1)  # Year & Month
        }
        publicationId = self.publications.insert(journal)
        return publicationId

    def insertAuthorToAuthors(self, last_name, first_name, afflication=None, paper=None):
        author = {
            "last_name": last_name,
            "first_name": first_name,
            "afflication": afflication,
            "paper": paper
        }
        authorId = self.authors.insert(author)
        return authorId

    def updateAuthorToAuthors(self, last_name, first_name, afflication=None, paper=None):
        author = {
            "last_name": last_name,
            "first_name": first_name,
            "afflication": afflication,
            # "paper": paper
        }
        ptr = self.authors.find({author}, {"paper": 1})
        if ptr == None:
            ptr = []
        authorToUpdate = {
            "last_name": last_name,
            "first_name": first_name,
            "afflication": afflication,
            "paper": ptr.apend(paper)
        }
        authorId = self.authors.update_one(author, {"$set": authorToUpdate}, upsert=True)
        return authorId

    def insertPaperToPaper(self, title, authors, publication, url=None, page_num=None):
        paper = {
            "title": title,
            "authors": authors,
            "publication": publication,
            "url": url,
            "page_num": page_num
        }
        paperId = self.paper.insert(paper)
        return paperId

    def oneClickInsertionToPaper(self, title, authors, publication_name, year, times=None, location=None, month=None,
                                 associated_volume=None, url=None, page_num=None):
        if month:
            self.insertJournalToPublications(publication_name, associated_volume, year, month)
        else:
            self.insertConferenceToPublications(publication_name, times, location, year)

        get_Paper_id = self.insertPaperToPaper(title, authors, publication_name, url, page_num)
        for author in authors:
            # author = author.spilt()
            first_name = author[0]
            last_name = author[1]
            afflication = author[2]  # 需要商讨

            self.updateAuthorToAuthors(last_name, first_name, afflication, get_Paper_id)
        # self.insertPaperToPaper(title, authors, publication_name, url, page_num)

    def queryAuthorForPaper(self, authorId, paperId):
        ptr = self.authors.find({"_id": authorId}, {"paper": 1, "_id": 0})

        author = ptr.next()
        paper = author["paper"]
        if paper == None:
            paper = []
        # print("Paper:" + paper)
        paper.append(paperId)

        self.authors.update_one({"_id": authorId}, {"$set": {"paper": paper}})  # 需要讨论下

        print(paper)

    def showPublications(self):
        ptr = self.publications.find()
        for item in ptr:
            print(item)

    # 3 Query all paper by the name of publication and time range
    def queryPaperWithYearRange(self, publication_name, year_start, year_end):

        # papersInfo = self.publications.find({"name":publication_name,"time":{"$gte":datetime.datetime(year_start,1,1),"$lt":datetime.datetime(year_end,1,1)}})

        publicationsInfo = self.publications.aggregate(
            [
                # find publication with given name and time range(>= year_start and < year_end)
                {
                    "$match": {"name": publication_name, "time": {"$gte": datetime.datetime(year_start, 1, 1),
                                                                  "$lt": datetime.datetime(year_end, 1, 1)}}
                },
                # find papers in paper collection with given publication(_id)
                {
                    "$lookup":
                        {
                            "from": "paper",
                            "localField": "_id",
                            "foreignField": "publication",
                            "as": "paper"
                        }
                }
            ]
        )

        for publicationInfo in publicationsInfo:
            # print(publicationInfo)
            time = publicationInfo["time"]
            # Conference or Journal?
            try:
                publicationInfo["location"]
                print(publicationInfo["name"], publicationInfo["times"], publicationInfo["location"], time.year)
            except:
                print(publicationInfo["name"], publicationInfo["associated_volume"], time.year, time.month)

            papersInfor = publicationInfo["paper"]
            for paperInfo in papersInfor:
                print(paperInfo["title"])
                authors = paperInfo["authors"]
                for author in authors:
                    print(author["first_name"], author["last_name"])
                print(paperInfo["url"])
                print(paperInfo["page_num"])

        return

    # 2 Query all info for paper by the name of author
    def queryAuthorsWithName(self, last_name, first_name):
        authorInfo = self.authors.aggregate(
            [
                {
                    "$match": {"last_name": last_name, "first_name": first_name}
                },
                {
                    "$unwind": "$paper",  # unwind document by paper array
                },
                {
                    "$lookup":  # look up paper info by paper(_id)
                        {
                            "from": "paper",
                            "localField": "paper",
                            "foreignField": "_id",
                            "as": "paper"
                        }
                },
                {
                    "$lookup":  # look up publication info by pubilication(_id)
                        {
                            "from": "publications",
                            "localField": "paper.publication",
                            "foreignField": "_id",
                            "as": "publication"
                        }
                },
                {
                    "$group":
                        {  # group up unwinded documents
                            "_id": "$_id",
                            "last_name": {"$first": "$last_name"},
                            "first_name": {"$first": "$first_name"},
                            "paper": {"$push": "$paper"},
                            "publication": {"$push": "$publication"}
                        }
                },

            ]
        )

        for author in authorInfo:
            # print(paperInfo)
            papersInfo = author["paper"]
            publicationsInfo = author["publication"]
            # print(author["paper"])
            for paperInfo in papersInfo:
                paper = paperInfo[0]
                print(paper["title"])
                authors = paper["authors"]
                for author in authors:
                    print(author["first_name"], author["last_name"])
                # print(paper["authors"])
            for publicationInfo in publicationsInfo:
                # print(publicationInfo)
                publication = publicationInfo[0]
                time = publication["time"]
                # Conference or Journal?
                try:
                    publication["location"]
                    print(publication["name"], publication["times"], publication["location"], time.year)
                except:
                    print(publication["name"], publication["associated_volume"], time.year, time.month)

        return

    # 1 Query all relevant info for paper by the title of paper
    def queryPaperWithTitle(self, title):
        author = self.paper.aggregate(
            [
                {
                    "$match": {"title": title}
                },
                {
                    "$unwind": "$authors",  # unwind document by authors array
                },
                {
                    "$lookup":  # look up authors info by _id
                        {
                            "from": "authors",
                            "localField": "authors._id",
                            "foreignField": "_id",
                            "as": "authors"
                        }
                },
                {
                    "$sort": {"authors.sort": -1}  # sort author in order by "sort"
                },
                {
                    "$group": {  # group up unwinded documents
                        "_id": "$_id",
                        "title": {"$first": "$title"},
                        "authors": {"$push": "$authors"},
                        "publication": {"$first": "$publication"},
                        "url": {"$first": "$url"},
                        "page_num": {"$first": "$page_num"}
                    }
                },
                {
                    "$lookup":  # look up publication info by _id
                        {
                            "from": "publications",
                            "localField": "publication",
                            "foreignField": "_id",
                            "as": "publication"
                        }
                },
            ]
        )

        for paper in author:
            print(paper)  # all paper info
            for authors in paper["authors"]:
                for author in authors:
                    print(author["_id"])  # all author id
        return


mongo = Mongo()
mongo.queryPaperWithTitle("Management")
mongo.queryAuthorsWithName("Yiwen", "Xu")
mongo.queryPaperWithYearRange("Journal", 1997, 2021)
