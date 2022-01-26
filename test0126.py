#場のカードは自分相手含めて6枚用意する
#相手１、自分１でインスタンス作成この時カードのpower1を参照する
 ##この時相手のカード属性が必要　
 ##フィールド１を作り両カード情報を入れて判定までした方がよいかも？
#個々の能力を処理してpower＋－して更新
 ####必要１power ２職業（ゴーレム、勇者等）３シンボル（勝敗により変わる）４隣のカードのシンボル
#勝敗判定　
#勝敗によりカードタップするのでマークが変わるのでインスタンスのシンボルを更新
#二試合目開始　相手２、自分２のインスタンス作成


#カード情報{No, カード名, power1,2,3, シンボル(勝敗により変わる)}
cards = 
    [
    #ゴーレム
    {'cardNo': 0, 'name': "ゴーレム", 'symbols': ["a","a"] 'p1': 4 'p2': 8 'p3': 4}),

    #勇者
    {'cardNo': 1, 'name': "勇者", 'symbols': ["b","b"] 'p1': 7 'p2': 5 'p3': 3}),
    
    #魔法使い
    {'cardNo': 2, 'name': "魔法使い", 'symbols': ["b","b"]'p1': 5 'p2': 3 'p3': 7}),
    ]

#アビリティ一覧
def golem_ab:

def hero_ab:

def wizard:


# フィールド１(自分)
class Field1:
    power = 0
    symbol= ""#勝敗によりシンボル決定
    symbols=[]#カードが持っているシンボル
    def data_set(card):#入ってくるのがcards[0]ゴーレムとすると
        self.symbols=card['symbols']
        self.symbol=card['symbols'][0]
        self.power=card['p1']
    def symbol_lose()
        symbolResult=card['symbols'][1]



 
    
# フィールド２(相手)
class Field2:
    power = 0
    symbol= ""
    def data_set(self,symbol,p1):
        self.symbol=symbol[0]
        self.power=p1
    def symbol_lose()
        symbolResult=symbol[1]

# フィールド３(自分)
class Field3:
    power = 0
    symbol= ""
    def data_set(self,symbol,p2):
        self.symbol=symbol[0]
        self.power=p1
    def symbol_lose()
        symbolResult=symbol[1]

# フィールド４(相手)
class Field4:
    power = 0
    symbol= ""
    def data_set(self,symbol,p2):
        self.symbol=symbol[0]
        self.power=p2
    def symbol_lose()
        symbolResult=symbol[1]

# フィールド５(自分)
class Field5:
    power = 0
    symbol= ""
    def data_set(self,symbol,p3):
        self.symbol=symbol[0]
        self.power=p3
    def symbol_lose()
        symbolResult=symbol[1]

# フィールド６(相手)
class Field6:
    power = 0
    symbol= ""
    def data_set(self,symbol,p3):
        self.symbol=symbol[0]
        self.power=p3
    def symbol_lose()
        symbolResult=symbol[1]


#フィールドインスタンス作成
field = Field().data_set(cards[])
