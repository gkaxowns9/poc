from winpwn import *

context.x64dbg = r"C:\tools\x64dbg\release\x64\x64dbg.exe"
context.log_level = "debug"

p = process("./jrev1.exe")
x64dbg.attach(p)

p.interactive()
