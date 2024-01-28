from zhujie import zhujie
from settings import main_photo1, list_to_n_bei, size_list

title1 = ""
pic1 = ""
content1 = "Для самых стильных девушек. Удобный и универсальный вариант бикини для пляжного отдыха и загара у бассейна."
title2 = ""
pic2 = ""

json_rich_l = []
for pic in main_photo1:
    json_rich=r"""
{{
  "content": [
    {{
      "widgetName": "raShowcase",
      "type": "chess",
      "blocks": [
        {{
          "img": {{
            "src": "{}",
            "srcMobile": "{}",
            "alt": "[купальник и море] Image not allowed to load",
            "width": 1920,
            "height": 1080,
            "widthMobile": 1920,
            "heightMobile": 1080,
            "position": "fill"
          }},
          "imgLink": "https://www.ozon.ru/seller/magic-angels-971848",
          "title": {{
            "content": [
              "модный купальник"
            ],
            "size": "size4",
            "align": "left",
            "color": "color1"
          }},
          "text": {{
            "size": "size2",
            "align": "left",
            "color": "color1",
            "content": [
              "Для самых стильных девушек. Удобный и универсальный вариант бикини для пляжного отдыха и загара у бассейна."
            ]
          }},
          "reverse": false
        }}
      ]
    }}
  ],
  "version": 0.3
}}
""".format(pic, pic)
    json_rich_l.append(json_rich)

json_rich_list = list_to_n_bei(the_list=json_rich_l, n=len(size_list))