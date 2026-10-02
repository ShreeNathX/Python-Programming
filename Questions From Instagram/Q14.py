def test():
    try:
        return 1
    finally:
        try:
            return 2
        finally:
            return 3

print(test())