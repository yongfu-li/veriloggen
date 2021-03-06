from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_matmul_ipcore

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] led;
  wire [32-1:0] maxi_awaddr;
  wire [8-1:0] maxi_awlen;
  wire maxi_awvalid;
  reg maxi_awready;
  wire [32-1:0] maxi_wdata;
  wire [4-1:0] maxi_wstrb;
  wire maxi_wlast;
  wire maxi_wvalid;
  reg maxi_wready;
  wire [32-1:0] maxi_araddr;
  wire [8-1:0] maxi_arlen;
  wire maxi_arvalid;
  reg maxi_arready;
  reg [32-1:0] maxi_rdata;
  reg maxi_rlast;
  reg maxi_rvalid;
  wire maxi_rready;
  reg [32-1:0] saxi_awaddr;
  reg saxi_awvalid;
  wire saxi_awready;
  reg [32-1:0] saxi_wdata;
  reg [4-1:0] saxi_wstrb;
  reg saxi_wvalid;
  wire saxi_wready;
  reg [32-1:0] saxi_araddr;
  reg saxi_arvalid;
  wire saxi_arready;
  wire [32-1:0] saxi_rdata;
  wire saxi_rvalid;
  reg saxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire memory_awvalid;
  reg memory_awready;
  wire [32-1:0] memory_wdata;
  wire [4-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire memory_arvalid;
  reg memory_arready;
  reg [32-1:0] memory_rdata;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("mymem.out", _memory_mem);
  end

  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_count;
  reg [32-1:0] _d1__memory_fsm;
  reg __memory_fsm_cond_100_0_1;
  reg __memory_fsm_cond_200_1_1;
  reg __memory_fsm_cond_211_2_1;
  assign memory_awaddr = maxi_awaddr;
  assign memory_awlen = maxi_awlen;
  assign memory_awvalid = maxi_awvalid;
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    maxi_awready = _tmp_0;
  end

  assign memory_wdata = maxi_wdata;
  assign memory_wstrb = maxi_wstrb;
  assign memory_wlast = maxi_wlast;
  assign memory_wvalid = maxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    maxi_wready = _tmp_1;
  end

  assign memory_araddr = maxi_araddr;
  assign memory_arlen = maxi_arlen;
  assign memory_arvalid = maxi_arvalid;
  wire _tmp_2;
  assign _tmp_2 = memory_arready;

  always @(*) begin
    maxi_arready = _tmp_2;
  end


  always @(*) begin
    maxi_rdata <= memory_rdata;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_rlast;

  always @(*) begin
    maxi_rlast = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = memory_rvalid;

  always @(*) begin
    maxi_rvalid = _tmp_4;
  end

  assign memory_rready = maxi_rready;
  reg [32-1:0] _saxi_awaddr;
  reg _saxi_awvalid;
  wire _saxi_awready;
  reg [32-1:0] _saxi_wdata;
  reg [4-1:0] _saxi_wstrb;
  reg _saxi_wvalid;
  wire _saxi_wready;
  reg [32-1:0] _saxi_araddr;
  reg _saxi_arvalid;
  wire _saxi_arready;
  wire [32-1:0] _saxi_rdata;
  wire _saxi_rvalid;
  wire _saxi_rready;
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _saxi_awaddr;

  always @(*) begin
    saxi_awaddr = _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = _saxi_awvalid;

  always @(*) begin
    saxi_awvalid = _tmp_6;
  end

  assign _saxi_awready = saxi_awready;
  wire [32-1:0] _tmp_7;
  assign _tmp_7 = _saxi_wdata;

  always @(*) begin
    saxi_wdata = _tmp_7;
  end

  wire [4-1:0] _tmp_8;
  assign _tmp_8 = _saxi_wstrb;

  always @(*) begin
    saxi_wstrb = _tmp_8;
  end

  wire _tmp_9;
  assign _tmp_9 = _saxi_wvalid;

  always @(*) begin
    saxi_wvalid = _tmp_9;
  end

  assign _saxi_wready = saxi_wready;
  wire [32-1:0] _tmp_10;
  assign _tmp_10 = _saxi_araddr;

  always @(*) begin
    saxi_araddr = _tmp_10;
  end

  wire _tmp_11;
  assign _tmp_11 = _saxi_arvalid;

  always @(*) begin
    saxi_arvalid = _tmp_11;
  end

  assign _saxi_arready = saxi_arready;
  assign _saxi_rdata = saxi_rdata;
  assign _saxi_rvalid = saxi_rvalid;
  wire _tmp_12;
  assign _tmp_12 = _saxi_rready;

  always @(*) begin
    saxi_rready = _tmp_12;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_17;
  reg signed [32-1:0] _th_ctrl_awaddr_18;
  reg signed [32-1:0] _th_ctrl_matrix_size_19;
  reg __saxi_cond_0_1;
  reg __saxi_cond_1_1;
  reg signed [32-1:0] _th_ctrl_a_offset_20;
  reg __saxi_cond_2_1;
  reg __saxi_cond_3_1;
  reg signed [32-1:0] _th_ctrl_b_offset_21;
  reg __saxi_cond_4_1;
  reg __saxi_cond_5_1;
  reg signed [32-1:0] _th_ctrl_c_offset_22;
  reg __saxi_cond_6_1;
  reg __saxi_cond_7_1;
  reg signed [32-1:0] _th_ctrl_start_time_23;
  reg __saxi_cond_8_1;
  reg __saxi_cond_9_1;
  reg signed [32-1:0] _th_ctrl_araddr_24;
  reg __saxi_cond_10_1;
  reg [32-1:0] _tmp_13;
  reg signed [32-1:0] _th_ctrl_v_25;
  reg __saxi_cond_11_1;
  assign _saxi_rready = (th_ctrl == 31) || (th_ctrl == 35);
  reg [32-1:0] _tmp_14;
  reg signed [32-1:0] _th_ctrl_end_time_26;
  reg signed [32-1:0] _th_ctrl_time_27;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .led(led),
    .maxi_awaddr(maxi_awaddr),
    .maxi_awlen(maxi_awlen),
    .maxi_awvalid(maxi_awvalid),
    .maxi_awready(maxi_awready),
    .maxi_wdata(maxi_wdata),
    .maxi_wstrb(maxi_wstrb),
    .maxi_wlast(maxi_wlast),
    .maxi_wvalid(maxi_wvalid),
    .maxi_wready(maxi_wready),
    .maxi_araddr(maxi_araddr),
    .maxi_arlen(maxi_arlen),
    .maxi_arvalid(maxi_arvalid),
    .maxi_arready(maxi_arready),
    .maxi_rdata(maxi_rdata),
    .maxi_rlast(maxi_rlast),
    .maxi_rvalid(maxi_rvalid),
    .maxi_rready(maxi_rready),
    .saxi_awaddr(saxi_awaddr),
    .saxi_awvalid(saxi_awvalid),
    .saxi_awready(saxi_awready),
    .saxi_wdata(saxi_wdata),
    .saxi_wstrb(saxi_wstrb),
    .saxi_wvalid(saxi_wvalid),
    .saxi_wready(saxi_wready),
    .saxi_araddr(saxi_araddr),
    .saxi_arvalid(saxi_arvalid),
    .saxi_arready(saxi_arready),
    .saxi_rdata(saxi_rdata),
    .saxi_rvalid(saxi_rvalid),
    .saxi_rready(saxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    memory_awready = 0;
    memory_wready = 0;
    memory_arready = 0;
    memory_rdata = 0;
    memory_rlast = 0;
    memory_rvalid = 0;
    _memory_fsm = _memory_fsm_init;
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_count = 0;
    _d1__memory_fsm = _memory_fsm_init;
    __memory_fsm_cond_100_0_1 = 0;
    __memory_fsm_cond_200_1_1 = 0;
    __memory_fsm_cond_211_2_1 = 0;
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    _saxi_wdata = 0;
    _saxi_wstrb = 0;
    _saxi_wvalid = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_17 = 0;
    _th_ctrl_awaddr_18 = 0;
    _th_ctrl_matrix_size_19 = 0;
    __saxi_cond_0_1 = 0;
    __saxi_cond_1_1 = 0;
    _th_ctrl_a_offset_20 = 0;
    __saxi_cond_2_1 = 0;
    __saxi_cond_3_1 = 0;
    _th_ctrl_b_offset_21 = 0;
    __saxi_cond_4_1 = 0;
    __saxi_cond_5_1 = 0;
    _th_ctrl_c_offset_22 = 0;
    __saxi_cond_6_1 = 0;
    __saxi_cond_7_1 = 0;
    _th_ctrl_start_time_23 = 0;
    __saxi_cond_8_1 = 0;
    __saxi_cond_9_1 = 0;
    _th_ctrl_araddr_24 = 0;
    __saxi_cond_10_1 = 0;
    _tmp_13 = 0;
    _th_ctrl_v_25 = 0;
    __saxi_cond_11_1 = 0;
    _tmp_14 = 0;
    _th_ctrl_end_time_26 = 0;
    _th_ctrl_time_27 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000000;
    $finish;
  end

  localparam _memory_fsm_200 = 200;
  localparam _memory_fsm_201 = 201;
  localparam _memory_fsm_202 = 202;
  localparam _memory_fsm_203 = 203;
  localparam _memory_fsm_204 = 204;
  localparam _memory_fsm_205 = 205;
  localparam _memory_fsm_206 = 206;
  localparam _memory_fsm_207 = 207;
  localparam _memory_fsm_208 = 208;
  localparam _memory_fsm_209 = 209;
  localparam _memory_fsm_210 = 210;
  localparam _memory_fsm_211 = 211;
  localparam _memory_fsm_100 = 100;
  localparam _memory_fsm_101 = 101;
  localparam _memory_fsm_102 = 102;
  localparam _memory_fsm_103 = 103;
  localparam _memory_fsm_104 = 104;
  localparam _memory_fsm_105 = 105;
  localparam _memory_fsm_106 = 106;
  localparam _memory_fsm_107 = 107;
  localparam _memory_fsm_108 = 108;
  localparam _memory_fsm_109 = 109;
  localparam _memory_fsm_110 = 110;
  localparam _memory_fsm_111 = 111;
  localparam _memory_fsm_112 = 112;

  always @(posedge CLK) begin
    if(RST) begin
      _memory_fsm <= _memory_fsm_init;
      _d1__memory_fsm <= _memory_fsm_init;
      memory_awready <= 0;
      _write_addr <= 0;
      _write_count <= 0;
      __memory_fsm_cond_100_0_1 <= 0;
      memory_wready <= 0;
      memory_arready <= 0;
      _read_addr <= 0;
      _read_count <= 0;
      __memory_fsm_cond_200_1_1 <= 0;
      memory_rdata[7:0] <= (0 >> 0) & { 8{ 1'd1 } };
      memory_rdata[15:8] <= (0 >> 8) & { 8{ 1'd1 } };
      memory_rdata[23:16] <= (0 >> 16) & { 8{ 1'd1 } };
      memory_rdata[31:24] <= (0 >> 24) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_fsm_cond_211_2_1 <= 0;
      memory_rdata <= 0;
      _sleep_count <= 0;
    end else begin
      _sleep_count <= _sleep_count + 1;
      if(_sleep_count == 3) begin
        _sleep_count <= 0;
      end 
      _d1__memory_fsm <= _memory_fsm;
      case(_d1__memory_fsm)
        _memory_fsm_100: begin
          if(__memory_fsm_cond_100_0_1) begin
            memory_awready <= 0;
          end 
        end
        _memory_fsm_200: begin
          if(__memory_fsm_cond_200_1_1) begin
            memory_arready <= 0;
          end 
        end
        _memory_fsm_211: begin
          if(__memory_fsm_cond_211_2_1) begin
            memory_rvalid <= 0;
            memory_rlast <= 0;
          end 
        end
      endcase
      case(_memory_fsm)
        _memory_fsm_init: begin
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_100;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_200;
          end 
        end
        _memory_fsm_100: begin
          if(memory_awvalid) begin
            memory_awready <= 1;
            _write_addr <= memory_awaddr;
            _write_count <= memory_awlen + 1;
          end 
          __memory_fsm_cond_100_0_1 <= 1;
          if(!memory_awvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_101;
          end 
        end
        _memory_fsm_101: begin
          _memory_fsm <= _memory_fsm_102;
        end
        _memory_fsm_102: begin
          _memory_fsm <= _memory_fsm_103;
        end
        _memory_fsm_103: begin
          _memory_fsm <= _memory_fsm_104;
        end
        _memory_fsm_104: begin
          _memory_fsm <= _memory_fsm_105;
        end
        _memory_fsm_105: begin
          _memory_fsm <= _memory_fsm_106;
        end
        _memory_fsm_106: begin
          _memory_fsm <= _memory_fsm_107;
        end
        _memory_fsm_107: begin
          _memory_fsm <= _memory_fsm_108;
        end
        _memory_fsm_108: begin
          _memory_fsm <= _memory_fsm_109;
        end
        _memory_fsm_109: begin
          _memory_fsm <= _memory_fsm_110;
        end
        _memory_fsm_110: begin
          _memory_fsm <= _memory_fsm_111;
        end
        _memory_fsm_111: begin
          memory_wready <= 1;
          _memory_fsm <= _memory_fsm_112;
        end
        _memory_fsm_112: begin
          if(memory_wvalid && memory_wstrb[0]) begin
            _memory_mem[_write_addr + 0] <= memory_wdata[7:0];
          end 
          if(memory_wvalid && memory_wstrb[1]) begin
            _memory_mem[_write_addr + 1] <= memory_wdata[15:8];
          end 
          if(memory_wvalid && memory_wstrb[2]) begin
            _memory_mem[_write_addr + 2] <= memory_wdata[23:16];
          end 
          if(memory_wvalid && memory_wstrb[3]) begin
            _memory_mem[_write_addr + 3] <= memory_wdata[31:24];
          end 
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 4;
            _write_count <= _write_count - 1;
          end 
          if(_sleep_count == 3) begin
            memory_wready <= 0;
          end else begin
            memory_wready <= 1;
          end
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            memory_wready <= 0;
          end 
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
        _memory_fsm_200: begin
          if(memory_arvalid) begin
            memory_arready <= 1;
            _read_addr <= memory_araddr;
            _read_count <= memory_arlen + 1;
          end 
          __memory_fsm_cond_200_1_1 <= 1;
          if(!memory_arvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_201;
          end 
        end
        _memory_fsm_201: begin
          _memory_fsm <= _memory_fsm_202;
        end
        _memory_fsm_202: begin
          _memory_fsm <= _memory_fsm_203;
        end
        _memory_fsm_203: begin
          _memory_fsm <= _memory_fsm_204;
        end
        _memory_fsm_204: begin
          _memory_fsm <= _memory_fsm_205;
        end
        _memory_fsm_205: begin
          _memory_fsm <= _memory_fsm_206;
        end
        _memory_fsm_206: begin
          _memory_fsm <= _memory_fsm_207;
        end
        _memory_fsm_207: begin
          _memory_fsm <= _memory_fsm_208;
        end
        _memory_fsm_208: begin
          _memory_fsm <= _memory_fsm_209;
        end
        _memory_fsm_209: begin
          _memory_fsm <= _memory_fsm_210;
        end
        _memory_fsm_210: begin
          _memory_fsm <= _memory_fsm_211;
        end
        _memory_fsm_211: begin
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[7:0] <= _memory_mem[_read_addr + 0];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[15:8] <= _memory_mem[_read_addr + 1];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[23:16] <= _memory_mem[_read_addr + 2];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[31:24] <= _memory_mem[_read_addr + 3];
          end 
          if((_sleep_count < 3) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 4;
            _read_count <= _read_count - 1;
          end 
          if((_sleep_count < 3) && (_read_count == 1) && memory_rready | !memory_rvalid) begin
            memory_rlast <= 1;
          end 
          __memory_fsm_cond_211_2_1 <= 1;
          if(memory_rvalid && !memory_rready) begin
            memory_rvalid <= memory_rvalid;
            memory_rdata <= memory_rdata;
            memory_rlast <= memory_rlast;
          end 
          if(memory_rvalid && memory_rready && (_read_count == 0)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _saxi_awaddr <= 0;
      _saxi_awvalid <= 0;
      __saxi_cond_0_1 <= 0;
      _saxi_wdata <= 0;
      _saxi_wvalid <= 0;
      _saxi_wstrb <= 0;
      __saxi_cond_1_1 <= 0;
      __saxi_cond_2_1 <= 0;
      __saxi_cond_3_1 <= 0;
      __saxi_cond_4_1 <= 0;
      __saxi_cond_5_1 <= 0;
      __saxi_cond_6_1 <= 0;
      __saxi_cond_7_1 <= 0;
      __saxi_cond_8_1 <= 0;
      __saxi_cond_9_1 <= 0;
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_10_1 <= 0;
      __saxi_cond_11_1 <= 0;
    end else begin
      if(__saxi_cond_0_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_1_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_2_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_3_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_4_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_5_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_6_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_7_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_8_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_9_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_10_1) begin
        _saxi_arvalid <= 0;
      end 
      if(__saxi_cond_11_1) begin
        _saxi_arvalid <= 0;
      end 
      if((th_ctrl == 7) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_18;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 8) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_matrix_size_19;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 12) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_18;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 13) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_a_offset_20;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 17) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_18;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 18) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_b_offset_21;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_5_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 22) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_18;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_6_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 23) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_c_offset_22;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_7_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 27) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_18;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_8_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 28) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_9_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 30) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_24;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_10_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
      if((th_ctrl == 34) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_24;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_11_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      counter <= 0;
    end else begin
      counter <= counter + 1;
    end
  end

  localparam th_ctrl_1 = 1;
  localparam th_ctrl_2 = 2;
  localparam th_ctrl_3 = 3;
  localparam th_ctrl_4 = 4;
  localparam th_ctrl_5 = 5;
  localparam th_ctrl_6 = 6;
  localparam th_ctrl_7 = 7;
  localparam th_ctrl_8 = 8;
  localparam th_ctrl_9 = 9;
  localparam th_ctrl_10 = 10;
  localparam th_ctrl_11 = 11;
  localparam th_ctrl_12 = 12;
  localparam th_ctrl_13 = 13;
  localparam th_ctrl_14 = 14;
  localparam th_ctrl_15 = 15;
  localparam th_ctrl_16 = 16;
  localparam th_ctrl_17 = 17;
  localparam th_ctrl_18 = 18;
  localparam th_ctrl_19 = 19;
  localparam th_ctrl_20 = 20;
  localparam th_ctrl_21 = 21;
  localparam th_ctrl_22 = 22;
  localparam th_ctrl_23 = 23;
  localparam th_ctrl_24 = 24;
  localparam th_ctrl_25 = 25;
  localparam th_ctrl_26 = 26;
  localparam th_ctrl_27 = 27;
  localparam th_ctrl_28 = 28;
  localparam th_ctrl_29 = 29;
  localparam th_ctrl_30 = 30;
  localparam th_ctrl_31 = 31;
  localparam th_ctrl_32 = 32;
  localparam th_ctrl_33 = 33;
  localparam th_ctrl_34 = 34;
  localparam th_ctrl_35 = 35;
  localparam th_ctrl_36 = 36;
  localparam th_ctrl_37 = 37;
  localparam th_ctrl_38 = 38;
  localparam th_ctrl_39 = 39;
  localparam th_ctrl_40 = 40;
  localparam th_ctrl_41 = 41;
  localparam th_ctrl_42 = 42;

  always @(posedge CLK) begin
    if(RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_17 <= 0;
      _th_ctrl_awaddr_18 <= 0;
      _th_ctrl_matrix_size_19 <= 0;
      _th_ctrl_a_offset_20 <= 0;
      _th_ctrl_b_offset_21 <= 0;
      _th_ctrl_c_offset_22 <= 0;
      _th_ctrl_start_time_23 <= 0;
      _th_ctrl_araddr_24 <= 0;
      _tmp_13 <= 0;
      _th_ctrl_v_25 <= 0;
      _tmp_14 <= 0;
      _th_ctrl_end_time_26 <= 0;
      _th_ctrl_time_27 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_17 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_17 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_17 <= _th_ctrl_i_17 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_18 <= 4;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          _th_ctrl_matrix_size_19 <= 16;
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          $display("# matrix_size = %d", _th_ctrl_matrix_size_19);
          th_ctrl <= th_ctrl_7;
        end
        th_ctrl_7: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_8;
          end 
        end
        th_ctrl_8: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          _th_ctrl_awaddr_18 <= 8;
          th_ctrl <= th_ctrl_10;
        end
        th_ctrl_10: begin
          _th_ctrl_a_offset_20 <= 0;
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          $display("# a_offset = %d", _th_ctrl_a_offset_20);
          th_ctrl <= th_ctrl_12;
        end
        th_ctrl_12: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_13;
          end 
        end
        th_ctrl_13: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_14;
          end 
        end
        th_ctrl_14: begin
          _th_ctrl_awaddr_18 <= 12;
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          _th_ctrl_b_offset_21 <= 1024;
          th_ctrl <= th_ctrl_16;
        end
        th_ctrl_16: begin
          $display("# b_offset = %d", _th_ctrl_b_offset_21);
          th_ctrl <= th_ctrl_17;
        end
        th_ctrl_17: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_18;
          end 
        end
        th_ctrl_18: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          _th_ctrl_awaddr_18 <= 16;
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          _th_ctrl_c_offset_22 <= 2048;
          th_ctrl <= th_ctrl_21;
        end
        th_ctrl_21: begin
          $display("# c_offset = %d", _th_ctrl_c_offset_22);
          th_ctrl <= th_ctrl_22;
        end
        th_ctrl_22: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_23;
          end 
        end
        th_ctrl_23: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_24;
          end 
        end
        th_ctrl_24: begin
          _th_ctrl_awaddr_18 <= 0;
          th_ctrl <= th_ctrl_25;
        end
        th_ctrl_25: begin
          _th_ctrl_start_time_23 <= counter;
          th_ctrl <= th_ctrl_26;
        end
        th_ctrl_26: begin
          $display("# start time = %d", _th_ctrl_start_time_23);
          th_ctrl <= th_ctrl_27;
        end
        th_ctrl_27: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_28;
          end 
        end
        th_ctrl_28: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_29;
          end 
        end
        th_ctrl_29: begin
          _th_ctrl_araddr_24 <= 20;
          th_ctrl <= th_ctrl_30;
        end
        th_ctrl_30: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_31;
          end 
        end
        th_ctrl_31: begin
          if(_saxi_rready && _saxi_rvalid) begin
            _tmp_13 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_32;
          end 
        end
        th_ctrl_32: begin
          _th_ctrl_v_25 <= _tmp_13;
          th_ctrl <= th_ctrl_33;
        end
        th_ctrl_33: begin
          if(_th_ctrl_v_25 == 0) begin
            th_ctrl <= th_ctrl_34;
          end else begin
            th_ctrl <= th_ctrl_38;
          end
        end
        th_ctrl_34: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_35;
          end 
        end
        th_ctrl_35: begin
          if(_saxi_rready && _saxi_rvalid) begin
            _tmp_14 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_36;
          end 
        end
        th_ctrl_36: begin
          _th_ctrl_v_25 <= _tmp_14;
          th_ctrl <= th_ctrl_37;
        end
        th_ctrl_37: begin
          th_ctrl <= th_ctrl_33;
        end
        th_ctrl_38: begin
          _th_ctrl_end_time_26 <= counter;
          th_ctrl <= th_ctrl_39;
        end
        th_ctrl_39: begin
          $display("# end time = %d", _th_ctrl_end_time_26);
          th_ctrl <= th_ctrl_40;
        end
        th_ctrl_40: begin
          _th_ctrl_time_27 <= _th_ctrl_end_time_26 - _th_ctrl_start_time_23;
          th_ctrl <= th_ctrl_41;
        end
        th_ctrl_41: begin
          $display("# exec time = %d", _th_ctrl_time_27);
          th_ctrl <= th_ctrl_42;
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] led,
  output reg [32-1:0] maxi_awaddr,
  output reg [8-1:0] maxi_awlen,
  output reg maxi_awvalid,
  input maxi_awready,
  output reg [32-1:0] maxi_wdata,
  output reg [4-1:0] maxi_wstrb,
  output reg maxi_wlast,
  output reg maxi_wvalid,
  input maxi_wready,
  output reg [32-1:0] maxi_araddr,
  output reg [8-1:0] maxi_arlen,
  output reg maxi_arvalid,
  input maxi_arready,
  input [32-1:0] maxi_rdata,
  input maxi_rlast,
  input maxi_rvalid,
  output maxi_rready,
  input [32-1:0] saxi_awaddr,
  input saxi_awvalid,
  output saxi_awready,
  input [32-1:0] saxi_wdata,
  input [4-1:0] saxi_wstrb,
  input saxi_wvalid,
  output saxi_wready,
  input [32-1:0] saxi_araddr,
  input saxi_arvalid,
  output saxi_arready,
  output reg [32-1:0] saxi_rdata,
  output reg saxi_rvalid,
  input saxi_rready
);

  reg [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  reg [32-1:0] ram_a_0_wdata;
  reg ram_a_0_wenable;

  ram_a
  inst_ram_a
  (
    .CLK(CLK),
    .ram_a_0_addr(ram_a_0_addr),
    .ram_a_0_rdata(ram_a_0_rdata),
    .ram_a_0_wdata(ram_a_0_wdata),
    .ram_a_0_wenable(ram_a_0_wenable)
  );

  reg [10-1:0] ram_b_0_addr;
  wire [32-1:0] ram_b_0_rdata;
  reg [32-1:0] ram_b_0_wdata;
  reg ram_b_0_wenable;

  ram_b
  inst_ram_b
  (
    .CLK(CLK),
    .ram_b_0_addr(ram_b_0_addr),
    .ram_b_0_rdata(ram_b_0_rdata),
    .ram_b_0_wdata(ram_b_0_wdata),
    .ram_b_0_wenable(ram_b_0_wenable)
  );

  reg [10-1:0] ram_c_0_addr;
  wire [32-1:0] ram_c_0_rdata;
  reg [32-1:0] ram_c_0_wdata;
  reg ram_c_0_wenable;

  ram_c
  inst_ram_c
  (
    .CLK(CLK),
    .ram_c_0_addr(ram_c_0_addr),
    .ram_c_0_rdata(ram_c_0_rdata),
    .ram_c_0_wdata(ram_c_0_wdata),
    .ram_c_0_wenable(ram_c_0_wenable)
  );

  reg [32-1:0] _saxi_register_0;
  reg [32-1:0] _saxi_register_1;
  reg [32-1:0] _saxi_register_2;
  reg [32-1:0] _saxi_register_3;
  reg [32-1:0] _saxi_register_4;
  reg [32-1:0] _saxi_register_5;
  reg [32-1:0] _saxi_register_6;
  reg [32-1:0] _saxi_register_7;
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg _saxi_flag_4;
  reg _saxi_flag_5;
  reg _saxi_flag_6;
  reg _saxi_flag_7;
  reg [32-1:0] _saxi_resetval_0;
  reg [32-1:0] _saxi_resetval_1;
  reg [32-1:0] _saxi_resetval_2;
  reg [32-1:0] _saxi_resetval_3;
  reg [32-1:0] _saxi_resetval_4;
  reg [32-1:0] _saxi_resetval_5;
  reg [32-1:0] _saxi_resetval_6;
  reg [32-1:0] _saxi_resetval_7;
  localparam _saxi_maskwidth = 3;
  localparam _saxi_mask = { _saxi_maskwidth{ 1'd1 } };
  localparam _saxi_shift = 2;
  reg [32-1:0] _saxi_register_fsm;
  localparam _saxi_register_fsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg _tmp_1;
  reg _tmp_2;
  reg _tmp_3;
  reg _tmp_4;
  assign saxi_awready = (_saxi_register_fsm == 0) && !_tmp_1 && !_tmp_2 && _tmp_3;
  assign saxi_arready = (_saxi_register_fsm == 0) && !_tmp_2 && !_tmp_1 && _tmp_4;
  reg [_saxi_maskwidth-1:0] _tmp_5;
  wire [32-1:0] _tmp_6;
  assign _tmp_6 = (_tmp_5 == 0)? _saxi_register_0 : 
                  (_tmp_5 == 1)? _saxi_register_1 : 
                  (_tmp_5 == 2)? _saxi_register_2 : 
                  (_tmp_5 == 3)? _saxi_register_3 : 
                  (_tmp_5 == 4)? _saxi_register_4 : 
                  (_tmp_5 == 5)? _saxi_register_5 : 
                  (_tmp_5 == 6)? _saxi_register_6 : 
                  (_tmp_5 == 7)? _saxi_register_7 : 'hx;
  wire _tmp_7;
  assign _tmp_7 = (_tmp_5 == 0)? _saxi_flag_0 : 
                  (_tmp_5 == 1)? _saxi_flag_1 : 
                  (_tmp_5 == 2)? _saxi_flag_2 : 
                  (_tmp_5 == 3)? _saxi_flag_3 : 
                  (_tmp_5 == 4)? _saxi_flag_4 : 
                  (_tmp_5 == 5)? _saxi_flag_5 : 
                  (_tmp_5 == 6)? _saxi_flag_6 : 
                  (_tmp_5 == 7)? _saxi_flag_7 : 'hx;
  wire [32-1:0] _tmp_8;
  assign _tmp_8 = (_tmp_5 == 0)? _saxi_resetval_0 : 
                  (_tmp_5 == 1)? _saxi_resetval_1 : 
                  (_tmp_5 == 2)? _saxi_resetval_2 : 
                  (_tmp_5 == 3)? _saxi_resetval_3 : 
                  (_tmp_5 == 4)? _saxi_resetval_4 : 
                  (_tmp_5 == 5)? _saxi_resetval_5 : 
                  (_tmp_5 == 6)? _saxi_resetval_6 : 
                  (_tmp_5 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg [32-1:0] th_matmul;
  localparam th_matmul_init = 0;
  reg signed [32-1:0] _th_matmul_matrix_size_0;
  reg signed [32-1:0] _th_matmul_a_offset_1;
  reg signed [32-1:0] _th_matmul_b_offset_2;
  reg signed [32-1:0] _th_matmul_c_offset_3;
  reg signed [32-1:0] _th_matmul_matrix_size_4;
  reg signed [32-1:0] _th_matmul_a_offset_5;
  reg signed [32-1:0] _th_matmul_b_offset_6;
  reg signed [32-1:0] _th_matmul_c_offset_7;
  reg signed [32-1:0] _th_matmul_a_addr_8;
  reg signed [32-1:0] _th_matmul_c_addr_9;
  reg signed [32-1:0] _th_matmul_i_10;
  reg [10-1:0] _tmp_9;
  reg [32-1:0] _tmp_10;
  reg [32-1:0] _tmp_11;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _tmp_12;
  reg [33-1:0] _tmp_13;
  reg [33-1:0] _tmp_14;
  reg [32-1:0] _tmp_15;
  reg _tmp_16;
  reg [33-1:0] _tmp_17;
  reg _tmp_18;
  wire [32-1:0] _tmp_data_19;
  wire _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_17 > 0) && !_tmp_18;
  reg _ram_a_cond_0_1;
  reg [9-1:0] _tmp_20;
  reg _maxi_cond_0_1;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_4_0_1;
  reg _tmp_21;
  reg __tmp_fsm_0_cond_5_1_1;
  reg signed [32-1:0] _th_matmul_b_addr_11;
  reg signed [32-1:0] _th_matmul_j_12;
  reg [10-1:0] _tmp_22;
  reg [32-1:0] _tmp_23;
  reg [32-1:0] _tmp_24;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_25;
  reg [33-1:0] _tmp_26;
  reg [33-1:0] _tmp_27;
  reg [32-1:0] _tmp_28;
  reg _tmp_29;
  reg [33-1:0] _tmp_30;
  reg _tmp_31;
  wire [32-1:0] _tmp_data_32;
  wire _tmp_valid_32;
  wire _tmp_ready_32;
  assign _tmp_ready_32 = (_tmp_30 > 0) && !_tmp_31;
  reg _ram_b_cond_0_1;
  reg [9-1:0] _tmp_33;
  reg _maxi_cond_1_1;
  assign maxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_1 == 4);
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_4_0_1;
  reg _tmp_34;
  reg __tmp_fsm_1_cond_5_1_1;
  reg signed [32-1:0] _th_matmul_sum_13;
  reg signed [32-1:0] _th_matmul_k_14;
  reg _tmp_35;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  reg signed [32-1:0] _tmp_36;
  reg signed [32-1:0] _th_matmul_x_15;
  reg _tmp_37;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  reg signed [32-1:0] _tmp_38;
  reg signed [32-1:0] _th_matmul_y_16;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_39;
  reg [32-1:0] _tmp_40;
  reg [32-1:0] _tmp_41;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_42;
  reg [33-1:0] _tmp_43;
  reg [33-1:0] _tmp_44;
  reg _tmp_45;
  reg _tmp_46;
  wire _tmp_47;
  wire _tmp_48;
  assign _tmp_48 = 1;
  localparam _tmp_49 = 1;
  wire [_tmp_49-1:0] _tmp_50;
  assign _tmp_50 = (_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46);
  reg [_tmp_49-1:0] __tmp_50_1;
  wire [32-1:0] _tmp_51;
  reg [32-1:0] __tmp_51_1;
  assign _tmp_51 = (__tmp_50_1)? ram_c_0_rdata : __tmp_51_1;
  reg _tmp_52;
  reg _tmp_53;
  reg _tmp_54;
  reg _tmp_55;
  reg [33-1:0] _tmp_56;
  reg [9-1:0] _tmp_57;
  reg _maxi_cond_2_1;
  reg _tmp_58;
  wire [32-1:0] _tmp_data_59;
  wire _tmp_valid_59;
  wire _tmp_ready_59;
  assign _tmp_ready_59 = (_tmp_fsm_2 == 4) && ((_tmp_57 > 0) && (maxi_wready || !maxi_wvalid));
  reg _maxi_cond_3_1;
  reg _tmp_60;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_5_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_17 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_18 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_35 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_35 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_18 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_35 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if((_tmp_fsm_0 == 1) && (_tmp_17 == 0)) begin
        ram_a_0_addr <= _tmp_9 - 1;
        _tmp_17 <= _tmp_11;
      end 
      if(_tmp_valid_19 && ((_tmp_17 > 0) && !_tmp_18) && (_tmp_17 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_19;
        ram_a_0_wenable <= 1;
        _tmp_17 <= _tmp_17 - 1;
      end 
      if(_tmp_valid_19 && ((_tmp_17 > 0) && !_tmp_18) && (_tmp_17 == 1)) begin
        _tmp_18 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      if(th_matmul == 21) begin
        ram_a_0_addr <= _th_matmul_k_14;
      end 
      _ram_a_cond_1_1 <= th_matmul == 21;
      _ram_a_cond_2_1 <= th_matmul == 21;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_30 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_31 <= 0;
      _ram_b_cond_0_1 <= 0;
      _ram_b_cond_1_1 <= 0;
      _tmp_37 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_37 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_31 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_37 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if((_tmp_fsm_1 == 1) && (_tmp_30 == 0)) begin
        ram_b_0_addr <= _tmp_22 - 1;
        _tmp_30 <= _tmp_24;
      end 
      if(_tmp_valid_32 && ((_tmp_30 > 0) && !_tmp_31) && (_tmp_30 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_32;
        ram_b_0_wenable <= 1;
        _tmp_30 <= _tmp_30 - 1;
      end 
      if(_tmp_valid_32 && ((_tmp_30 > 0) && !_tmp_31) && (_tmp_30 == 1)) begin
        _tmp_31 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      if(th_matmul == 23) begin
        ram_b_0_addr <= _th_matmul_k_14;
      end 
      _ram_b_cond_1_1 <= th_matmul == 23;
      _ram_b_cond_2_1 <= th_matmul == 23;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_50_1 <= 0;
      __tmp_51_1 <= 0;
      _tmp_55 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_52 <= 0;
      _tmp_56 <= 0;
    end else begin
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(th_matmul == 27) begin
        ram_c_0_addr <= _th_matmul_j_12;
        ram_c_0_wdata <= _th_matmul_sum_13;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= th_matmul == 27;
      __tmp_50_1 <= _tmp_50;
      __tmp_51_1 <= _tmp_51;
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_53) begin
        _tmp_55 <= 0;
        _tmp_45 <= 0;
        _tmp_46 <= 0;
        _tmp_53 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_52) begin
        _tmp_45 <= 1;
        _tmp_46 <= 1;
        _tmp_55 <= _tmp_54;
        _tmp_54 <= 0;
        _tmp_52 <= 0;
        _tmp_53 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_56 == 0) && !_tmp_54 && !_tmp_55) begin
        ram_c_0_addr <= _tmp_39;
        _tmp_56 <= _tmp_41 - 1;
        _tmp_52 <= 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && (_tmp_56 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_56 <= _tmp_56 - 1;
        _tmp_52 <= 1;
        _tmp_54 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && (_tmp_56 == 1)) begin
        _tmp_54 <= 1;
      end 
    end
  end

  assign _tmp_data_59 = _tmp_51;
  assign _tmp_valid_59 = _tmp_45;
  assign _tmp_47 = 1 && _tmp_ready_59;

  always @(posedge CLK) begin
    if(RST) begin
      maxi_araddr <= 0;
      maxi_arlen <= 0;
      maxi_arvalid <= 0;
      _tmp_20 <= 0;
      _maxi_cond_0_1 <= 0;
      _tmp_33 <= 0;
      _maxi_cond_1_1 <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      _tmp_57 <= 0;
      _maxi_cond_2_1 <= 0;
      maxi_wdata <= 0;
      maxi_wvalid <= 0;
      maxi_wlast <= 0;
      maxi_wstrb <= 0;
      _tmp_58 <= 0;
      _maxi_cond_3_1 <= 0;
    end else begin
      if(_maxi_cond_0_1) begin
        maxi_arvalid <= 0;
      end 
      if(_maxi_cond_1_1) begin
        maxi_arvalid <= 0;
      end 
      if(_maxi_cond_2_1) begin
        maxi_awvalid <= 0;
      end 
      if(_maxi_cond_3_1) begin
        maxi_wvalid <= 0;
        maxi_wlast <= 0;
        _tmp_58 <= 0;
      end 
      if((_tmp_fsm_0 == 3) && ((maxi_arready || !maxi_arvalid) && (_tmp_20 == 0))) begin
        maxi_araddr <= _tmp_12;
        maxi_arlen <= _tmp_13 - 1;
        maxi_arvalid <= 1;
        _tmp_20 <= _tmp_13;
      end 
      _maxi_cond_0_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
      if(maxi_rready && maxi_rvalid && (_tmp_20 > 0)) begin
        _tmp_20 <= _tmp_20 - 1;
      end 
      if((_tmp_fsm_1 == 3) && ((maxi_arready || !maxi_arvalid) && (_tmp_33 == 0))) begin
        maxi_araddr <= _tmp_25;
        maxi_arlen <= _tmp_26 - 1;
        maxi_arvalid <= 1;
        _tmp_33 <= _tmp_26;
      end 
      _maxi_cond_1_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
      if(maxi_rready && maxi_rvalid && (_tmp_33 > 0)) begin
        _tmp_33 <= _tmp_33 - 1;
      end 
      if((_tmp_fsm_2 == 3) && ((maxi_awready || !maxi_awvalid) && (_tmp_57 == 0))) begin
        maxi_awaddr <= _tmp_42;
        maxi_awlen <= _tmp_43 - 1;
        maxi_awvalid <= 1;
        _tmp_57 <= _tmp_43;
      end 
      if((_tmp_fsm_2 == 3) && ((maxi_awready || !maxi_awvalid) && (_tmp_57 == 0)) && (_tmp_43 == 0)) begin
        maxi_awvalid <= 0;
      end 
      _maxi_cond_2_1 <= 1;
      if(maxi_awvalid && !maxi_awready) begin
        maxi_awvalid <= maxi_awvalid;
      end 
      if(_tmp_valid_59 && ((_tmp_fsm_2 == 4) && ((_tmp_57 > 0) && (maxi_wready || !maxi_wvalid))) && ((_tmp_57 > 0) && (maxi_wready || !maxi_wvalid) && (_tmp_57 > 0))) begin
        maxi_wdata <= _tmp_data_59;
        maxi_wvalid <= 1;
        maxi_wlast <= 0;
        maxi_wstrb <= { 4{ 1'd1 } };
        _tmp_57 <= _tmp_57 - 1;
      end 
      if(_tmp_valid_59 && ((_tmp_fsm_2 == 4) && ((_tmp_57 > 0) && (maxi_wready || !maxi_wvalid))) && ((_tmp_57 > 0) && (maxi_wready || !maxi_wvalid) && (_tmp_57 > 0)) && (_tmp_57 == 1)) begin
        maxi_wlast <= 1;
        _tmp_58 <= 1;
      end 
      _maxi_cond_3_1 <= 1;
      if(maxi_wvalid && !maxi_wready) begin
        maxi_wvalid <= maxi_wvalid;
        maxi_wlast <= maxi_wlast;
        _tmp_58 <= _tmp_58;
      end 
    end
  end

  assign _tmp_data_19 = _tmp_15;
  assign _tmp_valid_19 = _tmp_16;
  assign _tmp_data_32 = _tmp_28;
  assign _tmp_valid_32 = _tmp_29;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_0 <= 0;
      saxi_rdata <= 0;
      saxi_rvalid <= 0;
      _saxi_cond_0_1 <= 0;
      _saxi_register_0 <= 0;
      _saxi_flag_0 <= 0;
      _saxi_register_1 <= 0;
      _saxi_flag_1 <= 0;
      _saxi_register_2 <= 0;
      _saxi_flag_2 <= 0;
      _saxi_register_3 <= 0;
      _saxi_flag_3 <= 0;
      _saxi_register_4 <= 0;
      _saxi_flag_4 <= 0;
      _saxi_register_5 <= 0;
      _saxi_flag_5 <= 0;
      _saxi_register_6 <= 0;
      _saxi_flag_6 <= 0;
      _saxi_register_7 <= 0;
      _saxi_flag_7 <= 0;
      _saxi_resetval_0 <= 0;
      _saxi_resetval_1 <= 0;
      _saxi_resetval_2 <= 0;
      _saxi_resetval_3 <= 0;
      _saxi_resetval_4 <= 0;
      _saxi_resetval_5 <= 0;
      _saxi_resetval_6 <= 0;
      _saxi_resetval_7 <= 0;
    end else begin
      if(_saxi_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      _tmp_3 <= saxi_awvalid;
      _tmp_4 <= saxi_arvalid;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      if(saxi_awready && saxi_awvalid) begin
        _tmp_0 <= saxi_awaddr;
        _tmp_1 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        _tmp_0 <= saxi_araddr;
        _tmp_2 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= _tmp_6;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 0)) begin
        _saxi_register_0 <= _tmp_8;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 1)) begin
        _saxi_register_1 <= _tmp_8;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 2)) begin
        _saxi_register_2 <= _tmp_8;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 3)) begin
        _saxi_register_3 <= _tmp_8;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 4)) begin
        _saxi_register_4 <= _tmp_8;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 5)) begin
        _saxi_register_5 <= _tmp_8;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 6)) begin
        _saxi_register_6 <= _tmp_8;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 7)) begin
        _saxi_register_7 <= _tmp_8;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 7)) begin
        _saxi_register_7 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 0)) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 1)) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 2)) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 3)) begin
        _saxi_register_3 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 4)) begin
        _saxi_register_4 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 5)) begin
        _saxi_register_5 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 6)) begin
        _saxi_register_6 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && (0 == 7)) begin
        _saxi_register_7 <= 0;
      end 
      if((th_matmul == 35) && (5 == 0)) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 1;
        _saxi_resetval_0 <= 0;
      end 
      if((th_matmul == 35) && (5 == 1)) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 1;
        _saxi_resetval_1 <= 0;
      end 
      if((th_matmul == 35) && (5 == 2)) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 1;
        _saxi_resetval_2 <= 0;
      end 
      if((th_matmul == 35) && (5 == 3)) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 1;
        _saxi_resetval_3 <= 0;
      end 
      if((th_matmul == 35) && (5 == 4)) begin
        _saxi_register_4 <= 1;
        _saxi_flag_4 <= 1;
        _saxi_resetval_4 <= 0;
      end 
      if((th_matmul == 35) && (5 == 5)) begin
        _saxi_register_5 <= 1;
        _saxi_flag_5 <= 1;
        _saxi_resetval_5 <= 0;
      end 
      if((th_matmul == 35) && (5 == 6)) begin
        _saxi_register_6 <= 1;
        _saxi_flag_6 <= 1;
        _saxi_resetval_6 <= 0;
      end 
      if((th_matmul == 35) && (5 == 7)) begin
        _saxi_register_7 <= 1;
        _saxi_flag_7 <= 1;
        _saxi_resetval_7 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(_tmp_2 || _tmp_1) begin
            _tmp_5 <= (_tmp_0 >> _saxi_shift) & _saxi_mask;
          end 
          if(_tmp_2) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(_tmp_1) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_2: begin
          _saxi_register_fsm <= _saxi_register_fsm_init;
        end
      endcase
    end
  end

  localparam th_matmul_1 = 1;
  localparam th_matmul_2 = 2;
  localparam th_matmul_3 = 3;
  localparam th_matmul_4 = 4;
  localparam th_matmul_5 = 5;
  localparam th_matmul_6 = 6;
  localparam th_matmul_7 = 7;
  localparam th_matmul_8 = 8;
  localparam th_matmul_9 = 9;
  localparam th_matmul_10 = 10;
  localparam th_matmul_11 = 11;
  localparam th_matmul_12 = 12;
  localparam th_matmul_13 = 13;
  localparam th_matmul_14 = 14;
  localparam th_matmul_15 = 15;
  localparam th_matmul_16 = 16;
  localparam th_matmul_17 = 17;
  localparam th_matmul_18 = 18;
  localparam th_matmul_19 = 19;
  localparam th_matmul_20 = 20;
  localparam th_matmul_21 = 21;
  localparam th_matmul_22 = 22;
  localparam th_matmul_23 = 23;
  localparam th_matmul_24 = 24;
  localparam th_matmul_25 = 25;
  localparam th_matmul_26 = 26;
  localparam th_matmul_27 = 27;
  localparam th_matmul_28 = 28;
  localparam th_matmul_29 = 29;
  localparam th_matmul_30 = 30;
  localparam th_matmul_31 = 31;
  localparam th_matmul_32 = 32;
  localparam th_matmul_33 = 33;
  localparam th_matmul_34 = 34;
  localparam th_matmul_35 = 35;
  localparam th_matmul_36 = 36;
  localparam th_matmul_37 = 37;

  always @(posedge CLK) begin
    if(RST) begin
      th_matmul <= th_matmul_init;
      _th_matmul_matrix_size_0 <= 0;
      _th_matmul_a_offset_1 <= 0;
      _th_matmul_b_offset_2 <= 0;
      _th_matmul_c_offset_3 <= 0;
      _th_matmul_matrix_size_4 <= 0;
      _th_matmul_a_offset_5 <= 0;
      _th_matmul_b_offset_6 <= 0;
      _th_matmul_c_offset_7 <= 0;
      _th_matmul_a_addr_8 <= 0;
      _th_matmul_c_addr_9 <= 0;
      _th_matmul_i_10 <= 0;
      _tmp_9 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _th_matmul_b_addr_11 <= 0;
      _th_matmul_j_12 <= 0;
      _tmp_22 <= 0;
      _tmp_23 <= 0;
      _tmp_24 <= 0;
      _th_matmul_sum_13 <= 0;
      _th_matmul_k_14 <= 0;
      _tmp_36 <= 0;
      _th_matmul_x_15 <= 0;
      _tmp_38 <= 0;
      _th_matmul_y_16 <= 0;
      _tmp_39 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
    end else begin
      case(th_matmul)
        th_matmul_init: begin
          th_matmul <= th_matmul_1;
        end
        th_matmul_1: begin
          if(1) begin
            th_matmul <= th_matmul_2;
          end else begin
            th_matmul <= th_matmul_37;
          end
        end
        th_matmul_2: begin
          if(_saxi_register_0 == 1) begin
            th_matmul <= th_matmul_3;
          end 
        end
        th_matmul_3: begin
          _th_matmul_matrix_size_0 <= _saxi_register_1;
          th_matmul <= th_matmul_4;
        end
        th_matmul_4: begin
          _th_matmul_a_offset_1 <= _saxi_register_2;
          th_matmul <= th_matmul_5;
        end
        th_matmul_5: begin
          _th_matmul_b_offset_2 <= _saxi_register_3;
          th_matmul <= th_matmul_6;
        end
        th_matmul_6: begin
          _th_matmul_c_offset_3 <= _saxi_register_4;
          th_matmul <= th_matmul_7;
        end
        th_matmul_7: begin
          _th_matmul_matrix_size_4 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_5 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_6 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_7 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_8;
        end
        th_matmul_8: begin
          _th_matmul_a_addr_8 <= _th_matmul_a_offset_5;
          _th_matmul_c_addr_9 <= _th_matmul_c_offset_7;
          th_matmul <= th_matmul_9;
        end
        th_matmul_9: begin
          _th_matmul_i_10 <= 0;
          th_matmul <= th_matmul_10;
        end
        th_matmul_10: begin
          if(_th_matmul_i_10 < _th_matmul_matrix_size_4) begin
            th_matmul <= th_matmul_11;
          end else begin
            th_matmul <= th_matmul_35;
          end
        end
        th_matmul_11: begin
          _tmp_9 <= 0;
          _tmp_10 <= _th_matmul_a_addr_8;
          _tmp_11 <= _th_matmul_matrix_size_4;
          th_matmul <= th_matmul_12;
        end
        th_matmul_12: begin
          if(_tmp_21) begin
            th_matmul <= th_matmul_13;
          end 
        end
        th_matmul_13: begin
          _th_matmul_b_addr_11 <= _th_matmul_b_offset_6;
          th_matmul <= th_matmul_14;
        end
        th_matmul_14: begin
          _th_matmul_j_12 <= 0;
          th_matmul <= th_matmul_15;
        end
        th_matmul_15: begin
          if(_th_matmul_j_12 < _th_matmul_matrix_size_4) begin
            th_matmul <= th_matmul_16;
          end else begin
            th_matmul <= th_matmul_30;
          end
        end
        th_matmul_16: begin
          _tmp_22 <= 0;
          _tmp_23 <= _th_matmul_b_addr_11;
          _tmp_24 <= _th_matmul_matrix_size_4;
          th_matmul <= th_matmul_17;
        end
        th_matmul_17: begin
          if(_tmp_34) begin
            th_matmul <= th_matmul_18;
          end 
        end
        th_matmul_18: begin
          _th_matmul_sum_13 <= 0;
          th_matmul <= th_matmul_19;
        end
        th_matmul_19: begin
          _th_matmul_k_14 <= 0;
          th_matmul <= th_matmul_20;
        end
        th_matmul_20: begin
          if(_th_matmul_k_14 < _th_matmul_matrix_size_4) begin
            th_matmul <= th_matmul_21;
          end else begin
            th_matmul <= th_matmul_27;
          end
        end
        th_matmul_21: begin
          if(_tmp_35) begin
            _tmp_36 <= ram_a_0_rdata;
          end 
          if(_tmp_35) begin
            th_matmul <= th_matmul_22;
          end 
        end
        th_matmul_22: begin
          _th_matmul_x_15 <= _tmp_36;
          th_matmul <= th_matmul_23;
        end
        th_matmul_23: begin
          if(_tmp_37) begin
            _tmp_38 <= ram_b_0_rdata;
          end 
          if(_tmp_37) begin
            th_matmul <= th_matmul_24;
          end 
        end
        th_matmul_24: begin
          _th_matmul_y_16 <= _tmp_38;
          th_matmul <= th_matmul_25;
        end
        th_matmul_25: begin
          _th_matmul_sum_13 <= _th_matmul_sum_13 + _th_matmul_x_15 * _th_matmul_y_16;
          th_matmul <= th_matmul_26;
        end
        th_matmul_26: begin
          _th_matmul_k_14 <= _th_matmul_k_14 + 1;
          th_matmul <= th_matmul_20;
        end
        th_matmul_27: begin
          th_matmul <= th_matmul_28;
        end
        th_matmul_28: begin
          _th_matmul_b_addr_11 <= _th_matmul_b_addr_11 + (_th_matmul_matrix_size_4 << 2);
          th_matmul <= th_matmul_29;
        end
        th_matmul_29: begin
          _th_matmul_j_12 <= _th_matmul_j_12 + 1;
          th_matmul <= th_matmul_15;
        end
        th_matmul_30: begin
          _tmp_39 <= 0;
          _tmp_40 <= _th_matmul_c_addr_9;
          _tmp_41 <= _th_matmul_matrix_size_4;
          th_matmul <= th_matmul_31;
        end
        th_matmul_31: begin
          if(_tmp_60) begin
            th_matmul <= th_matmul_32;
          end 
        end
        th_matmul_32: begin
          _th_matmul_a_addr_8 <= _th_matmul_a_addr_8 + (_th_matmul_matrix_size_4 << 2);
          th_matmul <= th_matmul_33;
        end
        th_matmul_33: begin
          _th_matmul_c_addr_9 <= _th_matmul_c_addr_9 + (_th_matmul_matrix_size_4 << 2);
          th_matmul <= th_matmul_34;
        end
        th_matmul_34: begin
          _th_matmul_i_10 <= _th_matmul_i_10 + 1;
          th_matmul <= th_matmul_10;
        end
        th_matmul_35: begin
          th_matmul <= th_matmul_36;
        end
        th_matmul_36: begin
          th_matmul <= th_matmul_1;
        end
      endcase
    end
  end

  localparam _tmp_fsm_0_1 = 1;
  localparam _tmp_fsm_0_2 = 2;
  localparam _tmp_fsm_0_3 = 3;
  localparam _tmp_fsm_0_4 = 4;
  localparam _tmp_fsm_0_5 = 5;
  localparam _tmp_fsm_0_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_0 <= _tmp_fsm_0_init;
      _d1__tmp_fsm_0 <= _tmp_fsm_0_init;
      _tmp_12 <= 0;
      _tmp_14 <= 0;
      _tmp_13 <= 0;
      __tmp_fsm_0_cond_4_0_1 <= 0;
      _tmp_16 <= 0;
      _tmp_15 <= 0;
      _tmp_21 <= 0;
      __tmp_fsm_0_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_4: begin
          if(__tmp_fsm_0_cond_4_0_1) begin
            _tmp_16 <= 0;
          end 
        end
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_1_1) begin
            _tmp_21 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_matmul == 12) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          _tmp_12 <= (_tmp_10 >> 2) << 2;
          _tmp_14 <= _tmp_11;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          if((_tmp_14 <= 256) && ((_tmp_12 & 4095) + (_tmp_14 << 2) >= 4096)) begin
            _tmp_13 <= 4096 - (_tmp_12 & 4095) >> 2;
            _tmp_14 <= _tmp_14 - (4096 - (_tmp_12 & 4095) >> 2);
          end else if(_tmp_14 <= 256) begin
            _tmp_13 <= _tmp_14;
            _tmp_14 <= 0;
          end else if((_tmp_12 & 4095) + 1024 >= 4096) begin
            _tmp_13 <= 4096 - (_tmp_12 & 4095) >> 2;
            _tmp_14 <= _tmp_14 - (4096 - (_tmp_12 & 4095) >> 2);
          end else begin
            _tmp_13 <= 256;
            _tmp_14 <= _tmp_14 - 256;
          end
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          if(maxi_arready || !maxi_arvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_4;
          end 
        end
        _tmp_fsm_0_4: begin
          __tmp_fsm_0_cond_4_0_1 <= 1;
          if(maxi_rready && maxi_rvalid) begin
            _tmp_15 <= maxi_rdata;
            _tmp_16 <= 1;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast) begin
            _tmp_12 <= _tmp_12 + (_tmp_13 << 2);
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_tmp_14 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_tmp_14 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_21 <= 1;
          __tmp_fsm_0_cond_5_1_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_6;
        end
        _tmp_fsm_0_6: begin
          _tmp_fsm_0 <= _tmp_fsm_0_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_1_1 = 1;
  localparam _tmp_fsm_1_2 = 2;
  localparam _tmp_fsm_1_3 = 3;
  localparam _tmp_fsm_1_4 = 4;
  localparam _tmp_fsm_1_5 = 5;
  localparam _tmp_fsm_1_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_1 <= _tmp_fsm_1_init;
      _d1__tmp_fsm_1 <= _tmp_fsm_1_init;
      _tmp_25 <= 0;
      _tmp_27 <= 0;
      _tmp_26 <= 0;
      __tmp_fsm_1_cond_4_0_1 <= 0;
      _tmp_29 <= 0;
      _tmp_28 <= 0;
      _tmp_34 <= 0;
      __tmp_fsm_1_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_4: begin
          if(__tmp_fsm_1_cond_4_0_1) begin
            _tmp_29 <= 0;
          end 
        end
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_1_1) begin
            _tmp_34 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_matmul == 17) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_25 <= (_tmp_23 >> 2) << 2;
          _tmp_27 <= _tmp_24;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_27 <= 256) && ((_tmp_25 & 4095) + (_tmp_27 << 2) >= 4096)) begin
            _tmp_26 <= 4096 - (_tmp_25 & 4095) >> 2;
            _tmp_27 <= _tmp_27 - (4096 - (_tmp_25 & 4095) >> 2);
          end else if(_tmp_27 <= 256) begin
            _tmp_26 <= _tmp_27;
            _tmp_27 <= 0;
          end else if((_tmp_25 & 4095) + 1024 >= 4096) begin
            _tmp_26 <= 4096 - (_tmp_25 & 4095) >> 2;
            _tmp_27 <= _tmp_27 - (4096 - (_tmp_25 & 4095) >> 2);
          end else begin
            _tmp_26 <= 256;
            _tmp_27 <= _tmp_27 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(maxi_arready || !maxi_arvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          __tmp_fsm_1_cond_4_0_1 <= 1;
          if(maxi_rready && maxi_rvalid) begin
            _tmp_28 <= maxi_rdata;
            _tmp_29 <= 1;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast) begin
            _tmp_25 <= _tmp_25 + (_tmp_26 << 2);
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_tmp_27 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_tmp_27 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_34 <= 1;
          __tmp_fsm_1_cond_5_1_1 <= 1;
          _tmp_fsm_1 <= _tmp_fsm_1_6;
        end
        _tmp_fsm_1_6: begin
          _tmp_fsm_1 <= _tmp_fsm_1_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_2_1 = 1;
  localparam _tmp_fsm_2_2 = 2;
  localparam _tmp_fsm_2_3 = 3;
  localparam _tmp_fsm_2_4 = 4;
  localparam _tmp_fsm_2_5 = 5;
  localparam _tmp_fsm_2_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_2 <= _tmp_fsm_2_init;
      _d1__tmp_fsm_2 <= _tmp_fsm_2_init;
      _tmp_42 <= 0;
      _tmp_44 <= 0;
      _tmp_43 <= 0;
      _tmp_60 <= 0;
      __tmp_fsm_2_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_0_1) begin
            _tmp_60 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_matmul == 31) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_42 <= (_tmp_40 >> 2) << 2;
          _tmp_44 <= _tmp_41;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_44 <= 256) && ((_tmp_42 & 4095) + (_tmp_44 << 2) >= 4096)) begin
            _tmp_43 <= 4096 - (_tmp_42 & 4095) >> 2;
            _tmp_44 <= _tmp_44 - (4096 - (_tmp_42 & 4095) >> 2);
          end else if(_tmp_44 <= 256) begin
            _tmp_43 <= _tmp_44;
            _tmp_44 <= 0;
          end else if((_tmp_42 & 4095) + 1024 >= 4096) begin
            _tmp_43 <= 4096 - (_tmp_42 & 4095) >> 2;
            _tmp_44 <= _tmp_44 - (4096 - (_tmp_42 & 4095) >> 2);
          end else begin
            _tmp_43 <= 256;
            _tmp_44 <= _tmp_44 - 256;
          end
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(maxi_awready || !maxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_4;
          end 
        end
        _tmp_fsm_2_4: begin
          if(_tmp_58 && maxi_wvalid && maxi_wready) begin
            _tmp_42 <= _tmp_42 + (_tmp_43 << 2);
          end 
          if(_tmp_58 && maxi_wvalid && maxi_wready && (_tmp_44 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(_tmp_58 && maxi_wvalid && maxi_wready && (_tmp_44 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_60 <= 1;
          __tmp_fsm_2_cond_5_0_1 <= 1;
          _tmp_fsm_2 <= _tmp_fsm_2_6;
        end
        _tmp_fsm_2_6: begin
          _tmp_fsm_2 <= _tmp_fsm_2_init;
        end
      endcase
    end
  end


endmodule



module ram_a
(
  input CLK,
  input [10-1:0] ram_a_0_addr,
  output [32-1:0] ram_a_0_rdata,
  input [32-1:0] ram_a_0_wdata,
  input ram_a_0_wenable
);

  reg [10-1:0] ram_a_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_0_wenable) begin
      mem[ram_a_0_addr] <= ram_a_0_wdata;
    end 
    ram_a_0_daddr <= ram_a_0_addr;
  end

  assign ram_a_0_rdata = mem[ram_a_0_daddr];

endmodule



module ram_b
(
  input CLK,
  input [10-1:0] ram_b_0_addr,
  output [32-1:0] ram_b_0_rdata,
  input [32-1:0] ram_b_0_wdata,
  input ram_b_0_wenable
);

  reg [10-1:0] ram_b_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_0_wenable) begin
      mem[ram_b_0_addr] <= ram_b_0_wdata;
    end 
    ram_b_0_daddr <= ram_b_0_addr;
  end

  assign ram_b_0_rdata = mem[ram_b_0_daddr];

endmodule



module ram_c
(
  input CLK,
  input [10-1:0] ram_c_0_addr,
  output [32-1:0] ram_c_0_rdata,
  input [32-1:0] ram_c_0_wdata,
  input ram_c_0_wenable
);

  reg [10-1:0] ram_c_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_0_wenable) begin
      mem[ram_c_0_addr] <= ram_c_0_wdata;
    end 
    ram_c_0_daddr <= ram_c_0_addr;
  end

  assign ram_c_0_rdata = mem[ram_c_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_matmul_ipcore.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
