from os import system
import eel
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,700)

item_master=[]
order=[]

@ eel.expose
def pos_system_master(csv_name):
    #マスター登録
    global item_master,order
    item_master=pos_system.master_input(csv_name)
    order=pos_system.Order(item_master)

@ eel.expose
def pos_system_order(code,count):
    # オーダー登録
    global order
    order.add_item_order(code,count)

@ eel.expose
def pos_system_order_view():
    global order
    order.view_item_list()

@ eel.expose
def pos_system_payment(payment):
    global order
    order.calculation_change(payment)

    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)