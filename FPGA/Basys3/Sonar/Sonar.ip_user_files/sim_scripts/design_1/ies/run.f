-makelib ies/xil_defaultlib -sv \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_base.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_dpdistram.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_dprom.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_sdpram.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_spram.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_sprom.sv" \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_memory/hdl/xpm_memory_tdpram.sv" \
-endlib
-makelib ies/xpm \
  "C:/Xilinx/Vivado/2016.2/data/ip/xpm/xpm_VCOMP.vhd" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0_drp_to_axi_stream.vhd" \
  "../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0_xadc_core_drp.vhd" \
  "../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0_axi_xadc.vhd" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_xadc_wiz_0_0/design_1_xadc_wiz_0_0.v" \
  "../../../bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0_clk_wiz.v" \
  "../../../bd/design_1/ip/design_1_clk_wiz_0_0/design_1_clk_wiz_0_0.v" \
  "../../../bd/design_1/hdl/design_1.v" \
-endlib
-makelib ies/xbip_utils_v3_0_6 \
  "../../../ipstatic/xbip_utils_v3_0/hdl/xbip_utils_v3_0_vh_rfs.vhd" \
-endlib
-makelib ies/axi_utils_v2_0_2 \
  "../../../ipstatic/axi_utils_v2_0/hdl/axi_utils_v2_0_vh_rfs.vhd" \
-endlib
-makelib ies/fir_compiler_v7_2_6 \
  "../../../ipstatic/fir_compiler_v7_2/hdl/fir_compiler_v7_2_vh_rfs.vhd" \
  "../../../ipstatic/fir_compiler_v7_2/hdl/fir_compiler_v7_2.vhd" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_fir_compiler_0_0/sim/design_1_fir_compiler_0_0.vhd" \
-endlib
-makelib ies/lib_cdc_v1_0_2 \
  "../../../ipstatic/lib_cdc_v1_0/hdl/src/vhdl/cdc_sync.vhd" \
-endlib
-makelib ies/proc_sys_reset_v5_0_9 \
  "../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/upcnt_n.vhd" \
  "../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/sequence_psr.vhd" \
  "../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/lpf.vhd" \
  "../../../ipstatic/proc_sys_reset_v5_0/hdl/src/vhdl/proc_sys_reset.vhd" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_proc_sys_reset_0_0/sim/design_1_proc_sys_reset_0_0.vhd" \
-endlib
-makelib ies/cic_compiler_v4_0_10 \
  "../../../ipstatic/cic_compiler_v4_0/hdl/cic_compiler_v4_0_vh_rfs.vhd" \
  "../../../ipstatic/cic_compiler_v4_0/hdl/cic_compiler_v4_0.vhd" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_cic_compiler_0_0/sim/design_1_cic_compiler_0_0.vhd" \
-endlib
-makelib ies/fifo_generator_v13_1_1 \
  "../../../ipstatic/fifo_generator_v13_1/simulation/fifo_generator_vlog_beh.v" \
-endlib
-makelib ies/fifo_generator_v13_1_1 \
  "../../../ipstatic/fifo_generator_v13_1/hdl/fifo_generator_v13_1_rfs.vhd" \
-endlib
-makelib ies/fifo_generator_v13_1_1 \
  "../../../ipstatic/fifo_generator_v13_1/hdl/fifo_generator_v13_1_rfs.v" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_fifo_generator_0_0/sim/design_1_fifo_generator_0_0.v" \
-endlib
-makelib ies/axis_infrastructure_v1_1_0 \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_mux_enc.v" \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_aclken_converter.v" \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_aclken_converter_wrapper.v" \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_axis2vector.v" \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_util_vector2axis.v" \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_clock_synchronizer.v" \
  "../../../ipstatic/axis_infrastructure_v1_1/hdl/verilog/axis_infrastructure_v1_1_cdc_handshake.v" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/hdl/tdata_design_1_axis_broadcaster_0_0.v" \
  "../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/hdl/tuser_design_1_axis_broadcaster_0_0.v" \
-endlib
-makelib ies/axis_broadcaster_v1_1_9 \
  "../../../ipstatic/axis_broadcaster_v1_1/hdl/verilog/axis_broadcaster_v1_1_core.v" \
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/hdl/top_design_1_axis_broadcaster_0_0.v" \
  "../../../bd/design_1/ip/design_1_axis_broadcaster_0_0/sim/design_1_axis_broadcaster_0_0.v" \
  "../../../bd/design_1/ip/design_1_fifo_generator_0_1/sim/design_1_fifo_generator_0_1.v" \
-endlib
-makelib ies/axis_register_slice_v1_1_9 \
  "../../../ipstatic/axis_register_slice_v1_1/hdl/verilog/axis_register_slice_v1_1_axisc_register_slice.v" \
  "../../../ipstatic/axis_register_slice_v1_1/hdl/verilog/axis_register_slice_v1_1_axis_register_slice.v" \
-endlib
-makelib ies/axis_switch_v1_1_9 \
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
-endlib
-makelib ies/xil_defaultlib \
  "../../../bd/design_1/ip/design_1_axis_switch_0_0/sim/design_1_axis_switch_0_0.v" \
  "../../../bd/design_1/ip/design_1_axis_switch_0_1/sim/design_1_axis_switch_0_1.v" \
  "../../../bd/design_1/ip/design_1_dist_split_0/hdl/tdata_design_1_dist_split_0.v" \
  "../../../bd/design_1/ip/design_1_dist_split_0/hdl/tuser_design_1_dist_split_0.v" \
  "../../../bd/design_1/ip/design_1_dist_split_0/hdl/top_design_1_dist_split_0.v" \
  "../../../bd/design_1/ip/design_1_dist_split_0/sim/design_1_dist_split_0.v" \
-endlib
-makelib ies/xil_defaultlib \
  glbl.v
-endlib

