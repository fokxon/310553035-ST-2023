import angr
import sys

main_addr = 0x401146
find_addr = 0x4012af
avoid_addr = 0x401294

class my_scanf(angr.SimProcedure):
    def run(self, fmt, s):
        simfd = self.state.posix.get_fd(sys.stdin.fileno())
        data, ret_size = simfd.read_data(4)
        self.state.memory.store(s, data)
        return 1

proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})
state = proj.factory.blank_state(addr=main_addr)

proj.hook_symbol('__isoc99_scanf', my_scanf(), replace=True)

simgr = proj.factory.simulation_manager(state)

simgr.explore(find=find_addr, avoid=avoid_addr)
if simgr.found:
    ofile = open('solve_input', 'w')
    for i in range(15):
        input = simgr.found[0].posix.dumps(sys.stdin.fileno())[i * 4 : i * 4 + 4]
        input = int.from_bytes(input, byteorder=sys.byteorder, signed=True)
        print(input, file=ofile)

else:
    print('Failed')