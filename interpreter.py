import sys

memory_cell_limit = 255


def execute(file):
    try:
        with open(file, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Cant't find file {file}")
        return 1
    evaluate(code)
    return 0


def evaluate(code):

    def jump_to_closing_bracket(temp_codeptr):
        brackets = 1
        while brackets:
            temp_codeptr += 1
            if code[temp_codeptr] == "[":
                brackets += 1
            elif code[temp_codeptr] == "]":
                brackets -= 1
        return temp_codeptr

    code = list(cleanup(code))

    memory, codeptr, memoryptr = [0], 0, 0
    # List keeps pointers to loops beginnings, None value means this loop have to be skipped
    loops = []

    while codeptr < len(code):

        command = code[codeptr]

        if command == ">":
            memoryptr += 1
            if memoryptr == len(memory):
                memory.append(0)
        if command == "<":
            if memoryptr <= 0:
                memoryptr = 0
            else:
                memoryptr -= 1
        if command == "+":
            if memory[memoryptr] == memory_cell_limit:
                memory[memoryptr] = 0
            else:
                memory[memoryptr] += 1
        if command == "-":
            if memory[memoryptr] == 0:
                memory[memoryptr] = memory_cell_limit
            else:
                memory[memoryptr] -= 1
        if command == ".":
            sys.stdout.write(chr(memory[memoryptr]))
        if command == ",":
            val = int(input(f"Enter value for cell {memoryptr+1}: "))
            if val < 0 or val > memory_cell_limit:
                print(f"Cell value must be from 0 to {memory_cell_limit}")
                print("Current cell value will be set to 0")
                memory[memoryptr] = 0
            else:
                memory[memoryptr] = val
        if command == "[":
            if memory[memoryptr] == 0:
                codeptr = jump_to_closing_bracket(codeptr)
            else:
                loops.append(codeptr+1)
        if command == "]":
            if memory[memoryptr] == 0:
                loops.pop()
            else:
                codeptr = loops[-1]
                continue
        codeptr += 1


def cleanup(code: str) -> str:
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


if __name__ == "__main__":
    file = input("Enter filename: (try examples/helloworld.bf)")
    err_code = execute(file)
    print(f"Exited with error code {err_code}.")
