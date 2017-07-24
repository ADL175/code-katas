def proper_parenthetics(str):
    """Tests for proper parenthetics, open:1; balanced:0; broken:-1."""
    open_par = 0
    close_par = 0
    if str[0] == ')':
        return -1
    for i in str:
        if close_par > open_par:
            return -1
        elif i == '(':
            open_par += 1
        elif i == ')':
            close_par += 1
    if open_par > close_par:
        return 1
    if close_par == open_par:
        return 0
    if close_par > open_par:
        return -1
