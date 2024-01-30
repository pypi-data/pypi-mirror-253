def registrar_transacao(self, data, descricao, valor, categoria):
    transacao = {"data": data, "descricao": descricao,
                 "valor": valor, "categoria": categoria}
    self.transacoes.append(transacao)
