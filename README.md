# BrainFuck-interpreter
This is an interpreter for BrainFuck written on python, see more information here: https://en.wikipedia.org/wiki/Brainfuck

Brainfuck is an esoteric programming language created in 1993 by Urban Müller.

Notable for its extreme minimalism, the language consists of only eight simple commands, a data pointer and an instruction pointer. While it is fully Turing complete, it is not intended for practical use, but to challenge and amuse programmers. Brainfuck requires one to break commands into microscopic steps.

The language's name is a reference to the slang term brainfuck, which refers to things so complicated or unusual that they exceed the limits of one's understanding as it was not meant or made for designing actual software but to challenge the boundaries of computer programming.

| Character  | Meaning |
| ------------- | ------------- |
| >  | Increment the data pointer (to point to the next cell to the right).  |
| <  | Decrement the data pointer (to point to the next cell to the left).  |
| +  | Increment (increase by one) the byte at the data pointer. |
| -  | Decrement (decrease by one) the byte at the data pointer.  |
| .  | 	Output the byte at the data pointer.  |
| [  | 	If the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.  |
| ]  |	If the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command. |
