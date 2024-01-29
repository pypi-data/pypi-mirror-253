import json, uuid, sys, os, datetime, mimetypes
from urllib.parse import parse_qs
import cgi
import threading
sys.path.append(os.getcwd())
from io import BytesIO
import xmldict
import jwt
import tempfile
import peewee as pw

try:
    from config import APP_SETTING, API_PERMISSION
except Exception:
    APP_SETTING = {}
    API_PERMISSION = {}

try:
    from models import MODEL_MAPPING
except Exception:
    MODEL_MAPPING = {}

try:
    from config.sql_template import SQL_TEMPLATE
except Exception:
    SQL_TEMPLATE = {}

from wsgiref.simple_server import make_server


# region tools

def jwt_encode(user):
    # 把需要用来做权限校验的字段 都加入token中
    # 例如：{ "id": user.id, "role": user.role， "org_id": user.org_id }
    user_dict = user.to_dict()
    data = {}
    for item in APP_SETTING["jwt"]["column"]:
        data[item] = user_dict[item] if item in user_dict else ""

    return jwt.encode(data, APP_SETTING["jwt"]["secret"], algorithm='HS256')


def jwt_decode(token):
    return jwt.decode(token, APP_SETTING["jwt"]["secret"], algorithms=['HS256'])


def row_to_dict(cursor, row):
    """将返回结果转换为dict"""
    d = {}
    for idx, col in enumerate(cursor.description):
        if str(col[0]).startswith('_'):
            continue

        d[col[0]] = row[idx]
        if isinstance(row[idx], datetime.datetime):
            d[col[0]] = row[idx].strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(row[idx], datetime.date):
            d[col[0]] = row[idx].strftime('%Y-%m-%d')
        else:
            d[col[0]] = row[idx]
    return d

# endregion


# region request

url_map = {}
class Request(threading.local):

    def getRequestText(self):
        MEMFILE_MAX = 1024 * 100

        maxread = max(0, self.content_length)
        stream = self._environ['wsgi.input']
        body = BytesIO() if maxread < MEMFILE_MAX else tempfile.TemporaryFile(mode='w+b')
        while maxread > 0:
            part = stream.read(min(maxread, MEMFILE_MAX))
            if not part:  # TODO: Wrong content_length. Error? Do nothing?
                break
            body.write(part)
            maxread -= len(part)
        return body.getvalue().decode()

    def bind(self, environ, url_map):
        self._environ = environ

        self._headers = None
        self._user = None
        self._BODY = ''
        self._GET = {}
        self._POST = {}
        self._FILES = {}

        self.path = self._environ.get('PATH_INFO', '')
        self.path_resource = ''
        self.path_operation = ''
        self.path_param = ''

        if self.path.startswith('/api/'):
            arr_path = str(str(self.path).replace('/api/', '')).split('/')
            self.path_resource = arr_path[0]
            self.path_operation = arr_path[1]
            self.path_param = arr_path[2] if len(arr_path) == 3 else None

        # region URL 参数
        query_string = self._environ.get('QUERY_STRING', '')
        raw_dict = parse_qs(query_string, keep_blank_values=1)
        for key, value in raw_dict.items():
            if len(value) == 1:
                self._GET[key] = value[0]
            else:
                self._GET[key] = value
        # endregion

        # region 请求处理
        if self.path_resource in url_map and self.path_operation in url_map[self.path_resource] \
                and url_map[self.path_resource][self.path_operation]["secret"] != None:
            secret = url_map[self.path_resource][self.path_operation]["secret"]
        elif self.path_resource == "file":
            secret = False
        else:
            secret = APP_SETTING["request"]["secret"]

        if self.path_resource != "file":
            self._BODY = self.getRequestText(self)
        if "multipart/form-data" in self.content_type and self.path_resource:
            raw_data = cgi.FieldStorage(fp=self._environ['wsgi.input'], environ=self._environ)
            if raw_data.list:
                for key in raw_data:
                    if raw_data[key].filename:
                        self._FILES[key] = raw_data[key]
                    elif isinstance(raw_data[key], list):
                        self._POST[key] = [v.value for v in raw_data[key]]
                    else:
                        self._POST[key] = raw_data[key].value

            if secret:
                self._POST = APP_SETTING["request"]["process"](self._POST)
        if "application/json" in self.content_type:
            self._POST = json.loads(self._BODY)
            if secret:
                self._POST = APP_SETTING["request"]["process"](self._POST)
        if "application/xml" in self.content_type or "text/xml" in self.content_type:
            self._POST = xmldict.xml_to_dict(self._BODY)
            if secret:
                self._POST = APP_SETTING["request"]["process"](self._POST)
        # endregion

    # region 请求信息

    @property
    def method(self):
        return self._environ.get('REQUEST_METHOD', 'GET').upper()

    @property
    def headers(self):
        if self._headers == None:
            self._headers = {}
            for key, value in dict(self._environ).items():
                if str(key).startswith("HTTP_"):
                    self._headers[str(key).replace("HTTP_", "")] = value
        return self._headers

    @property
    def user(self):
        if self._user == None:
            token = self.headers["AUTHORIZATION"] if "AUTHORIZATION" in self.headers and self.headers[
                "AUTHORIZATION"] else ""
            if token:
                self._user = jwt_decode(token)
            else:
                self._user = {
                    "id": "",
                    "username": "anymore",
                    "name": "匿名用户",
                    "role": "anymore"
                }
                for item in APP_SETTING["jwt"]["column"]:
                    if item not in self._user:
                        self._user[item] = ""
        return self._user

    @property
    def content_type(self):
        return self._environ.get('CONTENT_TYPE', '')

    @property
    def content_length(self):
        return int(self._environ.get('CONTENT_LENGTH', '') or -1)

    # endregion

    # region 请求数据

    @property
    def BODY(self):
        return self._BODY

    @property
    def GET(self):
        return self._GET

    @property
    def POST(self):
        return self._POST

    @property
    def FILES(self):
        return self._FILES

    # endregion
request = Request()

# endregion


# region db

db = pw.MySQLDatabase(
    host=APP_SETTING["db"]["host"] if "db" in APP_SETTING else "",
    port=APP_SETTING["db"]["port"] if "db" in APP_SETTING else "",
    user=APP_SETTING["db"]["user"] if "db" in APP_SETTING else "",
    passwd=APP_SETTING["db"]["passwd"] if "db" in APP_SETTING else "",
    database=APP_SETTING["db"]["database"] if "db" in APP_SETTING else "",
    charset='utf8'
)


def gen_id():
    return uuid.uuid4().hex


class BaseModel(pw.Model):
    id = pw.CharField(primary_key=True, unique=True, max_length=128, default=gen_id, verbose_name="主键ID")
    created = pw.DateTimeField(default=datetime.datetime.now, verbose_name="创建时间")
    is_del = pw.IntegerField(default=0)

    class Meta:
        database = db

    def to_dict(self):
        data = {}
        for k in self.__dict__['__data__'].keys():
            if str(k).startswith('_'):
                continue
            if isinstance(self.__dict__['__data__'][k], datetime.datetime):
                data[k] = self.__dict__['__data__'][k].strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(self.__dict__['__data__'][k], datetime.date):
                data[k] = self.__dict__['__data__'][k].strftime('%Y-%m-%d')
            else:
                data[k] = self.__dict__['__data__'][k]
        return data


# endregion


# region auto_view

def generate_where_and_params(dict_where):
    #     """
    #     __exact 精确等于 like ‘aaa’
    #     __contains 包含 like ‘%aaa%’
    #     __gt 大于
    #     __gte 大于等于
    #     __lt 小于
    #     __lte 小于等于
    #     __in 存在于一个list范围内 (1, 2)
    #     __isnull 为null 不是'' ， 值：true， false
    #     """
    #
    #     """
    #     __year 时间或日期字段的年份
    #     __month 时间或日期字段的月份
    #     __day 时间或日期字段的日
    #     __date 时间或日期字段的日期部分
    #     __startswith 以…开头
    #     __endswith 以…结尾
    #     """

    arr_where = []
    param_where = dict()
    for key in dict_where.keys():
        if dict_where[key] != '':
            arr_k = key.split("__")
            if len(arr_k) == 1:
                arr_where.append(key + " = {" + key + "}")
                param_where[arr_k[0]] = dict_where[key]
            if len(arr_k) == 2:
                field = arr_k[0]
                operation = str(arr_k[1]).lower()
                if operation == "exact":
                    arr_where.append(field + " = {" + field + "}")
                    param_where[arr_k[0]] = dict_where[key]
                if operation == "contains":
                    arr_where.append(field + " like {" + field + "}")
                    param_where[arr_k[0]] = "%" + dict_where[key] + "%"
                if operation == "gt":
                    arr_where.append(field + " > {" + field + "}")
                    param_where[arr_k[0]] = dict_where[key]
                if operation == "gte":
                    arr_where.append(field + " >= {" + field + "}")
                    param_where[arr_k[0]] = dict_where[key]
                if operation == "lt":
                    arr_where.append(field + " < {" + field + "}")
                    param_where[arr_k[0]] = dict_where[key]
                if operation == "lte":
                    arr_where.append(field + " <= {" + field + "}")
                    param_where[arr_k[0]] = dict_where[key]
                if operation == "in" and len(dict_where[key]) > 0:
                    arr_where.append(field + " in (" + ",".join(['\'' + item + '\'' if isinstance(item, str) else str(item) for item in dict_where[key]]) + ") ")
                    # param_where[arr_k[0]] = dict_where[key]
                if operation == "isnull" and dict_where[key] == True:
                    arr_where.append("ISNULL(" + field + ")")
                    # param_where[arr_k[0]] = dict_where[key]
                if operation == "isnull" and dict_where[key] == False:
                    arr_where.append("NOT ISNULL(" + field + ")")
                    # param_where[arr_k[0]] = dict_where[key]

    return arr_where, param_where


def auto_list(request, table_name):
    select = request.POST.get('select', '*')
    where = request.POST.get('where', '{}')
    order_by = request.POST.get('order_by', '')

    page = int(request.POST.get('page', '1'))
    size = int(request.POST.get('size', '10000'))

    str_sql = "select " + select + " from " + table_name

    if table_name in SQL_TEMPLATE:
        str_sql = "select " + select + " from (" + SQL_TEMPLATE[table_name] + ") t_template "

    dict_temp = json.loads(where)
    dict_template = dict()
    dict_where = dict()

    for key in dict_temp:
        if '__template' in key:
            dict_template[str(key).replace('__template', '')] = dict_temp[key]
        else:
            dict_where[key] = dict_temp[key]

    if dict_template:
        str_sql = str_sql.format(**dict_template)

    arr_where, param_where = generate_where_and_params(dict_where)

    if len(arr_where) > 0:
        str_sql += " where " + " and ".join(arr_where)

    if order_by:
        str_sql += " order by " + order_by

    data_sql = "select * from (" + str_sql + ") t limit " + str((page - 1) * size) + "," + str(size)
    data_cursor = db.execute_sql(data_sql.format(**param_where))
    data = data_cursor.fetchall()

    count_sql = "select count(*) from (" + str_sql + ") t "
    count_cursor = db.execute_sql(count_sql.format(**param_where))
    count = count_cursor.fetchall()

    return {
        "code": 200,
        "data": [row_to_dict(data_cursor, row) for row in data],
        "total": count[0][0],
        "msg": "Success"
    }


def auto_get(request, table_name, pk):
    select = request.POST.get('select', '*')
    str_sql = "select " + select + " from " + table_name + " where id = '{id}' "

    cursor = db.execute_sql(str_sql.format(**{"id": pk}))
    row = cursor.fetchone()

    if not row:
        return {
            "code": 404,
            "msg": "Not Found"
        }

    data = row_to_dict(cursor, row)

    return {
        "code": 200,
        "data": data,
        "msg": "Success"
    }


def auto_post(request, table_name):
    Model = MODEL_MAPPING[table_name]

    model = Model.create(**request.POST)

    return {
        "code": 200,
        "msg": "Success",
        "data": model.to_dict()
    }


def auto_put(request, table_name, pk):

    Model = MODEL_MAPPING[table_name]
    model = Model.get_or_none(Model.id == pk)

    if not model:
        return {"code": 400, "msg": "参数错误！"}

    for r in request.POST.keys():
        model.__setattr__(r, request.POST[r])

    model.save()

    return {
        "code": 200,
        "msg": "Success",
        "data": model.to_dict()
    }


def auto_delete(request, table_name, pk):
    Model = MODEL_MAPPING[table_name]
    model = Model.get_or_none(Model.id == pk)

    if not model:
        return {"code": 400, "msg": "参数错误！"}

    model.is_del = 1
    model.save()

    return {
        "code": 200,
        "msg": "Success"
    }


def auto_drop(request, table_name, pk):
    Model = MODEL_MAPPING[table_name]
    model = Model.get_or_none(Model.id == pk)

    if not model:
        return {"code": 400, "msg": "参数错误！"}

    model.delete_instance()

    return {
        "code": 200,
        "msg": "Success"
    }


auto_config = {
    "list": auto_list,
    "get": auto_get,
    "post": auto_post,
    "put": auto_put,
    "delete": auto_delete,
    "drop": auto_drop
}

# endregion


# region file_view

def file_file(request, operation):
    field_storage = request.FILES.get("file")

    allow_file_type = APP_SETTING["file"][operation]
    file_type = field_storage.filename.split('.')[-1]
    if str(file_type).lower() not in allow_file_type:
        return {
            "code": 400,
            "msg": "File Type Error!"
        }

    file_name = uuid.uuid4().hex + '.' + file_type

    root_path = os.getcwd()
    dt_path = datetime.datetime.now().strftime("%Y%m%d")
    full_path = os.path.join(root_path, 'static/files', dt_path)

    if not os.path.isdir(full_path):
        os.makedirs(full_path)

    with open(os.path.join(full_path, file_name), "wb") as f:
        f.write(field_storage.value)

    return {
        "code": 200,
        "data": '/static/files/' + dt_path + '/' + file_name,
        "msg": "Success"
    }

# endregion


# region doc_view

def doc_list(request):
    result = {}

    for resource_key, resource_value in url_map.items():
        resource = {}
        for operation_key, operation_value in resource_value.items():
            operation = {}
            for key, value in operation_value.items():
                if not callable(value):
                    operation[key] = value
            resource[operation_key] = operation
        result[resource_key] = resource

    return {
        "code": 200,
        "data": result,
        "msg": "Success"
    }


doc_config = {
    "list": doc_list
}

# endregion


def application(environ, star_response):
    request.bind(environ, url_map)

    # region html请求
    if request.method == "GET" and (request.content_type == "text/plain" or request.content_type == "text/html"):
        if request.path == '/favicon.ico':
            file_path = 'static/favicon.ico'
            if not os.path.exists(file_path) or not os.path.isfile(file_path):
                star_response('404 Not Found', [('Content-Type', 'text/html')])
                return [''.encode('utf-8'), ]

            mimetype, encoding = mimetypes.guess_type(file_path)
            star_response('200 OK', [('Content-Type', mimetype)])
            return '' if request.method == 'HEAD' else open(file_path, 'rb')

        elif str(request.path).startswith('/static/'):
            file_path = os.path.join("/static/", request.path).lstrip('/')
            if not os.path.exists(file_path) or not os.path.isfile(file_path):
                star_response('404 Not Found', [('Content-Type', 'text/html')])
                return [''.encode('utf-8'), ]

            mimetype, encoding = mimetypes.guess_type(file_path)
            star_response('200 OK', [('Content-Type', mimetype)])
            return '' if request.method == 'HEAD' else open(file_path, 'rb')
        else:
            if not request.path_resource or not request.path_operation:
                star_response('200 OK', [('Content-Type', 'text/html')])
                return ['''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body>接口不存在</body></html>'''.encode('utf-8'), ]

            star_response('200 OK', [('Content-Type', 'text/html')])
            return ['''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body>接口页面</body></html>'''.encode('utf-8'), ]

    # endregion

    # 资源
    path_resource = request.path_resource
    # 方法
    path_operation = request.path_operation
    # 参数
    path_param = request.path_param

    # region 接口权限判断
    permission = []
    if path_resource in API_PERMISSION:
        if path_operation in API_PERMISSION[path_resource]:
            permission = API_PERMISSION[path_resource][path_operation]
        elif path_operation in API_PERMISSION["__default"]:
            permission = API_PERMISSION["__default"][path_operation]
        else:
            permission = API_PERMISSION["__default"]["__other"]
    else:
        if path_operation in API_PERMISSION["__default"]:
            permission = API_PERMISSION["__default"][path_operation]
        else:
            permission = API_PERMISSION["__default"]["__other"]

    permission_check = False

    if len(permission) == 0:
        star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
        response = json.dumps({"code": 403, "msg": "Permission Denied"}).encode('utf-8')
        return [response, ]

    if "anymore" in permission:
        permission_check = True

    if "all" in permission and request.user and request.user["id"]:
        permission_check = True

    permission_role = []
    permission_column = []
    for item in permission:
        if "__" in item:
            permission_column.append(item)
        else:
            permission_role.append(item)

    if request.user["role"] in permission_role:
        permission_check = True

    if permission_check == False and len(permission_column) > 0 and path_param:
        permission_check_model = MODEL_MAPPING[path_resource].get_or_none(MODEL_MAPPING[path_resource].id == path_param)
        if not permission_check_model:
            star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
            response = json.dumps({"code": 404, "msg": "Not Found!"}).encode('utf-8')
            return [response, ]
        permission_check_model = permission_check_model.to_dict()
        for item in permission_column:
            user_column = item.split("__")[0]
            model_column = item.split("__")[1]
            if user_column in request.user and model_column in permission_check_model:
                if request.user[user_column] in permission_check_model[model_column]:
                    permission_check = True
                    break

    if not permission_check:
        star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
        response = json.dumps({"code": 403, "msg": "Permission Denied"}).encode('utf-8')
        return [response, ]
    # endregion

    # 请求地址 在url_map 中 已注册
    if path_resource in url_map and path_operation in url_map[path_resource]:
        if path_operation in url_map[path_resource]:
            func = url_map[path_resource][path_operation]

            if request.method not in func["method"]:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                response = json.dumps({"code": 405, "msg": "Method Not Allowed!"}).encode('utf-8')
                return [response, ]

            handle = func["handle"]
            if path_param is not None:
                result = handle(request, path_param)
            else:
                result = handle(request)

            if type(result) == dict:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                return [json.dumps(result).encode('utf-8'), ]
            elif type(result) == str:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                return [result.encode('utf-8'), ]
            else:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                return [result, ]
    elif path_resource == "file":
        # 文件接口
        if path_operation in APP_SETTING["file"]:
            if request.method != "POST":
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                response = json.dumps({"code": 405, "msg": "Method Not Allowed!"}).encode('utf-8')
                return [response, ]

            result = file_file(request, path_operation)

            star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
            response = json.dumps(result).encode('utf-8')
            return [response, ]
        else:
            star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
            response = json.dumps({"code": 404, "msg": "Not Found!"}).encode('utf-8')
            return [response, ]
    elif path_resource == "docs":
        # 文档接口
        if path_operation in doc_config:
            if request.method != "POST":
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                response = json.dumps({"code": 405, "msg": "Method Not Allowed!"}).encode('utf-8')
                return [response, ]

            result = doc_config[path_operation](request)

            star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
            response = json.dumps(result).encode('utf-8')
            return [response, ]
        else:
            star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
            response = json.dumps({"code": 404, "msg": "Not Found!"}).encode('utf-8')
            return [response, ]
    else:
        if path_operation in auto_config:
            if request.method != "POST":
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                response = json.dumps({"code": 405, "msg": "Method Not Allowed!"}).encode('utf-8')
                return [response, ]

            handle = auto_config[path_operation]

            if path_param is not None:
                result = handle(request, path_resource, path_param)
            else:
                result = handle(request, path_resource)

            if type(result) == dict:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                return [json.dumps(result).encode('utf-8'), ]
            elif type(result) == str:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                return [result.encode('utf-8'), ]
            else:
                star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
                return [result, ]
        else:
            star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
            response = json.dumps({"code": 404, "msg": "Not Found!"}).encode('utf-8')
            return [response, ]


def route(resource, operation, method=['POST'], secret=None):
    def wrapper(handler):
        if resource not in url_map:
            url_map[resource] = {}

        url_map[resource][operation] = {
            "method": method,
            "handle": handler,
            "secret": secret
        }
        return handler

    return wrapper


def run(host='127.0.0.1', port=8000):
    '''
    启动监听服务
    '''
    httpd = make_server(host, port, application)
    print('服务已启动 ...')
    print('正在监听 http://%s:%d/' % (host, port))
    print('按 Ctrl-C 退出')
    print('')
    httpd.serve_forever()
