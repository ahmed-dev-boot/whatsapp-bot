
from flask import Flask, request
import requests

app = Flask(__name__)

# بيانات UltraMsg
instance_id = "instance115588"
token = "0icx22pn1em4qssn"

def send_whatsapp_message(to, message):
    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "token": token,
        "to": to,
        "body": message
    }
    response = requests.post(url, headers=headers, data=data)
    print(f"تم الإرسال إلى {to}: {response.status_code}")
    return response.text

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.form
    sender = data.get("from")
    message = data.get("body", "").strip().lower()

    print(f"📥 رسالة من {sender}: {message}")

    # سيناريوهات الرد
    if "السعر" in message:
        reply = "الباقات تبدأ من 50 جنيه فقط 🎨✨"
    elif "السلام عليكم" in message:
        reply = "وعليكم السلام ورحمة الله وبركاته 👋"
    elif "عرض تقديمي" in message:
        reply = "أكيد! احكيلي عن نوع العرض وعدد الشرائح اللي محتاجها 😊"
    else:
        reply = "أنا بوت Slide Craft 🎨 أقدر أساعدك في تصميم عرضك التقديمي! ✨"

    send_whatsapp_message(sender, reply)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
