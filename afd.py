class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = start_state
        self.accept_states = accept_states

    def transition(self, symbol):
        if symbol not in self.alphabet:
            raise ValueError("Symbol not in alphabet")
        self.current_state = self.transitions.get((self.current_state, symbol))
        if self.current_state is None:
            raise ValueError("Invalid transition")

    def reset(self):
        self.current_state = self.start_state

    def is_accepted(self):
        return self.current_state in self.accept_states


# Exemplo de uso
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q2',
    ('q1', '0'): 'q1',
    ('q1', '1'): 'q1',
    ('q2', '0'): 'q2',
    ('q2', '1'): 'q2'
}
start_state = 'q0'
accept_states = {'q1'}

dfa = DFA(states, alphabet, transitions, start_state, accept_states)

# Testando com uma entrada
input_string = "1111"
for symbol in input_string:
    dfa.transition(symbol)

if dfa.is_accepted():
    print("A entrada é aceita pelo DFA.")
else:
    print("A entrada é rejeitada pelo DFA.")