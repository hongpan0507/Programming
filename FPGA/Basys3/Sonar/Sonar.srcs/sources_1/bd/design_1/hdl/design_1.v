//Copyright 1986-2016 Xilinx, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2016.2 (win64) Build 1577090 Thu Jun  2 16:32:40 MDT 2016
//Date        : Tue Oct 25 11:13:16 2016
//Host        : Jtop running 64-bit major release  (build 9200)
//Command     : generate_target design_1.bd
//Design      : design_1
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CORE_GENERATION_INFO = "design_1,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=design_1,x_ipVersion=1.00.a,x_ipLanguage=VERILOG,numBlks=11,numReposBlks=11,numNonXlnxBlks=0,numHierBlks=0,maxHierDepth=0,numSysgenBlks=0,numHlsBlks=0,numHdlrefBlks=0,numPkgbdBlks=0,bdsource=USER,da_board_cnt=1,synth_mode=Global}" *) (* HW_HANDOFF = "design_1.hwdef" *) 
module design_1
   (alng_sonar_v_n,
    alng_sonar_v_p,
    cic_rate_tdata,
    cic_rate_tready,
    cic_rate_tvalid,
    clk,
    clk_out,
    distance_q_primed,
    distance_q_tdata,
    distance_q_tready,
    distance_q_tvalid,
    distance_tdata,
    distance_tdest,
    distance_tid,
    distance_tready,
    distance_tvalid,
    no_filter,
    pll_reset,
    reset,
    reset_out,
    velocity_in_tdata,
    velocity_in_tready,
    velocity_in_tvalid,
    velocity_q_primed,
    velocity_q_tdata,
    velocity_q_tready,
    velocity_q_tvalid);
  input alng_sonar_v_n;
  input alng_sonar_v_p;
  input [15:0]cic_rate_tdata;
  output cic_rate_tready;
  input cic_rate_tvalid;
  input clk;
  output clk_out;
  output distance_q_primed;
  output [15:0]distance_q_tdata;
  input distance_q_tready;
  output distance_q_tvalid;
  output [15:0]distance_tdata;
  output [0:0]distance_tdest;
  output [4:0]distance_tid;
  input [0:0]distance_tready;
  output [0:0]distance_tvalid;
  input [0:0]no_filter;
  input pll_reset;
  input reset;
  output [0:0]reset_out;
  input [15:0]velocity_in_tdata;
  output velocity_in_tready;
  input velocity_in_tvalid;
  output velocity_q_primed;
  output [15:0]velocity_q_tdata;
  input velocity_q_tready;
  output velocity_q_tvalid;

  wire [15:0]ADC_M_AXIS_TDATA;
  wire [4:0]ADC_M_AXIS_TID;
  wire ADC_M_AXIS_TREADY;
  wire ADC_M_AXIS_TVALID;
  wire Reset_1;
  wire [15:0]S_AXIS_1_TDATA;
  wire S_AXIS_1_TREADY;
  wire S_AXIS_1_TVALID;
  wire Vaux6_1_V_N;
  wire Vaux6_1_V_P;
  wire [15:0]axis_broadcaster_0_M00_AXIS_TDATA;
  wire [0:0]axis_broadcaster_0_M00_AXIS_TDEST;
  wire [4:0]axis_broadcaster_0_M00_AXIS_TID;
  wire [0:0]axis_broadcaster_0_M00_AXIS_TREADY;
  wire [0:0]axis_broadcaster_0_M00_AXIS_TVALID;
  wire [31:16]axis_broadcaster_0_M01_AXIS_TDATA;
  wire axis_broadcaster_0_M01_AXIS_TREADY;
  wire [1:1]axis_broadcaster_0_M01_AXIS_TVALID;
  wire [15:0]axis_switch_0_M00_AXIS_TDATA;
  wire axis_switch_0_M00_AXIS_TREADY;
  wire [0:0]axis_switch_0_M00_AXIS_TVALID;
  wire [31:16]axis_switch_0_M01_AXIS_TDATA;
  wire [1:1]axis_switch_0_M01_AXIS_TDEST;
  wire [9:5]axis_switch_0_M01_AXIS_TID;
  wire [1:1]axis_switch_0_M01_AXIS_TREADY;
  wire [1:1]axis_switch_0_M01_AXIS_TVALID;
  wire [15:0]axis_switch_1_M00_AXIS_TDATA;
  wire [0:0]axis_switch_1_M00_AXIS_TDEST;
  wire [4:0]axis_switch_1_M00_AXIS_TID;
  wire axis_switch_1_M00_AXIS_TREADY;
  wire [0:0]axis_switch_1_M00_AXIS_TVALID;
  wire [15:0]cic_compiler_0_M_AXIS_DATA_TDATA;
  wire cic_compiler_0_M_AXIS_DATA_TREADY;
  wire cic_compiler_0_M_AXIS_DATA_TVALID;
  wire [15:0]cic_rate_1_TDATA;
  wire cic_rate_1_TREADY;
  wire cic_rate_1_TVALID;
  wire clk_in1_1;
  wire clk_wiz_0_clk_out1;
  wire clk_wiz_0_locked;
  wire [15:0]dist_cal_M_AXIS_DATA_TDATA;
  wire [0:0]dist_cal_M_AXIS_DATA_TREADY;
  wire dist_cal_M_AXIS_DATA_TVALID;
  wire [15:0]dist_split1_M00_AXIS_TDATA;
  wire [4:0]dist_split1_M00_AXIS_TID;
  wire [0:0]dist_split1_M00_AXIS_TREADY;
  wire [0:0]dist_split1_M00_AXIS_TVALID;
  wire [15:0]fifo_generator_0_M_AXIS_TDATA;
  wire fifo_generator_0_M_AXIS_TREADY;
  wire fifo_generator_0_M_AXIS_TVALID;
  wire fifo_generator_0_axis_prog_full;
  wire [0:0]proc_sys_reset_0_peripheral_aresetn;
  wire [0:0]proc_sys_reset_0_peripheral_reset;
  wire reset_2;
  wire [0:0]s_axis_tdest_1;
  wire [15:0]vel_fifo_M_AXIS_TDATA;
  wire vel_fifo_M_AXIS_TREADY;
  wire vel_fifo_M_AXIS_TVALID;
  wire vel_fifo_axis_prog_full;
  wire [1:0]NLW_dist_demux_m_axis_tdest_UNCONNECTED;
  wire [9:0]NLW_dist_demux_m_axis_tid_UNCONNECTED;

  assign Reset_1 = pll_reset;
  assign S_AXIS_1_TDATA = velocity_in_tdata[15:0];
  assign S_AXIS_1_TVALID = velocity_in_tvalid;
  assign Vaux6_1_V_N = alng_sonar_v_n;
  assign Vaux6_1_V_P = alng_sonar_v_p;
  assign axis_broadcaster_0_M00_AXIS_TREADY = distance_tready[0];
  assign cic_rate_1_TDATA = cic_rate_tdata[15:0];
  assign cic_rate_1_TVALID = cic_rate_tvalid;
  assign cic_rate_tready = cic_rate_1_TREADY;
  assign clk_in1_1 = clk;
  assign clk_out = clk_wiz_0_clk_out1;
  assign distance_q_primed = fifo_generator_0_axis_prog_full;
  assign distance_q_tdata[15:0] = fifo_generator_0_M_AXIS_TDATA;
  assign distance_q_tvalid = fifo_generator_0_M_AXIS_TVALID;
  assign distance_tdata[15:0] = axis_broadcaster_0_M00_AXIS_TDATA;
  assign distance_tdest[0] = axis_broadcaster_0_M00_AXIS_TDEST;
  assign distance_tid[4:0] = axis_broadcaster_0_M00_AXIS_TID;
  assign distance_tvalid[0] = axis_broadcaster_0_M00_AXIS_TVALID;
  assign fifo_generator_0_M_AXIS_TREADY = distance_q_tready;
  assign reset_2 = reset;
  assign reset_out[0] = proc_sys_reset_0_peripheral_reset;
  assign s_axis_tdest_1 = no_filter[0];
  assign vel_fifo_M_AXIS_TREADY = velocity_q_tready;
  assign velocity_in_tready = S_AXIS_1_TREADY;
  assign velocity_q_primed = vel_fifo_axis_prog_full;
  assign velocity_q_tdata[15:0] = vel_fifo_M_AXIS_TDATA;
  assign velocity_q_tvalid = vel_fifo_M_AXIS_TVALID;
  design_1_xadc_wiz_0_0 ADC
       (.m_axis_aclk(clk_wiz_0_clk_out1),
        .m_axis_resetn(proc_sys_reset_0_peripheral_aresetn),
        .m_axis_tdata(ADC_M_AXIS_TDATA),
        .m_axis_tid(ADC_M_AXIS_TID),
        .m_axis_tready(ADC_M_AXIS_TREADY),
        .m_axis_tvalid(ADC_M_AXIS_TVALID),
        .s_axis_aclk(clk_wiz_0_clk_out1),
        .vauxn6(Vaux6_1_V_N),
        .vauxp6(Vaux6_1_V_P),
        .vn_in(1'b0),
        .vp_in(1'b0));
  design_1_clk_wiz_0_0 clk_gen
       (.clk_in1(clk_in1_1),
        .clk_out1(clk_wiz_0_clk_out1),
        .locked(clk_wiz_0_locked),
        .reset(Reset_1));
  design_1_fir_compiler_0_0 dist_cal
       (.aclk(clk_wiz_0_clk_out1),
        .m_axis_data_tdata(dist_cal_M_AXIS_DATA_TDATA),
        .m_axis_data_tready(dist_cal_M_AXIS_DATA_TREADY),
        .m_axis_data_tvalid(dist_cal_M_AXIS_DATA_TVALID),
        .s_axis_data_tdata(cic_compiler_0_M_AXIS_DATA_TDATA),
        .s_axis_data_tready(cic_compiler_0_M_AXIS_DATA_TREADY),
        .s_axis_data_tvalid(cic_compiler_0_M_AXIS_DATA_TVALID));
  design_1_axis_switch_0_0 dist_demux
       (.aclk(clk_wiz_0_clk_out1),
        .aresetn(proc_sys_reset_0_peripheral_aresetn),
        .m_axis_tdata({axis_switch_0_M01_AXIS_TDATA,axis_switch_0_M00_AXIS_TDATA}),
        .m_axis_tdest({axis_switch_0_M01_AXIS_TDEST,NLW_dist_demux_m_axis_tdest_UNCONNECTED[0]}),
        .m_axis_tid({axis_switch_0_M01_AXIS_TID,NLW_dist_demux_m_axis_tid_UNCONNECTED[4:0]}),
        .m_axis_tready({axis_switch_0_M01_AXIS_TREADY,axis_switch_0_M00_AXIS_TREADY}),
        .m_axis_tvalid({axis_switch_0_M01_AXIS_TVALID,axis_switch_0_M00_AXIS_TVALID}),
        .s_axis_tdata(dist_split1_M00_AXIS_TDATA),
        .s_axis_tdest(s_axis_tdest_1),
        .s_axis_tid(dist_split1_M00_AXIS_TID),
        .s_axis_tready(dist_split1_M00_AXIS_TREADY),
        .s_axis_tvalid(dist_split1_M00_AXIS_TVALID));
  design_1_cic_compiler_0_0 dist_downsample
       (.aclk(clk_wiz_0_clk_out1),
        .m_axis_data_tdata(cic_compiler_0_M_AXIS_DATA_TDATA),
        .m_axis_data_tready(cic_compiler_0_M_AXIS_DATA_TREADY),
        .m_axis_data_tvalid(cic_compiler_0_M_AXIS_DATA_TVALID),
        .s_axis_config_tdata(cic_rate_1_TDATA),
        .s_axis_config_tready(cic_rate_1_TREADY),
        .s_axis_config_tvalid(cic_rate_1_TVALID),
        .s_axis_data_tdata(axis_switch_0_M00_AXIS_TDATA),
        .s_axis_data_tready(axis_switch_0_M00_AXIS_TREADY),
        .s_axis_data_tvalid(axis_switch_0_M00_AXIS_TVALID));
  design_1_fifo_generator_0_0 dist_fifo
       (.axis_prog_full(fifo_generator_0_axis_prog_full),
        .m_axis_tdata(fifo_generator_0_M_AXIS_TDATA),
        .m_axis_tready(fifo_generator_0_M_AXIS_TREADY),
        .m_axis_tvalid(fifo_generator_0_M_AXIS_TVALID),
        .s_aclk(clk_wiz_0_clk_out1),
        .s_aresetn(proc_sys_reset_0_peripheral_aresetn),
        .s_axis_tdata(axis_broadcaster_0_M01_AXIS_TDATA),
        .s_axis_tready(axis_broadcaster_0_M01_AXIS_TREADY),
        .s_axis_tvalid(axis_broadcaster_0_M01_AXIS_TVALID));
  design_1_axis_switch_0_1 dist_mux
       (.aclk(clk_wiz_0_clk_out1),
        .aresetn(proc_sys_reset_0_peripheral_aresetn),
        .m_axis_tdata(axis_switch_1_M00_AXIS_TDATA),
        .m_axis_tdest(axis_switch_1_M00_AXIS_TDEST),
        .m_axis_tid(axis_switch_1_M00_AXIS_TID),
        .m_axis_tready(axis_switch_1_M00_AXIS_TREADY),
        .m_axis_tvalid(axis_switch_1_M00_AXIS_TVALID),
        .s_axis_tdata({axis_switch_0_M01_AXIS_TDATA,dist_cal_M_AXIS_DATA_TDATA}),
        .s_axis_tdest({axis_switch_0_M01_AXIS_TDEST,1'b0}),
        .s_axis_tid({axis_switch_0_M01_AXIS_TID,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .s_axis_tready({axis_switch_0_M01_AXIS_TREADY,dist_cal_M_AXIS_DATA_TREADY}),
        .s_axis_tvalid({axis_switch_0_M01_AXIS_TVALID,dist_cal_M_AXIS_DATA_TVALID}),
        .s_req_suppress({1'b0,1'b0}));
  design_1_dist_split_0 dist_shift
       (.aclk(clk_wiz_0_clk_out1),
        .aresetn(proc_sys_reset_0_peripheral_aresetn),
        .m_axis_tdata(dist_split1_M00_AXIS_TDATA),
        .m_axis_tid(dist_split1_M00_AXIS_TID),
        .m_axis_tready({1'b1,dist_split1_M00_AXIS_TREADY}),
        .m_axis_tvalid(dist_split1_M00_AXIS_TVALID),
        .s_axis_tdata(ADC_M_AXIS_TDATA),
        .s_axis_tid(ADC_M_AXIS_TID),
        .s_axis_tready(ADC_M_AXIS_TREADY),
        .s_axis_tvalid(ADC_M_AXIS_TVALID));
  design_1_axis_broadcaster_0_0 dist_split
       (.aclk(clk_wiz_0_clk_out1),
        .aresetn(proc_sys_reset_0_peripheral_aresetn),
        .m_axis_tdata({axis_broadcaster_0_M01_AXIS_TDATA,axis_broadcaster_0_M00_AXIS_TDATA}),
        .m_axis_tdest(axis_broadcaster_0_M00_AXIS_TDEST),
        .m_axis_tid(axis_broadcaster_0_M00_AXIS_TID),
        .m_axis_tready({axis_broadcaster_0_M01_AXIS_TREADY,axis_broadcaster_0_M00_AXIS_TREADY}),
        .m_axis_tvalid({axis_broadcaster_0_M01_AXIS_TVALID,axis_broadcaster_0_M00_AXIS_TVALID}),
        .s_axis_tdata(axis_switch_1_M00_AXIS_TDATA),
        .s_axis_tdest(axis_switch_1_M00_AXIS_TDEST),
        .s_axis_tid(axis_switch_1_M00_AXIS_TID),
        .s_axis_tready(axis_switch_1_M00_AXIS_TREADY),
        .s_axis_tvalid(axis_switch_1_M00_AXIS_TVALID));
  design_1_proc_sys_reset_0_0 reset_gen
       (.aux_reset_in(1'b1),
        .dcm_locked(clk_wiz_0_locked),
        .ext_reset_in(reset_2),
        .mb_debug_sys_rst(1'b0),
        .peripheral_aresetn(proc_sys_reset_0_peripheral_aresetn),
        .peripheral_reset(proc_sys_reset_0_peripheral_reset),
        .slowest_sync_clk(clk_wiz_0_clk_out1));
  design_1_fifo_generator_0_1 vel_fifo
       (.axis_prog_full(vel_fifo_axis_prog_full),
        .m_axis_tdata(vel_fifo_M_AXIS_TDATA),
        .m_axis_tready(vel_fifo_M_AXIS_TREADY),
        .m_axis_tvalid(vel_fifo_M_AXIS_TVALID),
        .s_aclk(clk_wiz_0_clk_out1),
        .s_aresetn(proc_sys_reset_0_peripheral_aresetn),
        .s_axis_tdata(S_AXIS_1_TDATA),
        .s_axis_tready(S_AXIS_1_TREADY),
        .s_axis_tvalid(S_AXIS_1_TVALID));
endmodule
