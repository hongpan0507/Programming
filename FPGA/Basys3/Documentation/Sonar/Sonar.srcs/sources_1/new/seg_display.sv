`timescale 1ns / 1ps

module seg_display (
	input             clk        ,
	input             reset      ,
	input      [15:0] measurement,
	input             meas_is_neg,
	input             bleedover,
	input      [31:0] update_cycles,
	output reg [ 3:0] seg_sel    ,
	output reg [ 7:0] seg
);

	logic [ 4:0] curr_bcd          ;
	logic [ 1:0] curr_seg          ;
	logic [ 1:0] next_seg          ;
	logic [ 1:0] seg_enabled       ;
	logic [ 4:0] bcd          [3:0]; // Raw digits
	logic [ 4:0] formatted_bcd[3:0]; // Removed leading zeros, negative sign, etc
	logic [ 7:0] seg7              ;
	logic [ 3:0] seg_sel_last      ;
	logic [ 3:0] seg_sel_d         ;
	logic [31:0] count             ;

	// Create segment update timing
	always  @(posedge clk)
		begin
			if (reset) begin
				count       <= 0;
				curr_seg    <= 0;
				seg_enabled <= 0;
			end else begin
				if (count >= update_cycles) begin
					curr_seg <= curr_seg + 1;
					count    <= 0;
				end else begin
					count <= count + 1;
				end

				// Disable 7-seg output for a bit when changing digits so we don't bleed over
				if (count <= 1024)
					seg_enabled <= 0;
				else if (count >= update_cycles - 16)
					seg_enabled <= 0;
				else
					seg_enabled <= 1;
			end
		end

	// Convert from raw BCD to nicely formatted display
	function [3:0] [4:0] getFormattedDigits;
		input logic [4:0] bcd [3:0];
		input logic is_neg;
		logic found_leading_digit = 0;
		integer i;
		begin
			// Go from left-most digit rightwards, remove leading zeros, and add negative sign
			for (i=3; i>0; i=i-1) begin
				if (bcd[i] == 0 && !found_leading_digit) begin // Suppress leading zeros
					if(bcd[i-1] != 0 && is_neg)
						getFormattedDigits[i] = 5'h10; // Show negative sign if appropriate
					else
						getFormattedDigits[i] = 5'h1F; // Show nothing otherwise
				end else begin
					getFormattedDigits[i] = bcd[i];
					found_leading_digit   = 1;
				end
			end
			getFormattedDigits[0] = bcd[0]; // First digit always displayed
		end
	endfunction

	// Multiplex seven-segment digits according to current digit
	always  @(posedge clk)
		begin
			if (reset) begin
				seg_sel_last  <= 0;
				seg_sel_d     <= 0;
				seg_sel       <= 0;
				seg           <= 0;
				curr_bcd      <= 0;
				formatted_bcd <= '{4{5'b0}};
			end else begin
				// Get formatted digits
				{>> {formatted_bcd} } <= getFormattedDigits(bcd, meas_is_neg);

				// Cycle through digits for 7-segment display
				case (curr_seg)
					2'h0 : begin
						seg_sel_last <= 'b0111;
						seg_sel_d <= 'b1110;
						curr_bcd  <= formatted_bcd[0];
					end
					2'h1 : begin
						seg_sel_last <= 'b1110;
						seg_sel_d <= 'b1101;
						curr_bcd  <= formatted_bcd[1];
					end
					2'h2 : begin
						seg_sel_last <= 'b1101;
						seg_sel_d <= 'b1011;
						curr_bcd  <= formatted_bcd[2];
					end
					2'h3 : begin
						seg_sel_last <= 'b1011;
						seg_sel_d <= 'b0111;
						curr_bcd  <= formatted_bcd[3];
					end
					default : begin
						seg_sel_d <= 'b1111;
						curr_bcd  <= 5'h1F;
					end
				endcase

				// Turn off all digits when requested
				if (seg_enabled)
					seg_sel <= seg_sel_d;
				else begin
					if (!bleedover)
						seg_sel <= 'hF;
					else
						seg_sel <= seg_sel_last;
				end
				seg <= seg7;
			end

		end

	// Decode distance into digits
	bcd bcd_decoder (
		.clk      (clk        ),
		.number   (measurement),
		.thousands(bcd[3]     ),
		.hundreds (bcd[2]     ),
		.tens     (bcd[1]     ),
		.ones     (bcd[0]     )
	);

	// Decode digits into 7-segment display
	seg7 seg7_decoder (
		.bcd (curr_bcd),
		.dot (0       ),
		.seg7(seg7    )
	);

endmodule
