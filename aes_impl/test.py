import traceback


def test(expected, actual, verbose=0):
    if verbose == 1:
        if expected == actual:
            (filename, lineno, container, code) = traceback.extract_stack()[-2]
            print(f"Success: {code} .\nExpected and got '{expected}'\n")
        else:
            (filename, lineno, container, code) = traceback.extract_stack()[-2]
            print(f"Failed: {code} failed on line {lineno} in file {filename}."
                  f"\nExpected '{expected}' but got '{actual}'\n")

    else:
        if expected != actual:
            (filename, lineno, container, code) = traceback.extract_stack()[-2]
            print(f"Failed: {code} failed on line {lineno} in file {filename}."
                  f"\nExpected {expected} but got {actual}\n")
