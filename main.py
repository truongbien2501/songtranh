from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,CardTransition,SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton,MDFlatButton,MDRaisedButton,MDFloatingActionButtonSpeedDial
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
from kivymd.uix.list import OneLineListItem,OneLineIconListItem,IconLeftWidget,OneLineRightIconListItem,ImageRightWidget
from kivy.metrics import dp
from kivymd.icon_definitions import md_icons
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.datatables import MDDataTable
from kivy_garden.graph import Graph,BarPlot,LinePlot
from kivy.uix.popup import Popup
from kivymd.uix.imagelist import MDSmartTile
# import paramiko
Window.size = (350, 600)

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


    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):

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
                        height='450dp'
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
                        height='450dp'
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
                        height='450dp'
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
                        height='450dp'
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
                        height='450dp'
                    )
                )   
    def on_start(self):
        self.root.ids.tabs.add_widget(Tab(title="TVHN"))
        self.root.ids.tabs.add_widget(Tab(title="TVHV"))
        self.root.ids.tabs.add_widget(Tab(title="TVHD"))
        self.root.ids.tabs.add_widget(Tab(title="LULU"))
        self.root.ids.tabs.add_widget(Tab(title="CBLU"))
        
        #
        now = datetime.now()
        self.root.ids.ngay1.text = (now - timedelta(days=-3)).strftime('%d/%m')
        self.root.ids.ngay2.text = (now - timedelta(days=-2)).strftime('%d/%m')
        self.root.ids.ngay3.text = (now - timedelta(days=-1)).strftime('%d/%m')
        self.root.ids.ngay4.text = now.strftime('%d/%m')
        
        
        # self.root.ids.tramkttv_ho.add_widget(MDLabel(text='Trạm'))
        # self.root.ids.tramkttv_ho.add_widget(MDLabel(text='Trend'))
        # self.root.ids.tramkttv_ho.add_widget(MDLabel(text='Giờ'))
        # self.root.ids.tramkttv_ho.add_widget(MDLabel(text='Value'))
        # ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        # for tram in ds_tram:
        #     if 'mua' in tram[3]:
        #         muatong = self.TTB_API_muatong(tram[0],tram[2])
        #         # ten tram
        #         self.root.ids.tramkttv_ho.add_widget(MDLabel(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2'))
        #         # xu the
        #         if muatong[0] !='-':
        #             if float(muatong[0]) == 0:
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/0_mua.png"))
        #             elif float(muatong[0]) > 0 and float(muatong[0]) <10:
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/1_mua.png"))
        #             elif float(muatong[0]) >= 10 and float(muatong[0]) <30:
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/2_mua.png"))
        #             elif float(muatong[0]) >= 30:
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/3_mua.png"))
        #         else:
        #             self.root.ids.tramkttv_ho.add_widget(MDLabel(text='-'))
        #         # gio
        #         if muatong[-1] != '-':
        #             self.root.ids.tramkttv_ho.add_widget(MDLabel(text=muatong[-1].strftime('%H:%M'),font_style='Body2'))
        #         else:
        #             self.root.ids.tramkttv_ho.add_widget(MDLabel(text='-',font_style='Body2'))
        #         # gia tri
        #         self.root.ids.tramkttv_ho.add_widget(MDLabel(text=muatong[0],font_style='Body2'))
        #     else:
        #         muatong = self.TTB_API_yeutokhac(tram[0],tram[2])
        #         # ten tram
        #         self.root.ids.tramkttv_ho.add_widget(MDLabel(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2'))
        #          # xu the
        #         if muatong[0] !='-':
        #             if float(muatong[0]) == float(muatong[1]):
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/0_mua.png"))
        #             elif float(muatong[0]) >  float(muatong[1]):
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/4_nuoc.png"))
        #             elif float(muatong[0]) < float(muatong[1]) :
        #                 self.root.ids.tramkttv_ho.add_widget(Image(source="icon/1_nuoc.png"))
        #         else:
        #             self.root.ids.tramkttv_ho.add_widget(MDLabel(text='-',font_style='Body2'))
        #         # gio
        #         if muatong[-1] != '-':
        #             self.root.ids.tramkttv_ho.add_widget(MDLabel(text=muatong[-1].strftime('%H:%M'),font_style='Body2'))
        #         else:
        #             self.root.ids.tramkttv_ho.add_widget(MDLabel(text='-',font_style='Body2'))
        #         # gia tri
        #         self.root.ids.tramkttv_ho.add_widget(MDLabel(text=muatong[0],font_style='Body2'))
        
        
        
        # man hinh so lieu
        self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='Trạm',font_style='Body1'))
        self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='Trend',font_style='Body1'))
        self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='Giờ',font_style='Body1'))
        self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='Value',font_style='Body1'))

        ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        for tram in ds_tram:
            if 'mua' in tram[3]:
                muatong = self.TTB_API_muatong(tram[0],tram[2])
                # ten tram
                self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2',on_release=self.tram_pressed))
                # xu the
                if muatong[0] !='-':
                    if float(muatong[0]) == 0:
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/0_mua.png"))
                    elif float(muatong[0]) > 0 and float(muatong[0]) <10:
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/1_mua.png"))
                    elif float(muatong[0]) >= 10 and float(muatong[0]) <30:
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/2_mua.png"))
                    elif float(muatong[0]) >= 30:
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/3_mua.png"))    
                else:
                    self.root.ids.tramkttv_ho.add_widget(OneLineRightIconListItem(text='-'))
                # gio
                if muatong[-1] != '-':
                    self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text=muatong[-1].strftime('%H:%M'),font_style='Body2'))
                else:
                    self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='-',font_style='Body2'))
                # gia tri
                self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text=muatong[0],font_style='Body2'))
            else:
                muatong = self.TTB_API_yeutokhac(tram[0],tram[2])
                # ten tram
                self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2',on_release=self.tram_pressed))
                 # xu the
                if muatong[0] !='-':
                    if float(muatong[0]) == float(muatong[1]):
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/0_mua.png"))
                    elif float(muatong[0]) >  float(muatong[1]):
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/4_nuoc.png"))
                    elif float(muatong[0]) < float(muatong[1]) :
                        self.root.ids.tramkttv_ho.add_widget(Image(source="icon/1_nuoc.png"))
                else:
                    self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='-',font_style='Body2'))
                # gio
                if muatong[-1] != '-':
                    self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text=muatong[-1].strftime('%H:%M'),font_style='Body2'))
                else:
                    self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text='-',font_style='Body2'))
                # gia tri
                self.root.ids.tramkttv_ho.add_widget(OneLineListItem(text=muatong[0],font_style='Body2'))
        
        # ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        # for tram in ds_tram:
        #     if 'mua' in str(tram[3]):
        #             bieutuong = "weather-partly-rainy"                    
        #     elif 'mucnuoc' in str(tram[3]):
        #         bieutuong = 'waves-arrow-up'
        #     elif 'Q' in str(tram[3]):
        #         bieutuong = 'waves-arrow-right'     
        #     else:
        #         bieutuong = ''
        #     icon_item = OneLineIconListItem(
        #                 IconLeftWidget(icon=bieutuong),
        #                 text=self.chuyentram_vietnam(tram[1],2)[0],
        #                 on_release=self.tram_pressed)
        #     self.root.ids.tramkttv_ho.add_widget(icon_item)
        
        # tinh dung tich trang chu
        mucnuoc,qve = self.TTB_API_HC()
        self.root.ids.mucnuochientai.text = mucnuoc[-1]['Solieu']
        self.root.ids.luuluongve.text = qve[-1]['Solieu']
        array_data = np.genfromtxt('matram/H_W.txt', delimiter=",",names=True,encoding=None)
        row_index = np.where(array_data['H']==float(mucnuoc[-1]['Solieu']))[0][0]
        self.root.ids.dungtich.text = str(array_data['W'][row_index])
        self.root.ids.dungtichdb.text= '{:.2f}'.format(array_data['W'][row_index] + 0.07)

    def tram_pressed(self,instance): # su kien click vao tram
        clicked_text = instance.text
        # print('bạn đã click vào:' + clicked_text)
        app = MDApp.get_running_app()
        app.root.current = 'tram'
        self.root.ids.solieutram.clear_widgets()
        self.root.ids.tieude_tram.text = clicked_text
        yeuto = self.chuyentram_vietnam(clicked_text,1)
        # tt_tram = clicked_text.split('-')
        # tentram = str(tt_tram[0]).strip()
        # yeuto = str(tt_tram[1]).strip()
        # tentinh = self.ten_tinh_txt(self.root.ids.provin.title)
        # print(tentinh)
      
        solieu = self.TTB_API(yeuto[0],yeuto[1])
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
            
    def on_row_press(self, instance_table, instance_row): # click vao row cua bang
        tramten = instance_row.text
        app = MDApp.get_running_app()
        app.root.current = 'tram'
        self.root.ids.solieutram.clear_widgets()
        # self.root.ids.tieude_tram.clear_widgets()
        self.root.ids.tieude_tram.text = str(tramten)
        
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
        self.root.ids.tieude_tram_bieudo.text = self.root.ids.tieude_tram.text
        now = datetime.now()
        now = datetime(now.year,now.month,now.day)
        gt = []
        tg = []
        for child in self.root.ids.solieutram.children:
            # print(child.text)
            dl = str(child.text).split(':')
            gt.append(float(dl[3].strip()))
            tg.append(datetime.strptime(dl[0].strip() + ':' + dl[1].strip(),"%Y-%m-%d %H:%M"))
        tentram = self.root.ids.tieude_tram.text   # lay ten yeo to ve
        
        # index_date = tg.index(now)
        # data_ve = gt[index_date:]
        
        # print(data_ve)
        # print(gt)
        lists = ['Trà Đốc','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
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
        tentram = self.root.ids.tieude_tram.text   # lay ten yeo to ve
        lists = ['Trà Đốc','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
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
                self.plot = BarPlot(color=[1, 0, 0, 1],bar_width=2.5)
                self.graph.add_plot(self.plot)
                self.plot.points = [(t, g) for t, g in enumerate(datave)]
                
    def chuyentram_vietnam(self,tentram,tiento):
        trammua_vni = ['Mực nước','Q điều tiết','Q về','Trà Đốc','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
        trammua_eng = ['Song Tranh_H','Song Tranh_Qxa','Song Tranh_Qve','Song Tranh_mua','Tra Bui','Tra Giac','Tra Don','Tra Leng','Tra Mai','Tra Cang','Tra Van','Tra Nam 2','Tra Linh','Tra Mai(UBND)']
        matram = ['5ST','5ST','5ST','tramdapst2','TRABUI','tragiac','tradon','traleng','TRAMAI','tracang','travan','tranam2','tralinh','tramai(UBNDHnamTM)']
        tab_bang = ['ho_dakdrinh_mucnuoc','ho_dakdrinh_qve','ho_dakdrinh_qdieutiet','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh','mua_songtranh']
        if tiento == 1 : # neu ten dua vao la tieng viet tra ra ma tram va Tab
            idx = trammua_vni.index(tentram)
            yeuto  = [matram[idx],tab_bang[idx]]
            return yeuto
        elif tiento == 2 : # neu ten dua vao la tieng anh tra ra ten tieng viet ma tram va Tab
            idx = trammua_eng.index(tentram)
            yeuto  = [trammua_vni[idx],matram[idx],tab_bang[idx]]
            return yeuto

    def show_marker_info(self,tram):
        lists = ['Mực nước','Q điều tiết','Q về','Trà Đốc','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam 2','Trà Linh','Trà Mai(UBND)']
        # toast(tram + ':' + thongtin)
        content = MDBoxLayout(orientation='vertical',
                              md_bg_color= self.theme_cls.primary_color
                              )
        if tram in lists:
            mt_tab = self.chuyentram_vietnam(tram,1)
            muatong = self.TTB_API_muatong(mt_tab[0],mt_tab[1])
            cont = 'Lượng mưa đo được:\n   - 1h: ' + muatong[0] + ' mm\n   - 3h: ' + muatong[1] + ' mm\n   - 6h: ' + muatong[2] + ' mm\n   - 12h: ' + muatong[3] + ' mm\n   - 24h: ' + muatong[4] + ' mm\n'
            content.add_widget(MDLabel(text=cont,
                                    text_color= (1, 1, 1, 1),
                                        theme_text_color= "Custom"
                                    ))
            # Thêm nút tắt thông báo
            dismiss_button = MDIconButton(icon='close-circle-outline',pos_hint= {"center_x": .5, "center_y": .5})
            content.add_widget(dismiss_button)
            # Tạo popup với nội dung và nút tắt thông báo
            popup = Popup(title=tram, content=content, size_hint=(1, 0.5))
            # Thiết lập hàm callback khi nút tắt được nhấn
            dismiss_button.bind(on_release=popup.dismiss)
            popup.open()

    def chuyentram_eng(self,tentram):
        trammua_vni = ['Trà Đốc','Trà Bui','Trà Giác','Trà Dơn','Trà Leng','Trà Mai','Trà Cang','Trà Vân','Trà Nam','Trà Linh']
        trammua_eng = ['tramdapst2','TRABUI','tragiac','tradon','traleng','TRAMAI','tracang','travan','tranam2','tralinh']
        if tentram in trammua_vni:
            idx = trammua_vni.index(tentram)
        return trammua_eng[idx]
    
    def callback_solieutram(self):
        app = MDApp.get_running_app()
        app.root.current = 'trangchu'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"        

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
            return '-','-','-','-','-','-','-','-'
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
        return mua1,mua3,mua6,mua12,mua24,mua48,mua72,giohientai
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
            return '-','-','-','-','-','-','-','-'
        else:
            giohientai = datetime.strptime(mua[-1]['Thoigian_SL'], '%Y-%m-%d %H:%M:%S')
            h1 = mua[-1]['SoLieu']
            h3 = mua[-3]['SoLieu']
            h6 = mua[-6]['SoLieu']
            h12 = mua[-12]['SoLieu']
            h24 = mua[-24]['SoLieu']
            h48 = mua[-48]['SoLieu']
            try:
                h72 = mua[-72]['SoLieu']
            except:
                h72 ='-'
        return h1,h3,h6,h12,h24,h48,h72,giohientai
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

    def callback_trangchu(self):
        app = MDApp.get_running_app()
        app.root.current = 'trangchu'
        
    def callback_dienmua(self,**kwargs):
        self.root.ids.dienmua_layout.clear_widgets()
        app = MDApp.get_running_app()
        app.root.current = 'dienmua'
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='Trạm-Giờ',font_style='Body2'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='1h',font_style='H6'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='3h',font_style='H6'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='6h',font_style='H6'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='12h',font_style='H6'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='24h',font_style='H6'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='48h',font_style='H6'))
        self.root.ids.dienmua_layout.add_widget(OneLineListItem(text='72h',font_style='H6'))
        ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        for tram in ds_tram:
            if 'mua' in tram[3]:
                muatong = self.TTB_API_muatong(tram[0],tram[2])
                self.root.ids.dienmua_layout.add_widget(OneLineListItem(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2'))
                for p in range(7):
                    self.root.ids.dienmua_layout.add_widget(OneLineListItem(text=str(muatong[p]),font_style='Body2'))
            else:
                muatong = self.TTB_API_yeutokhac(tram[0],tram[2])
                self.root.ids.dienmua_layout.add_widget(OneLineListItem(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2'))
                for p in range(7):
                    self.root.ids.dienmua_layout.add_widget(OneLineListItem(text=str(muatong[p]),font_style='Body2'))

        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='Trạm-Giờ',font_style='Body2'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='1h',font_style='H6'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='3h',font_style='H6'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='6h',font_style='H6'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='12h',font_style='H6'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='24h',font_style='H6'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='48h',font_style='H6'))
        # self.root.ids.dienmua_layout.add_widget(MDLabel(text='72h',font_style='H6'))
        # ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        # for tram in ds_tram:
        #     if 'mua' in tram[3]:
        #         muatong = self.TTB_API_muatong(tram[0],tram[2])
        #         self.root.ids.dienmua_layout.add_widget(MDLabel(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2'))
        #         for p in range(7):
        #             self.root.ids.dienmua_layout.add_widget(MDLabel(text=str(muatong[p]),font_style='Body2'))
        #     else:
        #         muatong = self.TTB_API_yeutokhac(tram[0],tram[2])
        #         self.root.ids.dienmua_layout.add_widget(MDLabel(text=str(self.chuyentram_vietnam(tram[1],2)[0]),font_style='Body2'))
        #         for p in range(7):
        #             self.root.ids.dienmua_layout.add_widget(MDLabel(text=str(muatong[p]),font_style='Body2'))

        
        
        
        # bang_girl = MDGridLayout(cols=8, rows=14)
        # for a in range(1,9):
        #     for b in range(1,15):
        #         bang_girl.add_widget(MDLabel(text="value:" + str(a) + '-' + str(b)))
                
        
        # bang_girl.add_widget(MDLabel(text='vcl2'))
        # bang_girl.add_widget(MDLabel(text='vcl3'))
        # self.root.ids.dienmua_layout.add_widget(bang_girl)
        
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Orange"
        # data_tables = MDDataTable(
        #     size_hint=(1, 0.99),
        #     use_pagination=True,
        #     rows_num=7,
        #     column_data=[
        #         ("Trạm-Giờ", dp(20)),
        #         ("1h", dp(20)),
        #         ("3h", dp(20)),
        #         ("6h", dp(20)),
        #         ("12h", dp(20)),
        #         ("24h", dp(20)),
        #         ("48h", dp(20)),
        #         ("72h", dp(20)),
        #     ],
        # )
        # ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        # for tram in ds_tram:
        #     if 'mua' in tram[3]:
        #         muatong = self.TTB_API_muatong(tram[0],tram[2])
        #         data_tables.add_row((self.chuyentram_vietnam(tram[1],2)[0], muatong[0], muatong[1],muatong[2], muatong[3], muatong[4],muatong[5],muatong[6]))
        #     else:
        #         muatong = self.TTB_API_yeutokhac(tram[0],tram[2])
        #         data_tables.add_row((self.chuyentram_vietnam(tram[1],2)[0], muatong[0], muatong[1],muatong[2], muatong[3], muatong[4],muatong[5],muatong[6]))
        # self.root.ids.dienmua_layout.add_widget(data_tables)

    def search_tram(self, search_text):# su kien tìm kiếm
        self.root.ids.tramkttv_ho.clear_widgets()
        
        ds_tram = np.genfromtxt('matram/mucnuoc.txt' , delimiter=',', dtype=None, names=True, encoding=None)
        for tram in ds_tram:
            tramtv = self.chuyentram_vietnam(str(tram[1]),2)
            if  tramtv[0]== str(search_text):
                if 'mua' in str(tram[3]):
                        bieutuong = "weather-partly-rainy"                    
                elif 'mucnuoc' in str(tram[3]):
                    bieutuong = 'waves-arrow-up'
                elif 'Q' in str(tram[3]):
                    bieutuong = 'waves-arrow-right'     
                else:
                    bieutuong = ''
                icon_item = OneLineIconListItem(
                            IconLeftWidget(icon=bieutuong),
                            text=self.chuyentram_vietnam(tram[1],2)[0],
                            on_release=self.tram_pressed
                        )
                self.root.ids.tramkttv_ho.add_widget(icon_item)
   

    # def get_image_from_ssh(ip, username, password, ssh_path):
    #     # Tạo một kết nối SSH đến máy chủ
    #     ssh_client = paramiko.SSHClient()
    #     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #     ssh_client.connect(ip, username=username, password=password)
    #     # Lấy nội dung của tệp ảnh từ máy chủ
    #     sftp_client = ssh_client.open_sftp()
    #     image_file = sftp_client.open(ssh_path, 'rb')
    #     image_data = image_file.read()
    #     sftp_client.close()
    #     ssh_client.close()
        
    #     # Chuyển dữ liệu ảnh thành đối tượng hình ảnh (PIL)
    #     image = Image.open(io.BytesIO(image_data))
    #     return image

if __name__ == '__main__':
    Hochua().run()
