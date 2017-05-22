`timescale 1ns / 1ps

module sonar #(
	parameter CLK_HZ = 100_000_000
) (
	input             clk    ,
	// Sonar module connections
	input             XADC_p ,
	input             XADC_n ,
	output            UART_RX,
	// User inputs
	input      [ 4:0] btn    ,
	input      [15:0] sw     ,
	// User outputs
	output reg [ 3:0] seg_sel,
	output reg [ 7:0] seg    ,
	output reg [15:0] led    
);

	logic               clk_out          ; // Buffered clock from block design
	logic               reset            ;

	logic        [15:0] cic_rate         ;
	logic        [15:0] cic_rate_q       ;
	logic               cic_rate_update  ;

	// Distance interface
	logic               distance_tvalid  ;
	logic signed [15:0] distance_tdata   ;
	logic signed [16:0] distance         ;

	// Derived velocity and acceleration variables
	logic signed [15:0] distance_q       ;
	logic               distance_q_primed;
	logic               velocity_tvalid  ;
	logic               velocity_q_tvalid;
	logic               velocity_q_primed;
	logic signed [15:0] velocity         ;
	logic signed [15:0] velocity_q       ;
	logic signed [15:0] acceleration     ;

	// 7-segment character
	logic        [15:0] measurement      ;
	logic               meas_is_neg      ;
	logic        [31:0] update_cycles    ;

	// LED bar
	logic        [ 7:0] led_bar          ;
	logic signed [ 7:0] led_bar_signed   ;
	logic               led_signed_mode  ;

	// Samples per second calculation
	logic        [31:0] count             ;
	logic        [16:0] adc_sample_count  ;
	logic        [16:0] sample_count      ;
	logic               sample_count_reset;
	logic        [ 7:0] samps             ;


	assign UART_RX   = 1'bZ; // MUST BE SET TO Z OR 1 ENABLE SONAR

	design_1 block_design (
		.clk               (clk               ),
		.clk_out           (clk_out           ),
		.pll_reset         (0                 ), // Never reset PLL, assume input clock always present
		.reset             (~btn[0]           ), // Center button BTNC resets everything
		.reset_out         (reset             ),
		.alng_sonar_v_p    (XADC_p            ),
		.alng_sonar_v_n    (XADC_n            ), // MUST BE GROUNDED
		.no_filter         (sw[15]            ),
        .cic_rate_tdata    (cic_rate          ),
        .cic_rate_tvalid   (cic_rate_update   ),
		
		.distance_tdata    (distance_tdata    ),
		.distance_tready   (1                 ), // Always ready for new samples
		.distance_tvalid   (distance_tvalid   ),
		.distance_q_tdata  (distance_q        ),
		.distance_q_tready (distance_q_primed ),
		.distance_q_primed (distance_q_primed ),
		
		.velocity_in_tdata (velocity          ),
		.velocity_in_tready(1                 ),
		.velocity_in_tvalid(velocity_tvalid   ),
		.velocity_q_primed (velocity_q_primed ),
		.velocity_q_tready (velocity_q_primed ),
		.velocity_q_tdata  (velocity_q        ),
		.velocity_q_tvalid (velocity_q_tvalid )
	);


	seg_display #(
		) seg_display_i (
		.clk        (clk_out    ),
		.reset      (reset      ),
		.measurement(measurement),
		.meas_is_neg(meas_is_neg),
		.seg_sel    (seg_sel    ),
		.seg        (seg        ),
		.update_cycles(update_cycles),
		.bleedover  (sw[12]     )
	);

	// Capture distance, velocity, and acceleration
	always  @(posedge clk_out)
		begin
			if (reset) begin
				distance        <= 0;
				velocity        <= 0;
				velocity_tvalid <= 0;
				acceleration    <= 0;
				sample_count    <= 0;
			end else begin

				velocity_tvalid <= 0;
				// Get distance from block design and feed velocity back in
				if (distance_tvalid) begin
					distance        <= distance_tdata;
					velocity        <= distance_tdata - distance_q;
					velocity_tvalid <= 1;
					sample_count    <= sample_count + 1;
				end 
				// Calculate acceleration from stored velocity
				if (velocity_q_tvalid) begin
					acceleration    <= velocity - velocity_q;
				end
				if (sample_count_reset)
					sample_count <= 0;
			end
		end

	// Choose which measurement goes to displays
	always  @(posedge clk_out)
		begin
			if (reset) begin
				measurement     <= 0;
				meas_is_neg     <= 0;
				led_signed_mode <= 0;
			end else begin

				// Mux different measurement types to outputs based on switches
				case (sw[3:0])
					0 : begin // Show Distance
						if (distance >= 0) begin
							measurement <= distance>>7;
							meas_is_neg <= 0;
						end else begin
							measurement <= (-distance)>>7;
							meas_is_neg <= 1;
						end
						led_bar         <= measurement>>3;
						led_signed_mode <= 0;
					end
					1 : begin // Show Velocity
						if (velocity >= 0) begin
							measurement <= velocity>>4;
							meas_is_neg <= 0;
						end else begin
							measurement <= (-velocity)>>4;
							meas_is_neg <= 1;
						end
						led_bar         <= (velocity + 16'sh40)>>>7;
						led_signed_mode <= 1;
					end
					2 : begin // Show Acceleration
						if (acceleration >= 0) begin
							measurement <= acceleration>>4;
							meas_is_neg <= 0;
						end else begin
							measurement <= (-acceleration)>>4;
							meas_is_neg <= 1;
						end
						led_bar         <= (acceleration + 16'sh40)>>>7;
						led_signed_mode <= 1;
					end
					3 : begin // Show Samples Per Second
						measurement     <= samps;
						meas_is_neg     <= 0;
						led_bar         <= samps>>2;
						led_signed_mode <= 0;
					end

					default : begin // Invalid
						measurement     <= 8'hFF;
						meas_is_neg     <= 0;
						led_bar         <= 8'hFF;
						led_signed_mode <= 0;
					end
				endcase

			end

		end

	// Count samples produced
	always  @(posedge clk_out)
		begin
			if (reset) begin
				count              <= 0;
				samps              <= 0;
				sample_count_reset <= 0;
			end else begin
				if (count > CLK_HZ) begin // Update sample rate once per second
					count <= 0;
					if (sample_count < 9999)
						samps <= sample_count;
					else
						samps <= 9999; // Overflow
					sample_count_reset <= 1;
					adc_sample_count   <= 0;
				end else begin
					count              <= count + 1;
					sample_count_reset <= 0;
				end
			end
		end

	// Control CIC rate based on switch settings
	always  @(posedge clk_out)
		begin
			if (reset) begin
				cic_rate        <= 0;
				cic_rate_q      <= 0;
				cic_rate_update <= 0;
			end else begin
				case (sw[14:13])
					0 : cic_rate <= 7539; // 49 ms
					1 : cic_rate <= 1884; // 12 ms
					2 : cic_rate <= 753;  // 4 ms
					3 : cic_rate <= 105;  // 0.65 ms
					default : cic_rate <= 7539;
				endcase
				cic_rate_q <= cic_rate;
				if (cic_rate_q != cic_rate)
					cic_rate_update <= 1;
				else
					cic_rate_update <= 0;
			end
		end

	// 7-Seg update speed
	always  @(posedge clk_out)
		begin
			if (reset) begin
				update_cycles <= CLK_HZ/1000;
			end else begin
				case (sw[11:10])
					0 : update_cycles        <= CLK_HZ/1000;
					1 : update_cycles        <= CLK_HZ/250;
					2 : update_cycles        <= CLK_HZ/100;
					3 : update_cycles        <= CLK_HZ/10;
					default : update_cycles  <= CLK_HZ/1000;
				endcase
			end
		end

	// LED bar meter
	always @(posedge clk_out)
		begin
			if (reset) begin
				led            <= {16{1'b1}};
				led_bar_signed <= 0;
			end else begin
				if (!led_signed_mode) begin // "Unsigned" mode, where bar fills from right to left
					case (led_bar)
						0       : led <=                16'b0;
						1       : led <=                16'b1;
						2       : led <=               16'b11;
						3       : led <=              16'b111;
						4       : led <=             16'b1111;
						5       : led <=            16'b11111;
						6       : led <=           16'b111111;
						7       : led <=          16'b1111111;
						8       : led <=         16'b11111111;
						9       : led <=        16'b111111111;
						10      : led <=       16'b1111111111;
						11      : led <=      16'b11111111111;
						12      : led <=     16'b111111111111;
						13      : led <=    16'b1111111111111;
						14      : led <=   16'b11111111111111;
						15      : led <=  16'b111111111111111;
						default : led <= 16'b1111111111111111; // Overflow
					endcase
				end else begin // "Signed" mode, where bar fills from middle out 
					if ($signed(led_bar) > 8) // Handle overflow
						led_bar_signed <= 9;
					else if ($signed(led_bar) < -8)
						led_bar_signed <= -9;
					else
						led_bar_signed <= $signed(led_bar);
					case (led_bar_signed)
						-9      : led <=         16'b11111111;  // Negative overflow
						-8      : led <=         16'b11111111;
						-7      : led <=         16'b11111110;
						-6      : led <=         16'b11111100;
						-5      : led <=         16'b11111000;
						-4      : led <=         16'b11110000;
						-3      : led <=         16'b11100000;
						-2      : led <=         16'b11000000;
						-1      : led <=         16'b10000000;
						0       : led <=         16'b0       ;  // Zero
						1       : led <=        16'b100000000;
						2       : led <=       16'b1100000000;
						3       : led <=      16'b11100000000;
						4       : led <=     16'b111100000000;
						5       : led <=    16'b1111100000000;
						6       : led <=   16'b11111100000000;
						7       : led <=  16'b111111100000000;
						8       : led <= 16'b1111111100000000;
						9       : led <= 16'b1111111100000000;  // Positive overflow
						default : led <= 16'b0000000000000000;
					endcase
				end
			end
		end


endmodule
