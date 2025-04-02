

#1 DEBUG 2 INFO 3 WARNING 4 ERROR 5 CRITUCAL

from logging import getLogger, FileHandler,Formatter,DEBUG,ERROR
formatter= Formatter('[%(levelname)s]%(asctime)s - %(message)s(%(filename)s)')
logger=getLogger(__name__)
handler=FileHandler('log2,txt', encoding='utf-8')
handler.setLevel(DEBUG)
handler.setFormatter(formatter)

error_handler=FileHandler('error.txt', encoding='utf-8')
error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.addHandler(error_handler)

logger.info('プログラムが開始しました')
logger.debug('入力値は1000です')
logger.warning('ファイルの容量が200GBを超えました')
logger.error('ファイルが存在していません')

#　初めてchatGDPに感謝した
#　新しいファイルに書き出す際に文字が出力されない場合は、 encoding='utf-8'を書き出すとでる




