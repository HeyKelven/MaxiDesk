import tools

data = tools.read_csv(tools.path_vendas)

id = tools.write_csv(tools.path_vendas,data)

print("sua ordem de serviço é: %05d\nGuarde o número, pois somente com ele, você conseguirá acompanhar o seu chamado" % id)