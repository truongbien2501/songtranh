from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.list import MDList

class Test(MDApp):
    def build(self):
        mlist = MDList()
        mlist.cols = 8 # thiết lập số cột
        # thêm các item vào list
        for i in range(40): 
            item = OneLineAvatarIconListItem(text=f'Item {i}')
            mlist.add_widget(item)

        return mlist


Test().run()