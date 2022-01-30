def get_dir():
    return __file__[:-9]


def log_all_available_imports():
    import pkgutil

    return str(list(pkgutil.iter_modules()))
