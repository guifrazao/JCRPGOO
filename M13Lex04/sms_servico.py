from notificacao import ServicoNotificacao

class ServicoSMS(ServicoNotificacao):
    def notificar(self, nome_funcionario, mensagem):
        print(f"Enviando SMS para {nome_funcionario}: {mensagem}")
