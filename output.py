################## Scheduling Plots ######################

## FCFS 
plt.plot(core_plot[1], 'r', label='CPU Usage')
plt.plot(memory_plot[1], 'b',label='Memory Usage')
plt.title("FCFS - Best Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(core_plot[0], 'r', label='CPU Usage')
plt.plot(memory_plot[0], 'b',label='Memory Usage')
plt.title("FCFS - First Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(core_plot[2], 'r', label='CPU Usage')
plt.plot(memory_plot[2], 'b',label='Memory Usage')
plt.title("FCFS - Worst Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

## Shortest Job First
plt.plot(core_plot[4], 'g', label='CPU Usage')
plt.plot(memory_plot[4], 'y',label='Memory Usage')
plt.title("Shortest job First - Best Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(core_plot[3], 'g', label='CPU Usage')
plt.plot(memory_plot[3], 'y',label='Memory Usage')
plt.title("Shortest job First - First Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(core_plot[5], 'g', label='CPU Usage')
plt.plot(memory_plot[5], 'y',label='Memory Usage')
plt.title("Shortest job First - Worst Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

## Shortest Duration Job First
plt.plot(core_plot[7], 'magenta', label='CPU Usage')
plt.plot(memory_plot[7], 'b',label='Memory Usage')
plt.title("Shortest Duration Job First - Best Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(core_plot[6], 'magenta', label='CPU Usage')
plt.plot(memory_plot[6], 'b',label='Memory Usage')
plt.title("Shortest Duration Job First - First Fit Usage")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(core_plot[8], 'magenta', label='CPU Usage')
plt.plot(memory_plot[8], 'b',label='Memory Usage')
plt.title("Shortest Duration Job First - Worst Fit Usage")
plt.legend()
plt.grid(True)
plt.show()
