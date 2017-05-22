# 
# Synthesis run script generated by Vivado
# 

set_msg_config -id {HDL 9-1061} -limit 100000
set_msg_config -id {HDL 9-1654} -limit 100000
create_project -in_memory -part xc7a35tcpg236-1

set_param project.singleFileAddWarning.threshold 0
set_param project.compositeFile.enableAutoGeneration 0
set_param synth.vivado.isSynthRun true
set_property webtalk.parent_dir E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.cache/wt [current_project]
set_property parent.project_path E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.xpr [current_project]
set_property default_lib xil_defaultlib [current_project]
set_property target_language Verilog [current_project]
read_verilog -library xil_defaultlib {
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/multi_4_4_pp3.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Binary_to_BCD_B2_bcdout2.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/multi_4_4_pp2.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Divider.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/multi_4_4_pp1.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/multi_4_4_pp0.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Adder_Subtractor.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Binary_to_BCD_B1_bcdout1.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Display_QU.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Seg_7_Display.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Binary_to_BCD_B_bcdout.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Display_REM.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Segment_Scroll.v
  E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/sources_1/imports/Abacus_Verilog_SrcFiles/Basys3_Abacus_Top.v
}
foreach dcp [get_files -quiet -all *.dcp] {
  set_property used_in_implementation false $dcp
}
read_xdc E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/constrs_1/imports/basys3_constrain/Basys3_Master.xdc
set_property used_in_implementation false [get_files E:/Github/Programming/FPGA/Basys3/tutorial1_basys_intro/basys_intro/basys_intro.srcs/constrs_1/imports/basys3_constrain/Basys3_Master.xdc]


synth_design -top Basys3_Abacus_Top -part xc7a35tcpg236-1


write_checkpoint -force -noxdef Basys3_Abacus_Top.dcp

catch { report_utilization -file Basys3_Abacus_Top_utilization_synth.rpt -pb Basys3_Abacus_Top_utilization_synth.pb }
