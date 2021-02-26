import openpyxl
wb = openpyxl.Workbook()
# 创建工作薄
sheet = wb.active
# 获取工作活动表
sheet.title = "xxxx"
# 工作表重新命名

sheet["A1"] = '歌曲名'
sheet["B1"] = "所属专辑"
sheet["C1"] = "播放时长"
sheet["D1"] = "播放链接"

music_name = "你好夏天"
ablm = "夏天"
time = "12"
link = "wwww"

sheet.append([music_name, ablm, time, link])
wb.save('/Users/sandy/Desktop/music.xlsx')
