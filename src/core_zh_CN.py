def login(self, enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None):
    ''' 按照微信文档中所述的方法进行网页登录
        登录过程
            - 下载并打开一个QR(Quick Read)码
            - 程序会暂停并记录QR码的扫描状态,来让你扫码
            - 最终程序会完成登录并显示你的昵称
        参数
            - enableCmdQR: 使用命令行而不是一张图片来显示QR码
                - 填入整数值来适应不同CLI界面的字符宽度
            - picDir: 存放QR码图片的路径
            - qrCallback: 用来接收uuid,status,QR码的方法(可以用来自动扫码)
            - loginCallback: 登录成功后的回调函数
                - 缺省设定是清空命令行并删除QR码图片
            - exitCallback: 注销登录后的回调函数
                - 应当包含注销的调用
        如何使用
            ..code::python

                import itchat
                itchat.login()

        该函数定义在 components/login.py
        登录的每一步都可以在外部调用
            - 你可以通过查看源代码来研究如何登录
            - 也可以根据你自己的需求修改
    '''
    raise NotImplementedError()

def get_QRuuid(self):
    ''' 获取QR码的uuid
        uuid是QR码的非重复记号
            - 登录时,你需要先获取uuid
            - 下载QR码时,你需要将uuid传递给它
            - 检查登录状态时,也需要uuid
        如果uuid过期了,只需要再获取一个就可以了
        该函数定义在 components/login.py
    '''
    raise NotImplementedError()

def get_QR(self, uuid=None, enableCmdQR=False, picDir=None, qrCallback=None):
    ''' 下载并展示QR码
        参数
            - uuid: 如果没有输入uuid,则将会使用你最新获取的uuid
            - enableCmdQR: 用命令行展示QR码
            - picDir: 存储QR码的路径
            - qrCallback: 用来接收uuid,status,QR码的回调函数
        该函数定义在 components/login.py
    '''
    raise NotImplementedError()

def check_login(self, uuid=None):
    ''' 检查登录状态
        参数
            - uuid: 如果没有输入uuid,则将会使用你最新获取的uuid
        返回值:
            - 返回一个字符串
            - 返回值列表
                - 200: 登陆成功
                - 201: 等待确认通过
                - 408: uuid过期
                - 0  : 未知错误
        前置依赖
            - 需要定义好 syncUrl 和 fileUrl
            - 需要定义好 BaseRequest
        定义好上述内容之后才能够使用该函数
        该函数定义在 components/login.py
    '''
    raise NotImplementedError()

def web_init(self):
    ''' 获取初始化所需要的信息
        前置依赖
            - own account info is set
            - inviteStartCount is set
            - syncKey is set
            - part of contact is fetched
        it is defined in components/login.py
    '''
    raise NotImplementedError()

