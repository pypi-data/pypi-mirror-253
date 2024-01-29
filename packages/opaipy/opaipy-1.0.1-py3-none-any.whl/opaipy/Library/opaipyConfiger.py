import LibHanger.Library.uwLogger as Logger
from LibHanger.Library.uwGlobals import configer
from LibHanger.Library.uwGlobals import *
from opaipy.Library.opaipyGlobals import *

class opaipyConfiger(configer):
    
    """
    opaipy共通設定クラス
    """
    
    def __init__(self, _tgv:opaipyGlobal, _file, _configFolderName = ''):
        
        """
        コンストラクタ
        """
        
        # opaipy.ini
        da = opaipyConfig()
        da.getConfig(_file, _configFolderName)

        # gvセット
        _tgv.opaipyConfig = da
        
        # ロガー設定
        Logger.setting(da)
