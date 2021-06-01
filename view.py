from os import system
import eel
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,700)


@ eel.expose
def pos_system_order(code,count,csv_name):
    #マスター登録
    item_master=pos_system.master_input(csv_name)

    # オーダー登録
    code_count=pos_system.add_item_order(code,count,item_master)
    return code_count

    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)