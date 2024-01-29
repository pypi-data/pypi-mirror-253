import os
import openai
import json
import LibHanger.Library.uwLogger as Logger

class opaipyBase():
    
    """
    opaipyBase
    """
    
    class aiLang():
        
        """
        言語設定
        """
        
        jp = 'Jp'
        """ 日本語 """

        en = 'En'
        """ 英語 """

    def __init__(self, _rootPath, _organization, _api_key, _jsonFilePath) -> None:
        
        """
        コンストラクタ
        
        Parameters
        ----------
        _organization : str
            organization
        _api_key : str
            api_key
        """

        # 認証情報
        openai.organization = _organization
        openai.api_key = _api_key

        # ルートパス
        self.rootPathFull = _rootPath
        self.rootPath = os.path.dirname(_rootPath)

        # openai - response
        self.response = None

        # PromptJsonFile Path
        self.jsonFilePath = _jsonFilePath
    
    @property
    def responseMessage(self):
        
        """
        OpenAIからの返答
        """
        return self.response['choices'][0]['message']['content']
    
    def request(self, _jsonFileName):
        
        """
        openAIから返答を取得する

        Parameters
        ----------
        _jsonFileName : str
            プロンプトのjsonファイル名
        """

        # ファイル名
        jsonFilePath = os.path.join(
            os.path.dirname(self.rootPath), 
            self.jsonFilePath,
            _jsonFileName)
        
        # jsonファイルチェック
        if not os.path.exists(jsonFilePath):
            Logger.logging.info('jsonfile is not found.')
            return

        # jsonファイルOpen
        with open(jsonFilePath, encoding="utf-8") as f:
            prompt = json.loads(f.read())

        # openaiの返答を取得する
        self.response = openai.ChatCompletion.create(
            model= prompt['model'],
            messages=[
                {"role": "system", "content": prompt['systemContent']},
                {"role": "user", "content": '\n'.join(prompt['userContent'])},
                #{"role": "assistant", "content": "補足説明を記載（使わなくてもOK）"},
            ],)
    