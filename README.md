# LogView
* a tool to view logs.
* it can float on the toplayer of your windows.
* it's easy to add commands to it, for viewing commonly used logs.

# GetIns
* a tool to collect which instructions are used in the ELF file.
* It should can be disassembled by llvm-objdump (or you can change the tool in getins.py).

usage: ./getins.py elffile
options:  
-s : not list how times that instructions appear.

# CmpIns
* a tool that can find  out the diffrences between .ins file(can be created by GetIns tool)

usage: ./getins.py elffile1 elffile2
options:  
-new : list the instructions that appered in elfflie2 and not in elffile1.
-dis : list the instructions that appered in elfflie1 and not in elffile2.
