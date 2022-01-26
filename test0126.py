#場のカードは自分相手含めて6枚用意する
#相手１、自分１でインスタンス作成この時カードのpower1を参照する
 ##この時相手のカード属性が必要　
 ##フィールド１を作り両カード情報を入れて判定までした方がよいかも？
#個々の能力を処理してpower＋－して更新
 ####必要１power ２職業（ゴーレム、勇者等）３シンボル（勝敗により変わる）４隣のカードのシンボル
#勝敗判定　
#勝敗によりカードタップするのでマークが変わるのでインスタンスのシンボルを更新
#二試合目開始　相手２、自分２のインスタンス作成


# フィールド１(自分)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p1']

# フィールド２(相手)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p1']

# フィールド３(自分)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p2']
    def symbol1_set(self,symbol1)
        self.symbol1=symbol1

# フィールド４(相手)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p2']
    def symbol2_set(self,symbol2)
         self.symbol2=symbol2



# フィールド５(自分)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p3']
    def symbol2_set(self,symbol3)
        self.symbol3=symbol3


# フィールド６(相手)
class field1:
    def data_set(self,symbol,p1):
        self.symbol=['symlol']
        self.power=['p3']
    def symbol2_set(self,symbol4)
        self.symbol4=symbol4


#カード名、power1,2,3、シンボル(勝敗により変わる)
cards = [
    Golem({'cardNo': 0, 'name': "ゴーレム", 'symbol': ["a","a"] 'p1': 4 'p2': 8 'p3': 4}),

    Hero({'cardNo': 1, 'name': "勇者", 'symbol': ["b","b"] 'p1': 7 'p2': 5 'p3': 3}),
    
    Wizard({'cardNo': 2, 'name': "魔法使い", 'symbol': ["b","b"]'p1': 5 'p2': 3 'p3': 7})
        ]

#アビリティ一覧
def golem_ab:

def hero_ab:

def wizard:
