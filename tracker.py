import requests
from bs4 import BeautifulSoup
import tkinter as tk
import re

class DormNetTracker(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Window Setting
        self.title('Dormnet Tracker')
        self.geometry('250x100')
        self.configure(background='white')

        self.header_label = tk.Label(self, text='輸入宿網IP以取得當前上傳流量')
        self.header_label.pack()

        self.ip_frame = tk.Frame(self)
        self.ip_frame.pack(side=tk.TOP)
        self.ip_label = tk.Label(self.ip_frame, text='IP Address:')
        self.ip_label.pack(side=tk.LEFT)
        self.ip_entry = tk.Entry(self.ip_frame)
        self.ip_entry.pack(side=tk.LEFT)


        self.result_label = tk.Label(self)
        self.result_label.pack()

        self.get_netflow_btn = tk.Button(self, text='取得當前流量', command=self.get_netflow)
        self.get_netflow_btn.pack()

        # Run
        # self.run()
        self.update_flow()
        

    def get_netflow(self):
        ip = self.ip_entry.get()
        data = {'ip':str(ip), 'submit':"Submit"}
        session = requests.Session()
        r = session.post('https://uncia.cc.ncu.edu.tw/dormnet/index.php?section=netflow', data = data)
        soup = BeautifulSoup(r.content, 'html.parser')
        t = soup.find("td", string='24hr 總量').find_next_sibling("td").text
        print(t[t.find("(")+1:t.find(")")])
        self.result_label.configure(text='當前24小時內上傳流量:' + t[t.find("(")+1:t.find(")")])

    def update_flow(self):
        pattern = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        if(re.match(pattern, self.ip_entry.get())):
            self.get_netflow()
            print("Get netflow")
        self.after(600,000, self.update_flow)
            

if __name__ == '__main__':
    app = DormNetTracker()
    app.mainloop()