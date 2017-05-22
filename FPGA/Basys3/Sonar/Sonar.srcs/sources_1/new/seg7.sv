// Run-of-the-mill 7-segment encoder, now with negative sign!

module seg7 (
	input  [4:0] bcd ,
	input        dot ,
	output [7:0] seg7
);

	logic [6:0] seg7_i;

	assign seg7 = {seg7_i, ~dot};

	always @(bcd)
		begin
			case (bcd)
				5'h0    : seg7_i = 7'b1000000;
				5'h1    : seg7_i = 7'b1111001;
				5'h2    : seg7_i = 7'b0100100;
				5'h3    : seg7_i = 7'b0110000;
				5'h4    : seg7_i = 7'b0011001;
				5'h5    : seg7_i = 7'b0010010;
				5'h6    : seg7_i = 7'b0000010;
				5'h7    : seg7_i = 7'b1111000;
				5'h8    : seg7_i = 7'b0000000;
				5'h9    : seg7_i = 7'b0011000;
				5'hA    : seg7_i = 7'b0001000;
				5'hB    : seg7_i = 7'b0000011;
				5'hC    : seg7_i = 7'b1000110;
				5'hD    : seg7_i = 7'b0100001;
				5'hE    : seg7_i = 7'b0000110;
				5'hF    : seg7_i = 7'b0001110;
				5'h10   : seg7_i = 7'b0111111; // Negative Sign
				default : seg7_i = 7'b1111111;
			endcase
		end

endmodule