from flask import Blueprint, render_template, request, flash
from flask.scaffold import F
from chatbot import bot

views = Blueprint('views', __name__)
Sonny = bot.Sonny

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/get')
def get_bot_response():

    userText = request.args.get('msg')
    reponse = str(Sonny.get_response(userText))

    #Google search this paper if bot doesnt know about it
    words = ['thủ tục', 'hành chính', 'giấy tờ', 'đơn', 'giấy phép', 'đăng ký']
    if reponse == bot.DEFAULT_REPONSE:
        from underthesea import pos_tag        
        tags = pos_tag(userText)
        if any(w[0].lower() in words for w in tags):
            print("asdassd")
            from googlesearch import search
            # Make a request to google search
            try:
                url = list(search(userText, tld='com', lang='vi', num=1, stop=1, pause=2, country='vi'))[0]
                reponse = f'{bot.DEFAULT_REPONSE} Nhưng mình nghĩ bạn có thể tham khảo thêm tại đây: {url}'
            except Exception as e:
                reponse = bot.DEFAULT_REPONSE
                print(e.__traceback__)

    return reponse