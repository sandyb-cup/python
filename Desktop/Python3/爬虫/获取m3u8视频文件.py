import requests
import os

url = 'https://jx.618g.com/?url=https://v.youku.com/v_show/id_XNDcxMzYxMTk4NA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dselectbutton_9&showid=efbfbd4506efbfbd4715'
url2 = "https://jx.618g.com/?url=https://v.qq.com/x/cover/l8r3gm1zzu5u3nk.html?report_recomm_player=ptag%3Dv_qq_com%7Crtype%3Dcid%7CalgId%3D5419%7CbucketId%3DEXP%3ANRBE%3D10156%7CPROFILE%3D10156%7CSELECTOR%3D10156%7CENGINE%3D10156%7CRANK%3D10156%7CINDEX%3D10156%7CACCESS%3D10156%7Creason%3Dscms_20190828008046%7CreasonType%3D%7Ccid%3Dl8r3gm1zzu5u3nk%7Cvid%3D%7Cpid%3D%7Cmodule%3D410%7CpageType%3DfilmIndex%7Cseqnum%3D5764938539_1599394563.483765_4114%7Cvideo_rec_report%3Dflush_num%3A%7Cis_insert%3A%7Cinsert_type%3A%7Cload_type%3A%7Ca_exp_id%3ANRBE-10156%23PROFILE-10156%23SELECTOR-10156%23ENGINE-10156%23RANK-10156%23INDEX-10156%23ACCESS-10156%7Ca_src_key%3A100137%7Ca_seqnum%3A5764938539_1599394563.483765_4114%7Ca_area_code%3A%7Ca_scene_type%3A2%7Ce_module_type%3A410%7C%7Ca_module_id%3A20190828008046%7Ce_item_id%3Al8r3gm1zzu5u3nk%7Ce_item_type%3A13%7Ce_item_mixid%3A%7C%7Ca_alg_id%3A5419%7Ca_alg_type%3A410%7Citem_score%3A0.1"
url3 ='https://jx.618g.com/?url=https://v.qq.com/x/cover/5oylcwhsdtfsjn0.html'
tenxun = 'https://v.qq.com/x/cover/mzc00200h97lhuv/w0035wqosie.html'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
res = requests.get(tenxun, headers=headers)
text = res.text
print(text)
res_json = res.json




