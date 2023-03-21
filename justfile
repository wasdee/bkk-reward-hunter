encrypt-curl:
    find . -name "*.curl" -exec keybase encrypt circleoncircles -i {} -o {}.encrypted \;