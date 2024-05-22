import datetime
import locale
import os

today = datetime.date.today()
dirname = today.strftime('%Y%m%d')

if os.path.exists((dirname)):
    print('ディレクトリが存在')
else:
    os.mkdir(dirname)

locale.setlocale(locale.LC_ALL, 'ja_JP.UFT-8')
datein = input('YYYY/mm/ddの形式で日付を入力してください。')

try:
    date = datetime.datetime.strptime(datein, '%Y%m%d')
    print(date.strftime('入力された日付は%Aです'))
except ValueError as ex:
    print('日付の入力が正しくありません')

try:
    date = datetime.datetime.strptime(datein, '%Y%m%d')
    tw_after = date + datetime.timedelta(weeks=2)
    print(tw_after.strftime('入力された日の二週間後は%Y年%m月%d日です'))
    print(tw_after)
except ValueError as ex:
    print('日付の入力が正しくありません')





