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
from kivymd.uix.list import OneLineListItem
from kivy.metrics import dp
# Window.size = (350, 600)

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Homescreen(ScreenManager):
    def login(self,username, password):
        # print('da click')
        # Thực hiện xác thực đăng nhập ở đây (ví dụ: kiểm tra tên đăng nhập và mật khẩu)
        if username == 'admin' and password == 'admin':
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

    # def on_start(self):
    #     self.root.ids.tabs.add_widget(Tab(title="TVHN"))
    #     self.root.ids.tabs.add_widget(Tab(title="TVHV"))
    #     self.root.ids.tabs.add_widget(Tab(title="TVHD"))
    #     self.root.ids.tabs.add_widget(Tab(title="LULU"))
    #     self.root.ids.tabs.add_widget(Tab(title="CBLU"))
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):

        if tab_text=='TVHN':
            images = []
            self.root.ids.box_images.clear_widgets()
            for p in range(4):
                try:
                    linkimage = 'tin_TVHN_{}.png'.format(str(p))
                    self.read_ftp_sever_image(linkimage)
                    images.append('cache/' + linkimage )
                except:
                    pass
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        width=Window.size[0] - dp(20),
                        height=Window.size[1] - dp(20)
                    )
                )   
            # self.read_ftp_sever_image('tin_TVHN_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_TVHN_0.png'
        elif tab_text=='TVHV':
            images = []
            self.root.ids.box_images.clear_widgets()
            for p in range(4):
                try:
                    linkimage = 'tin_TVHV_{}.png'.format(str(p))
                    self.read_ftp_sever_image(linkimage)
                    images.append('cache/' + linkimage )
                except:
                    pass
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height="350dp"
                    )
                )   
            # self.read_ftp_sever_image('tin_TVHV_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_TVHV_0.png'  
        elif tab_text=='TVHD':
            images = []
            self.root.ids.box_images.clear_widgets()
            for p in range(4):
                try:
                    linkimage = 'tin_TVHD_{}.png'.format(str(p))
                    self.read_ftp_sever_image(linkimage)
                    images.append('cache/' + linkimage )
                except:
                    pass
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height="350dp"
                    )
                )   
            # self.read_ftp_sever_image('tin_TVHD_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_TVHD_0.png'            
        elif tab_text=='LULU':
            images = []
            self.root.ids.box_images.clear_widgets()
            for p in range(4):
                try:
                    linkimage = 'tin_LULU_{}.png'.format(str(p))
                    self.read_ftp_sever_image(linkimage)
                    images.append('cache/' + linkimage )
                except:
                    pass
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height="350dp"
                    )
                )   
            # self.read_ftp_sever_image('tin_LULU_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_LULU_0.png'
        elif tab_text=='CBLU':
            images = []
            self.root.ids.box_images.clear_widgets()
            for p in range(4):
                try:
                    linkimage = 'tin_CBLU_{}.png'.format(str(p))
                    self.read_ftp_sever_image(linkimage)
                    images.append('cache/' + linkimage )
                except:
                    pass
            for image in images:
                self.root.ids.box_images.add_widget(
                    Image(
                        source=image,
                        size_hint=(1, None),
                        height="350dp"
                    )
                )   
            # self.read_ftp_sever_image('tin_CBLU_0.png')
            # self.root.ids.image_bantin.source = 'cache/tin_CBLU_0.png'
    
    def on_start(self):
        self.root.ids.tabs.add_widget(Tab(title="TVHN"))
        self.root.ids.tabs.add_widget(Tab(title="TVHV"))
        self.root.ids.tabs.add_widget(Tab(title="TVHD"))
        self.root.ids.tabs.add_widget(Tab(title="LULU"))
        self.root.ids.tabs.add_widget(Tab(title="CBLU"))
        
        
        trammua = ['Sông Tranh','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam','Trà Linh']
        for i in range(len(trammua)):
            self.root.ids.container.add_widget(
                OneLineListItem(
                    text=str(i+1) + '. ' + trammua[i] + ':                ' + '25 mm'
                    # text_color='aliceblue',  # Màu trắng cho chữ, sử dụng giá trị RGBA
                )
            )
    
        #  # list of images
        # images = ['cache/tin_TVHN_0.png', 'cache/tin_TVHN_0.png'] 
        
        # for image in images:
        self.root.ids.box_images.add_widget(
            Image(
                source='',
                size_hint=(1, None),
                height="250dp"
            )
        )

    def callback_trangchu(self):
        app = MDApp.get_running_app()
        app.root.current = 'trangchu'
        
    def callback_for_menu_items(self, *args):
        toast(args[0])

    # def show_example_grid_bottom_sheet(self):
    #     # pass
    #     bottom_sheet_menu = MDGridBottomSheet()
    #     data = {
    #         "Hạn ngắn": "facebook",
    #         "Hạn vừa": "youtube",
    #         "Hạn dài": "twitter",
    #         "Lũ": "cloud-circle",
    #         "Cảnh báo lũ": "camera",
    #     }
    #     for item in data.items():
    #         bottom_sheet_menu.add_item(
    #             item[0],
    #             lambda x, y=item[0]: self.callback_for_menu_items(y),
    #             icon_src=item[1],
    #         )
    #     bottom_sheet_menu.open()
    
    # def callback_for_menu_items(self, selected_item):
    #     # Thực hiện cập nhật hình ảnh dựa trên mục được chọn
    #     if selected_item == "Hạn ngắn":
    #         self.read_ftp_sever_image('TVHN_0.png')
    #         self.root.ids.image_bantin.source = 'cache/TVHN_0.png'
    #     elif selected_item == "Hạn vừa":
    #         self.read_ftp_sever_image('TVHV_0.png')
    #         self.root.ids.image_bantin.source = 'cache/TVHV_0.png'
    #     elif selected_item == "Hạn dài":
    #         self.read_ftp_sever_image('TVHD_0.png')
    #         self.root.ids.image_bantin.source = 'cache/TVHD_0.png'
    #     elif selected_item == "Lũ":
    #         self.read_ftp_sever_image('LULU_0.png')
    #         self.root.ids.image_bantin.source = 'cache/LULU_0.png'
    #     elif selected_item == "Cảnh báo lũ":
    #         self.read_ftp_sever_image('CBLU_0.png')
    #         self.root.ids.image_bantin.source = 'cache/CBLU_0.png'
    
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

    def load_new_image(self):
            # Load a new image when scrolling to the top
            # Replace this logic with loading the next image from your source
            self.root.ids.image.source = 'path_to_new_image.png'
if __name__ == '__main__':
    Hochua().run()
