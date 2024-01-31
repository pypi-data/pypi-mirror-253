import re
import codecs
import decimal
from email.utils import parseaddr
from datetime import datetime, date, time
import pprint

# oconv converts data to be displayed or rendered.
class oconv(object):
    @staticmethod
    def none(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        if data == 'null':
            return ''
        return data

    @staticmethod
    def phone(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        if not data:
            return data
        data = re.search(r'\d{10}$', re.sub("[^0-9]", "", data)).group()
        return "({}) {}-{}".format(data[:3],data[3:6],data[6:])


    @staticmethod
    def day_of_week(data, abbrev=False):
        if isinstance(data, list):
            new = []
            for day in data:
                new.append(oconv.day_of_week(day, abbrev=abbrev))
            return ','.join(new)
        if data == None:
            return ''
        if data == 'None':
            return ''
        if not data:
            return data
        if abbrev:
            return {
                1: 'Mon',
                2: 'Tue',
                3: 'Wed',
                4: 'Thu',
                5: 'Fri',
                6: 'Sat',
                7: 'Sun'
            }[int(data)]
        return {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }[int(data)]

    @staticmethod
    def date(*args, **kwds):
        kwds.setdefault('fmt','%Y-%m-%d')
        def _(param):
            if isinstance(param,(datetime, date)):
                return param.strftime( kwds['fmt'] )
            else:
                return param
        if args and args[0]:
            return _(args[0])
        return _

    @staticmethod
    def time(*args, **kwds):
        kwds.setdefault('fmt','%X')
        def _(param):
            if isinstance(param,(datetime, time)):
                return param.strftime( kwds['fmt'] )
            else:
                return param
        if args and args[0]:
            return _(args[0])
        return _

    @staticmethod
    def timestamp(*args, **kwds):
        kwds.setdefault('fmt','%c')
        def _(param):
            if isinstance(param,(datetime)):
                return param.strftime( kwds['fmt'] )
            else:
                return param
        if args:
            return _(args[0])
        return _

    @staticmethod
    def email(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return data.lower()

    @staticmethod
    def pointer(data):
        try:
            return int(data)
        except:
            return ''

    @staticmethod
    def rot13(data):
        return codecs.decode(data,'rot13')

    @staticmethod
    def boolean(data):
        if isinstance(data,str):
            if data.lower() in ['false','','f','off','no']:
                return False
        return bool(data)

    @staticmethod
    def money(data):
        if data in [None,'']:
            return ''
        data = re.sub("[^0-9\.-]", "", str(data))
        return '${:,.2f}'.format(decimal.Decimal(data))

    @staticmethod
    def round(precision, data=None):
        def function(data):
            data = re.sub("[^0-9\.]", "", str(data))
            if data == '':
                return '0'
            return '{:.{prec}f}'.format(decimal.Decimal(data), prec=precision)
        if data == None:
            return function
        return function(data)

    @staticmethod
    def ein(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        if not data:
            return data
        data = re.search(r'\d{9}$', re.sub("[^0-9]", "", data)).group()
        return "{}-{}".format(data[:2],data[2:])

    @staticmethod
    def list(data):
        if data in (None,'None'):
            return None
        if isinstance(data, list):
            return data
        if isinstance(data, str):
            if data[0] == '[':
                return eval(data)
        return [data]

    @staticmethod
    def title(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return str(data).title()

    @staticmethod
    def lower(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return str(data).lower()

    @staticmethod
    def upper(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return str(data).upper()

    @staticmethod
    def padding(length, char):
        def inner(data):
            if data is None:
                return ''
            return str(data).rjust(length, char)
        return inner

    @staticmethod
    def pprint(data):
        try:
            return pprint.pformat(eval(data))
        except:
            return data

    @staticmethod
    def string(data):
        if data == None:
            return ''
        return str(data)

# iconv converts data to be stored in the database.
# The source is generally user input from html forms.
class iconv(object):
    @staticmethod
    def none(data):
        if data == '':
            return None
        if data == 'null':
            return None
        if data == '@NULL':
            return None
        return data

    @staticmethod
    def phone(data):
        if data == 'None':
            return None
        if not data:
            return data
        return re.search(r'\d{10}$', re.sub("[^0-9]", "", data)).group()

    @staticmethod
    def day_of_week(data):
        if not data:
            return data
        return {
            'monday': 1,
            'tuesday': 2,
            'wednesday': 3,
            'thursday': 4,
            'friday': 5,
            'saturday': 6,
            'sunday': 7,
            'mon': 1,
            'tue': 2,
            'wed': 3,
            'thu': 4,
            'fri': 5,
            'sat': 6,
            'sun': 7
        }[data.lower()]

    @staticmethod
    def date(*args, **kwds):
        kwds.setdefault('fmt', '%Y-%m-%d')
        def _(param):
            if isinstance(param,str):
                return datetime.strptime(param, kwds['fmt']).date()
            else:
                return param
        if args and args[0]:
            return _(args[0])
        return _

    @staticmethod
    def time(*args, **kwds):
        kwds.setdefault('fmt','%X')
        def _(param):
            if isinstance(param, str):
                return datetime.strptime(param, kwds['fmt']).time()
            else:
                return param
        if args and args[0]:
            return _(args[0])
        return _

    @staticmethod
    def timestamp(*args, **kwds):
        kwds.setdefault('fmt','%c')
        def _(param):
            if isinstance(param, str):
                return datetime.strptime(param, kwds['fmt'])
            else:
                return param
        if args and args[0]:
            return _(args[0])
        return _

    @staticmethod
    def email(data):
        if not data:
            return None
        if data == 'None':
            return None
        data = data.strip().lower()
        if '@' not in data:
            raise Exception()
        email = parseaddr(data)[1]
        mailbox,domain = email.split('@')
        if '.' in domain:
            if len(domain.split('.')[1]) < 1:
                raise Exception()
        else:
            raise Exception()
        return data

    @staticmethod
    def integer(data):
        return int(re.sub("[^0-9\.-]", "", str(data)))

    @staticmethod
    def boolean(data):
        if isinstance(data,str):
            if data.lower() in ['false','','f','off','no']:
                return False
        return bool(data)

    @staticmethod
    def rot13(data):
        return codecs.encode(data,'rot13')

    @staticmethod
    def pointer(data):
        if data == '@new': return data
        if data == '': return None
        if data == None: return None
        if data == '@NULL': return None
        return int(data)

    @staticmethod
    def money(data):
        if data == 'None':
            return None
        if not data:
            return data
        return decimal.Decimal(re.sub("[^0-9\.-]", "", str(data)))

    @staticmethod
    def round(precision, data=None):
        def function(data):
            if data == 'None':
                return None
            if not data:
                return data
            if isinstance(data, str):
                data = re.sub("[^0-9\.-]", "", data)
            return decimal.Decimal(data).quantize(decimal.Decimal(10) ** -precision, rounding=decimal.ROUND_HALF_UP)
        if data == None:
            return function
        return function(data)

    @staticmethod
    def decimal(data):
        if data == 'None':
            return None
        if not data:
            return data
        return decimal.Decimal(re.sub("[^0-9\.-]", "", str(data)))

    @staticmethod
    def ein(data):
        if data == 'None':
            return None
        if not data:
            return data
        return re.search(r'^\d{9}$', re.sub("[^0-9]", "", data)).group()

    @staticmethod
    def list(data):
        if data in (None,'None'):
            return None
        if isinstance(data, str):
            if data[0] == '[':
                return data
        if not isinstance(data, list):
            data = [data]
        return repr(data)

    @staticmethod
    def title(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return str(data).title()

    @staticmethod
    def lower(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return str(data).lower()


    @staticmethod
    def upper(data):
        if data == None:
            return ''
        if data == 'None':
            return ''
        return str(data).upper()

    @staticmethod
    def padding(length, char):
        def inner(data):
            if data in [None,'None','']:
                return None
            return str(data).rjust(length, char)
        return inner

    @staticmethod
    def string(data):
        if data == '':
            return None
        return str(data)

if __name__=='__main__':
    print(iconv.money("$123.441.234c"))
