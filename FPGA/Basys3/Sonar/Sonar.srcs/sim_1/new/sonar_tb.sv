`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/25/2016 03:18:02 PM
// Design Name: 
// Module Name: sonar_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module sonar_tb(

    );
logic clk;

sonar sonar_i (
	.clk    (clk),
	.XADC_p (0),
	.XADC_n (0),
	.btn    (0),
	.seg_sel(),
	.seg    (),
	.led    (),
	.UART_RX()
);


	initial begin
		clk = 0;
	end

	initial begin
		clk = 0;
		forever begin
			#5 clk = 0;
			#5 clk = 1;
		end
	end


endmodule
