proc start_step { step } {
  set stopFile ".stop.rst"
  if {[file isfile .stop.rst]} {
    puts ""
    puts "*** Halting run - EA reset detected ***"
    puts ""
    puts ""
    return -code error
  }
  set beginFile ".$step.begin.rst"
  set platform "$::tcl_platform(platform)"
  set user "$::tcl_platform(user)"
  set pid [pid]
  set host ""
  if { [string equal $platform unix] } {
    if { [info exist ::env(HOSTNAME)] } {
      set host $::env(HOSTNAME)
    }
  } else {
    if { [info exist ::env(COMPUTERNAME)] } {
      set host $::env(COMPUTERNAME)
    }
  }
  set ch [open $beginFile w]
  puts $ch "<?xml version=\"1.0\"?>"
  puts $ch "<ProcessHandle Version=\"1\" Minor=\"0\">"
  puts $ch "    <Process Command=\".planAhead.\" Owner=\"$user\" Host=\"$host\" Pid=\"$pid\">"
  puts $ch "    </Process>"
  puts $ch "</ProcessHandle>"
  close $ch
}

proc end_step { step } {
  set endFile ".$step.end.rst"
  set ch [open $endFile w]
  close $ch
}

proc step_failed { step } {
  set endFile ".$step.error.rst"
  set ch [open $endFile w]
  close $ch
}


start_step init_design
set rc [catch {
  create_msg_db init_design.pb
  set_param xicom.use_bs_reader 1
  set_property design_mode GateLvl [current_fileset]
  set_param project.singleFileAddWarning.threshold 0
  set_property webtalk.parent_dir W:/Sonar.cache/wt [current_project]
  set_property parent.project_path W:/Sonar.xpr [current_project]
  set_property ip_repo_paths w:/Sonar.cache/ip [current_project]
  set_property ip_output_repo w:/Sonar.cache/ip [current_project]
  set_property XPM_LIBRARIES {XPM_CDC XPM_MEMORY} [current_project]
  add_files -quiet W:/Sonar.runs/synth_1/sonar.dcp
  read_xdc -ref design_1_xadc_wiz_0_0 -cells inst w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0.xdc]
  read_xdc -prop_thru_buffers -ref design_1_clk_wiz_0_0 -cells inst w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0_board.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0_board.xdc]
  read_xdc -ref design_1_clk_wiz_0_0 -cells inst w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0.xdc]
  read_xdc -ref design_1_fir_compiler_0_0 -cells U0 w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_fir_compiler_0_0/fir_compiler_v7_2_6/constraints/fir_compiler_v7_2.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_fir_compiler_0_0/fir_compiler_v7_2_6/constraints/fir_compiler_v7_2.xdc]
  read_xdc -prop_thru_buffers -ref design_1_proc_sys_reset_0_0 -cells U0 w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_proc_sys_reset_0_0/design_1_proc_sys_reset_0_0_board.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_proc_sys_reset_0_0/design_1_proc_sys_reset_0_0_board.xdc]
  read_xdc -ref design_1_proc_sys_reset_0_0 -cells U0 w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_proc_sys_reset_0_0/design_1_proc_sys_reset_0_0.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_proc_sys_reset_0_0/design_1_proc_sys_reset_0_0.xdc]
  read_xdc -ref design_1_fifo_generator_0_0 -cells U0 w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_fifo_generator_0_0/design_1_fifo_generator_0_0/design_1_fifo_generator_0_0.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_fifo_generator_0_0/design_1_fifo_generator_0_0/design_1_fifo_generator_0_0.xdc]
  read_xdc -ref design_1_fifo_generator_0_1 -cells U0 w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_fifo_generator_0_1/design_1_fifo_generator_0_1/design_1_fifo_generator_0_1.xdc
  set_property processing_order EARLY [get_files w:/Sonar.srcs/sources_1/bd/design_1/ip/design_1_fifo_generator_0_1/design_1_fifo_generator_0_1/design_1_fifo_generator_0_1.xdc]
  read_xdc W:/Sonar.srcs/constrs_1/imports/Basys3_Master.xdc
  link_design -top sonar -part xc7a35tcpg236-1
  write_hwdef -file sonar.hwdef
  close_msg_db -file init_design.pb
} RESULT]
if {$rc} {
  step_failed init_design
  return -code error $RESULT
} else {
  end_step init_design
}

start_step opt_design
set rc [catch {
  create_msg_db opt_design.pb
  opt_design 
  write_checkpoint -force sonar_opt.dcp
  report_drc -file sonar_drc_opted.rpt
  close_msg_db -file opt_design.pb
} RESULT]
if {$rc} {
  step_failed opt_design
  return -code error $RESULT
} else {
  end_step opt_design
}

start_step place_design
set rc [catch {
  create_msg_db place_design.pb
  implement_debug_core 
  place_design 
  write_checkpoint -force sonar_placed.dcp
  report_io -file sonar_io_placed.rpt
  report_utilization -file sonar_utilization_placed.rpt -pb sonar_utilization_placed.pb
  report_control_sets -verbose -file sonar_control_sets_placed.rpt
  close_msg_db -file place_design.pb
} RESULT]
if {$rc} {
  step_failed place_design
  return -code error $RESULT
} else {
  end_step place_design
}

start_step route_design
set rc [catch {
  create_msg_db route_design.pb
  route_design 
  write_checkpoint -force sonar_routed.dcp
  report_drc -file sonar_drc_routed.rpt -pb sonar_drc_routed.pb
  report_timing_summary -warn_on_violation -max_paths 10 -file sonar_timing_summary_routed.rpt -rpx sonar_timing_summary_routed.rpx
  report_power -file sonar_power_routed.rpt -pb sonar_power_summary_routed.pb -rpx sonar_power_routed.rpx
  report_route_status -file sonar_route_status.rpt -pb sonar_route_status.pb
  report_clock_utilization -file sonar_clock_utilization_routed.rpt
  close_msg_db -file route_design.pb
} RESULT]
if {$rc} {
  step_failed route_design
  return -code error $RESULT
} else {
  end_step route_design
}

start_step write_bitstream
set rc [catch {
  create_msg_db write_bitstream.pb
  catch { write_mem_info -force sonar.mmi }
  write_bitstream -force sonar.bit -bin_file
  set src_rc [catch { 
    puts "source W:/Sonar.srcs/sources_1/new/program_fpga.tcl"
    source W:/Sonar.srcs/sources_1/new/program_fpga.tcl
  } _RESULT] 
  if {$src_rc} { 
    send_msg_id runtcl-1 error "$_RESULT"
    send_msg_id runtcl-2 error "sourcing script W:/Sonar.srcs/sources_1/new/program_fpga.tcl failed"
    return -code error
  }
  catch { write_sysdef -hwdef sonar.hwdef -bitfile sonar.bit -meminfo sonar.mmi -file sonar.sysdef }
  catch {write_debug_probes -quiet -force debug_nets}
  close_msg_db -file write_bitstream.pb
} RESULT]
if {$rc} {
  step_failed write_bitstream
  return -code error $RESULT
} else {
  end_step write_bitstream
}

