from lexical.usefull_funct import remove_substring
from structure.GLC import GLC
from structure.constants import LAMBDA

def lambda_terminator(language : GLC):
    '''
        track and remove lambdas from variable, except the start one
    '''
    null_variables = []
    new_transition_rules = []
    for transition in language.get_transitions_list():
        if transition[1] == LAMBDA:
            null_variables.append(transition[0])
            if transition[0] == language.get_initial_variable():
                new_transition_rules.append(transition)
        else:
            new_transition_rules.append(transition)
    check_again = True
    while check_again:
        check_again = False
        for transition in language.get_transitions_list():
            if transition[1] in null_variables and not (transition[0] in null_variables):
                null_variables.append(transition[0])
                check_again = True

    no_lambda_transitions = new_transition_rules
    check_again = True
    while check_again:
        check_again = False
        for transition in new_transition_rules:
            position = 0
            while position < len(transition[1]):
                if transition[1][position] in null_variables:
                    new_rule = remove_substring(position, transition[1])
                    if new_rule == '':
                        new_rule = LAMBDA
                    new_transition = [transition[0], new_rule]

                    if not (new_transition in no_lambda_transitions) and transition[0] != new_rule:

                        if (new_rule == LAMBDA and transition[0] == language.get_initial_variable()) or new_rule != LAMBDA:
                            no_lambda_transitions.append(new_transition)
                            check_again = True

                position += 1
        new_transition_rules = no_lambda_transitions
    
    language.set_transitions_list(no_lambda_transitions)