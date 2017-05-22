
################################################################
# This is a generated script based on design: design_1
#
# Though there are limitations about the generated script,
# the main purpose of this utility is to make learning
# IP Integrator Tcl commands easier.
################################################################

namespace eval _tcl {
proc get_script_folder {} {
   set script_path [file normalize [info script]]
   set script_folder [file dirname $script_path]
   return $script_folder
}
}
variable script_folder
set script_folder [_tcl::get_script_folder]

################################################################
# Check if script is running in correct Vivado version.
################################################################
set scripts_vivado_version 2016.2
set current_vivado_version [version -short]

if { [string first $scripts_vivado_version $current_vivado_version] == -1 } {
   puts ""
   catch {common::send_msg_id "BD_TCL-109" "ERROR" "This script was generated using Vivado <$scripts_vivado_version> and is being run in <$current_vivado_version> of Vivado. Please run the script in Vivado <$scripts_vivado_version> then open the design in Vivado <$current_vivado_version>. Upgrade the design by running \"Tools => Report => Report IP Status...\", then run write_bd_tcl to create an updated script."}

   return 1
}

################################################################
# START
################################################################

# To test this script, run the following commands from Vivado Tcl console:
# source design_1_script.tcl

# If there is no project opened, this script will create a
# project, but make sure you do not have an existing project
# <./myproj/project_1.xpr> in the current working folder.

set list_projs [get_projects -quiet]
if { $list_projs eq "" } {
   create_project project_1 myproj -part xc7a35tcpg236-1
}


# CHANGE DESIGN NAME HERE
set design_name design_1

# If you do not already have an existing IP Integrator design open,
# you can create a design using the following command:
#    create_bd_design $design_name

# Creating design if needed
set errMsg ""
set nRet 0

set cur_design [current_bd_design -quiet]
set list_cells [get_bd_cells -quiet]

if { ${design_name} eq "" } {
   # USE CASES:
   #    1) Design_name not set

   set errMsg "Please set the variable <design_name> to a non-empty value."
   set nRet 1

} elseif { ${cur_design} ne "" && ${list_cells} eq "" } {
   # USE CASES:
   #    2): Current design opened AND is empty AND names same.
   #    3): Current design opened AND is empty AND names diff; design_name NOT in project.
   #    4): Current design opened AND is empty AND names diff; design_name exists in project.

   if { $cur_design ne $design_name } {
      common::send_msg_id "BD_TCL-001" "INFO" "Changing value of <design_name> from <$design_name> to <$cur_design> since current design is empty."
      set design_name [get_property NAME $cur_design]
   }
   common::send_msg_id "BD_TCL-002" "INFO" "Constructing design in IPI design <$cur_design>..."

} elseif { ${cur_design} ne "" && $list_cells ne "" && $cur_design eq $design_name } {
   # USE CASES:
   #    5) Current design opened AND has components AND same names.

   set errMsg "Design <$design_name> already exists in your project, please set the variable <design_name> to another value."
   set nRet 1
} elseif { [get_files -quiet ${design_name}.bd] ne "" } {
   # USE CASES: 
   #    6) Current opened design, has components, but diff names, design_name exists in project.
   #    7) No opened design, design_name exists in project.

   set errMsg "Design <$design_name> already exists in your project, please set the variable <design_name> to another value."
   set nRet 2

} else {
   # USE CASES:
   #    8) No opened design, design_name not in project.
   #    9) Current opened design, has components, but diff names, design_name not in project.

   common::send_msg_id "BD_TCL-003" "INFO" "Currently there is no design <$design_name> in project, so creating one..."

   create_bd_design $design_name

   common::send_msg_id "BD_TCL-004" "INFO" "Making design <$design_name> as current_bd_design."
   current_bd_design $design_name

}

common::send_msg_id "BD_TCL-005" "INFO" "Currently the variable <design_name> is equal to \"$design_name\"."

if { $nRet != 0 } {
   catch {common::send_msg_id "BD_TCL-114" "ERROR" $errMsg}
   return $nRet
}

##################################################################
# DESIGN PROCs
##################################################################



# Procedure to create entire design; Provide argument to make
# procedure reusable. If parentCell is "", will use root.
proc create_root_design { parentCell } {

  variable script_folder

  if { $parentCell eq "" } {
     set parentCell [get_bd_cells /]
  }

  # Get object for parentCell
  set parentObj [get_bd_cells $parentCell]
  if { $parentObj == "" } {
     catch {common::send_msg_id "BD_TCL-100" "ERROR" "Unable to find parent cell <$parentCell>!"}
     return
  }

  # Make sure parentObj is hier blk
  set parentType [get_property TYPE $parentObj]
  if { $parentType ne "hier" } {
     catch {common::send_msg_id "BD_TCL-101" "ERROR" "Parent <$parentObj> has TYPE = <$parentType>. Expected to be <hier>."}
     return
  }

  # Save current instance; Restore later
  set oldCurInst [current_bd_instance .]

  # Set parent object as current
  current_bd_instance $parentObj


  # Create interface ports
  set alng_sonar [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:diff_analog_io_rtl:1.0 alng_sonar ]
  set cic_rate [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:axis_rtl:1.0 cic_rate ]
  set_property -dict [ list \
CONFIG.HAS_TKEEP {0} \
CONFIG.HAS_TLAST {0} \
CONFIG.HAS_TREADY {1} \
CONFIG.HAS_TSTRB {0} \
CONFIG.LAYERED_METADATA {undef} \
CONFIG.TDATA_NUM_BYTES {2} \
CONFIG.TDEST_WIDTH {0} \
CONFIG.TID_WIDTH {0} \
CONFIG.TUSER_WIDTH {0} \
 ] $cic_rate
  set distance [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:axis_rtl:1.0 distance ]
  set distance_q [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:axis_rtl:1.0 distance_q ]
  set velocity_in [ create_bd_intf_port -mode Slave -vlnv xilinx.com:interface:axis_rtl:1.0 velocity_in ]
  set_property -dict [ list \
CONFIG.HAS_TKEEP {0} \
CONFIG.HAS_TLAST {0} \
CONFIG.HAS_TREADY {1} \
CONFIG.HAS_TSTRB {0} \
CONFIG.LAYERED_METADATA {undef} \
CONFIG.TDATA_NUM_BYTES {2} \
CONFIG.TDEST_WIDTH {0} \
CONFIG.TID_WIDTH {0} \
CONFIG.TUSER_WIDTH {0} \
 ] $velocity_in
  set velocity_q [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:axis_rtl:1.0 velocity_q ]

  # Create ports
  set clk [ create_bd_port -dir I -type clk clk ]
  set clk_out [ create_bd_port -dir O -type clk clk_out ]
  set_property -dict [ list \
CONFIG.ASSOCIATED_BUSIF {distance:distance_q:filter_in:adc_out:velocity_in:velocity_q:cic_rate:S00_AXIS} \
 ] $clk_out
  set distance_q_primed [ create_bd_port -dir O distance_q_primed ]
  set no_filter [ create_bd_port -dir I -from 0 -to 0 no_filter ]
  set pll_reset [ create_bd_port -dir I -type rst pll_reset ]
  set_property -dict [ list \
CONFIG.POLARITY {ACTIVE_HIGH} \
 ] $pll_reset
  set reset [ create_bd_port -dir I -type rst reset ]
  set reset_out [ create_bd_port -dir O -from 0 -to 0 -type rst reset_out ]
  set velocity_q_primed [ create_bd_port -dir O velocity_q_primed ]

  # Create instance: ADC, and set properties
  set ADC [ create_bd_cell -type ip -vlnv xilinx.com:ip:xadc_wiz:3.3 ADC ]
  set_property -dict [ list \
CONFIG.ACQUISITION_TIME {4} \
CONFIG.ADC_CONVERSION_RATE {160} \
CONFIG.ADC_OFFSET_CALIBRATION {false} \
CONFIG.BIPOLAR_OPERATION {false} \
CONFIG.CHANNEL_AVERAGING {None} \
CONFIG.CHANNEL_ENABLE_VP_VN {false} \
CONFIG.DCLK_FREQUENCY {100} \
CONFIG.ENABLE_AXI4STREAM {true} \
CONFIG.ENABLE_RESET {true} \
CONFIG.EXTERNAL_MUX_CHANNEL {VP_VN} \
CONFIG.INTERFACE_SELECTION {None} \
CONFIG.OT_ALARM {false} \
CONFIG.POWER_DOWN_ADCB {true} \
CONFIG.SEQUENCER_MODE {Off} \
CONFIG.SINGLE_CHANNEL_ACQUISITION_TIME {false} \
CONFIG.SINGLE_CHANNEL_SELECTION {VAUXP6_VAUXN6} \
CONFIG.STIMULUS_FREQ {10} \
CONFIG.USER_TEMP_ALARM {false} \
CONFIG.VCCAUX_ALARM {false} \
CONFIG.VCCINT_ALARM {false} \
CONFIG.WAVEFORM_TYPE {TRIANGLE} \
CONFIG.XADC_STARUP_SELECTION {single_channel} \
 ] $ADC

  # Need to retain value_src of defaults
  set_property -dict [ list \
CONFIG.DCLK_FREQUENCY.VALUE_SRC {DEFAULT} \
 ] $ADC

  # Create instance: clk_gen, and set properties
  set clk_gen [ create_bd_cell -type ip -vlnv xilinx.com:ip:clk_wiz:5.3 clk_gen ]
  set_property -dict [ list \
CONFIG.CLKOUT1_JITTER {130.958} \
CONFIG.CLKOUT1_PHASE_ERROR {98.575} \
CONFIG.MMCM_CLKFBOUT_MULT_F {10.000} \
CONFIG.MMCM_CLKIN1_PERIOD {10.0} \
CONFIG.MMCM_CLKIN2_PERIOD {10.0} \
CONFIG.MMCM_CLKOUT0_DIVIDE_F {10.000} \
CONFIG.MMCM_COMPENSATION {ZHOLD} \
 ] $clk_gen

  # Need to retain value_src of defaults
  set_property -dict [ list \
CONFIG.CLKOUT1_JITTER.VALUE_SRC {DEFAULT} \
CONFIG.CLKOUT1_PHASE_ERROR.VALUE_SRC {DEFAULT} \
CONFIG.MMCM_CLKFBOUT_MULT_F.VALUE_SRC {DEFAULT} \
CONFIG.MMCM_CLKIN1_PERIOD.VALUE_SRC {DEFAULT} \
CONFIG.MMCM_CLKIN2_PERIOD.VALUE_SRC {DEFAULT} \
CONFIG.MMCM_CLKOUT0_DIVIDE_F.VALUE_SRC {DEFAULT} \
CONFIG.MMCM_COMPENSATION.VALUE_SRC {DEFAULT} \
 ] $clk_gen

  # Create instance: dist_cal, and set properties
  set dist_cal [ create_bd_cell -type ip -vlnv xilinx.com:ip:fir_compiler:7.2 dist_cal ]
  set_property -dict [ list \
CONFIG.BestPrecision {false} \
CONFIG.Clock_Frequency {100.0} \
CONFIG.CoefficientVector {0.0001,   -0.0001,    0.0001,    0.7654,    0.0001,   -0.0001,    0.0001} \
CONFIG.Coefficient_Fractional_Bits {18} \
CONFIG.Coefficient_Sets {1} \
CONFIG.Coefficient_Sign {Signed} \
CONFIG.Coefficient_Structure {Inferred} \
CONFIG.Coefficient_Width {19} \
CONFIG.Filter_Architecture {Systolic_Multiply_Accumulate} \
CONFIG.M_DATA_Has_TREADY {true} \
CONFIG.Output_Rounding_Mode {Convergent_Rounding_to_Even} \
CONFIG.Output_Width {16} \
CONFIG.Quantization {Quantize_Only} \
CONFIG.Sample_Frequency {0.0001} \
 ] $dist_cal

  # Create instance: dist_demux, and set properties
  set dist_demux [ create_bd_cell -type ip -vlnv xilinx.com:ip:axis_switch:1.1 dist_demux ]
  set_property -dict [ list \
CONFIG.DECODER_REG {1} \
CONFIG.NUM_MI {2} \
CONFIG.NUM_SI {1} \
 ] $dist_demux

  # Create instance: dist_downsample, and set properties
  set dist_downsample [ create_bd_cell -type ip -vlnv xilinx.com:ip:cic_compiler:4.0 dist_downsample ]
  set_property -dict [ list \
CONFIG.Clock_Frequency {100} \
CONFIG.Differential_Delay {1} \
CONFIG.Filter_Type {Decimation} \
CONFIG.Fixed_Or_Initial_Rate {7539} \
CONFIG.HAS_DOUT_TREADY {true} \
CONFIG.Input_Sample_Frequency {1} \
CONFIG.Maximum_Rate {7539} \
CONFIG.Minimum_Rate {100} \
CONFIG.Number_Of_Stages {3} \
CONFIG.Output_Data_Width {16} \
CONFIG.Quantization {Truncation} \
CONFIG.SamplePeriod {1} \
CONFIG.Sample_Rate_Changes {Programmable} \
 ] $dist_downsample

  # Create instance: dist_fifo, and set properties
  set dist_fifo [ create_bd_cell -type ip -vlnv xilinx.com:ip:fifo_generator:13.1 dist_fifo ]
  set_property -dict [ list \
CONFIG.Empty_Threshold_Assert_Value_axis {14} \
CONFIG.Empty_Threshold_Assert_Value_rach {14} \
CONFIG.Empty_Threshold_Assert_Value_wach {14} \
CONFIG.Empty_Threshold_Assert_Value_wrch {14} \
CONFIG.FIFO_Implementation_axis {Common_Clock_Distributed_RAM} \
CONFIG.FIFO_Implementation_rach {Common_Clock_Distributed_RAM} \
CONFIG.FIFO_Implementation_wach {Common_Clock_Distributed_RAM} \
CONFIG.FIFO_Implementation_wrch {Common_Clock_Distributed_RAM} \
CONFIG.Full_Flags_Reset_Value {1} \
CONFIG.Full_Threshold_Assert_Value_axis {5} \
CONFIG.Full_Threshold_Assert_Value_rach {15} \
CONFIG.Full_Threshold_Assert_Value_wach {15} \
CONFIG.Full_Threshold_Assert_Value_wrch {15} \
CONFIG.INTERFACE_TYPE {AXI_STREAM} \
CONFIG.Input_Depth_axis {16} \
CONFIG.Programmable_Empty_Type_axis {No_Programmable_Empty_Threshold} \
CONFIG.Programmable_Full_Type_axis {Single_Programmable_Full_Threshold_Constant} \
CONFIG.Reset_Type {Asynchronous_Reset} \
CONFIG.TDATA_NUM_BYTES {2} \
CONFIG.TKEEP_WIDTH {2} \
CONFIG.TSTRB_WIDTH {2} \
CONFIG.TUSER_WIDTH {0} \
 ] $dist_fifo

  # Create instance: dist_mux, and set properties
  set dist_mux [ create_bd_cell -type ip -vlnv xilinx.com:ip:axis_switch:1.1 dist_mux ]
  set_property -dict [ list \
CONFIG.DECODER_REG {0} \
CONFIG.M00_AXIS_HIGHTDEST {0x00000003} \
CONFIG.NUM_MI {1} \
CONFIG.NUM_SI {2} \
 ] $dist_mux

  # Create instance: dist_shift, and set properties
  set dist_shift [ create_bd_cell -type ip -vlnv xilinx.com:ip:axis_broadcaster:1.1 dist_shift ]
  set_property -dict [ list \
CONFIG.M00_TDATA_REMAP {{1'b0, tdata[15:1]}} \
CONFIG.M01_TDATA_REMAP {16'b0} \
 ] $dist_shift

  # Create instance: dist_split, and set properties
  set dist_split [ create_bd_cell -type ip -vlnv xilinx.com:ip:axis_broadcaster:1.1 dist_split ]

  # Create instance: reset_gen, and set properties
  set reset_gen [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 reset_gen ]

  # Create instance: vel_fifo, and set properties
  set vel_fifo [ create_bd_cell -type ip -vlnv xilinx.com:ip:fifo_generator:13.1 vel_fifo ]
  set_property -dict [ list \
CONFIG.Empty_Threshold_Assert_Value_axis {14} \
CONFIG.Empty_Threshold_Assert_Value_rach {14} \
CONFIG.Empty_Threshold_Assert_Value_wach {14} \
CONFIG.Empty_Threshold_Assert_Value_wrch {14} \
CONFIG.FIFO_Implementation_axis {Common_Clock_Distributed_RAM} \
CONFIG.FIFO_Implementation_rach {Common_Clock_Distributed_RAM} \
CONFIG.FIFO_Implementation_wach {Common_Clock_Distributed_RAM} \
CONFIG.FIFO_Implementation_wrch {Common_Clock_Distributed_RAM} \
CONFIG.Full_Flags_Reset_Value {1} \
CONFIG.Full_Threshold_Assert_Value_axis {5} \
CONFIG.Full_Threshold_Assert_Value_rach {15} \
CONFIG.Full_Threshold_Assert_Value_wach {15} \
CONFIG.Full_Threshold_Assert_Value_wrch {15} \
CONFIG.INTERFACE_TYPE {AXI_STREAM} \
CONFIG.Input_Depth_axis {16} \
CONFIG.Programmable_Empty_Type_axis {No_Programmable_Empty_Threshold} \
CONFIG.Programmable_Full_Type_axis {Single_Programmable_Full_Threshold_Constant} \
CONFIG.Reset_Type {Asynchronous_Reset} \
CONFIG.TDATA_NUM_BYTES {2} \
CONFIG.TKEEP_WIDTH {2} \
CONFIG.TSTRB_WIDTH {2} \
CONFIG.TUSER_WIDTH {0} \
 ] $vel_fifo

  # Create interface connections
  connect_bd_intf_net -intf_net ADC_M_AXIS [get_bd_intf_pins ADC/M_AXIS] [get_bd_intf_pins dist_shift/S_AXIS]
  connect_bd_intf_net -intf_net S_AXIS_1 [get_bd_intf_ports velocity_in] [get_bd_intf_pins vel_fifo/S_AXIS]
  connect_bd_intf_net -intf_net Vaux6_1 [get_bd_intf_ports alng_sonar] [get_bd_intf_pins ADC/Vaux6]
  connect_bd_intf_net -intf_net axis_broadcaster_0_M00_AXIS [get_bd_intf_ports distance] [get_bd_intf_pins dist_split/M00_AXIS]
  connect_bd_intf_net -intf_net axis_broadcaster_0_M01_AXIS [get_bd_intf_pins dist_fifo/S_AXIS] [get_bd_intf_pins dist_split/M01_AXIS]
  connect_bd_intf_net -intf_net axis_switch_0_M00_AXIS [get_bd_intf_pins dist_demux/M00_AXIS] [get_bd_intf_pins dist_downsample/S_AXIS_DATA]
  connect_bd_intf_net -intf_net axis_switch_0_M01_AXIS [get_bd_intf_pins dist_demux/M01_AXIS] [get_bd_intf_pins dist_mux/S01_AXIS]
  connect_bd_intf_net -intf_net axis_switch_1_M00_AXIS [get_bd_intf_pins dist_mux/M00_AXIS] [get_bd_intf_pins dist_split/S_AXIS]
  connect_bd_intf_net -intf_net cic_compiler_0_M_AXIS_DATA [get_bd_intf_pins dist_cal/S_AXIS_DATA] [get_bd_intf_pins dist_downsample/M_AXIS_DATA]
  connect_bd_intf_net -intf_net cic_rate_1 [get_bd_intf_ports cic_rate] [get_bd_intf_pins dist_downsample/S_AXIS_CONFIG]
  connect_bd_intf_net -intf_net dist_cal_M_AXIS_DATA [get_bd_intf_pins dist_cal/M_AXIS_DATA] [get_bd_intf_pins dist_mux/S00_AXIS]
  connect_bd_intf_net -intf_net dist_split1_M00_AXIS [get_bd_intf_pins dist_demux/S00_AXIS] [get_bd_intf_pins dist_shift/M00_AXIS]
  connect_bd_intf_net -intf_net fifo_generator_0_M_AXIS [get_bd_intf_ports distance_q] [get_bd_intf_pins dist_fifo/M_AXIS]
  connect_bd_intf_net -intf_net vel_fifo_M_AXIS [get_bd_intf_ports velocity_q] [get_bd_intf_pins vel_fifo/M_AXIS]

  # Create port connections
  connect_bd_net -net Reset_1 [get_bd_ports pll_reset] [get_bd_pins clk_gen/reset]
  connect_bd_net -net clk_in1_1 [get_bd_ports clk] [get_bd_pins clk_gen/clk_in1]
  connect_bd_net -net clk_wiz_0_clk_out1 [get_bd_ports clk_out] [get_bd_pins ADC/m_axis_aclk] [get_bd_pins ADC/s_axis_aclk] [get_bd_pins clk_gen/clk_out1] [get_bd_pins dist_cal/aclk] [get_bd_pins dist_demux/aclk] [get_bd_pins dist_downsample/aclk] [get_bd_pins dist_fifo/s_aclk] [get_bd_pins dist_mux/aclk] [get_bd_pins dist_shift/aclk] [get_bd_pins dist_split/aclk] [get_bd_pins reset_gen/slowest_sync_clk] [get_bd_pins vel_fifo/s_aclk]
  connect_bd_net -net clk_wiz_0_locked [get_bd_pins clk_gen/locked] [get_bd_pins reset_gen/dcm_locked]
  connect_bd_net -net fifo_generator_0_axis_prog_full [get_bd_ports distance_q_primed] [get_bd_pins dist_fifo/axis_prog_full]
  connect_bd_net -net proc_sys_reset_0_peripheral_aresetn [get_bd_pins ADC/m_axis_resetn] [get_bd_pins dist_demux/aresetn] [get_bd_pins dist_fifo/s_aresetn] [get_bd_pins dist_mux/aresetn] [get_bd_pins dist_shift/aresetn] [get_bd_pins dist_split/aresetn] [get_bd_pins reset_gen/peripheral_aresetn] [get_bd_pins vel_fifo/s_aresetn]
  connect_bd_net -net proc_sys_reset_0_peripheral_reset [get_bd_ports reset_out] [get_bd_pins reset_gen/peripheral_reset]
  connect_bd_net -net reset_2 [get_bd_ports reset] [get_bd_pins reset_gen/ext_reset_in]
  connect_bd_net -net s_axis_tdest_1 [get_bd_ports no_filter] [get_bd_pins dist_demux/s_axis_tdest]
  connect_bd_net -net vel_fifo_axis_prog_full [get_bd_ports velocity_q_primed] [get_bd_pins vel_fifo/axis_prog_full]

  # Create address segments

  # Perform GUI Layout
  regenerate_bd_layout -layout_string {
   comment_0: "CIC decimates by large or 
variable amounts efficiently - 
this one decimates to a 
49 ms sampling period",
   comment_1: "FIR can be frequency selective,
but just adjusts gain to produce 
inches right now",
   comment_2: "Give verilog both current and delayed samples
for velocity estimation",
   comment_3: "adc_out produces data at 153.85 kSPS",
   commentid: "comment_0|comment_1|comment_2|comment_3|",
   fillcolor_comment_0: "",
   fillcolor_comment_1: "",
   fillcolor_comment_3: "",
   font_comment_0: "13",
   font_comment_1: "13",
   font_comment_2: "13",
   font_comment_3: "13",
   guistr: "# # String gsaved with Nlview 6.5.12  2016-01-29 bk=1.3547 VDI=39 GEI=35 GUI=JA:1.6
#  -string -flagsOSRD
preplace port pll_reset -pg 1 -y 100 -defaultsOSRD
preplace port distance_q -pg 1 -y 335 -defaultsOSRD
preplace port velocity_q_primed -pg 1 -y 540 -defaultsOSRD
preplace port velocity_in -pg 1 -y 505 -defaultsOSRD
preplace port clk_out -pg 1 -y 440 -defaultsOSRD
preplace port cic_rate -pg 1 -y 320 -defaultsOSRD
preplace port distance -pg 1 -y 415 -defaultsOSRD
preplace port distance_q_primed -pg 1 -y 360 -defaultsOSRD
preplace port clk -pg 1 -y 120 -defaultsOSRD
preplace port velocity_q -pg 1 -y 515 -defaultsOSRD
preplace port alng_sonar -pg 1 -y 200 -defaultsOSRD
preplace port reset -pg 1 -y 50 -defaultsOSRD
preplace portBus no_filter -pg 1 -y 460 -defaultsOSRD
preplace portBus reset_out -pg 1 -y 80 -defaultsOSRD
preplace inst dist_demux -pg 1 -lvl 3 -y 400 -defaultsOSRD
preplace inst dist_shift -pg 1 -lvl 2 -y 390 -defaultsOSRD -resize 240 100
preplace inst dist_split -pg 1 -lvl 7 -y 425 -defaultsOSRD
preplace inst dist_downsample -pg 1 -lvl 4 -y 320 -defaultsOSRD
preplace inst clk_gen -pg 1 -lvl 7 -y 110 -defaultsOSRD
preplace inst dist_mux -pg 1 -lvl 6 -y 415 -defaultsOSRD -resize 200 100
preplace inst reset_gen -pg 1 -lvl 8 -y 80 -defaultsOSRD
preplace inst vel_fifo -pg 1 -lvl 8 -y 525 -defaultsOSRD
preplace inst dist_fifo -pg 1 -lvl 8 -y 345 -defaultsOSRD
preplace inst ADC -pg 1 -lvl 1 -y 220 -defaultsOSRD
preplace inst dist_cal -pg 1 -lvl 5 -y 340 -defaultsOSRD
preplace netloc Vaux6_1 1 0 1 NJ
preplace netloc axis_switch_0_M01_AXIS 1 3 3 N 400 NJ 400 NJ
preplace netloc axis_switch_0_M00_AXIS 1 3 1 900
preplace netloc axis_broadcaster_0_M00_AXIS 1 7 2 NJ 420 NJ
preplace netloc clk_wiz_0_locked 1 7 1 N
preplace netloc fifo_generator_0_axis_prog_full 1 8 1 NJ
preplace netloc clk_in1_1 1 0 7 NJ 110 NJ 110 NJ 110 NJ 110 NJ 110 NJ 110 NJ
preplace netloc fifo_generator_0_M_AXIS 1 8 1 NJ
preplace netloc dist_split1_M00_AXIS 1 2 1 580
preplace netloc ADC_M_AXIS 1 1 1 270
preplace netloc cic_compiler_0_M_AXIS_DATA 1 4 1 1180
preplace netloc axis_broadcaster_0_M01_AXIS 1 7 1 2000
preplace netloc vel_fifo_M_AXIS 1 8 1 NJ
preplace netloc axis_switch_1_M00_AXIS 1 6 1 N
preplace netloc s_axis_tdest_1 1 0 3 NJ 460 NJ 460 NJ
preplace netloc vel_fifo_axis_prog_full 1 8 1 NJ
preplace netloc cic_rate_1 1 0 4 NJ 320 NJ 320 NJ 320 NJ
preplace netloc dist_cal_M_AXIS_DATA 1 5 1 1440
preplace netloc clk_wiz_0_clk_out1 1 0 9 30 120 280 300 590 300 890 390 1180 410 1460 330 1710 330 1990 440 NJ
preplace netloc S_AXIS_1 1 0 8 NJ 500 NJ 500 NJ 500 NJ 500 NJ 500 NJ 500 NJ 500 NJ
preplace netloc proc_sys_reset_0_peripheral_reset 1 8 1 NJ
preplace netloc proc_sys_reset_0_peripheral_aresetn 1 0 9 30 330 290 310 570 310 NJ 420 NJ 420 1450 350 1700 360 2010 430 2340
preplace netloc Reset_1 1 0 7 NJ 90 NJ 90 NJ 90 NJ 90 NJ 90 NJ 90 NJ
preplace netloc reset_2 1 0 8 NJ 50 NJ 50 NJ 50 NJ 50 NJ 50 NJ 50 NJ 50 NJ
preplace cgraphic comment_3 place abs 262 139 textcolor 4 linecolor 3 linewidth 2
preplace cgraphic comment_2 place abs 1965 591 textcolor 4 linecolor 3 linewidth 2
preplace cgraphic comment_1 place abs 1178 232 textcolor 4 linecolor 3 linewidth 2
preplace cgraphic comment_0 place abs 904 189 textcolor 4 linecolor 3 linewidth 2
levelinfo -pg 1 0 150 430 740 1040 1310 1580 1850 2180 2370 -top 0 -bot 600
",
   linecolor_comment_0: "",
   linecolor_comment_1: "",
   linecolor_comment_3: "",
   textcolor_comment_0: "",
   textcolor_comment_1: "",
   textcolor_comment_3: "",
}

  # Restore current instance
  current_bd_instance $oldCurInst

  save_bd_design
}
# End of create_root_design()


##################################################################
# MAIN FLOW
##################################################################

create_root_design ""


