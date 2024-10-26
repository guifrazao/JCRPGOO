from Modulos import *

def main():
    # Criar dois jogadores
    player1_name = input("Digite o nome do jogador 1: ")
    player2_name = input("Digite o nome do jogador 2: ")
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    
    # Criar o jogo com ambos os jogadores
    game = GuessingGame.create_game([player1, player2])
    
    print("\n" + "="*40)
    print("✨ BEM-VINDO AO JOGO DA ADIVINHAÇÃO ✨")
    print("🎯 Tente adivinhar o número secreto entre 1 e 100!")
    print("="*40)
    
    current_player = player1  # Definindo o jogador que começa

    while True:
        try:
            print("\n" + "-"*40)
            print(f"🔄 Turno de {current_player.get_name()}")
            guess = int(input(f"🎲 {current_player.get_name()}, faça um palpite (1-100): "))
            result = game.make_guess(current_player, guess)
            print(result)
            if "Parabéns" in result:
                print(f"\n🏆 {current_player.get_name()} venceu o jogo! 🏆")
                break
            # Alternar para o próximo jogador
            current_player = player2 if current_player == player1 else player1
        except ValueError as e:
            print(f"❗ Erro: {e}")

main()
