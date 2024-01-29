from LibHanger.Library.uwGlobals import globalValues
from opaipy.Library.opaipyConfig import opaipyConfig

class opaipyGlobal(globalValues):
    
    def __init__(self):
        
        """
        コンストラクタ
        """
        
        # 基底側コンストラクタ呼び出し
        super().__init__()

        self.opaipyConfig:opaipyConfig = None
        """ opaipy共通設定 """

# インスタンス生成(import時に実行される)
gvOna = opaipyGlobal()
