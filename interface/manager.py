import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import csv
import time
import subprocess

#p = subprocess.Popen(['airodump-ng', 'wlan0mon', '-w from_py', '--output-format', 'csv'])

## Quick fix really dirty
time.sleep(2)

def get_ap():
    csv_file = open('test2.csv', 'r') # When used with airodump add space at start
    csv_file.readline() ## Ignore first line tricks
    csv_file.readline() ## Ignore second line
    reader = csv.reader(csv_file, delimiter=',')
    AP_list = []
    for row in reader:
        try:
            data = (row[0].strip(), row[3].strip(), row[13].strip())
            AP_list.append(data)
        except:
            break
    csv_file.close()
    return AP_list

def get_client():
    client_list = []
    printed = False
    csv_file = open('test2.csv', 'r') # When used with airodump add space at start
    values = csv_file.readlines()
    for line in values:
        try:
            if 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs' in line:
                printed = True
                continue
            if printed:
                splited_line = line.split(',')
                data = (splited_line[0].strip(), splited_line[5].strip())
                client_list.append(data)
        except:
            break
    csv_file.close()
    return client_list

## TODO
def filter_client():
    return NotImplemented

class SelectBSSIDWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="BSSID Select")

        ## Box
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        ## List Model AP
        self.AP_liststore_model = Gtk.ListStore(str, str, str)
        self.AP_list = get_ap()
        for AP in self.AP_list:
            self.AP_liststore_model.append(list(AP))
        self.current_filter_language = None

        ## Define AP Treeview
        self.treeview_ap = Gtk.TreeView(model=self.AP_liststore_model)
        ## Scrollable Window
        self.scrollable_treeview_ap = Gtk.ScrolledWindow()
        self.scrollable_treeview_ap.add(self.treeview_ap)
        ## Render text
        self.renderer_text = Gtk.CellRendererText()
        ## Set Columns
        self.column_bssid = Gtk.TreeViewColumn("BSSID", self.renderer_text, text=0)
        self.column_bssid_channel = Gtk.TreeViewColumn("Channel", self.renderer_text, text=1)
        self.column_apname = Gtk.TreeViewColumn("AP name", self.renderer_text, text=2)
        ## Add Column
        self.treeview_ap.append_column(self.column_bssid)
        self.treeview_ap.append_column(self.column_bssid_channel)
        self.treeview_ap.append_column(self.column_apname)

        ## Add scrollable Window to box
        self.box.pack_start(self.scrollable_treeview_ap, True, True, 0)

        ## List Model AP Client
        self.clientAP_liststore_model = Gtk.ListStore(str, str)
        self.clientAP_list = get_client()
        for client in self.clientAP_list:
            self.clientAP_liststore_model.append(list(client))
        self.current_filter_language = None
        
        self.treeview_client_ap = Gtk.TreeView(model=self.clientAP_liststore_model)
        self.scrollable_treeview_client = Gtk.ScrolledWindow()
        self.scrollable_treeview_client.add(self.treeview_client_ap)
        self.renderer_clients_text = Gtk.CellRendererText()
        self.column_client_SSID = Gtk.TreeViewColumn("ESSID", self.renderer_clients_text, text=0)
        self.column_client_BSSID = Gtk.TreeViewColumn("BSSID", self.renderer_clients_text, text=1)
        self.treeview_client_ap.append_column(self.column_client_SSID)
        self.treeview_client_ap.append_column(self.column_client_BSSID)
        self.box.pack_start(self.scrollable_treeview_client, True, True, 0)

        ## Define refresh button
        self.button_bssid_refresh = Gtk.Button(label="Refresh")
        self.button_bssid_refresh.connect("clicked", self.on_button_refresh_clicked)
        self.box.pack_start(self.button_bssid_refresh, True, True, 0)
        
        ## Define deauth button
        self.button_deauthclient = Gtk.Button(label="Deauth Clients")
        self.button_deauthclient.connect("clicked", self.on_button_deauth_clicked)
        self.box.pack_start(self.button_deauthclient, True, True, 0)

        ## Start fake AP
        self.button_fakeAP = Gtk.Button(label="Start fake AP")
        self.button_fakeAP.connect("clicked", self.on_fakeAP_clicked)
        self.box.pack_start(self.button_fakeAP, True, True, 0)

        ## Start SSlstrip
        self.button_sslstrip = Gtk.Button(label="SSlstrip attack")
        self.button_sslstrip.connect("clicked", self.on_button_sslstrip_clicked)
        self.box.pack_start(self.button_sslstrip, True, True, 0)


    ######## Function

    ## Buttons 
    def on_button_refresh_clicked(self, widget):
        AP_list = get_ap()
        self.AP_liststore_model.clear()
        for AP in AP_list:
            self.AP_liststore_model.append(list(AP))
        
        client_list = get_client()
        self.clientAP_liststore_model.clear()
        for client in client_list:
            self.clientAP_liststore_model.append(list(client))

        print("Refresh BSSID/Client Liste")

    def on_button_deauth_clicked(self, widget):
        selection_ap = self.treeview_ap.get_selection()
        model_ap, treeiter_ap = selection_ap.get_selected()
        print (model_ap[treeiter_ap][0])
        if treeiter_ap is not None:
            for client in self.clientAP_list:
                if client[1] == model_ap[treeiter_ap][0]:
                    print ("True")
                    #subprocess.Popen(['aireplay-ng', '--deauth', '10', '-a', model_ap[treeiter_ap][0], '-c', client[0], 'wlan0mon', '-D'])

    def on_fakeAP_clicked(self, widget):
        config_system = subprocess.run([ "/bin/bash",'../conf/config.sh'])
        print ("Fake AP start")

    def on_button_sslstrip_clicked(self, widget):
        print ("sslstrip start")

win = SelectBSSIDWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


try:
    p.terminate()
except NameError:
    pass