from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,CardTransition,SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton,MDFlatButton,MDRaisedButton,MDFloatingActionButtonSpeedDial
from kivy_garden.mapview import MapView,MarkerMapLayer,MapMarkerPopup
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.utils import get_color_from_hex
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior, CircularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.swiper import MDSwiper
from kivy.uix.behaviors import ButtonBehavior
import numpy as np
import requests
from datetime import datetime,timedelta
import io
from PIL import Image as PILImage
from ftplib import FTP
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem,OneLineIconListItem,IconLeftWidget
from kivy.metrics import dp
from kivymd.icon_definitions import md_icons
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.datatables import MDDataTable
from kivy_garden.graph import Graph,BarPlot,LinePlot
# Window.size = (350, 600)

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Homescreen(ScreenManager):
    def login(self,username, password):
        # print('da click')
        # Thực hiện xác thực đăng nhập ở đây (ví dụ: kiểm tra tên đăng nhập và mật khẩu)
        if username == 'admin' and password == 'ttb':
            app = MDApp.get_running_app()
            app.root.current = 'trangchu'  # Chuyển đến màn hình chính
        else:
            # self.show_error_dialog()
            self.thongbao()

    def thongbao(self):
        toast("Không đúng tên hoặc mật khẩu")
        
class RectangularRippleButton(MDBoxLayout, RectangularRippleBehavior, ButtonBehavior, BackgroundColorBehavior):
    pass


class RectangularRippleImage(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class Hochua(MDApp):
    # data = {
    #         "Hạn ngắn": "facebook",
    #         "Hạn vừa": "youtube",
    #         "Hạn dài": "twitter",
    #         "Lũ": "cloud-circle",
    #         "Cảnh báo lũ": "camera",
    #         }

    def build(self):
        self.mucnuoc,self.qve = self.TTB_API_HC()
        
        # self.theme_cls.colors = colors
        # self.theme_cls.primary_palette = "Teal"
        # self.theme_cls.accent_palette = "Red"
        self.title = "Hồ chứa KTTV"
        self.theme_cls.primary_palette = "Pink"
        Builder.load_file('main.kv')
        self.scr = Homescreen()
        self.scr.current = 'trangchu'
        # self.scr.ids.bottom_navigation.switch_tab('chart')
        return self.scr


    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):

        if tab_text=='TVHN':
            self.root.ids.box_images.clear_widgets()
            self.read_ftp_sever_image('tin_TVHN_0.png')
            self.read_ftp_sever_image('tin_TVHN_1.png')
            images =['cache/tin_TVHN_0.png','cache/tin_TVHN_1.png']
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height='430dp'
                    )
                )   
            # self.read_ftp_sever_image('tin_TVHN_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_TVHN_0.png'
        elif tab_text=='TVHV':
            self.root.ids.box_images.clear_widgets()
            self.read_ftp_sever_image('tin_TVHV_0.png')
            self.read_ftp_sever_image('tin_TVHV_1.png')
            images =['cache/tin_TVHV_0.png','cache/tin_TVHV_1.png']
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height='430dp'
                    )
                )   
            # self.read_ftp_sever_image('tin_TVHV_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_TVHV_0.png'  
        elif tab_text=='TVHD':
            self.root.ids.box_images.clear_widgets()
            self.read_ftp_sever_image('tin_TVHD_0.png')
            self.read_ftp_sever_image('tin_TVHD_1.png')
            self.read_ftp_sever_image('tin_TVHD_2.png')
            images =['cache/tin_TVHD_0.png','cache/tin_TVHD_1.png','tin_TVHD_2.png']
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height='430dp'
                    )
                )   

        elif tab_text=='LULU':
            self.root.ids.box_images.clear_widgets()
            self.read_ftp_sever_image('tin_LULU_0.png')
            self.read_ftp_sever_image('tin_LULU_1.png')
            images =['cache/tin_LULU_0.png','cache/tin_LULU_1.png']
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height='430dp'
                    )
                )   

        elif tab_text=='CBLU':
            self.root.ids.box_images.clear_widgets()
            self.read_ftp_sever_image('tin_CBLU_0.png')
            images =['cache/tin_CBLU_0.png']
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height='430dp'
                    )
                )   
    def on_start(self):
        self.root.ids.tabs.add_widget(Tab(title="TVHN"))
        self.root.ids.tabs.add_widget(Tab(title="TVHV"))
        self.root.ids.tabs.add_widget(Tab(title="TVHD"))
        self.root.ids.tabs.add_widget(Tab(title="LULU"))
        self.root.ids.tabs.add_widget(Tab(title="CBLU"))
        
        data_tables = MDDataTable(
            size_hint=(1, 0.99),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Trạm-Giờ", dp(20)),
                ("1h", dp(20)),
                ("3h", dp(20)),
                ("6h", dp(20)),
                ("12h", dp(20)),
                ("24h", dp(20)),
                ("48h", dp(20)),
                ("72h", dp(20)),
            ],
        )
        ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        for tram in ds_tram:
            if 'mua' in tram[3]:
                muatong = self.TTB_API_muatong(tram[0],tram[2])
                data_tables.add_row((self.chuyentram_vietnam(tram[1],2)[0], muatong[0], muatong[1],muatong[2], muatong[3], muatong[4],muatong[5],muatong[6]))
            else:
                muatong = self.TTB_API_yeutokhac(tram[0],tram[2])
                data_tables.add_row((self.chuyentram_vietnam(tram[1],2)[0], muatong[0], muatong[1],muatong[2], muatong[3], muatong[4],muatong[5],muatong[6]))
                
        data_tables.bind(on_row_press=self.on_row_press)
        self.root.ids.dienmua_layout.add_widget(data_tables)
            
    
    def on_row_press(self, instance_table, instance_row): # click vao row cua bang
        tramten = instance_row.text
        app = MDApp.get_running_app()
        app.root.current = 'tram'
        self.root.ids.solieutram.clear_widgets()
        # self.root.ids.tieude_tram.clear_widgets()
        self.root.ids.tieude_tram.title = str(tramten)
        
        mt_tab = self.chuyentram_vietnam(str(tramten),1)
        
        solieu = self.TTB_API(mt_tab[0],mt_tab[1])
        # print(solieu)
        for tencot in solieu:
            if 'SoLieu'in tencot:
                tencot_sl = 'SoLieu'
            else:
                tencot_sl = 'Solieu'
        for value in range(len(solieu) - 1, -1, -1):
            icon_item = OneLineIconListItem(
                text=solieu[value]['Thoigian_SL'] + ' : ' + solieu[value][tencot_sl]
            )
            # gán su kien cho icon
            self.root.ids.solieutram.add_widget(icon_item)

       
    def vebieudo(self,**kwargs):
        self.root.ids.tieude_tram_bieudo.title = self.root.ids.tieude_tram.title
        now = datetime.now()
        now = datetime(now.year,now.month,now.day)
        gt = []
        tg = []
        for child in self.root.ids.solieutram.children:
            # print(child.text)
            dl = str(child.text).split(':')
            gt.append(float(dl[3].strip()))
            tg.append(datetime.strptime(dl[0].strip() + ':' + dl[1].strip(),"%Y-%m-%d %H:%M"))
        tentram = self.root.ids.tieude_tram.title   # lay ten yeo to ve
        
        # index_date = tg.index(now)
        # data_ve = gt[index_date:]
        
        # print(data_ve)
        # print(gt)
        lists = ['Sông Tranh_mua','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
        if tentram in lists:
            result_list = []
            cumulative_sum = 0
            for num in gt:
                cumulative_sum += num
                result_list.append(cumulative_sum)
            gt  = result_list
        data_ve = gt
        # # print(gt)
        # # print(tg)
        app = MDApp.get_running_app()
        app.root.current = 'bieudo_ve'
        # 'Q điều tiết','Q về'
        if tentram =='Mực nước':
            legen = 'Mực nước(cm)'
        elif tentram =='Q điều tiết' or tentram =='Q về':
            legen = tentram +'(m3/s)'
        else:
            legen = tentram + '(mm)'
        self.root.ids.modulation.clear_widgets()
        if len(data_ve) >3:
            data_ve =np.array(data_ve)
            if tentram in lists:
                val_y_tick = (round(int(max(data_ve)),-1) + 10) - (round(int(min(data_ve)),-1)-10)
                val_y_tick = val_y_tick/10
                ymax = round(int(max(data_ve)),-1)+10
                ymin = 0
            else:
                val_y_tick = (round(int(max(data_ve)),-1) + 10) - (round(int(min(data_ve)),-1)-10)
                val_y_tick = val_y_tick/10
                ymax = round(int(max(data_ve)),-1)+10
                ymin = round(int(min(data_ve)),-1)-10    
                
            self.samples = len(data_ve)
            self.graph = Graph(y_ticks_major=val_y_tick,
                    x_ticks_major=6,
                    border_color=[0, 0, 1, 1],
                    tick_color=[0, 1, 1, 0.7],
                    x_grid=True, y_grid=True,
                    xmin=-0, xmax=self.samples,
                    ymin=ymin, ymax=ymax,
                    draw_border=True,
                    x_grid_label=True, y_grid_label=True,
                    xlabel='Giờ',ylabel=legen)

            self.root.ids.modulation.add_widget(self.graph)
            self.plot = LinePlot(color=[1, 0, 0, 1],line_width=1.5)
            self.graph.add_plot(self.plot)
            self.plot.points = [(t, g) for t, g in enumerate(data_ve)]

    def vebieudo_bar(self,**kwargs):
        now = datetime.now()
        now = datetime(now.year,now.month,now.day)
        tentram = self.root.ids.tieude_tram.title   # lay ten yeo to ve
        lists = ['Sông Tranh_mua','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
        if tentram in lists:
            gt = []
            tg = []
            for child in self.root.ids.solieutram.children:
                # print(child.text)
                dl = str(child.text).split(':')
                gt.append(float(dl[3].strip()))
                tg.append(datetime.strptime(dl[0].strip() + ':' + dl[1].strip(),"%Y-%m-%d %H:%M"))
            # print(tentram)
            # print(gt)
            # # print(gt)
            # # print(tg)
            # index_date = tg.index(now)
            # datave = gt[index_date:]
            datave =gt
            app = MDApp.get_running_app()
            app.root.current = 'bieudo_ve'
            # 
            self.root.ids.modulation.clear_widgets()

            if len(datave) >3:
                datave =np.array(datave)              
        
                val_y_tick = (round(int(max(gt)),-1) + 10) - (round(int(min(gt)),-1)-10)
                val_y_tick = val_y_tick/5
                ymax = round(int(max(gt)),-1)+10
                ymin = 0
                    
                self.samples = len(datave)
                self.graph = Graph(y_ticks_major=val_y_tick,
                        x_ticks_major=6,
                        border_color=[0, 0, 1, 1],
                        tick_color=[0, 1, 1, 0.7],
                        x_grid=True, y_grid=True,
                        xmin=-0, xmax=self.samples,
                        ymin=ymin, ymax=ymax,
                        draw_border=True,
                        x_grid_label=True, y_grid_label=True,
                        xlabel='Giờ',ylabel=str(tentram) + '(mm)')

                self.root.ids.modulation.add_widget(self.graph)
                self.plot = BarPlot(color=[1, 0, 0, 1],bar_width=1.5)
                self.graph.add_plot(self.plot)
                self.plot.points = [(t, g) for t, g in enumerate(datave)]
                
    def chuyentram_vietnam(self,tentram,tiento):
        trammua_vni = ['Mực nước','Q điều tiết','Q về','Sông Tranh_mua','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
        trammua_eng = ['Song Tranh_H','Song Tranh_Qxa','Song Tranh_Qve','Song Tranh_mua','Tra Bui','Tra Giac','Tra Don','Tra Leng','Tra Mai','Tra Cang','Tra Van','Tra Nam 2','Tra Linh','Tra Mai(UBND)']
        matram = ['5ST','5ST','5ST','tramdapst2','TRABUI','tragiac','tradon','traleng','TRAMAI','tracang','travan','tranam2','tralinh','tramai(UBNDHnamTM)']
        tab_bang = ['ho_dakdrinh_mucnuoc','ho_dakdrinh_qve','ho_dakdrinh_qdieutiet','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh']
        if tiento == 1 :
            idx = trammua_vni.index(tentram)
            yeuto  = [matram[idx],tab_bang[idx]]
            return yeuto
        elif tiento == 2 :
            idx = trammua_eng.index(tentram)
            yeuto  = [trammua_vni[idx],matram[idx],tab_bang[idx]]
            return yeuto


    def chuyentram_eng(self,tentram):
        trammua_vni = ['Sông Tranh','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam','Trà Linh']
        trammua_eng = ['tramdapst2','TRABUI','tragiac','tradon','traleng','TRAMAI','tracang','travan','tranam2','tralinh']
        if tentram in trammua_vni:
            idx = trammua_vni.index(tentram)
        return trammua_eng[idx]


    def callback_trangchu(self):
        app = MDApp.get_running_app()
        app.root.current = 'trangchu'
        
    def callback_for_menu_items(self, *args):
        toast(args[0])

    def show_example_grid_bottom_sheet(self):
        # pass
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Mực nước": "waves-arrow-up",
            "Q đến": "alpha-q-circle",
            "Q xả": "alpha-d-circle-outline",
            "Mưa": "weather-pouring",
            "Mưa tại đập": "alpha-c-circle-outline",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    
    def callback_for_menu_items(self, selected_item):
        # Thực hiện cập nhật hình ảnh dựa trên mục được chọn
        if selected_item == "Mực nước":
            self.read_ftp_sever_image('chart_H.png')
            self.root.ids.image_chart_td.source = 'cache/chart_H.png'
        elif selected_item == "Q đến":
            self.read_ftp_sever_image('chart_Q.png')
            self.root.ids.image_chart_td.source = 'cache/chart_Q.png'
        elif selected_item == "Q xả":
            self.read_ftp_sever_image('chart_Q_xa.png')
            self.root.ids.image_chart_td.source = 'cache/chart_Q_xa.png'
        elif selected_item == "Mưa":
            self.read_ftp_sever_image('chart_mua_tranam2.png')
            self.root.ids.image_chart_td.source = 'cache/chart_mua_tranam2.png'
        elif selected_item == "Mưa tại đập":
            self.read_ftp_sever_image('chart_mua_tramdapst2.png')
            self.root.ids.image_chart_td.source = 'cache/chart_mua_tramdapst2.png'
    
    def show_marker_info(self,tram,thongtin):
        toast(tram + ':' + thongtin)

            
    def update_image_source(self, new_image_path):
        pass
        
    def TTB_API_HC(self):
        now = datetime.now()
        kt = datetime(now.year,now.month,now.day,now.hour)
        bd = kt - timedelta(days=1)
        # data = pd.DataFrame()
        # data['time'] = pd.date_range(bd,kt,freq='T')
        matram = '5ST'
        # muc nuoc
        pth = 'http://113.160.225.84:2018/API_TTB/JSON/solieu.php?matram={}&ten_table={}&sophut=1&tinhtong=0&thoigianbd=%27{}%2000:00:00%27&thoigiankt=%27{}%2023:59:00%27'
        pth = pth.format(matram,'ho_dakdrinh_mucnuoc',bd.strftime('%Y-%m-%d'),kt.strftime('%Y-%m-%d'))
        response = requests.get(pth)
        mucnuoc = np.array(response.json())
        # mua
        pth = 'http://113.160.225.84:2018/API_TTB/JSON/solieu.php?matram={}&ten_table={}&sophut=1&tinhtong=0&thoigianbd=%27{}%2000:00:00%27&thoigiankt=%27{}%2023:59:00%27'
        pth = pth.format(matram,'ho_dakdrinh_qve',bd.strftime('%Y-%m-%d'),kt.strftime('%Y-%m-%d'))
        response = requests.get(pth)
        mua = np.array(response.json())
        return mucnuoc,mua
    def TTB_API(self,matram,ten_bang):
        if 'mua' in ten_bang:
            tinhtong = 1
        else:
            tinhtong = 0
        now = datetime.now()
        kt = datetime(now.year,now.month,now.day,now.hour)
        bd = kt - timedelta(days=3)
        # mua
        pth = 'http://113.160.225.84:2018/API_TTB/JSON/solieu.php?matram={}&ten_table={}&sophut=60&tinhtong={}&thoigianbd=%27{}%2000:00:00%27&thoigiankt=%27{}%2023:59:00%27'
        pth = pth.format(matram,ten_bang,tinhtong,bd.strftime('%Y-%m-%d'),kt.strftime('%Y-%m-%d'))
        # print(pth)
        response = requests.get(pth)
        mua = np.array(response.json())
        # print(mua)
        # if len(mua) < 5:
        #     return '-','-'
        return mua    
    def tinhmua(self,data,bd,kt):
        tonngmua = 0
        for a in range(data.shape[0]-1,1,-1):
            date_object = datetime.strptime(data[a]['Thoigian_SL'], "%Y-%m-%d %H:%M:%S")
            if date_object > bd and date_object <=kt:
                tonngmua+= float(data[a]['SoLieu'])
        return tonngmua
    
    
    def TTB_API_SONGTRANH(self,matram):
        now = datetime.now()
        kt = datetime(now.year,now.month,now.day,now.hour)
        bd = kt - timedelta(days=3)
        # mua
        pth = 'http://113.160.225.84:2018/API_TTB/JSON/solieu.php?matram={}&ten_table={}&sophut=60&tinhtong=0&thoigianbd=%27{}%2000:00:00%27&thoigiankt=%27{}%2023:59:00%27'
        pth = pth.format(matram,'mua_songtranh',bd.strftime('%Y-%m-%d'),kt.strftime('%Y-%m-%d'))
        # print(pth)
        response = requests.get(pth)
        mua = np.array(response.json())
        # print(mua)
        if len(mua) < 5:
            return '-','-'
        
        return mua
    
    def TTB_API_muatong(self,matram,tenbang):
        now = datetime.now()
        kt = datetime(now.year,now.month,now.day,now.hour)
        bd = kt - timedelta(days=3)
        # mua
        pth = 'http://113.160.225.84:2018/API_TTB/JSON/solieu.php?matram={}&ten_table={}&sophut=60&tinhtong=1&thoigianbd=%27{}%2000:00:00%27&thoigiankt=%27{}%2023:59:00%27'
        pth = pth.format(matram,tenbang,bd.strftime('%Y-%m-%d'),kt.strftime('%Y-%m-%d'))
        response = requests.get(pth)
        mua = np.array(response.json())
        if len(mua) < 5:
            return '-','-','-','-','-','-','-'
        else:
            giohientai = datetime.strptime(mua[-1]['Thoigian_SL'], '%Y-%m-%d %H:%M:%S')
            mua1 = self.tinhmua(mua,giohientai-timedelta(hours=1),giohientai)
            mua1 = '{:.2f}'.format(mua1)
            mua3 = self.tinhmua(mua,giohientai-timedelta(hours=3),giohientai)
            mua3 = '{:.2f}'.format(mua3)
            mua6 = self.tinhmua(mua,giohientai-timedelta(hours=6),giohientai)
            mua6 = '{:.2f}'.format(mua6)
            mua12 = self.tinhmua(mua,giohientai-timedelta(hours=12),giohientai)
            mua12 = '{:.2f}'.format(mua12)
            mua24 = self.tinhmua(mua,giohientai-timedelta(hours=24),giohientai)
            mua24 = '{:.2f}'.format(mua24)
            mua48 = self.tinhmua(mua,giohientai-timedelta(hours=48),giohientai)
            mua48 = '{:.2f}'.format(mua48)
            mua72 = self.tinhmua(mua,giohientai-timedelta(hours=72),giohientai)
            mua72 = '{:.2f}'.format(mua72)
        return mua1,mua3,mua6,mua12,mua24,mua48,mua72
    def TTB_API_yeutokhac(self,matram,tenbang):
        now = datetime.now()
        kt = datetime(now.year,now.month,now.day,now.hour)
        bd = kt - timedelta(days=3)
        # mua
        pth = 'http://113.160.225.84:2018/API_TTB/JSON/solieu.php?matram={}&ten_table={}&sophut=60&tinhtong=1&thoigianbd=%27{}%2000:00:00%27&thoigiankt=%27{}%2023:59:00%27'
        pth = pth.format(matram,tenbang,bd.strftime('%Y-%m-%d'),kt.strftime('%Y-%m-%d'))
        # print(pth)
        response = requests.get(pth)
        mua = np.array(response.json())
        if len(mua) < 5:
            return '-','-','-','-','-','-','-'
        else:
            # giohientai = datetime.strptime(mua[-1]['Thoigian_SL'], '%Y-%m-%d %H:%M:%S')
            h1 = mua[-1]['SoLieu']
            h3 = mua[-3]['SoLieu']
            h6 = mua[-6]['SoLieu']
            h12 = mua[-12]['SoLieu']
            h24 = mua[-24]['SoLieu']
            h48 = mua[-48]['SoLieu']
            h72 = mua[-72]['SoLieu']
        return h1,h3,h6,h12,h24,h48,h72   
    def read_ftp_sever_image(self,tenanh):
        # Thông tin máy chủ FTP và đường dẫn đến file ftp://203.209.181.174/DAKDRINH/Image
        ftp_host = '203.209.181.174'
        ftp_user = 'admin'
        ftp_password = 'Supportdng'
        file_path = 'SONGTRANH/Image' + '/' + tenanh
        # Kết nối đến máy chủ FTP
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_password)
        with open('cache/'+ tenanh, 'wb') as local_file:
            ftp.retrbinary('RETR ' + file_path, local_file.write)
        ftp.quit()
        
    
    def get_ftp_image(self,tram):
        self.read_ftp_sever_image(tram)
        self.root.ids.image_chart_tvhn.source = "cache/" + tram


    def get_custom_value(self):
        mucnuoc,qve = self.TTB_API_HC()
        # Trả về giá trị bạn muốn
        return mucnuoc[-1]['Solieu'],qve[-1]['Solieu']


if __name__ == '__main__':
    Hochua().run()
