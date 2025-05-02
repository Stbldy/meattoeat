from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    incoming_msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "меню" in incoming_msg:
        msg.body("🥩 Меню Meat to Eat:\n- Рибай: 7000 тг/кг\n- Колбаски BBQ: 3500 тг\n- Телятина: 6000 тг/кг")
    elif "доставка" in incoming_msg:
        msg.body("🚚 Доставка по Алматы с 10:00 до 20:00.\nУкажите адрес для оформления.")
    else:
        msg.body("Привет! Напиши 'меню' или 'доставка', чтобы начать.")

    return str(resp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
