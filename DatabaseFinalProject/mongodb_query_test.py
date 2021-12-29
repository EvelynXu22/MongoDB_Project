'''
Author: your name
Date: 2021-11-23 12:21:13
LastEditTime: 2021-11-28 21:40:52
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /workplace_vscode/DatabaseFinalProject/mongodb_create.py
'''

import datetime
import pymongo
from bson.objectid import ObjectId



# from dateutil import parser

# dblist = myclient.list_database_names()
# print(dblist)

paper = [
    {
    'title':'Database Management',
    'authors':[
        {
            'last_name':'David',
            'first_name':'Lin',
            'sort':1
        },
        {
            'last_name':'Yiwen',
            'first_name':'Xu',
            'sort':2
        }
    ],
    'publication':'Jornal',
    'url':"http://sshshshsh"
},
{
    'title':'MongoDB Textbook',
    'authors':[
        {
            'last_name':'David',
            'first_name':'Lin',
            'sort':1
        },
        {
            'last_name':'Yiwen',
            'first_name':'Xu',
            'sort':2
        }
    ],
    'publication':'Jornal',
    'url':"http://sshshshsh"
}
]

afflication1 = [
    {
        "emoployer":"A",
        "start_date": datetime.datetime(1990,1,1),
        "end_date":datetime.datetime(1991,1,1)
    },
    {
        "emoployer":"B",
        "start_date":datetime.datetime(2000,1,1),
        "end_date":datetime.datetime(2001,1,1)
    }
]

afflication2 = [
    {
        "emoployer":"C",
        "start_date": datetime.datetime(1990,1,1),
        "end_date":datetime.datetime(1992,1,1)
    },
    {
        "emoployer":"D",
        "start_date":datetime.datetime(2021,1,1),
        "end_date":datetime.datetime(2022,1,1)
    }
]


class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost',27017)
        self.db = self.client.SMUKI
        self.publications = self.db.publications
        self.authors = self.db.authors
        self.paper = self.db.paper


    def insertConferenceToPublications(self,name,times,location,year):

        conference = {
            "name":name,
            "times":times,
            "location":location,
            "time":datetime.datetime(year,1,1)  #Year Only
        }

        publicationId = self.publications.insert(conference)
        return publicationId
    
       # 梁爽添加
    
    # Test
    def updateConferenceToPublications(self, name, times, location, year):

        conference = {
            "name": name,
            "times": times,
            "location": location,
            "time": datetime.datetime(year, 1, 1)  # Year Only
        }
        pubilicationId = self.publications.find(conference)
        if pubilicationId.count() == 0:  # 不存在当前出版方
            publicationId = self.publications.insert(conference)
        else:
            publication = pubilicationId.next()
            publicationId = publication["_id"]
        # publicationId = self.publications.update_one(conference, {"$set": conference}, upsert = True)
        return publicationId

    def insertJournalToPublications(self,name,associated_volume,year,month):

        journal = {
            "name":name,
            "associated_volume":associated_volume,
            "time":datetime.datetime(year,month,1)  #Year & Month
        }
        publicationId = self.publications.insert(journal)
        return publicationId
    
        # 梁爽添加
    
    # Test
    def updateJournalToPublications(self, name, associated_volume, year, month):

        journal = {
            "name": name,
            "associated_volume": associated_volume,
            "time": datetime.datetime(year, month, 1)  # Year & Month
        }
        publicationId = self.publications.find(journal)
        # publication = publicationId.next()
        # listid = list(publicationId)
        if publicationId.count() == 0:
            publicationId = self.publications.insert(journal)
        # publicationId = self.publications.update_one(journal, {"$set": journal}, upsert = True)
        else:
            publication = publicationId.next()
            publicationId = publication['_id']

        return publicationId

    def insertAuthorToAuthors(self,last_name,first_name,affiliation = None,paper=None):

        author = {
            "last_name":last_name,
            "first_name":first_name,
            "affiliation":affiliation,
            "paper":paper 
        }
        authorId = self.authors.insert(author)
        return authorId

    #  Test
    def updateNameAndAffiliationToAuthors(self, last_name, first_name, affiliation=None, paper=None):

        author = {
            "last_name": last_name,
            "first_name": first_name,
            "affiliation": affiliation,
            # "paper": paper
        }
        authorId = self.authors.find(author)
     
        # listid = list(authorId)
        if authorId.count()==0:
            authorToInput = {
                "last_name": last_name,
                "first_name": first_name,
                "affiliation": affiliation,
                "paper": []
            }
            authorId = self.authors.insert(authorToInput)
        else:
            author = authorId.next()
            authorId = author["_id"]
            
        # authorId = self.authors.insert(author)
        return authorId

    def queryAuthorForPaper(self,authorId,paperId):
        ptr = self.authors.find({"_id":authorId},{"paper":1,"_id":0})

        author = ptr.next()
        paper = author["paper"]
        if paper == None:
            paper = []
        # print("Paper:" + paper)
        paper.append(paperId)

        self.authors.update_one({"_id":authorId},{"$set":{"paper":paper}})

        print(paper)

    def insertPaperToPaper(self,title,authors,publication,url = None,page_num=None):
        paper = {
            "title":title,
            "authors":authors,
            "publication":publication,
            "url":url,
            "page_num":page_num
        }
        paperId = self.paper.insert(paper)

        return paperId

    def showPublications(self):
        ptr = self.publications.find()
        for item in ptr:
            print(item)
   
    # Test
    def updateAuthorToAuthors(self, last_name, first_name, affiliation=None, paper=None):
        author = {
            "last_name": last_name,
            "first_name": first_name,
            "affiliation": affiliation,
            # "paper": paper
        }

        ptr = self.authors.find({"last_name":last_name,"fisrst_name":first_name,"affiliation":affiliation}, {"paper": 1})
        
        print(ptr)
        if ptr.count() == 0:
            oldPaper = []
        else:
            for item in ptr:
                oldPaper = item["paper"]
                print(oldPaper)
        # author = ptr  .next()
        # paper = author["paper"]
        oldPaper.append(paper)
        authorToUpdate = {
            "last_name": last_name,
            "first_name": first_name,
            "affiliation": affiliation,
            "paper": oldPaper
        }
        authorId = self.authors.update_one(author, {"$set": authorToUpdate}, upsert=True)
        return authorId
    
    # Test
    def oneClickInsertionToPaper(self, title, authors, publication_name, year, times=None, location=None, month=None,
                                 associated_volume=None, url=None, page_num=None):
        if month:
            get_PublicationId = self.updateJournalToPublications(publication_name, associated_volume, year, month)
        else:
            get_PublicationId = self.updateConferenceToPublications(publication_name, times, location, year)
        paper_author_list_toInsert = []
        cyclicCounter = 1
        for author in authors:
            first_name = author["first_name"]
            last_name = author["last_name"]
            try:
                affiliation = author["affiliation"]  # 需要商讨
            except:
                affiliation = None
            get_AuthorId = self.updateNameAndAffiliationToAuthors(last_name, first_name, affiliation)
            temp = {
                "_id": get_AuthorId,
                'last_name': last_name,
                'first_name': first_name,
                'sort': cyclicCounter
            }
            paper_author_list_toInsert.append(temp)
            cyclicCounter = cyclicCounter + 1
        get_Paper_id = self.insertPaperToPaper(title, paper_author_list_toInsert, get_PublicationId, url, page_num)
        # get_Paper_id = self.insertPaperToPaper(title, paper_author_list_toInsert, publication_name, url, page_num)
        for author in authors:
            # author = author.spilt()
            first_name = author["first_name"]
            last_name = author["last_name"]
            try:
                affiliation = author["affiliation"]  # 需要商讨
            except:
                affiliation = None

            self.updateAuthorToAuthors(last_name, first_name, affiliation, get_Paper_id)


    # 3 Query all paper by the name of publication and time range
    def queryPaperWithYearRange(self,publication_name,year_start,year_end):

        # papersInfo = self.publications.find({"name":publication_name,"time":{"$gte":datetime.datetime(year_start,1,1),"$lt":datetime.datetime(year_end,1,1)}})

        publicationsInfo = self.publications.aggregate(
            [
                # find publication with given name and time range(>= year_start and < year_end)
                {
                    "$match":{"name":publication_name,"time":{"$gte":datetime.datetime(year_start,1,1),"$lt":datetime.datetime(year_end,1,1)}}
                },
                # find papers in paper collection with given publication(_id)
                {
                    "$lookup":
                    {
                        "from":"paper",
                        "localField":"_id",
                        "foreignField":"publication",
                        "as":"paper"
                    }
                }
            ]
        )
        result = []
        for publicationInfo in publicationsInfo:
            print(publicationInfo)
            # result.append(publicationInfo)
            # time = publicationInfo["time"]
            # # Conference or Journal?
            # try:
            #     publicationInfo["location"]
            #     print(publicationInfo["name"],publicationInfo["times"],publicationInfo["location"],time.year)
            # except:
            #     print(publicationInfo["name"],publicationInfo["associated_volume"],time.year,time.month)
        
            # papersInfor = publicationInfo["paper"]
            # for paperInfo in papersInfor:
            #     print(paperInfo["title"])
            #     authors = paperInfo["authors"]
            #     for author in authors:
            #         print(author["first_name"],author["last_name"])
            #     print(paperInfo["url"])
            #     print(paperInfo["page_num"])

        return result

    # 2 Query all info for paper by the name of author
    def queryAuthorsWithName(self,last_name,first_name):
        authorInfo = self.authors.aggregate(
                [
                    {
                        "$match":{"last_name":last_name,"first_name":first_name}
                    },
                    {
                        "$unwind": "$paper",  # unwind document by paper array
                    },
                    {
                        "$lookup":                  # look up paper info by paper(_id)
                        {
                            "from":"paper",   
                            "localField":"paper", 
                            "foreignField": "_id",  
                            "as": "paper"  
                        }
                    },
                    {
                        "$lookup":                  # look up publication info by pubilication(_id)
                        {
                            "from":"publications",   
                            "localField":"paper.publication", 
                            "foreignField": "_id",  
                            "as": "publication"  
                        }
                    },
                    { 
                        "$group": 
                        {              # group up unwinded documents
                            "_id": "$_id",
                            "last_name":{"$first":"$last_name"},
                            "first_name":{"$first":"$first_name"},
                            "paper":{"$push":"$paper"},
                            "publication":{"$push":"$publication"}
                        }
                    },
    
                ]
            )



        result = []
        for author in authorInfo:
            # print(author)
            result.append(author)
            # print(author)
            # papersInfo = author["paper"]
            # publicationsInfo = author["publication"]
            # # print(author["paper"])
            # for paperInfo in papersInfo:
            #     paper = paperInfo[0]
            #     print(paper["title"])
            #     authors = paper["authors"]
            #     for author in authors:
            #         print(author["first_name"],author["last_name"])
            #     # print(paper["authors"])
            # for publicationInfo in publicationsInfo:
            #     # print(publicationInfo)
            #     publication = publicationInfo[0]
            #     time = publication["time"]     
            #     # Conference or Journal?
            #     try:
            #         publication["location"]
            #         print(publication["name"],publication["times"],publication["location"],time.year)
            #     except:
            #         print(publication["name"],publication["associated_volume"],time.year,time.month)
        print(result)
        return result

    # 1 Query all relevant info for paper by the title of paper
    def queryPaperWithTitle(self,title):
        papers = self.paper.aggregate(
            [
                {
                    "$match": {"title": title}
                },      
                {
                    "$unwind": "$authors",  # unwind document by authors array
                },
                {
                "$lookup":                  # look up authors info by _id
                    {
                        "from":"authors",   
                        "localField":"authors._id", 
                        "foreignField": "_id",  
                        "as": "authors"  
                    }
                },
                {
                    "$sort":{"authors.sort":1}    #sort author in order by "sort"
                },
                { 
                    "$group": {              # group up unwinded documents
                        "_id": "$_id",
                        "title":{"$first":"$title"},
                        "authors": { "$push": "$authors" },
                        "publication":{"$first":"$publication"},
                        "url":{"$first":"$url"},
                        "page_num":{"$first":"$page_num"}
                        }
                },
                {
                "$lookup":                   # look up publication info by _id
                    {
                        "from":"publications",
                        "localField":"publication",
                        "foreignField": "_id",  
                        "as": "publication"  
                    }
                },
            ]
        )
        


        result = []
        for paper in papers:
            result.append(paper)
            # print(paper)    # all paper info
            # for authors in paper["authors"]:
            #     for author in authors:
            #         print(author["_id"])    # all author id
        print(result)
        return result
    


mongo = Mongo()

# mongo.oneClickInsertionToPaper()
# mongo.queryPaperWithTitle("Management")   # Q1
# mongo.queryAuthorsWithName("Yiwen","Xu")  # Q2
# mongo.queryPaperWithYearRange("Journal",1997,2021)    #Q3



# region Create Test Date

# publicationId = mongo.insertConferenceToPublications("Sicence","21th","Dallas",1999)
# authorId = mongo.insertAuthorToAuthors("Yiwen","Xu",afflication1)
# authorId2 = mongo.insertAuthorToAuthors("Shuang","Liang",afflication2)
authors = [{
    # "_id":authorId,
    "last_name":"Yiwen",
    "first_name":"Xu",
    "affiliation":afflication1
},
{
    #  "_id":authorId2,
    "last_name":"Shuang",
    "first_name":"Liang",
    "affiliation":afflication2
}
]
# mongo.oneClickInsertionToPaper("paperTilleTest1",authors,"oublicationTest1",2021,None,None,10,"associated_volumeTest1",url='www.smu.edu',page_num=45)
mongo.oneClickInsertionToPaper("paperTilleTest3",authors,"oublicationTest2",1997,"17th","Dallas")
# paperId = mongo.insertPaperToPaper("Management",authors,publicationId)
# paperId2 = mongo.insertPaperToPaper("Algorithm",authors,publicationId)

# mongo.queryAuthorForPaper(authorId,paperId)
# mongo.queryAuthorForPaper(authorId2,paperId)
# mongo.queryAuthorForPaper(authorId,paperId2)
# mongo.queryAuthorForPaper(authorId2,paperId2)


# publicationId = mongo.insertJournalToPublications("Journal","volume",1997,12)
# authorId = mongo.insertAuthorToAuthors("Yiwen","Xu",afflication2)
# authors = [{
#     "_id":authorId,
#     "last_name":"Yiwen",
#     "first_name":"Xu",
#     "sort":1
# }]
# paperId = mongo.insertPaperToPaper("MongoDB",authors,publicationId)
# mongo.queryAuthorForPaper(authorId,paperId)

# publicationId = mongo.insertJournalToPublications("Journal","volume",2020,1)
# authorId = mongo.insertAuthorToAuthors("Yiwen","Xu",afflication2)
# authors = [{
#     "_id":authorId,
#     "last_name":"Yiwen",
#     "first_name":"Xu",
#     "sort":1
# }]
# paperId = mongo.insertPaperToPaper("MSL",authors,publicationId)
# mongo.queryAuthorForPaper(authorId,paperId)



# endregion


# region Few reference code

# mongo.showPublications()
# mongo.insertJournalToPublications("Journal","volume3","2020-12-21")

# with myclient:

    
    # db = myclient.SMUKI
#     db.Paper.insert_many(paper)
#     print(db.collection_names())

# paper = mongo.paper.find()
# print(db.Paper.find().count())
# print(paper.next())
# print(paper.next())
# print(paper.next())
# print(paper)

# mongo.showPulications()
# print(parser.parse("2020-07-07"))
# print(datetime.datetime(2009,11,11))
    # def connectDB():
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")


    # def showDB():


# db = connectDB()
# print(db.SMUKI.Paper.find().count())

# endregion
