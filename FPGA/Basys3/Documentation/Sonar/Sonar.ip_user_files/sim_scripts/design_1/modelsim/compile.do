vlib work
vlib msim

vlib msim/xil_defaultlib
vlib msim/xpm
vlib msim/xbip_utils_v3_0_6
vlib msim/axi_utils_v2_0_2
vlib msim/fir_compiler_v7_2_6
vlib msim/lib_cdc_v1_0_2
vlib msim/proc_sys_reset_v5_0_9
vlib msim/cic_compiler_v4_0_10
vlib msim/fifo_generator_v13_1_1
vlib msim/axis_infrastructure_v1_1_0
vlib msim/axis_broadcaster_v1_1_9
vlib msim/axis_register_slice_v1_1_9
vlib msim/axis_switch_v1_1_9

vmap xil_defaultlib msim/xil_defaultlib
vmap xpm msim/xpm
vmap xbip_utils_v3_0_6 msim/xbip_utils_v3_0_6
vmap axi_utils_v2_0_2 msim/axi_utils_v2_0_2
vmap fir_compiler_v7_2_6 msim/fir_compiler_v7_2_6
vmap lib_cdc_v1_0_2 msim/lib_cdc_v1_0_2
vmap proc_sys_reset_v5_0_9 msim/proc_sys_reset_v5_0_9
vmap cic_compiler_v4_0_10 msim/cic_compiler_v4_0_10
vmap fifo_generator_v13_1_1 msim/fifo_generator_v13_1_1
vmap axis_infrastructure_v1_1_0 msim/axis_infrastructure_v1_1_0
vmap axis_broadcaster_v1_1_9 msim/axis_broadcaster_v1_1_9
vmap axis_register_slice_v1_1_9 msim/axis_register_slice_v1_1_9
vmap axis_switch_v1_1_9 msim/axis_switch_v1_1_9

vlog -work xil_defaultlib -64 -incr -sv "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_base.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_dpdistram.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_dprom.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_sdpram.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_spram.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_sprom.sv" \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_tdpram.sv" \

vcom -work xpm -64 -93 \
"C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_VCOMP.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0_drp_to_axi_stream.vhd" \
"../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0_xadc_core_drp.vhd" \
"../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0_axi_xadc.vhd" \

vlog -work xil_defaultlib -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0.v" \
"../../../bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0_clk_wiz.v" \
"../../../bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0.v" \
"../../../bd/design_1/hdl/design_1.v" \

vcom -work xbip_utils_v3_0_6 -64 -93 \
"../../../ipstatic/xbip_utils_v3_0/hdl/xbip_utils_v3_0_vh_rfs.vhd" \

vcom -work axi_utils_v2_0_2 -64 -93 \
"../../../ipstatic/axi_utils_v2_0/hdl/axi_utils_v2_0_vh_rfs.vhd" \

vcom -work fir_compiler_v7_2_6 -64 -93 \
"../../../ipstatic/fir_compiler_v7_2/hdl/fir_compiler_v7_2_vh_rfs.vhd" \
"../../../ipstatic/fir_compiler_v7_2/hdl/fir_compiler_v7_2.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_fir_compiler_0_0/sim/design_1_fir_compiler_0_0.vhd" \

vcom -work lib_cdc_v1_0_2 -64 -93 \
"../../../ipstatic/lib_cdc_v1_0/hdl/src/vhdl/cdc_sync.vhd" \

vcom -work proc_sys_reset_v5_0_9 -64 -93 \
"../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/upcnt_n.vhd" \
"../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/sequence_psr.vhd" \
"../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/lpf.vhd" \
"../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/proc_sys_reset.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_proc_sys_reset_0_0/sim/design_1_proc_sys_reset_0_0.vhd" \

vcom -work cic_compiler_v4_0_10 -64 -93 \
"../../../ipstatic/cic_compiler_v4_0/hdl/cic_compiler_v4_0_vh_rfs.vhd" \
"../../../ipstatic/cic_compiler_v4_0/hdl/cic_compiler_v4_0.vhd" \

vcom -work xil_defaultlib -64 -93 \
"../../../bd/design_1/ip/design_1_cic_compiler_0_0/sim/design_1_cic_compiler_0_0.vhd" \

vlog -work fifo_generator_v13_1_1 -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../ipstatic/fifo_generator_v13_1/simulation/fifo_generator_vlog_beh.v" \

vcom -work fifo_generator_v13_1_1 -64 -93 \
"../../../ipstatic/fifo_generator_v13_1/hdl/fifo_generator_v13_1_rfs.vhd" \

vlog -work fifo_generator_v13_1_1 -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../ipstatic/fifo_generator_v13_1/hdl/fifo_generator_v13_1_rfs.v" \

vlog -work xil_defaultlib -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../bd/design_1/ip/design_1_fifo_generator_0_0/sim/design_1_fifo_generator_0_0.v" \

vlog -work axis_infrastructure_v1_1_0 -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_mux_enc.v" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_aclken_converter.v" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_aclken_converter_wrapper.v" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_axis2vector.v" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_vector2axis.v" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_clock_synchronizer.v" \
"../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_cdc_handshake.v" \

vlog -work xil_defaultlib -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/hdl/tdata_design_1_axis_broadcaster_0_0.v" \
"../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/hdl/tuser_design_1_axis_broadcaster_0_0.v" \

vlog -work axis_broadcaster_v1_1_9 -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../ipstatic/axis_broadcaster_v1_1/hdl/verilog/axis_broadcaster_v1_1_core.v" \

vlog -work xil_defaultlib -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/hdl/top_design_1_axis_broadcaster_0_0.v" \
"../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/sim/design_1_axis_broadcaster_0_0.v" \
"../../../bd/design_1/ip/design_1_fifo_generator_0_1/sim/design_1_fifo_generator_0_1.v" \

vlog -work axis_register_slice_v1_1_9 -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../ipstatic/axis_register_slice_v1_1/hdl/verilog/axis_register_slice_v1_1_axisc_register_slice.v" \
"../../../ipstatic/axis_register_slice_v1_1/hdl/verilog/axis_register_slice_v1_1_axis_register_slice.v" \

vlog -work axis_switch_v1_1_9 -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_arb_rr.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_arb_trr.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axisc_decoder.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axisc_transfer_mux.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axisc_arb_responder.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axis_switch_arbiter.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_dynamic_priority_encoder.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axi_ctrl_read.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axi_ctrl_write.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axi_ctrl_top.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_static_router_config_dp.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_static_router_config.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_static_router.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_reg_bank_16x32.v" \
"../../../ipstatic/axis_switch_v1_1/hdl/verilog/axis_switch_v1_1_axis_switch.v" \

vlog -work xil_defaultlib -64 -incr "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" "+incdir+../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog" "+incdir+../../../ipstatic/clk_wiz_v5_3" \
"../../../bd/design_1/ip/design_1_axis_switch_0_0/sim/design_1_axis_switch_0_0.v" \
"../../../bd/design_1/ip/design_1_axis_switch_0_1/sim/design_1_axis_switch_0_1.v" \
"../../../bd/design_1/ip/design_1_dist_split_0/hdl/tdata_design_1_dist_split_0.v" \
"../../../bd/design_1/ip/design_1_dist_split_0/hdl/tuser_design_1_dist_split_0.v" \
"../../../bd/design_1/ip/design_1_dist_split_0/hdl/top_design_1_dist_split_0.v" \
"../../../bd/design_1/ip/design_1_dist_split_0/sim/design_1_dist_split_0.v" \

vlog -work xil_defaultlib "glbl.v"

