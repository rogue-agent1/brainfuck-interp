import sys, argparse

def interpret(code, input_data=""):
    tape = [0] * 30000
    ptr = dp = ip = 0
    output = []
    brackets = {}
    stack = []
    for i, c in enumerate(code):
        if c == "[": stack.append(i)
        elif c == "]":
            j = stack.pop()
            brackets[j] = i
            brackets[i] = j
    while ip < len(code):
        c = code[ip]
        if c == ">": ptr = (ptr + 1) % 30000
        elif c == "<": ptr = (ptr - 1) % 30000
        elif c == "+": tape[ptr] = (tape[ptr] + 1) % 256
        elif c == "-": tape[ptr] = (tape[ptr] - 1) % 256
        elif c == ".": output.append(chr(tape[ptr]))
        elif c == ",":
            tape[ptr] = ord(input_data[dp]) if dp < len(input_data) else 0
            dp += 1
        elif c == "[" and tape[ptr] == 0: ip = brackets[ip]
        elif c == "]" and tape[ptr] != 0: ip = brackets[ip]
        ip += 1
    return "".join(output)

def main():
    p = argparse.ArgumentParser(description="Brainfuck interpreter")
    p.add_argument("file", nargs="?")
    p.add_argument("-c", "--code")
    p.add_argument("-i", "--input", default="")
    args = p.parse_args()
    if args.code: code = args.code
    elif args.file: code = open(args.file).read()
    else: code = sys.stdin.read()
    print(interpret(code, args.input))

if __name__ == "__main__":
    main()
