from automata.fa.dfa import DFA

dfa = DFA(
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'd'},
    input_symbols = {'b', 'a'},
    # b means heads and a means tails
    transitions = {
        'q0':{'b':'q2','a':'q1'},
        'q1':{'b':'q2', 'a':'q3'},
        'q2':{'b':'q4','a':'q1'},
      'q3':{'b':'q2','a':'q5'},
        'q4':{'b':'d','a':'q1'},
        'q5':{'b':'q5','a':'q5'},
        'd':{'b':'d','a':'d'}
    }, 
    initial_state = 'q0',
    final_states= {'q5'}
)

if (dfa.accepts_input('baa')):
  print("Player may cross the bridge unharmed. You win")
else:
  print("Troll will eat you. You Lose.")
