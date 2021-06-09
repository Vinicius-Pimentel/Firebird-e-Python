import fdb
import os

con = fdb.connect(host="localhost",database="C:/SIC/ARQ01/ARQSIST.FDB", user="sysdba", password="masterkey")

cur = con.cursor()
codigoClientesSemCarteira = cur.execute("select codic from arqcad where restricao_cobr = 'NNSS'")
#esse código pega o ID dos clientes que não usam carteira

lista = cur.fetchall()

codigoAtualizar = lista
#print(lista) - printa o código dos clientes que serão atualizados no terminal
atualizar = lista

if os.path.exists("C:\SIC\log_clientes.txt"):                    #|
    arquivo = open("C:\SIC\log_clientes.txt", "w")               #|
    arquivo.write(f"Código dos clientes atualizados: {lista} ")  #|
    arquivo.close()                                              #| Gera a log dos clientes que
else:                                                            #| tiveram os dados atualizados
    arquivo = open("C:\SIC\log_clientes.txt", "a")               #|
    arquivo.write(f"Código dos clientes atualizados: {lista} ")  #|
    arquivo.close()                                              #|


print('Aguarde um momento, os dados estão sendo atualizados!')

cur.execute("DELETE FROM ARQCADCOBR") #apaga todos os dados da tabela

for atualizar in codigoAtualizar:         #atualiza o cadastro de cobranças permitidas dos clientes
    cur.execute(f"INSERT INTO arqcadcobr (CODIGO, ARQCADCOBR.TIPOC, TIPO_COBRANCA) VALUES ({('%i' % (atualizar))}, 'C', 1)")
    cur.execute(f"INSERT INTO arqcadcobr (CODIGO, ARQCADCOBR.TIPOC, TIPO_COBRANCA) VALUES ({('%i' % (atualizar))}, 'C', 10)")
    cur.execute(f"INSERT INTO arqcadcobr (CODIGO, ARQCADCOBR.TIPOC, TIPO_COBRANCA) VALUES ({('%i' % (atualizar))}, 'C', 7)")
    cur.execute(f"INSERT INTO arqcadcobr (CODIGO, ARQCADCOBR.TIPOC, TIPO_COBRANCA) VALUES ({('%i' % (atualizar))}, 'C', 12)")
    cur.execute(f"INSERT INTO arqcadcobr (CODIGO, ARQCADCOBR.TIPOC, TIPO_COBRANCA) VALUES ({('%i' % (atualizar))}, 'C', 18)")
    cur.execute("update arqcad set restricao_cobr = 'NNNN' where restricao_cobr = 'NNSS'")
    
con.commit()
cur.close()
con.close()

print('Dados atualizados com sucesso!')
