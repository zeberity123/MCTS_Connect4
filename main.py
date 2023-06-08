import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from connect_four import game
import numpy as np

print(f'\n(1): 2 Human Players')
print(f'(2): Play against AI')
print(f'(3): Test_MCTS')
connect_four = game.Game()

try:
    print(f'\nPlease Enter 1~3: ', end='')
    input1 = int(input())
    if input1 == 1:
        print('-----------------------------------')
        print(f'Play text version: 1')
        print(f'Play GUI version: 2')

        try:
            print(f'\nPlease Enter 1 or 2: ', end='')
            input2 = int(input())

        except:
            print(f'\nWrong input! Please Enter 1 or 2.')
        
        if input2 == 1:
            connect_four.play_text()

        elif input2 == 2:
            connect_four.play_gui()
        
        else:
            print(f'\nWrong input! Please Enter 1 or 2.')
    
    elif input1 == 2:
        print('-----------------------------------')
        print(f'Play text version: 1')
        print(f'Play GUI version: 2')

        try:
            print(f'\nPlease Enter 1 or 2: ', end='')
            input2 = int(input())

        except:
            print(f'\nWrong input! Please Enter 1 or 2.')
        
        if input2 == 1:
            print('-----------------------------------')
            print(f'Human Play First: 1')
            print(f'AI Play First: 2')
            try:
                print(f'\nPlease Enter 1 or 2: ', end='')
                input3 = int(input())

            except:
                print(f'')
            
            if input3 == 1:
                connect_four.play_mcts(False, 1500, 1.41) # (who_go_first, n_of_iteration, c_value)

            elif input3 == 2:
                connect_four.play_mcts(True, 1500, 1.41) # (who_go_first, n_of_iteration, c_value)
            
            else:
                print(f'\nWrong input! Please Enter 1 or 2.')

        elif input2 == 2:
            print('-----------------------------------')
            print(f'Human Play First: 1')
            print(f'AI Play First: 2')
            try:
                print(f'\nPlease Enter 1 or 2: ', end='')
                input3 = int(input())

            except:
                print(f'\nWrong input! Please Enter 1 or 2.')
            
            if input3 == 1:
                connect_four.play_gui_mcts(1) # (first_player)

            elif input3 == 2:
                connect_four.play_gui_mcts(-1) # (second_player)
            
            else:
                print(f'\nWrong input! Please Enter 1 or 2.')
        
        else:
            print(f'\nWrong input! Please Enter 1 or 2.')

    elif input1 == 3:
        c_values = [1.4, 1.4]
        n_of_simulations = [1,5]

        completed1 = connect_four.auto_mcts(100,100,c_values[0],c_values[1],n_of_simulations[0],n_of_simulations[1]) # (n_of_games, n_of_iterations, c1, c2, s1, s2)
        result1 = completed1[0]
        print(f'\nstart 2 \n')
        completed2 = connect_four.auto_mcts(100,100,c_values[1],c_values[0],n_of_simulations[1],n_of_simulations[0])
        result2 = completed2[0]

        # print(f'\nWhen c_value: {c_values[0]}goes first:')
        print(f'\nWhen number_of_simulations: {n_of_simulations[0]} goes first:')
        print(f'  Player O: {result1[0]} wins')
        print(f'  Player X: {result1[1]} wins')
        print(f'  Tie     : {result1[2]} games')
        print(f'  Time taken for P1: {sum(completed1[1]):.3f} seconds, Average: {np.mean(completed1[1]):.3f}  seconds')
        print(f'  Time taken for P2: {sum(completed1[2]):.3f}  seconds, Average: {np.mean(completed1[2]):.3f}  seconds')

        # print(f'When c_value: {c_values[1]}goes first:')
        print(f'When number_of_simulations: {n_of_simulations[1]} goes first:')
        print(f'  Player O: {result2[0]} wins')
        print(f'  Player X: {result2[1]} wins')
        print(f'  Tie     : {result2[2]} games')
        print(f'  Time taken for P1: {sum(completed2[1]):.3f}  seconds, Average: {np.mean(completed2[1]):.3f}  seconds')
        print(f'  Time taken for P2: {sum(completed2[2]):.3f}  seconds, Average: {np.mean(completed2[2]):.3f}  seconds')

    else:
        print(f'Wrong input! Please Enter 1~3.')

except KeyboardInterrupt:
    sys.exit()

except:
    print('end')
    raise Exception()
    # print(f'Wrong input! Please Enter 1~2.')

