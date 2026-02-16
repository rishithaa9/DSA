def aOrB(k, a, b, c):
    # Convert hex strings to integers
    A = int(a, 16)
    B = int(b, 16)
    C = int(c, 16)

    changes = 0

    # Step 1: Make A | B == C with minimum changes
    for i in range(0, max(len(a), len(b), len(c)) * 4):
        bitA = (A >> i) & 1
        bitB = (B >> i) & 1
        bitC = (C >> i) & 1

        if bitC == 0:
            if bitA == 1:
                A &= ~(1 << i)
                changes += 1
            if bitB == 1:
                B &= ~(1 << i)
                changes += 1
        else:  # bitC == 1
            if bitA == 0 and bitB == 0:
                B |= (1 << i)
                changes += 1

        if changes > k:
            print(-1)
            return

    # Step 2: Minimize A, then B (if extra changes allowed)
    for i in reversed(range(0, max(len(a), len(b), len(c)) * 4)):
        if changes >= k:
            break

        bitA = (A >> i) & 1
        bitB = (B >> i) & 1
        bitC = (C >> i) & 1

        if bitC == 1:
            # Try removing 1 from A
            if bitA == 1 and bitB == 1:
                A &= ~(1 << i)
                changes += 1
            # Try removing 1 from B
            elif bitA == 0 and bitB == 1 and changes < k:
                B &= ~(1 << i)
                A |= (1 << i)
                changes += 2

            if changes > k:
                print(-1)
                return

    # Print results in uppercase hexadecimal
    print(hex(A)[2:].upper())
    print(hex(B)[2:].upper())


# Input handling
if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        k = int(input().strip())
        a = input().strip()
        b = input().strip()
        c = input().strip()
        aOrB(k, a, b, c)
