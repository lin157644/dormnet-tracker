import requests
from bs4 import BeautifulSoup
import tkinter as tk


window = tk.Tk()
# Window Setting
window.title('Dormnet Tracker')
window.geometry('250x100')
window.configure(background='white')


def get_netflow():
    ip = ip_entry.get()

    
    data = {'ip':str(ip), 'submit':"Submit"}
    session = requests.Session()
    r = session.post('https://uncia.cc.ncu.edu.tw/dormnet/index.php?section=netflow', data = data)

    # if r.status_code == requests.codes.ok:
    #     with open('r.html', 'wb') as f:
    #         f.write(r.content)
    #         print('OK')

    soup = BeautifulSoup(r.content, 'html.parser')
    t = soup.find("td", string='24hr 總量').find_next_sibling("td").text
    print(t[t.find("(")+1:t.find(")")])
    result_label.configure(text='當前24小時內上傳流量:' + t[t.find("(")+1:t.find(")")])

header_label = tk.Label(window, text='輸入宿網IP以取得當前上傳流量')
header_label.pack()

ip_frame = tk.Frame(window)
ip_frame.pack(side=tk.TOP)
ip_label = tk.Label(ip_frame, text='IP Address:')
ip_label.pack(side=tk.LEFT)
ip_entry = tk.Entry(ip_frame)
ip_entry.pack(side=tk.LEFT)


result_label = tk.Label(window)
result_label.pack()

get_netflow_btn = tk.Button(window, text='取得當前流量', command=get_netflow)
get_netflow_btn.pack()

# Run
window.mainloop()