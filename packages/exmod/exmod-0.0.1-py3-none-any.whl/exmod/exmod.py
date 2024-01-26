def main():
    import sys

    for pos, arg in enumerate(sys.argv):
        print('Argument %d: %s' % (pos, arg))

if __name__ == '__main__':
    main()