texto = open('popula_banco.sql')
saída = open('sql_organizado.sql', 'w')
texto2 = ''

teste = "insert into comclien values(	1 	,'0001','AARONSON FURNITURE'   	    ,'AARONSON FURNITURE LTD'	,'2015-02-17 23:14:50',     '17.807.928/0001-85', '(21) 8167-6584' ,'QUEIMADOS'             ,'RJ' );"

var = ''
var = teste.split()

print(var)
