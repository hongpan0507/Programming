@echo off
set xv_path=C:\\Xilinx\\Vivado\\2016.2\\bin
call %xv_path%/xelab  -wto bb8fc462102944dcb1598696aeca1ab0 -m64 --debug typical --relax --mt 2 -L xil_defaultlib -L xpm -L xbip_utils_v3_0_6 -L c_reg_fd_v12_0_2 -L xbip_dsp48_wrapper_v3_0_4 -L xbip_pipe_v3_0_2 -L xbip_dsp48_addsub_v3_0_2 -L xbip_addsub_v3_0_2 -L c_addsub_v12_0_9 -L c_gate_bit_v12_0_2 -L xbip_counter_v3_0_2 -L c_counter_binary_v12_0_9 -L axi_utils_v2_0_2 -L fir_compiler_v7_2_6 -L lib_cdc_v1_0_2 -L proc_sys_reset_v5_0_9 -L cic_compiler_v4_0_10 -L unisims_ver -L unimacro_ver -L secureip --snapshot sonar_tb_behav xil_defaultlib.sonar_tb xil_defaultlib.glbl -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0
