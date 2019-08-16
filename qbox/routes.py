from qbox import qbox

@qbox.route('/')
@qbox.route('/index')
def index():
    return "QBox reporting"
