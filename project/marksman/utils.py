

def handle_choice(choices: dict) -> None:

    # this function is specific to my use case and not generic
    # the number of choices in the dict is expected to be one or two and not large
    # the choices dict should be like this -> key : choice str, value : choice func
    # all choice str are meant to have unique prefix chars
    # this handler does not resolve prefix collisions, the first come first server

    ch_list = []
    msg = 'Choose your action  '
    for ch in choices.keys():
        ch_list.append(ch[0])
        msg += f' ({ch[0]}){ch[1:]} '
    user_choice = input(msg).lower().strip()
    if not user_choice:
        print('You did not choose anything. Exiting')
        return
    for ch in choices.keys():
        if ch.startswith(user_choice):
            func = choices.get(ch)
            return func()
    print('Invalid choice')


def clear_screen():
    pass


def display_table():
    pass
