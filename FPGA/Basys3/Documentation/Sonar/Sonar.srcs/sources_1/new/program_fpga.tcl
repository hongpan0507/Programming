open_hw
connect_hw_server
open_hw_target
set_property PROBES.FILE {} [lindex [get_hw_devices] 0]
set_property PROGRAM.FILE {W:/Sonar.runs/impl_1/sonar.bit} [lindex [get_hw_devices] 0]
program_hw_devices [lindex [get_hw_devices] 0]