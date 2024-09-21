# In mutable the reference is changed 
# Immutable = reference created is never changed in memory 

# Type "help", "copyright", "credits" or "license" for more information.
# >>> 1 + '1'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 2 ** 23
# 8388608
# >>> 2 ** 100000
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# >>> 2 ** 10000
# 19950631168807583848837421626835850838234968318861924548520089498529438830221946631919961684036194597899331129423209124271556491349413781117593785932096323957855730046793794526765246551266059895520550086918193311542508608460618104685509074866089624888090489894838009253941633257850621568309473902556912388065225096643874441046759871626985453222868538161694315775629640762836880760732228535091641476183956381458969463899410840960536267821064621427333394036525565649530603142680234969400335934316651459297773279665775606172582031407994198179607378245683762280037302885487251900834464581454650557929601414833921615734588139257095379769119277800826957735674444123062018757836325502728323789270710373802866393031428133241401624195671690574061419654342324638801248856147305207431992259611796250130992860241708340807605932320161268492288496255841312844061536738951487114256315111089745514203313820202931640957596464756010405845841566072044962867016515061920631004186422275908670900574606417856951911456055068251250406007519842261898059237118054444788072906395242548339221982707404473162376760846613033778706039803413197133493654622700563169937455508241780972810983291314403571877524768509857276937926433221599399876886660808368837838027643282775172273657572744784112294389733810861607423253291974813120197604178281965697475898164531258434135959862784130128185406283476649088690521047580882615823961985770122407044330583075869039319604603404973156583208672105913300903752823415539745394397715257455290510212310947321610753474825740775273986348298498340756937955646638621874569499279016572103701364433135817214311791398222983845847334440270964182851005072927748364550578634501100852987812389473928699540834346158807043959118985815145779177143619698728131459483783202081474982171858011389071228250905826817436220577475921417653715687725614904582904992461028630081535583308130101987675856234343538955409175623400844887526162643568648833519463720377293240094456246923254350400678027273837755376406726898636241037491410966718557050759098100246789880178271925953381282421954028302759408448955014676668389697996886241636313376393903373455801407636741877711055384225739499110186468219696581651485130494222369947714763069155468217682876200362777257723781365331611196811280792669481887201298643660768551639860534602297871557517947385246369446923087894265948217008051120322365496288169035739121368338393591756418733850510970271613915439590991598154654417336311656936031122249937969999226781732358023111862644575299135758175008199839236284615249881088960232244362173771618086357015468484058622329792853875623486556440536962622018963571028812361567512543338303270029097668650568557157505516727518899194129711337690149916181315171544007728650573189557450920330185304847113818315407324053319038462084036421763703911550639789000742853672196280903477974533320468368795868580237952218629120080742819551317948157624448298518461509704888027274721574688131594750409732115080498190455803416826949787141316063210686391511681774304792596709376
# >>> clear()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'clear' is not defined
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> import random
# >>> random.random()
# 0.4882031575454032
# >>> random.choice([1,2,3,4,4,9,5,78)]
#   File "<stdin>", line 1
#     random.choice([1,2,3,4,4,9,5,78)]
#                                    ^
# SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
# >>> random.choice([1,2,3,4,4,9,5,78])
# 9
# >>> random.choice([1,2,3,4,4,9,5,78])
# 2
# >>> random.choice([1,2,3,4,4,9,5,78])
# 1
# >>> random.choice([1,2,3,4,4,9,5,78])
# 5
# >>> random.choice([1,2,3,4,4,9,5,78])
# 3
# >>> for x in range(10):
# ...     random.choice([1,2,3,4,5,6,7,8,9])
# ...
# 7
# 9
# 3
# 3
# 7
# 2
# 9
# 7
# 6
# 3
# >>> name = 'Ahmed Mujtaba'
# >>> len(name)
# 13
# >>> name[9]
# 't'
# >>> name[-9]
# 'd'
# >>> newName = name[2:9]
# >>> newName
# 'med Muj'
# >>> dir(name)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> myList = [1,2,3,4,5,6,7,8,9]
# >>> myList
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> myList.add('Ahmed')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'add'
# >>> dir(name)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> dir(myList
# ... di
#   File "<stdin>", line 1
#     dir(myList
#         ^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>>
# >>> dir(myList)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> myList.insert('Ahmed')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: insert expected 2 arguments, got 1
# >>> myList
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> myList.extend('Ahmed')
# >>> myList
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'h', 'm', 'e', 'd']
# >>> dictionary = {'name':'Ahmed' , 'rollNo', 15, 'Class': 'BsCS sem 5'}
#   File "<stdin>", line 1
#     dictionary = {'name':'Ahmed' , 'rollNo', 15, 'Class': 'BsCS sem 5'}
#                                           ^
# SyntaxError: ':' expected after dictionary key
# >>> dictionary = {'name':'Ahmed' , 'rollNo': 15, 'Class': 'BsCS sem 5'}
# >>> dictionary
# {'name': 'Ahmed', 'rollNo': 15, 'Class': 'BsCS sem 5'}
# >>> len(dictionary)
# 3
# >>> dir(dictionary)
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# >>> dictionary[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 0
# >>> dictionary['name']
# 'Ahmed'
# >>> dictionary[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 0
# >>> myTuple = ('Ahmed', 2, 'Chai' , 'Code')
# >>> myTuple
# ('Ahmed', 2, 'Chai', 'Code')
# >>> myTuple[0]
# 'Ahmed'
# >>> len(myTuple)
# 4
# >>>
