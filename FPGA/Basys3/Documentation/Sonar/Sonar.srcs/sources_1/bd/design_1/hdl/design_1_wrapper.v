//Copyright 1986-2016 Xilinx, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2016.2 (win64) Build 1577090 Thu Jun  2 16:32:40 MDT 2016
//Date        : Tue Oct 25 11:13:16 2016
//Host        : Jtop running 64-bit major release  (build 9200)
//Command     : generate_target design_1_wrapper.bd
//Design      : design_1_wrapper
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

module design_1_wrapper
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

  wire alng_sonar_v_n;
  wire alng_sonar_v_p;
  wire [15:0]cic_rate_tdata;
  wire cic_rate_tready;
  wire cic_rate_tvalid;
  wire clk;
  wire clk_out;
  wire distance_q_primed;
  wire [15:0]distance_q_tdata;
  wire distance_q_tready;
  wire distance_q_tvalid;
  wire [15:0]distance_tdata;
  wire [0:0]distance_tdest;
  wire [4:0]distance_tid;
  wire [0:0]distance_tready;
  wire [0:0]distance_tvalid;
  wire [0:0]no_filter;
  wire pll_reset;
  wire reset;
  wire [0:0]reset_out;
  wire [15:0]velocity_in_tdata;
  wire velocity_in_tready;
  wire velocity_in_tvalid;
  wire velocity_q_primed;
  wire [15:0]velocity_q_tdata;
  wire velocity_q_tready;
  wire velocity_q_tvalid;

  design_1 design_1_i
       (.alng_sonar_v_n(alng_sonar_v_n),
        .alng_sonar_v_p(alng_sonar_v_p),
        .cic_rate_tdata(cic_rate_tdata),
        .cic_rate_tready(cic_rate_tready),
        .cic_rate_tvalid(cic_rate_tvalid),
        .clk(clk),
        .clk_out(clk_out),
        .distance_q_primed(distance_q_primed),
        .distance_q_tdata(distance_q_tdata),
        .distance_q_tready(distance_q_tready),
        .distance_q_tvalid(distance_q_tvalid),
        .distance_tdata(distance_tdata),
        .distance_tdest(distance_tdest),
        .distance_tid(distance_tid),
        .distance_tready(distance_tready),
        .distance_tvalid(distance_tvalid),
        .no_filter(no_filter),
        .pll_reset(pll_reset),
        .reset(reset),
        .reset_out(reset_out),
        .velocity_in_tdata(velocity_in_tdata),
        .velocity_in_tready(velocity_in_tready),
        .velocity_in_tvalid(velocity_in_tvalid),
        .velocity_q_primed(velocity_q_primed),
        .velocity_q_tdata(velocity_q_tdata),
        .velocity_q_tready(velocity_q_tready),
        .velocity_q_tvalid(velocity_q_tvalid));
endmodule
