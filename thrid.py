from Tkinter import Tk, BOTH
from ttk import Frame, Label, Button, Style
import httplib2
import json

username = username
password = password

class ticketWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Zendesk Views")
        self.style = Style()
        self.style.theme_use("default")
        self.style.configure("TFrame", background="#333")
        self.style.configure("TLabel", backgroun="#444")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        ticket1 = ticketViews(parent, 26887076)
        ticket2 = ticketViews(parent, 35868228)

    def centerWindow(self):
        w = 250
        h = 100

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw) /2
        y = (sh) /2
        self.parent.geometry('%dx%d+%d+%d' % (w, h ,x ,y))

    def createQuit(self):
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)

class ticketViews():

    def __init__(self, parent, id):
        self.client = client = httplib2.Http(disable_ssl_certificate_validation=True)
        self.client.add_credentials(username, password)

        ## Pull View Name
        self.viewResp, self.viewContent = client.request("https://rackspacecloud.zendesk.com/api/v2/views/" + str(id) + ".json")
        self.viewData = json.loads(self.viewContent)
        print repr(self.viewData)
        self.countResp, self.countContent = client.request("https://rackspacecloud.zendesk.com/api/v2/views/" + str(id) + "/count.json")
        self.viewResp, self.viewContent = client.request("https://rackspacecloud.zendesk.com/api/v2/views/" + str(id) + ".json")
        self.countData = json.loads(self.countContent)
        print repr(self.countContent)
        
        self.parent = parent
        print(self.parent.winfo_width())
        self.label = Label(text=self.viewData["view"]["title"] + " " + str(self.countData["view_count"]["value"]))
        self.label.pack(fill=BOTH)
        
def main():

    root = Tk()
    ex = ticketWindow(root)

    root.mainloop()

if __name__ == '__main__':
    main()
