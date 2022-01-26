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
cards = [
    Golem({'cardNo': 0, 'name': "ゴーレム", 'symbol': ["a","a"] 'p1': 4 'p2': 8 'p3': 4}),

    Hero({'cardNo': 1, 'name': "勇者", 'symbol': ["b","b"] 'p1': 7 'p2': 5 'p3': 3}),
    
    Wizard({'cardNo': 2, 'name': "魔法使い", 'symbol': ["b","b"]'p1': 5 'p2': 3 'p3': 7})
        ]


# フィールド１(自分)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p1']

# フィールド２(相手)
class field2:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p1']

# フィールド３(自分)
class field3:
    def data_set(self,symbol,p2):
        self.symbol=['symlol']
        self.power=['p2']
    def symbol_set(self,symbol)
        symbolResult=symbol[0]

# フィールド４(相手)
class field4:
    def data_set(self,symbol,p2):
        self.symbol=['symlol']
        self.power=['p2']
    def symbol_set(self,symbol)
        symbolResult=symbol[0]

# フィールド５(自分)
class field5:
    def data_set(self,symbol,p3):
        self.symbol=['symlol']
        self.power=['p3']
    def symbol_set(self,symbol)
        symbolResult=symbol[0]

# フィールド６(相手)
class field6:
    def data_set(self,symbol,p3):
        self.symbol=['symlol']
        self.power=['p3']
    def symbol_set(self,symbol)
        symbolResult=symbol[0]


#アビリティ一覧
def golem_ab:

def hero_ab:

def wizard:
