import urllib.request
import json

TOKEN = "hLMaj4GuN3QsAum1bZmVR+r+57X/QbUeH/XqmO7FkpaVW9mmKfTAsH4u6G4LozwjYCRnQaR0cXMNrbvjnaZl4yDZcsM7e31pwvK38GxM7WzWffgaxz7CSP4tY7Edh/g4znkyvLx0DN2ITkXqLhDpGAdB04t89/1O/w1cDnyilFU="

menu_obj = {
    "size": {
        "width": 2500,
        "height": 1686
    },
    "selected": True,
    "name": "88tea-2026-spring",
    "chatBarText": "選單",
    "areas": [
        {
            "bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
            "action": {"type": "message", "text": "當季新茶"}
        },
        {
            "bounds": {"x": 833, "y": 0, "width": 833, "height": 843},
            "action": {"type": "message", "text": "茶品總覽"}
        },
        {
            "bounds": {"x": 1666, "y": 0, "width": 834, "height": 843},
            "action": {"type": "message", "text": "我要訂購"}
        },
        {
            "bounds": {"x": 0, "y": 843, "width": 833, "height": 843},
            "action": {"type": "uri", "uri": "https://88tea.tw/blog/2026-spring-tea-guide"}
        },
        {
            "bounds": {"x": 833, "y": 843, "width": 833, "height": 843},
            "action": {"type": "message", "text": "客戶好評"}
        },
        {
            "bounds": {"x": 1666, "y": 843, "width": 834, "height": 843},
            "action": {"type": "message", "text": "請客服聯絡我"}
        }
    ]
}

# 1. Create
req = urllib.request.Request("https://api.line.me/v2/bot/richmenu", data=json.dumps(menu_obj).encode('utf-8'))
req.add_header("Authorization", f"Bearer {TOKEN}")
req.add_header("Content-Type", "application/json")

try:
    with urllib.request.urlopen(req) as res:
        rich_menu_id = json.loads(res.read().decode())['richMenuId']
        print(f"Created: {rich_menu_id}")
        
        # 2. Upload Image
        with open('/Users/chen/.openclaw/workspace/taiwan88tea/line-menu/cropped_menu.jpg', 'rb') as f:
            img_data = f.read()
            
        req2 = urllib.request.Request(f"https://api-data.line.me/v2/bot/richmenu/{rich_menu_id}/content", data=img_data)
        req2.add_header("Authorization", f"Bearer {TOKEN}")
        req2.add_header("Content-Type", "image/jpeg")
        with urllib.request.urlopen(req2) as res2:
            print("Image uploaded")
            
        # 3. Set Default
        req3 = urllib.request.Request(f"https://api.line.me/v2/bot/user/all/richmenu/{rich_menu_id}", data=b"", method="POST")
        req3.add_header("Authorization", f"Bearer {TOKEN}")
        with urllib.request.urlopen(req3) as res3:
            print("Set as default!")

except Exception as e:
    print("Error:", e)
    if hasattr(e, 'read'):
        print(e.read().decode())
