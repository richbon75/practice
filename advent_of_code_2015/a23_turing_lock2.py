
# read in and parse the program
prog = list()
f = open("a23_input.txt",'r')
for line in f:
    cmd = line.strip('\n').split(' ')
    cmd[1] = cmd[1].strip(',')
    if cmd[1].strip(',') not in ('a', 'b'):
        cmd.append(cmd[1])
        cmd[1] = None
    if len(cmd) == 3:
        cmd[2] = int(cmd[2])
    prog.append(cmd)
f.close()
for p in prog:
    print(p)

# init and run the program
# this time, a starts as 1
regs = {'a':1, 'b':0}
pc = 0
while pc < len(prog):
    # fetch next instruction
    cmd = prog[pc]
    # execute instruction
    if cmd[0] == 'hlf':
        regs[cmd[1]] = regs[cmd[1]] // 2
    elif cmd[0] == 'tpl':
        regs[cmd[1]] *= 3
    elif cmd[0] == 'inc':
        regs[cmd[1]] += 1
    elif cmd[0] == 'jmp':
        pc += cmd[2]
        continue
    elif cmd[0] == 'jie':
        if regs[cmd[1]] % 2 == 0:
            pc += cmd[2]
            continue
    elif cmd[0] == 'jio':
        if regs[cmd[1]] == 1:
            pc += cmd[2]
            continue
    # increment pc
    pc += 1
print('Program run complete')
print(regs)



