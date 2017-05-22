onbreak {quit -f}
onerror {quit -f}

vsim -voptargs="+acc" -t 1ps -L unisims_ver -L unimacro_ver -L secureip -L xil_defaultlib -L xpm -L xbip_utils_v3_0_6 -L axi_utils_v2_0_2 -L fir_compiler_v7_2_6 -L lib_cdc_v1_0_2 -L proc_sys_reset_v5_0_9 -L cic_compiler_v4_0_10 -L fifo_generator_v13_1_1 -L axis_infrastructure_v1_1_0 -L axis_broadcaster_v1_1_9 -L axis_register_slice_v1_1_9 -L axis_switch_v1_1_9 -lib xil_defaultlib xil_defaultlib.design_1 xil_defaultlib.glbl

do {wave.do}

view wave
view structure
view signals

do {design_1.udo}

run -all

quit -force
