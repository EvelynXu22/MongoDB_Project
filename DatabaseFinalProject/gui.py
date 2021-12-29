from tkinter import *
from mongodb_query_test import *

WINDOW_SIZE = '700x1000'
BORDER_WITH = 3
TEXT_WIDTH = 60
TEXT_HEIGHT = 1


class MY_GUI:
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.mongo = Mongo()
    def set_init_window(self):
        self.insertPage()
        self.queryPage()

    def queryPage(self):

        self.query_label = Label(self.init_window_name,text="Query",font=('',15))
        self.query_label.grid(row=18,column=0)

        self.query_title_label = Label(self.init_window_name, text='Paper Title')
        self.query_title_label.grid(row=19, column=0)
        self.query_title_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_title_text.grid(row=19, column=1)
        self.query1_button = Button(self.init_window_name, text='Query#1', width=15, command=self.query1)
        self.query1_button.grid(row=20, column=2)

        self.query_last_name_label = Label(self.init_window_name, text='Author Last Name')
        self.query_last_name_label.grid(row=21, column=0)
        self.query_first_name_label = Label(self.init_window_name, text='Author First Name')
        self.query_first_name_label.grid(row=22, column=0)
        self.query_last_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_last_name_text.grid(row=21, column=1)
        self.query_first_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_first_name_text.grid(row=22, column=1)
        self.query2_button = Button(self.init_window_name, text='Query#2', width=15, command=self.query2)
        self.query2_button.grid(row=23, column=2)


        self.query_publication_label = Label(self.init_window_name, text='Publication Name')
        self.query_publication_label.grid(row=24, column=0)
        self.query_start_year_label = Label(self.init_window_name, text='Start Year')
        self.query_start_year_label.grid(row=25, column=0)
        self.query_end_year_label = Label(self.init_window_name, text='End Year')
        self.query_end_year_label.grid(row=26, column=0)
        self.query_publication_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_publication_text.grid(row=24, column=1)
        self.query_start_year_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_start_year_text.grid(row=25, column=1)
        self.query_end_year_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.query_end_year_text.grid(row=26, column=1)
        self.query3_button = Button(self.init_window_name, text='Query#3', width=15, command=self.query3)
        self.query3_button.grid(row=27, column=2)

        self.query_result_label = Label(self.init_window_name, text='Query Result')
        self.query_result_label.grid(row=28, column=0)
        self.query_result_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT*10)
        self.query_result_text.grid(row=28, column=1)
    def insertPage(self):

        self.is_submit = False
        self.selection = StringVar()
        self.resultText = StringVar()


        self.init_window_name.title("Paper Search Database")
        self.init_window_name.geometry(WINDOW_SIZE)

        self.insert_label = Label(self.init_window_name,text='Insert',font=('',15))
        self.insert_label.grid(row=0,column=0)

        self.title_label = Label(self.init_window_name,text='Paper Title')
        self.title_label.grid(row=2,column=0)
        self.author_label = Label(self.init_window_name,text='Author')
        self.author_label.grid(row=3,column=0)

        self.publication_label = Label(self.init_window_name, text='Publication')
        self.publication_label.grid(row=4, column=0)
        self.name_label = Label(self.init_window_name, text='Name')
        self.name_label.grid(row=5, column=0)
        self.times_label = Label(self.init_window_name, text='Times')
        self.times_label.grid(row=6, column=0)
        self.location_label = Label(self.init_window_name, text='Location')
        self.location_label.grid(row=7, column=0)
        self.time_year_label = Label(self.init_window_name, text='Time(Year)')
        self.time_year_label.grid(row=8, column=0)
        self.journal_name_label = Label(self.init_window_name, text='Name')
        self.journal_name_label.grid(row=9, column=0)
        self.associated_label = Label(self.init_window_name, text='Associated Volume')
        self.associated_label.grid(row=10, column=0)
        self.journal_time_year_label = Label(self.init_window_name, text='Time(Year)')
        self.journal_time_year_label.grid(row=11, column=0)
        self.journal_time_month_label = Label(self.init_window_name, text='Time(Month)')
        self.journal_time_month_label.grid(row=12, column=0)

        self.url_label = Label(self.init_window_name, text='URL(Optional)')
        self.url_label.grid(row=13, column=0)
        self.page_num_label = Label(self.init_window_name, text='Page Number(Optional)')
        self.page_num_label.grid(row=14, column=0)
        self.result_label = Label(self.init_window_name, textvariable=self.resultText,fg='red')
        self.result_label.grid(row=15, column=1)

        self.title_text = Text(self.init_window_name,width=TEXT_WIDTH,height=TEXT_HEIGHT)
        self.title_text.grid(row=2,column=1)
        self.author_text = Text(self.init_window_name, width=TEXT_WIDTH,height=TEXT_HEIGHT*3)
        self.author_text.grid(row=3, column=1)

        self.conference_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.conference_name_text.grid(row=5, column=1)
        self.times_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.times_text.grid(row=6, column=1)
        self.location_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.location_text.grid(row=7, column=1)
        self.time_year_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.time_year_text.grid(row=8, column=1)

        self.journal_name_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT,stat=DISABLED,bg='gray')
        self.journal_name_text.grid(row=9, column=1)
        self.associated_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT,stat=DISABLED,bg='gray')
        self.associated_text.grid(row=10, column=1)
        self.journal_time_year_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT,stat=DISABLED,bg='gray')
        self.journal_time_year_text.grid(row=11, column=1)
        self.journal_time_month_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT,stat=DISABLED,bg='gray')
        self.journal_time_month_text.grid(row=12, column=1)


        self.url_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.url_text.grid(row=13, column=1)
        self.page_num_text = Text(self.init_window_name, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.page_num_text.grid(row=14, column=1)


        self.author_button = Button(self.init_window_name,text='Submit Author',width=15,command=self.submitAuthor)
        self.author_button.grid(row=3,column=2)
        self.all_button = Button(self.init_window_name, text='Submit All', width=15, command=self.submitAll)
        self.all_button.grid(row=16, column=1)
        self.clear_button = Button(self.init_window_name, text='Clear', width=15, command=self.clear)
        self.clear_button.grid(row=16, column=2)

        self.publication_conference_selection = Radiobutton(self.init_window_name,text='Conference',variable=self.selection,value='Conference',command=self.selection_input)
        self.publication_journal_selection = Radiobutton(self.init_window_name,text='Journal',variable=self.selection,value='Journal',command=self.selection_input)
        self.publication_conference_selection.grid(row=4,column=1)
        self.publication_journal_selection.grid(row=4, column=2)
        # Default select 'conference'
        self.publication_conference_selection.select()



    # click submit author button
    def submitAuthor(self):

        author = self.author_text.get(1.0,END)
        self.author_text.delete(1.0,END)

        print(author)
        return author

    # click submit all button
    def submitAll(self):
        if not self.is_submit:

            title = self.title_text.get(1.0,END)
            author = self.author_text.get(1.0,END)
            url = self.url_text.get(1.0, END)
            page_num = self.page_num_text.get(1.0, END)

            conference_name = self.conference_name_text.get(1.0, END)
            times = self.times_text.get(1.0, END)
            location = self.location_text.get(1.0, END)
            conference_year = self.time_year_text.get(1.0, END)

            journal_name = self.journal_name_text.get(1.0, END)
            associated = self.associated_text.get(1.0, END)
            joournal_year = self.journal_time_year_text.get(1.0, END)
            journal_month = self.journal_time_month_text.get(1.0, END)


            print("SubmitAll")
            self.resultText.set("Success")
            self.is_submit = True
        else:
            self.resultText.set("Please Clear")

    # click clear button
    def clear(self):
        self.title_text.delete(1.0, END)
        self.author_text.delete(1.0, END)
        self.url_text.delete(1.0, END)
        self.page_num_text.delete(1.0, END)

        self.conference_name_text.delete(1.0, END)
        self.times_text.delete(1.0, END)
        self.location_text.delete(1.0, END)
        self.time_year_text.delete(1.0, END)

        self.journal_name_text.delete(1.0, END)
        self.associated_text.delete(1.0, END)
        self.journal_time_year_text.delete(1.0, END)
        self.journal_time_month_text.delete(1.0, END)

        self.resultText.set("")
        self.is_submit = False

        print("Clear")

    # When choose Conference or Journal
    def selection_input(self):
        get = self.selection.get()
        print(get)

        if get == 'Conference':
            self.conference_name_text["state"] = NORMAL
            self.times_text["state"] = NORMAL
            self.location_text["state"] = NORMAL
            self.time_year_text["state"] = NORMAL

            self.conference_name_text["bg"] = 'white'
            self.times_text["bg"] = 'white'
            self.location_text["bg"] = 'white'
            self.time_year_text["bg"] = 'white'

            self.journal_name_text["state"] = DISABLED
            self.associated_text["state"] = DISABLED
            self.journal_time_year_text["state"] = DISABLED
            self.journal_time_month_text["state"] = DISABLED

            self.journal_name_text["bg"] = 'gray'
            self.associated_text["bg"] = 'gray'
            self.journal_time_year_text["bg"] = 'gray'
            self.journal_time_month_text["bg"] = 'gray'

            print("Conference")

        else:
            self.conference_name_text["state"] = DISABLED
            self.times_text["state"] = DISABLED
            self.location_text["state"] = DISABLED
            self.time_year_text["state"] = DISABLED

            self.conference_name_text["bg"] = 'gray'
            self.times_text["bg"] = 'gray'
            self.location_text["bg"] = 'gray'
            self.time_year_text["bg"] = 'gray'

            self.journal_name_text["state"] = NORMAL
            self.associated_text["state"] = NORMAL
            self.journal_time_year_text["state"] = NORMAL
            self.journal_time_month_text["state"] = NORMAL

            self.journal_name_text["bg"] = 'white'
            self.associated_text["bg"] = 'white'
            self.journal_time_year_text["bg"] = 'white'
            self.journal_time_month_text["bg"] = 'white'

            print("Journal")

            # self.publication_text.insert(1.0, 'Please input Journal Information')

    # click Query1 button
    def query1(self):
        paperTitle = self.query_title_text.get(1.0,END)

        # check whether filled required information for searching
        if paperTitle.isspace():
            self.showNotice()
            return
        # else
        result = mongo.queryPaperWithTitle(paperTitle)

        # show result to result text field
        # self.query_result_text.insert(1.0,result)
        print(result)

        print("Query1")
        return

    # click Query2 button
    def query2(self):
        last_name = self.query_last_name_text.get(1.0,END)
        first_name = self.query_first_name_text.get(1.0,END)

        # check whether filled required information for searching
        if last_name.isspace() or first_name.isspace():
            self.showNotice()
            return
        # else
        result = mongo.queryAuthorsWithName(self,last_name,first_name)
        # show result to result text field
        # self.query_result_text.insert(1.0,result)
        print(result)

        print("Query2")
        return

    # click Query3 button
    def query3(self):
        publication = self.query_publication_text.get(1.0,END)
        start = self.query_start_year_text.get(1.0,END)
        end = self.query_end_year_text.get(1.0,END)

        # check whether filled required information for searching
        if publication.isspace() or start.isspace() or end.isspace():
            self.showNotice()
            return
        # else

        print("Query3")
        result = mongo.queryPaperWithYearRange(publication,int(start),int(end))

        # show result to result text field
        # self.query_result_text.insert(1.0,result)
        print(result)

        return
    
    # show notice in result text field
    def showNotice(self):
        self.query_result_text.delete(1.0, END)
        self.query_result_text.insert(1.0,"Please Input Enough Information")


def gui_start():
    init_window = Tk()
    PORTAL = MY_GUI(init_window)
    PORTAL.set_init_window()
    init_window.mainloop()

    # PORTAL.query2()

gui_start()
