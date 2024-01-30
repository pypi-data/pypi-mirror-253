from flask import request, jsonify
import psutil,time,os,sys,json
from collections import OrderedDict

is_array = lambda var: isinstance(var, (list, tuple, OrderedDict))
is_string = lambda var: isinstance(var, (str))

class CoreFlask():
    """
    """
    version = '1.0.13'  # Version updated 2024-01-29 1
    app = None          # Flask app sent from main.py
    _p = None           # CorePerformance
    session = None      # CoreSession
    system = None       # CoreSystem
    logs = None         # CoreLogs
    errors = None       # CoreLogs
    isThis = None       # CoreIs
    cache = None        # CoreCache

    security = None     # CoreSecurity
    user = None         # CoreUser
    config = None       # CoreConfig
    request = None      # CoreRequest
    localization = None # CoreLocalization
    model = None        # CoreModel

    def __init__(self,app,root_path=''):
        self.app = app
        self._p = CorePerformance()
#         self.session = CoreSession()
        self.system = CoreSystem(root_path)
        self.logs = CoreLog()
        self.errors = CoreLog()
        self.isThis = CoreIs()
        self.cache = CoreCache()
        # self._p.add('Construct Class with objects (__p,session[started=false],system,logs,errors,isThis,cache): Core.__init__' , __file__);

        self.security = CoreSecurity(self)
#        self.user = CoreUser(self)
        self.config_file = self.system.root_path+'/config.json' if os.path.isfile(self.system.root_path+'/config.json') else ""
        self.config = CoreConfig(self,self.config_file)
#         self.request = CoreRequest(self)
#         self.localization = CoreLocalization(self)
#         self.model = CoreModel(self)
#         self._p.add('Loaded security,user,config,request,localization,model objects with __session[started=false')
        return None

    def dispatch(self):
        """Return a friendly HTTP response."""

        #region SET [script_path] && [module_path]
        # Evaluate if the route is API path based on core_api_url
        file = '_version' if self.system.url['parts'][0] == "" else self.system.url['parts'][0]

        if file[0] == '_':
            script_path = os.path.dirname(__file__)+"/api/"+file+".py"
            module_path = "cloudframework.api."+file
        else:
            script_path = self.system.root_path+"/api/"+file+".py"
            module_path = "api."+file
        #endregion

        #region EVALUATE if not os.path.isfile(script_path) then return 404
        if not os.path.isfile(script_path):
            response = self.app.response_class(
                response=json.dumps({
                    "success":False,
                    "status":404,
                    "code":"endpoint-not-found",
                    "module":module_path
                }),
                status=404,
                mimetype='application/json'
            )
            return response
        #endregion

        #region CREATE [api = module.API(self)] where [module = __import__(module_path,..)]
        module = __import__(module_path, globals(), locals(), ['API'], 0)
        # create the api object

        api = module.API(self)
        #endregion

        #region EXECUTE [api.main()] and return [api.send()]
        api.main()
        return api.send()
        #endregion

class CoreSystem:
    """
    https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data
    """
    root_path = None
    app_path = None
    app_url = None
    url = None
    spacename = None
    test = "Hello"

    def __init__(self,root_path=''):
        if not root_path: root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.root_path = root_path
        # print os.path.abspath(__file__)
        self.app_path = self.root_path+'/_webapp'
        self.app_url = '/_webapp'
        self.spacename = 'cloudframework'

        self.url = OrderedDict()

        self.url['https'] = True if ('https' in request.base_url) else False
        self.url['protocol'] = 'https' if self.url['https'] else 'http'
        self.url['url'] = request.path
        self.url['params'] = request.full_path.split('?')[1]
        self.url['url_uri'] = request.full_path

        self.url['host'] = request.host
        self.url['host_base_url'] = request.url_root
        self.url['host_url'] = request.base_url
        self.url['host_url_uri'] = request.url

        self.url['script_name'] = request.script_root
        self.url['parts'] = self.url['url'].split('/')
        self.url['parts'].pop(0)

    def getUrl(self,key):
        if key in self.url:
            return self.url[key]
        else:
            return None

class CorePerformance:
    """
    """
    data = None
    root_path = None
    def __init__(self):
        self.data = OrderedDict()
        self.data['initMicrotime'] = time.time()
        self.data['lastMicrotime'] = self.data['initMicrotime']
        self.data['initMemory'] = psutil.virtual_memory()
        self.data['lastMemory'] = self.data['initMemory']
        self.data['lastIndex'] = 1
        self.data['info'] = []
        self.data['info'].append( "File :"+__file__.replace(os.path.dirname(os.path.dirname(__file__)),""))
        self.data['info'].append("Init Memory Usage: "+str(self.data['initMemory']))
        self.data['init'] = OrderedDict()
        self.root_path = os.path.dirname(os.path.dirname(__file__))

    # init to calculate time and memory spent passing a spacename and key
    def init(self,spacename,key):

        # <editor-fold desc="Init self.data['init'][spacename][key]['mem'],['time'],['ok']">
        if spacename not in self.data['init'].keys():
            self.data['init'][spacename] = {}
        self.data['init'][spacename][key] = {"mem":psutil.virtual_memory(),"time":time.time(),"ok":True}
        # </editor-fold>

    # end a call after a init to calculate time and memory spent
    def end(self,spacename,key,ok=True,msg=''):

        # <editor-fold desc="Verify if a previous init exist. If not return False and self.data['init'][spacename][key]['error']">
        if spacename not in self.data['init'].keys():
            self.data['init'][spacename] = {key:{"error":"CorePerformance.end with no previous CorePerformance.init"}}
            return False

        if key not in self.data['init'][spacename]:
            self.data['init'][spacename][key] = {"error":"CorePerformance.end with no previous CorePerformance.init"}
            return False
        # </editor-fold>

        # <editor-fold desc="Verify if a previous init exist. If not return False and self.data['init'][spacename][key]['error']">
        self.data['init'][spacename][key] = {
            "mem": self.data['init'][spacename][key]['mem'] - psutil.virtual_memory()
            , "time": time.time()-self.data['init'][spacename][key]['time']
            , "ok": ok }

        if not ok:
            self.data['init'][spacename][key]['notes'] =  msg
        # </editor-fold>

    # add a entry for performance
    def add(self,title,file='',type='all'):

        # Hidding full path (security)
        file = file.replace(os.path.dirname(os.path.dirname(__file__)),"")

        # Preparing the line to save
        line = ''
        if type == 'note':
            line += "["+type
        else:
            line += str(self.data['lastIndex'])+" ["

        if file.__len__():
            file = " ("+file+")"

        # Calculating memory
        _mem = psutil.virtual_memory()  - self.data['lastMemory'];
        if type == 'all' or type=='endnote' or type=='memory':
            line+= str(round(_mem, 3))+' Mb';
            self.data['lastMemory'] = psutil.virtual_memory()

        # Calculating memory
        _time = time.time() -self.data['lastMicrotime']
        if type == 'all' or type=='endnote' or type=='time':
            line+= ', '+str(round(_time, 3))+' secs';
            self.data['lastMicrotime'] = time.time()

        # Adding the title
        line += '] '+str(title)

        # Adding accum data

        if type!='note':
            line = "[ "+str(round(psutil.virtual_memory(),3))+" Mb, "+str(round(time.time() -self.data['initMicrotime'],3))+" secs] / "+line+file

        if type=='endnote':
            line = "["+type+"] "+line

        self.data['info'].append(line)
        self.data['lastIndex']+=1

class CoreConfig():
    """Class to control the application configuration
    """
    core = None
    data = None
    lang = None
    _configPaths = None

    def __init__(self, core,file=''):
        """Init the configuration
        """
        self.core = core            # type: Core
        self.data = OrderedDict()
        self.lang = 'en'
        self._configPaths = []

        # init system values
        self.set('core_system_url',core.system.url['url'])
        self.set('core_system_default_lang',self.lang)
        self.set('core_api_url','/p/api')
        self.set('core_model_default','/model.json')
        self.set('core_spacename','cloudframework')

        self.set('wapploca_api_url', 'https://wapploca.org/h/api/wapploca')
        self.set('wapploca_cache_expiration_time',3600)
        self.set('_webapp', self.core.system.app_url)
        self.set('webapp_menupath_rule', None)
        self.set('webapp_menupath_data', [])

        # read file of configuration
        if file:
            if os.path.isfile(file):
                self.readConfigJSONFile(file)
            else:
                self.core.logs.add("the following config file does not exist: "+file)

        # process special tags
        if(self.get('core_default_lang')):
            self.lang = self.get('core_default_lang')

    # read a configJSON file and send it to processConfigData
    def readConfigJSONFile(self, file):
        # Control we are not reading the same file to avoid infinite loops
        if file in self._configPaths:
            self.core.logs.add("Recursive config file: " + file);
            return

        # try to read the file
        self._configPaths.append(file)
        try:
            # open the file and send it to json.load expecting a valid json
            with open(file) as data_file:
                data = json.load(data_file,object_pairs_hook=OrderedDict)
            # process the data
            self.processConfigData(data)
        except Exception as inst:
            self.core.errors.add('Error CoreConfig.readConfigJSONFile reading file: '+file)
            print(inst)
            # self.core.errors.add(inst.message)

    def processConfigData(self,data):
        """ process a dictionary of config orders assignin it to data
        """
        for (cond, vars) in data.items():
            # just a comment
            if cond =='--': continue

            # convert potential tags {{tag}} when it is a string
            if is_string(vars):
                vars = self.convertTags(vars)

            # Evaluate to include the condition
            include = False # if True then we will include
            tagcode = ''    # if !='' then it is a tagcode with a special meaning.

            # if there is a potential tagcode
            if ':' in cond:
                cond = self.convertTags(cond.strip())
                (tagcode,tagvalue)  = cond.split(':',2)
                tagcode = tagcode.strip()
                tagvalue = tagvalue.strip()

                if self.isConditionalTag(tagcode):
                    # depends of the contion the info will be include in config
                    include = self.getConditionalTagResult(tagcode,tagvalue)

                elif self.isAssignationTag(tagcode):
                    # execute a command
                    self.setAssignationTag(tagcode, tagvalue, vars)

                else:
                    # unknown tagcode
                    self.core.errors.add('unknown tag: |' +tagcode + '|')
                    continue
            # it is just a key=>value
            else:
                include = True
                vars = {cond:vars}  # convert vars into a dict

            # continue if we do not have to include in CoreConfig.data
            if not include: continue

            # add in CoreConfig.data or call recursively processConfigData for potential tagcodes
            for (key, value) in vars.items():
                # it is a comment
                if key ==' --':continue

                # it is a potential tagcode
                if ':' in key:
                    self.processConfigData({key:value})
                # it is a key=>value
                else:
                    self.set(key,value)

    def convertTags(self, data):
        """ convert potential tags {{tag}}
        """

        # if not string the convert to string
        dumped = False
        if not(is_string(data)):
            data = json.dumps(data)
            dumped = True

        # Apply transformations
        if '{{rootPath}}' in data:  data = data.replace('{{rootPath}}',self.core.system.root_path)
        # TODO: apply transaformation
        # appPath
        # lang
        # confVar

        # reconvert to original
        if dumped:
            data = json.loads(data, object_pairs_hook=OrderedDict)


        # return transformed data
        return data

    def isConditionalTag(self,tag):
        """return true if the tag is conditional array"""
        return tag.lower() in ["uservar", "authvar", "confvar", "sessionvar", "servervar", "auth", "noauth", "development", "production"
            , "indomain", "domain", "interminal", "url", "noturl", "inurl", "notinurl", "beginurl", "notbeginurl"
            , "inmenupath", "notinmenupath", "isversion", "false", "true"]

    def getConditionalTagResult(self,tagcode, tagvalue):
        """return True or False based in a tagcode and tagvalue
        """
        ret = False # False by defautl

        # tags to evaluate
        evaluateTags = []

        # does tagvalue multples tagcodes '|', then add pairs tagcode: single value for or conditions
        while '|' in tagvalue:
            (tagvalue,tags) = tagvalue.split('|',2)
            evaluateTags.append([tagcode.strip().lower(),tagvalue.strip()])
            (tagcode,tagvalue) = tags.split(':',2)

        # add the last tagcode,tagvalue
        evaluateTags.append([tagcode.strip().lower(), tagvalue.strip()])

        # start evaluating tags
        for evaluateTag in evaluateTags:
            tagcode = evaluateTag[0].strip()
            tagvalue = evaluateTag[1].strip()
            if tagcode == 'uservar' or tagcode == 'authvar':
                pass
            elif tagcode =='confvar':
                pass
            elif tagcode =='true':
                ret = True
            elif tagcode =='false':
                pass
            elif tagcode =='interminal':
                ret = self.core.isThis.terminal();
            elif tagcode == 'indomain' or tagcode== 'domain':
                if 'HTTP_HOST' in os.environ:
                    HTTP_HOST = os.environ['HTTP_HOST']
                    domains = tagvalue.split(',')
                    for domain in domains:
                        pass
            elif tagcode =='production':
                ret = self.core.isThis.production()
            elif tagcode =='development':
                ret = self.core.isThis.development()
            else:
                self.core.errors.add('unknown tag: |'+ tagcode+ '|')
            if ret: break

        # return ret
        return ret

    def isAssignationTag(self,tag):
        """return true if the tag is assignation tag array"""
        return tag.lower() in ["webapp", "set", "include", "redirect", "menu","coreversion"]

    def setAssignationTag(self,tagcode, tagvalue, vars):
        # type: (object, object, object) -> object
        tagcode = tagcode.strip().lower()
        if tagcode == 'webapp':
            self.set(tagcode,vars)
            self.core.setAppPath(vars)
        elif tagcode == 'set': self.set(tagvalue, vars)
        elif tagcode == 'include':
            self.readConfigJSONFile(vars)
            pass
        elif tagcode == 'redirect': pass
        elif tagcode == 'menu':
            # The menu is only available for WSGI app
            if not self.core.isThis.terminal():
                # menu has to be an array of elements in vars
                if not(is_array(vars)):
                    self.core.errors.add("menu: tag does not contain an array")
                else:
                    vars = self.convertTags(vars) # convert potencial tags
                    for value in vars:
                        # verify the structure is right
                        if not(is_array(value)) or 'path' not in value.keys():
                            self.core.errors.add("menu: element does not contains an array with the path element")
                            # print type(value) is OrderedDict
                        # add the line in pushMenu
                        else:
                            self.pushMenu(value)
                            pass
        elif tagcode == 'coreversion': pass
        else: self.core.errors.add('unknown tag: |' + tagcode + '|')

    def pushMenu(self, line):
        if 'webapp_menupath_rule' in self.data.keys() and self.data['webapp_menupath_rule']:
            # when menu path is set is because a previous menu has been found
            return

        if not (is_array(line)) or 'path' not in line.keys():
            self.core.logs.add('Missing path in menu line')
            self.core.logs.add(line)
        else:
            _found = False
            if '{*}' in line['path']:
                _found = self.core.system.url['url'].find(line['path'].replace('{*}','')) == 0
            else:
                _found = self.core.system.url['url'] == line['path'];

            # if _found we set all the vars as a config vars
            if _found:
                self.set('webapp_menupath_data', line)
                self.set('webapp_menupath_rule', line['path'])
                for (key,value) in line.items():
                    if 'path' == key: continue
                    value = self.convertTags(value)
                    self.set(key,value)

    def get(self,key):
        """get a key from data"""
        if(key in self.data):
            return self.data[key]
        else:
            return None

    def set(self,key,value):
        """set a key into data"""
        self.data[key] = value

class CoreRequest():
    """
    """
    core = None

    def __init__(self, core):
        self.core = core    # type: Core



class CoreLog:
    """
    """
    lines = 0
    data = None

    def __init__(self):
        self.lines = 0
        self.data =[]

    def set(self,value):
        self.data = [value]
        self.lines = 1

    def add(self,value):
        self.data.append(value)
        self.lines+=1


class CoreIs:
    """
    """
    def __init__(self):
        pass
    def development(self):
        return os.getenv('GAE_ENV','') == ''
    def production(self):
        return os.getenv('GAE_ENV','') != ''
    def terminal(self):
        return not('REMOTE_ADDR' in os.environ)


class CoreCache:
    """
    """
    def __init__(self):
        pass


class CoreSecurity:
    """
    """
    core = None

    def __init__(self,core):
        self.core = core            # type: Core
