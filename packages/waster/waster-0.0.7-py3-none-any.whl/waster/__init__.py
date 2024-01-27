"""
Waster is a simple microservice used to test the behaviour of the infrastructures.
"""

def main():
    """
    A main function that is really simple for an entrypoint to the most simple python program...

    :rtype: int
    """
    import importlib.metadata

    try:
        print(f'Waster {importlib.metadata.version(__name__)}')
    except importlib.metadata.PackageNotFoundError:
        print(f'Waster (version unknown)')
    return 0


if __name__ == '__main__':
    main()
