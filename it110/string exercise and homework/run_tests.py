import colorama, datetime, os, shlex, signal, subprocess, sys, time

def run(command_chain, timeout = 30):
    """
    Runs the specified command chain and returns (True, <output>) on success. 
    If the command doesn't return within the specified time (in seconds), 
    (False, "") is returned. 
    """

    command_list = command_chain.split("|")
    start = datetime.datetime.now()
    process = None
    for command in command_list:
        tokens = shlex.split(command.strip())
        program = []
        for token in tokens:
            if token == "<" or token == ">":
                break
            program.append(token)
        stdin = None if not "<" in tokens \
                else open(tokens[tokens.index("<") + 1], "r")
        stdout = subprocess.PIPE if not ">" in tokens \
                 else open(tokens[tokens.index(">") + 1], "w")
        if process == None:
            process = subprocess.Popen(program, stdin = stdin, 
                                       stdout = stdout, 
                                       stderr = subprocess.STDOUT)
        else:
            process = subprocess.Popen(program, stdin = process.stdout, 
                                       stdout = stdout, 
                                       stderr = subprocess.STDOUT)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return False, ""
    return (True, process.stdout.read().strip().replace("\r\n", "\n")) \
        if process.stdout != None else (True, "")
    
def ok():
    """
    Returns the string "Pass" in green.
    """
    return "%sPass" %(colorama.Fore.GREEN)

def notok():
    """
    Returns the string "Fail" in red.
    """

    return "%sFail" %(colorama.Fore.RED)

def Problem1():
    print "***** Watson-Crick Complement *****"
    command = "python wc_complement.py ACTGACG"
    sought = """TGACTGC"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem2():
    print "***** Domain Type *****"
    command = "python domain_type.py http://www.swamiiyer.net/cs110/"
    sought = """net"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem3():
    print "***** Password Checker *****"
    command = "python password_checker.py Abcde1fg"
    sought = """False"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python password_checker.py Abcde1@g"
    sought = """True"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem4():
    print "***** Set Distance *****"
    command = "python set_distance.py \"b, c\" \"a, b, c, d\""
    sought = """0.5"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python set_distance.py \"7, 3, 2, 4, 1\" \"4, 1, 9, 7, 5\""
    sought = """0.571428571429"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem5():
    print "***** Word Frequencies *****"
    command = "echo it was the best of times it was the worst of times | python word_frequencies.py"
    sought = """of -> 2
it -> 2
times -> 2
the -> 2
was -> 2
worst -> 1
best -> 1"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

if __name__ == "__main__":
    colorama.init(autoreset = True)
    problems = [None, Problem1, Problem2, Problem3, Problem4, Problem5]
    args = map(int, sys.argv[1:])
    args = args if len(args) > 0 else range(1, len(problems))
    for i in args:
        problems[i]()
        print ""
