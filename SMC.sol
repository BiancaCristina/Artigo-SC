pragma solidity >=0.4.25 <0.6.0;

contract SMC {
  enum StatesSMC { State1}

  // por algum motivo da erro quando uso [4][3]...
  // https://github.com/ethereum/solidity/issues/8364
  bool[3][4] TruthTable;
  bool[3][4] TruthTableA;
  bool[3][4] TruthTableB;

  StatesSMC myState;
    
  

  constructor(bool[12] memory _tt, bool[12] memory _tta) public {
    for (uint i=0;i<4;i++) {
       for (uint j=0;j<3;j++) {
	   TruthTable[i][j]  = _tt[i*3+j];
	   TruthTableA[i][j]  = _tta[i*3+j];
       }
    }  
  }

  function receivesTableFromB(bool[12] memory _tt) public {
  }

  function receivesLinesFromA(uint l1, uint l2) public {
  //apenas guarda os valores recebidos
  }

  function receivesLinesFromB(uint l1, uint l2) public {
  }

  function receivesInversionFromA() public {
  }

  function receivesInversionFromB() public {
  }


  function getValue() public returns (bool) {
  // juntas as linhas de A e B
  // aplica as inversoes
  // e retorna
  }
  

  // gets TT uploaded by A
  function getTTA() public returns (bool[3][4] memory) {
	   return TruthTableA;
  }

  
  
}
