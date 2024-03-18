# 字典推导式
dial_codes = [
	(86, 'China'),
	(91, 'India'),
	(1, 'United States'),
	(62, 'Indonesia'),
	(55, 'Brazil'),
	(92, 'Pakistan'),
	(880, 'Bangladesh'),
	(234, 'Nigeria'),
	(7, 'Russia'),
	(81, 'Japan'),
]

country_code = {country: code for code, country in dial_codes}
print(type(country_code))
print(country_code)

x = {code: country.upper() for country, code in country_code.items() if code < 66}
print(x)


# 映射解包
def dump(**kwargs):
	return kwargs

print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 1}})

# 使用 | 合并映射
d1 = {'a' : 1, 'b' : 3}
d2 = {'a' : 2, 'b' : 4, 'c':6}
print(d1 | d2)

# 模式匹配处理映射
def get_creator(record: dict) -> list:
	match record:
		case {'type':'book', 'api': '2', 'authors':[*names]}:
			return names
		case {'type':'book', 'api': '2', 'author':name}:
			return [name]
		case {'type':'book'}:
			raise ValueError(f"Invalid 'book' record : {record!r}")
		case {'type':'movie', 'director':name}:
			return [name]
		case _:
			raise ValueError(f'Invalid record: {record!r}')