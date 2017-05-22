set PROMfile "W:/Sonar.runs/impl_1/sonar.mcs"
write_cfgmem  -format mcs -size 4 -interface SPIx4 -loadbit "up 0x00000000 W:/Sonar.runs/impl_1/sonar.bit " -force -file $PROMfile
set my_mem_device [lindex [get_cfgmem_parts {s25fl032p-spi-x1_x2_x4}] 0]
set my_hw_cfgmem [create_hw_cfgmem -hw_device [lindex [get_hw_devices] 0] -mem_dev $my_mem_device]

set_property PROGRAM.ADDRESS_RANGE  {use_file} $my_hw_cfgmem
set_property PROGRAM.FILES [list $PROMfile ] $my_hw_cfgmem
set_property PROGRAM.UNUSED_PIN_TERMINATION {pull-none} $my_hw_cfgmem
set_property PROGRAM.BLANK_CHECK  0 $my_hw_cfgmem
set_property PROGRAM.ERASE  1 $my_hw_cfgmem
set_property PROGRAM.CFG_PROGRAM  1 $my_hw_cfgmem
set_property PROGRAM.VERIFY  1 $my_hw_cfgmem
set_property PROGRAM.CHECKSUM  0 $my_hw_cfgmem
startgroup 
if {![string equal [get_property PROGRAM.HW_CFGMEM_TYPE  [lindex [get_hw_devices] 0]] [get_property MEM_TYPE [get_property CFGMEM_PART [get_property PROGRAM.HW_CFGMEM [lindex [get_hw_devices] 0 ]]]]] }  { create_hw_bitstream -hw_device [lindex [get_hw_devices] 0] [get_property PROGRAM.HW_CFGMEM_BITFILE [ lindex [get_hw_devices] 0]]; program_hw_devices [lindex [get_hw_devices] 0]; }; 
program_hw_cfgmem -hw_cfgmem [get_property PROGRAM.HW_CFGMEM [lindex [get_hw_devices] 0 ]]