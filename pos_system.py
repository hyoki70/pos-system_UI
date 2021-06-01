import pandas as pd
import datetime
import eel

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

    
#オーダーを入力し、マスターに登録されているかをチェック、あればオーダー登録
def add_item_order(code,count,item_master):
    master_code_check=[]
    for master_code in item_master:
        master_code_check.append(master_code.item_code)
    if code in master_code_check:
        eel.view_log_js(f"商品コード:{code} を{count}個 注文受付しました")
        eel.view_log_js("続けて注文を入力してください/終了時は「注文完了」ボタンを押して下さい")
        eel.erase_input()
        return code,count
    else:
        eel.view_log_js("入力された商品コードはありません")
        eel.erase_input()

#商品コードからマスターに登録した商品名と価格を探す
def item_search(self,item_code):
    for item in self.item_master:
        if item_code == item.item_code:
            return item.item_name,item.price

#オーダー内容を表示する
def view_item_list(self):
    self.total_price=0
    self.receipt=""
    for item,count in zip(self.item_order_list,self.item_order_count):
        name_price=self.item_search(item)
        item_total_price=int(name_price[1])*int(count)
        self.write_receipt(f"商品コード:{item} 商品名:{name_price[0]} 価格:{name_price[1]}円 =>注文個数:{count}個 合計金額:{item_total_price}円")
        self.total_price+=item_total_price
    self.write_receipt(f"お買い上げの合計金額は{self.total_price}円になります")

#お会計
def calculation_change(self):
    while True:
        payment=int(input("支払い金額を入力してください=>"))
        if payment > self.total_price:
            change=payment-self.total_price
            self.write_receipt(f"{payment}円お預かりします。お釣り{change}円になります")
            print("ありがとうございました")
            self.create_receipt()
            break
        elif payment == self.total_price:
            self.write_receipt(f"{payment}円ちょうどお預かりします")
            print("ありがとうございました")
            self.create_receipt()
            break
        else:
            print("支払い金額が足りません。もう一度入力してください")

def write_receipt(self,text):
    print(text)
    self.receipt+=text+"\n"

def create_receipt(self):
    time_now = datetime.datetime.now()
    write_time=time_now.strftime('%Y年%m月%d日 %H_%M_%S')
    receipt_name=f"レシート {write_time}.txt"
    with open(receipt_name, mode="a", encoding='UTF-8') as f:
        f.write(self.receipt)

            

        


#マスター登録
def master_input(csv_name):
    master_list=[]
    df=pd.read_csv(csv_name,dtype=object)
    code_list=(list(df["商品コード"]))
    name_list=list(df["商品名"])
    price_list=list(df["価格"])
    for code,name,price in zip(code_list,name_list,price_list):
        master_list.append(Item(code,name,price))
    return master_list


    
    
### メイン処理
def main():
    # マスタ登録
    item_master=master_input()
    
if __name__ == "__main__":
    main()