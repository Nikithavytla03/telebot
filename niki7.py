import telegram.ext
Token = "5626761596:AAGOeVY22EaOP3rjsglKx_PNJKRAykrn--o"
updater = telegram.ext.Updater("5626761596:AAGOeVY22EaOP3rjsglKx_PNJKRAykrn--o", use_context=True)

dispatcher = updater.dispatcher
def start(update, context):
    update.message.reply_text("weclome to chat_bot,you can chat with me with the help of /help command ")
def help(update, context):
    update.message.reply_text(
    """
    /start -> welcome to chat_bot
    /help  -> this particular message will display set of commands
    /content -> about the chat_bot 
    /technical_skills ->provides my technical skill certificates
    /name
    /qualification
    /dob
    /hobbies
    /email
    /twitter
    /linkedin 
    /github 
    /bye
    /hi
    /hy
    /gn
    /good_afternnon
    /gm
    /hwru
    /hello
    /cu

      """
    )
def qualification(update, context):
    update.message.reply_text("b.tech in cse from vignan's insititute of information and technology")
def linkedin(update, context):
    update.message.reply_text("this is my linkedin profile:https://www.linkedin.com/in/nikitha-vytla-42135520b/")
def github(update, context):
    update.message.reply_text("this is my github account:https://github.com/Nikithavytla03")
def twitter(update, context):
    update.message.reply_text("this is my twitter account:https://twitter.com/nikithavytla03")
def hobbies(update, context):
    update.message.reply_text("my hobbies are watching movies and listening to music")

def email(update, context):
    update.message.reply_text("you can contact me by:nikithavytla03@gmail.com")
def technical_skills(update, context):
    update.message.reply_text(
    """
    /c_language -> completed certification in sololearn
    /cpp_language ->completed certification in sololearn
   
    /python_for_beginners -> completed certification in sololearn 
    /python_core -> completed certification in sololearn 
    /intermediate_python -> completed certification in sololearn 
    /numpy_library -> completed the course in greatlearning
    /html -> completed the course in sololearn
    /flask_framework-> completed the course in greatlearning
    /hackerrank ->coding certifiaction on problem solving

    """

    )
def name(update, context):
    update.message.reply_text("my name is:NIKITHA VYTLA")
def dob(update, context):
    update.message.reply_text("date-of-birth:6th nov,2002")
def hi(update, context):
    update.message.reply_text("hello")
def hello(update, context):
    update.message.reply_text("hi")
def hy(update, context):
    update.message.reply_text("how can i help u")
def gm(update, context):
    update.message.reply_text("good morning,how r u?")
def hwru(update, context):
    update.message.reply_text("i am fine")
def good_afternoon(update, context):
    update.message.reply_text("gud afternoon,had ur lunch?")
def gn(update, context):
    update.message.reply_text("gud ni8,sweet dreams")
def bye(update, contex):
    update.message.reply_text("hope u will come soon")
def cu(update, context):
    update.message.reply_text("hope u will come soon")

    

def c_language(update, context):
    update.message.reply_text("here is my certification-link:https://www.sololearn.com/certificates/course/en/21777823/1089/landscape/png")
def cpp_language(update, context):
    update.message.reply_text("here is my certification-link:https://www.sololearn.com/certificates/course/en/21777823/1051/landscape/png")
def python_for_beginners(update, context):
    update.message.reply_text("here is my certification-link:https://www.sololearn.com/certificates/course/en/21777823/1157/landscape/png")
def python_core(update, context): 
    update.message.reply_text("here is my certification-link:https://www.sololearn.com/certificates/course/en/21777823/1073/landscape/png")
def intermediate_python(update, context):
    update.message.reply_text("here is my certification-link:https://www.sololearn.com/certificates/course/en/21777823/1158/landscape/png")


def html(update, context):
    update.message.reply_text("here is my certification-link:https://www.sololearn.com/certificates/course/en/21777823/1014/landscape/png")
def flask_framework(update, context):
    update.message.reply_text("here is my certification-link:https://olympus.mygreatlearning.com/courses/62867/certificate")
def numpy_library(update, context):
    update.message.reply_text("here is my certification-link:https://olympus.mygreatlearning.com/courses/50633/certificate")
def hackerrank(update, context):
    update.message.reply_text("here is my certification-link:https://www.hackerrank.com/certificates/559bb7da3bbd")
def content(update, context):
    update.message.reply_text("this chat_bot is created by nikitha vytla")

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))

dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
dispatcher.add_handler(telegram.ext.CommandHandler('content',content))
dispatcher.add_handler(telegram.ext.CommandHandler('technical_skills',technical_skills))
dispatcher.add_handler(telegram.ext.CommandHandler('html',html))
dispatcher.add_handler(telegram.ext.CommandHandler('flask_framework',flask_framework))
dispatcher.add_handler(telegram.ext.CommandHandler('numpy_library',numpy_library))
dispatcher.add_handler(telegram.ext.CommandHandler('intermediate_python',intermediate_python))
dispatcher.add_handler(telegram.ext.CommandHandler('python_core',python_core))
dispatcher.add_handler(telegram.ext.CommandHandler('python_for_beginners',python_for_beginners))
dispatcher.add_handler(telegram.ext.CommandHandler('cpp_language',cpp_language))
dispatcher.add_handler(telegram.ext.CommandHandler('c_language',c_language))
dispatcher.add_handler(telegram.ext.CommandHandler('name',name))
dispatcher.add_handler(telegram.ext.CommandHandler('dob',dob))
dispatcher.add_handler(telegram.ext.CommandHandler('hi',hi))
dispatcher.add_handler(telegram.ext.CommandHandler('hy',hy))
dispatcher.add_handler(telegram.ext.CommandHandler('hwru',hwru))
dispatcher.add_handler(telegram.ext.CommandHandler('bye',bye))
dispatcher.add_handler(telegram.ext.CommandHandler('cu',cu))
dispatcher.add_handler(telegram.ext.CommandHandler('good_afternnon',good_afternoon))
dispatcher.add_handler(telegram.ext.CommandHandler('hello',hello))
dispatcher.add_handler(telegram.ext.CommandHandler('gn',gn))
dispatcher.add_handler(telegram.ext.CommandHandler('gm',gm))
dispatcher.add_handler(telegram.ext.CommandHandler('qualification',qualification))
dispatcher.add_handler(telegram.ext.CommandHandler('hackerrank',hackerrank))
dispatcher.add_handler(telegram.ext.CommandHandler('email',email))
dispatcher.add_handler(telegram.ext.CommandHandler('twitter',twitter))
dispatcher.add_handler(telegram.ext.CommandHandler('github',github))
dispatcher.add_handler(telegram.ext.CommandHandler('linkedin',linkedin))
dispatcher.add_handler(telegram.ext.CommandHandler('hobbies',hobbies))


updater.start_polling()
updater.idle()
