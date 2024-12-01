from notificacao import ServicoNotificacao

class ServicoEmail(ServicoNotificacao):
    def notificar(self, nome_funcionario, mensagem):
        print(f"Enviando email para {nome_funcionario}: {mensagem}")
