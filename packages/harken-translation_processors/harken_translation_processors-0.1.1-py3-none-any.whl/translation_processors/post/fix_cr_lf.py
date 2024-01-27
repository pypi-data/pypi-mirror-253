def fix_cr_lf(src: str, tgt: str) -> str:
    new_tgt = tgt
    if (len(src) >= 1
            and src[-1] == "\n"
            and tgt[-1] != "\n"):
        new_tgt += "\n"
    elif (len(src) >= 1
          and src[-1] == " "
          and tgt[-1] != " "):
        new_tgt += " "
    if (len(src) >= 2
            and src[-2] == " "
            and tgt != " "):
        new_tgt = new_tgt[:-1] + ' ' + new_tgt[-1:]

    return new_tgt

__all__ = ["fix_cr_lf"]
