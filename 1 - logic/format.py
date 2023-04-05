a = 'AAA'
b = 'BBB'
c = 1.80

string = 'a={} b={} c={}'
formatted = string.format(a, b, c)
# print(formatted)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
# print(formato.format(nome, idade))

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
# print(formato.format(n=nome, i=idade))
