@pytest.mark.parametrize("reaction,rxntype",[
("(NH2)2CO + H2O = 2 NH3 + CO2","uncategorized"),
("(NH4)2SO4 + 2 NaClO4 = 2 NH4ClO4 + Na2SO4","double replacement"),
("10 FeSO4 + 2 KMnO4 + 8 H2SO4 = 5 Fe2(SO4)3 + 2 MnSO4 + K2SO4 + 8 H2O","uncategorized"),
("10 HSiCl3 + 15 H2O = H10Si10O15 + 30 HCl","uncategorized"),
("10 KClO3 + 3 P4 = 3 P4O10 + 10 KCl","uncategorized"),
("10 Na + 2 NaNO3 = 6 Na2O + N2","single replacement"),
("10 Rb + 2 RbNO3 = 6 Rb2O + N2","single replacement"),
("12 HClO4 + P4O10 = 4 H3PO4 + 6 Cl2O7","uncategorized"),
("15 C18H32O2 + 44 CH3OH = 16 C17H34O2 + 14 C3H8O3","uncategorized"),
("16 Al + 3 S8 = 8 Al2S3","synthesis"),
("16 Cu + S8 = 8 Cu2S","synthesis"),
("2 Ag(OH) + H2SO3 = Ag2SO3 + 2 H2O","double replacement"),
("2 Ag2CO3 = 4 Ag + 2 CO2 + O2","decomposition"),
("2 Ag2O + 2 S = 2 Ag2S + O2","uncategorized"),
("2 Ag2O = 4 Ag + O2","decomposition"),
("2 AgNO3 + Na2CO3 = Ag2CO3 + 2 NaNO3","double replacement"),
("2 AgNO3 + Na2S = Ag2S + 2 NaNO3","double replacement"),
("2 AgNO3 + ZnCl2 = 2 AgCl + Zn(NO3)2","double replacement"),
("2 Al + 2 NaOH + 2 H2O = 2 NaAlO2 + 3 H2","uncategorized"),
("2 Al + 3 Br2 = 2 AlBr3","synthesis"),
("2 Al + 3 Cl2 = 2 AlCl3","synthesis"),
("2 Al + 3 CuCl2 = 2 AlCl3 + 3 Cu","single replacement"),
("2 Al + 3 CuO = Al2O3 + 3 Cu","single replacement"),
("2 Al + 3 F2 = 2 AlF3","synthesis"),
("2 Al + 3 FeCl2 = 2 AlCl3 + 3 Fe","single replacement"),
("2 Al + 3 H2S = Al2S3 + 3 H2","single replacement"),
("2 Al + 3 H2SO4 = Al2(SO4)3 + 3 H2","single replacement"),
("2 Al + 3 Pb(NO3)2 = 2 Al(NO3)3 + 3 Pb","single replacement"),
("2 Al + 3 ZnCl2 = 2 AlCl3 + 3 Zn","single replacement"),
("2 Al + 6 HCl = 2 AlCl3 + 3 H2","single replacement"),
("2 Al + Cr2O3 = Al2O3 + 2 Cr","single replacement"),
("2 Al + Fe2O3 = Al2O3 + 2 Fe","single replacement"),
("2 Al + I2 = 2 AlI","synthesis"),
("2 Al(OH)3 + 3 H2CO3 = Al2(CO3)3 + 6 H2O","double replacement"),
("2 Al(OH)3 + 3 H2SO4 = Al2(SO4)3 + 6 H2O","double replacement"),
("2 Al(OH)3 = Al2O3 + 3 H2O","decomposition"),
("2 AlCl3 + 3 H2S = Al2S3 + 6 HCl","double replacement"),
("2 AlCl3 = 2 Al + 3 Cl2","decomposition"),
("2 Au2O3 = 4 Au + 3 O2","decomposition"),
("2 B + 3 F2 = 2 BF3","synthesis"),
("2 B5H9 + 12 O2 = 5 B2O3 + 9 H2O","uncategorized"),
("2 C + 2 H2O = CH4 + CO2","uncategorized"),
("2 C + O2 = 2 CO","synthesis"),
("2 C10H22 + 31 O2 = 20 CO2 + 22 H2O","combustion"),
("2 C2H2 + 5 O2 = 4 CO2 + 2 H2O","combustion"),
("2 C2H2O2 + 3 O2 = 4 CO2 + 2 H2O","combustion"),
("2 C2H4 + O2 + 4 HCl = 2 C2H4Cl2 + 2 H2O","uncategorized"),
("2 C2H6 + 7 O2 = 4 CO2 + 6 H2O","combustion"),
("2 C2H6 + 7 O2 = 4 CO2 + 6 H2O","combustion"),
("2 C3H2 + 7 O2 = 6 CO2 + 2 H2O","combustion"),
("2 C3H6 + 2 NH3 + 3 O2 = 2 C3H3N + 6 H2O","uncategorized"),
("2 C3H6 + 9 O2 = 6 CO2 + 6 H2O","combustion"),
("2 C3H7OH + 9 O2 = 6 CO2 + 8 H2O","combustion"),
("2 C4H10 + 13 O2 = 8 CO2 + 10 H2O","combustion"),
("2 C4H10 + 5 O2 = 4 CH3COOH + 2 H2O","combustion"),
("2 C4H10 + 13 O2 = 8 CO2 + 10 H2O","combustion"),
("2 C4H10 + 13 O2 = 8 CO2 + 10 HOH","combustion"),
("2 C5H12 + 11 O2 = 10 CO + 12 H2O","combustion"),
("2 C6H6 + 15 O2 = 12 CO2 + 6 H2O","combustion"),
("2 C7H6O2 + 15 O2 = 14 CO2 + 6 H2O","combustion"),
("2 C8H10 + 21 O2 = 16 CO2 + 10 H2O","combustion"),
("2 C8H18 + 25 O2 = 16 CO2 + 18 H2O","combustion"),
("2 CH3CH2CH2OH + 9 O2 = 6 CO2 + 8 H2O","combustion"),
("2 CH3CH3 + 7 O2 = 4 CO2 + 6 H2O","combustion"),
("2 CH3COOH + CaO = (CH3COO)2Ca + H2O","uncategorized"),
("2 CH4 = C2H2 + 3 H2","decomposition"),
("2 CO + 2 NO = 2 CO2 + N2","uncategorized"),
("2 CO + O2 = 2 CO2","synthesis"),
("2 Ca + O2 = 2 CaO","synthesis"),
("2 CaO + 2 SO2 + O2 = 2 CaSO4","synthesis"),
("2 CaO = 2 Ca + O2","decomposition"),
("2 CeO2 + 2 KI + 8 HCl = 2 KCl + 2 CeCl3 + 4 H2O + I2","uncategorized"),
("2 Cl + Ba = BaCl2","synthesis"),
("2 CoSO4 + 7 Na2S2O4 + 12 H2O = 2 CoS2 + 12 H2SO4 + 14 Na","uncategorized"),
("2 Cr + 3 O2 = 2 CrO3","synthesis"),
("2 Cr2O3 + 3 Si = 4 Cr + 3 SiO2","single replacement"),
("2 CrO3 + 3 C = 2 Cr + 3 CO2","single replacement"),
("2 Cu + O2 = 2 CuO","synthesis"),
("2 Cu + S = Cu2S","synthesis"),
("2 Cu(NO3)2 = 2 CuO + 4 NO2 + O2","decomposition"),
("2 Cu2S + 3 O2 = 2 Cu2O + 2 SO2","uncategorized"),
("2 CuFeS2 + 5 O2 = 2 Cu + 2 FeO + 4 SO2","uncategorized"),
("2 CuO = 2 Cu + O2","decomposition"),
("2 F2 + 2 H2O = 4 HF + O2","uncategorized"),
("2 Fe + 3 Cl2 = 2 FeCl3","synthesis"),
("2 Fe + 3 H2SO4 = Fe2(SO4)3 + 3 H2","single replacement"),
("2 Fe + 3 S = Fe2S3","synthesis"),
("2 Fe(OH)3 + 3 H2SO4 = Fe2(SO4)3 + 6 H2O","double replacement"),
("2 Fe(OH)3 + P2O5 = 2 FePO4 + 3 H2O","uncategorized"),
("2 Fe(OH)3 = Fe2O3 + 3 H2O","decomposition"),
("2 Fe + 3 H2SO4 = Fe2(SO4)3 + 3 H2","single replacement"),
("2 Fe2O3 + 3 C = 4 Fe + 3 CO2","single replacement"),
("2 Fe2O3 = 4 Fe + 3 O2","decomposition"),
("2 FeBr3 + 3 H2SO4 = Fe2(SO4)3 + 6 HBr","double replacement"),
("2 FeBr3 = 2 Fe + 3 Br2","decomposition"),
("2 FeCl2 + Cl2 = 2 FeCl3","synthesis"),
("2 FeCl3 + 3 Na2CO3 = 6 NaCl + Fe2(CO3)3","double replacement"),
("2 FeCl3 + 3 Na2CO3 = Fe2(CO3)3 + 6 NaCl","double replacement"),
("2 FeCl3 + 3(NH4)2S = Fe2S3 + 6 NH4Cl","double replacement"),
("2 GaBr3 + 3 Na2SO3 = Ga2(SO3)3 + 6 NaBr","double replacement"),
("2 H + NO = H2O + N","uncategorized"),
("2 H2 + O2 = 2 H2O","synthesis"),
("2 H2 + O2 = 2 H2O","synthesis"),
("2 H2O = 2 H2 + O2","decomposition"),
("2 H2O2 = 2 H2O + O2","decomposition"),
("2 H2O2 = O2 + 2 H2O","decomposition"),
("2 H2S + 3 O2 = 2 SO2 + 2 H2O","uncategorized"),
("2 H2S + O2 = 2 H2O + 2 S","uncategorized"),
("2 H2S + 3 O2 = 2 SO2 + 2 H2O","uncategorized"),
("2 H2S + O2 = 2 H2O + 2 S","uncategorized"),
("2 H3PO4 + 3 Mg(OH)2 = Mg3(PO4)2 + 6 H2O","double replacement"),
("2 HBr + Ba(OH)2 = BaBr2 + 2 H2O","double replacement"),
("2 HCl + Ba(OH)2 = BaCl2 + 2 H2O","double replacement"),
("2 HCl + Ca(OH)2 = CaCl2 + 2 H2O","double replacement"),
("2 HCl + CaCO3 = CaCl2 + H2O + CO2","uncategorized"),
("2 HCl + Mg(OH)2 = 2 H2O + MgCl2","double replacement"),
("2 HCl + Mg(OH)2 = MgCl2 + 2 H2O","double replacement"),
("2 HCl + 2 Mg = H2 + 2 MgCl","single replacement"),
("2 HClO4 + Ba(OH)2 = Ba(ClO4)2 + 2 H2O","double replacement"),
("2 HClO4 + Ca(OH)2 = Ca(ClO4)2 + 2 H2O","double replacement"),
("2 HNO3 + 3 H3AsO3 = 2 NO + 3 H3AsO4 + H2O","uncategorized"),
("2 HNO3 + Ba(OH)2 = Ba(NO3)2 + 2 H2O","double replacement"),
("2 HNO3 + Mg(OH)2 = 2 H2O + Mg(NO3)2","double replacement"),
("2 Hg + O2 = 2 HgO","synthesis"),
("2 HgO + Cl2 = 2 HgCl + O2","uncategorized"),
("2 HgO = 2 Hg + O2","decomposition"),
("2 I2O5 = 2 I2 + 5 O2","decomposition"),
("2 K + 2 H2O = 2 KOH + H2","single replacement"),
("2 K + 2 NH3 = 2 KNH2 + H2","uncategorized"),
("2 K + Cl2 = 2 KCl","synthesis"),
("2 K + S = K2S","synthesis"),
("2 K2CrO4 + 2 HCl = K2Cr2O7 + 2 KCl + H2O","uncategorized"),
("2 K3PO4 + 3 Ca(NO3)2 = Ca3(PO4)2 + 6 KNO3","double replacement"),
("2 KCIO3 = 2 KCI + 3 O2","decomposition"),
("2 KCl + F2 = 2 KF + Cl2","single replacement"),
("2 KCl + H2O = K2O + 2 HCl","uncategorized"),
("2 KClO3 = 2 KCl + 3 O2","decomposition"),
("2 KI + Cl2 = 2 KCl + I2","single replacement"),
("2 KI + H2O2 = 2 KOH + I2","uncategorized"),
("2 KI + PbSO4 = K2SO4 + PbI2","double replacement"),
("2 KMnO4 + 16 HCl = 2 KCl + 2 MnCl2 + 8 H2O + 5 Cl2","uncategorized"),
("2 KMnO4 = K2MnO4 + MnO2 + O2","decomposition"),
("2 KNO3 = 2 KNO2 + O2","decomposition"),
("2 KOH + H2CO3 = 2 H2O + K2CO3","double replacement"),
("2 Li + 2 H2O = 2 LiOH + H2","single replacement"),
("2 Li2O = 4 Li + O2","decomposition"),
("2 LiBr = 2 Li + Br2","decomposition"),
("2 LiOH + CO2 = Li2CO3 + H2O","uncategorized"),
("2 Mg + O2 = 2 MgO","synthesis"),
("2 MnO2 + CO = Mn2O3 + CO2","uncategorized"),
("2 N2 + 3 O2 = 2 N2O3","synthesis"),
("2 N2 + 5 O2 = 2 N2O5","synthesis"),
("2 N2 + 6 H2O = 4 NH3 + 3 O2","uncategorized"),
("2 N2 + O2 = 2 N2O","synthesis"),
("2 N2O + 3 O2 = 4 NO2","synthesis"),
("2 N2O5 = 4 NO2 + O2","decomposition"),
("2 NH3 + CO2 = CO(NH2)2 + H2O","uncategorized"),
("2 NH3 + H2SO4 = (NH4)2SO4","synthesis"),
("2 NH3 = N2 + 3 H2","decomposition"),
("2 NH4 + 3 O2 = 2 NO + 4 H2O","uncategorized"),
("2 NO + 2 CO = N2 + 2 CO2","uncategorized"),
("2 NO + O2 = 2 NO2","synthesis"),
("2 NO2 + 4 CO = N2 + 4 CO2","uncategorized"),
("2 NO2 + O2 = 2 NO3","synthesis"),
("2 NO2 = 2 NO + O2","decomposition"),
("2 Na + 2 H2O = 2 NaOH + H2","single replacement"),
("2 Na + Br2 = 2 NaBr","synthesis"),
("2 Na + SO4 = Na2SO4","synthesis"),
("2 Na2CO3 + 2 PbSO4 + C = 2 Na2SO4 + 3 CO2 + 2 Pb","uncategorized"),
("2 Na3PO4 + 3 BaCl2 = Ba3(PO4)2 + 6 NaCl","double replacement"),
("2 NaBr + Ca(OH)2 = CaBr2 + 2 NaOH","double replacement"),
("2 NaC2H3O2 + H2CO3 = Na2CO3 + 2 HC2H3O2","double replacement"),
("2 NaCN + H2SO4 = Na2SO4 + 2 HCN","double replacement"),
("2 NaCl + 2 H2O = 2 NaOH + Cl2 + H2","uncategorized"),
("2 NaCl + H2SO4 = Na2SO4 + 2 HCl","double replacement"),
("2 NaCl + Pb(NO3)2 = PbCl2 + 2 NaNO3","double replacement"),
("2 NaClO2 + Cl2 = 2 ClO2 + 2 NaCl","uncategorized"),
("2 NaHCO3 = Na2CO3 + CO2 + H2O","decomposition"),
("2 NaI + Cl2 = 2 NaCl + I2","single replacement"),
("2 NaNO3 = 2 NaNO2 + O2","decomposition"),
("2 NaOH + CO2 = Na2CO3 + H2O","uncategorized"),
("2 NaOH + H2PO3 = Na2PO3 + 2 H2O","double replacement"),
("2 P + 3 Cl2 = 2 PCl3","synthesis"),
("2 PBO + C = 2 PB + CO2","uncategorized"),
("2 Pb(NO3)2 = 2 PbO + 4 NO2 + O2","decomposition"),
("2 PbO + 2 SO2 = 2 PbS + 3 O2","uncategorized"),
("2 PbO + C = 2 Pb + CO2","single replacement"),
("2 PbO = 2 Pb + O2","decomposition"),
("2 Rb2O = 4 Rb + O2","decomposition"),
("2 SO2 + O2 = 2 SO3","synthesis"),
("2 Zn + O2 = 2 ZnO","synthesis"),
("2 ZnS + 3 O2 = 2 ZnO + 2 SO2","uncategorized"),
("2(NH4)3PO4 + 3 MgO = Mg3(PO4)2 + 3 H2O + 6 NH3","uncategorized"),
("3 Al + 3 NH4ClO4 = Al2O3 + AlCl3 + 3 NO + 6 H2O","uncategorized"),
("3 BaCl2 + Al2(SO4)3 = 3 BaSO4 + 2 AlCl3","double replacement"),
("3 BaO + 2 H3PO4 = Ba3(PO4)2 + 3 H2O","double replacement"),
("3 Br2 + S + 4 H2O = 6 HBr + H2SO4","uncategorized"),
("3 C12H24O2 + CH3OH = 2 C17H34O2 + C3H8O3","uncategorized"),
("3 C2H5COOH + Al(OH)3 = (C2H5COO)3Al + 3 H2O","uncategorized"),
("3 C6H12 + 4 KMnO4 + 2 H2O = 3 C6H12O2 + 4 MnO2 + 4 KOH","uncategorized"),
("3 Ca + 2 FeCl3 = 3 CaCl2 + 2 Fe","single replacement"),
("3 CaCl2 + 2 K3PO4 = Ca3(PO4)2 + 6 KCl","double replacement"),
("3 CaO + P2O5 = Ca3(PO4)2","synthesis"),
("3 Cl2 + 6 KOH = 5 KCl + KClO3 + 3 H2O","uncategorized"),
("3 Co2 + 2 H2 = 2 H2Co3","synthesis"),
("3 CoSO4 + 7 Na2S2O3 + 11 H2O = 3 CoS2 + 11 H2SO4 + 14 Na","uncategorized"),
("3 Cu + 8 HNO3 = 3 Cu(NO3)2 + 2 NO + 4 H2O","uncategorized"),
("3 Fe + 2 O2 = Fe3O4","synthesis"),
("3 Fe(OH)2 + 2 H3PO4 = Fe3(PO4)2 + 6 H2O","double replacement"),
("3 Fe + 4 H2O = Fe3O4 + 4 H2","single replacement"),
("3 H2 + Fe2O3 = 2 Fe + 3 H2O","single replacement"),
("3 H2 + SO2 = H2S + 2 H2O","uncategorized"),
("3 Hg(OH)2 + 2 H3AsO4 = Hg3(AsO4)2 + 6 H2O","double replacement"),
("3 K + Al(NO3)3 = Al + 3 KNO3","single replacement"),
("3 K2MnO4 + 2 H2O = 2 KMnO4 + MnO2 + 4 KOH","uncategorized"),
("3 KOH + H3PO4 = K3PO4 + 3 H2O","double replacement"),
("3 Li2O + 2 H3PO4 = 2 Li3PO4 + 3 H2O","double replacement"),
("3 Mg + 2 H3PO4 = Mg3(PO4)2 + 3 H2","single replacement"),
("3 Mg + 2 H3PO4 = Mg3(PO4)2 + 6 H","single replacement"),
("3 Mg + N2 = Mg3N2","synthesis"),
("3 NO2 + H2O = 2 HNO3 + NO","uncategorized"),
("3 NO2 + H2O = 2 NHO3 + NO","uncategorized"),
("3 Na + FeCl3 = 3 NaCl + Fe","single replacement"),
("3 NaOH + H3AsO4 = Na3AsO4 + 3 H2O","double replacement"),
("3 NaOH + H3PO4 = Na3PO4 + 3 H2O","double replacement"),
("3 P + 5 HNO3 + 2 H2O = 3 H3PO4 + 5 NO","uncategorized"),
("3 PbCl4 + 4 Al(NO3)3 = 3 Pb(NO3)4 + 4 AlCl3","double replacement"),
("3 Zn + 2 P = Zn3P2","synthesis"),
("3(NH4)2CO3 + 2 Al(NO3)3 = 6 NH4NO3 + Al2(CO3)3","double replacement"),
("30 C18H30O2 + 133 CH3OH = 32 C17H34O2 + 43 C3H8O3","uncategorized"),
("30 C18H34O2 + 43 CH3OH = 32 C17H34O2 + 13 C3H8O3","uncategorized"),
("30 CO2 + 3 H20 = 5 C6H12O6 + 15 O2","uncategorized"),
("4 Ag + 2 H2S + O2 = 2 Ag2S + 2 H2O","uncategorized"),
("4 Al + 3 O2 = 2 Al2O3","synthesis"),
("4 Au + 8 NaCN + O2 + 2 H2O = 4 NaAu(CN)2 + 4 NaOH","uncategorized"),
("4 C + S8 = 4 CS2","synthesis"),
("4 C3H5(NO3)3 = 12 CO2 + 10 H2O + 6 N2 + O2","decomposition"),
("4 C3H5(NO3)3 = 12 CO2 + 6 N2 + 10 H2O + O2","decomposition"),
("4 C3H5N3O9 = 12 CO2 + 5 N2 + 2 NO + 10 H2O","decomposition"),
("4 C3H5N3O9 = 12 CO2 + 6 N2 + O2 + 10 H2O","decomposition"),
("4 C6H12 + 15 O2 = 4 H2C6H3O4 + 14 H2O","combustion"),
("4 CH3O2 + 3 O2 = 4 CO2 + 6 H2O","combustion"),
("4 CO2 + 6 H2O = 2 C2H6 + 7 O2","uncategorized"),
("4 CoSO4 + 7 Na2S2O3 + 3 H2O = 4 CoS2 + 3 H2SO4 + 7 Na2SO4","uncategorized"),
("4 CuO + CH4 = 4 Cu + CO2 + 2 H2O","uncategorized"),
("4 Fe + 3 O2 = 2 Fe2O3","synthesis"),
("4 FeS + 7 O2 = 2 Fe2O3 + 4 SO2","uncategorized"),
("4 FeS2 + 11 O2 = 2 Fe2O3 + 8 SO2","uncategorized"),
("4 H2SiCl2 + 4 H2O = H8Si4O4 + 8 HCl","uncategorized"),
("4 HCN + 5 O2 = 2 N2 + 4 CO2 + 2 H2O","uncategorized"),
("4 HCl + O2 = 2 Cl2 + 2 H2O","uncategorized"),
("4 HCl + O2 = 2 H2O + 2 Cl2","uncategorized"),
("4 HCl + O2 = 2 H2O + 4 Cl","uncategorized"),
("4 HCl + O2 = 4 Cl + 2 H2O","uncategorized"),
("4 HNO3 = 4 NO2 + 2 H2O + O2","decomposition"),
("4 K + O2 = 2 K2O","synthesis"),
("4 KClO3 = 3 KClO4 + KCl","decomposition"),
("4 Li + O2 = 2 Li2O","synthesis"),
("4 NH3 + 3 O2 = 2 N2 + 6 H2O","uncategorized"),
("4 NH3 + 5 O2 = 4 NO + 6 H2O","uncategorized"),
("4 NH3 + 7 O2 = 2 N2O4 + 6 H2O","uncategorized"),
("4 NH3 + 7 O2 = 4 NO2 + 6 H2O","uncategorized"),
("4 NO2 + O2 + 2 H2O = 4 HNO3","synthesis"),
("4 Na + O2 = 2 Na2O","synthesis"),
("4 Zn + 10 HNO3 = 4 Zn(NO3)2 + NH4NO3 + 3 H2O","uncategorized"),
("4 Zn + 5 H2SO4 = 4 ZnSO4 + H2S + 4 H2O","uncategorized"),
("5 C14H20O2 + 31 CH3OH = 4 C17H34O2 + 11 C3H8O3","uncategorized"),
("5 NaBr + NaBrO3 + 3 H2SO4 = 3 Br2 + 3 Na2SO4 + 3 H2O","uncategorized"),
("6 CO2 + 6 H2O = C6H12O6 + 6 O2","uncategorized"),
("6 Cs + N2 = 2 Cs3N","synthesis"),
("6 KNO3 + Sn3(PO4)2 = 2 K3PO4 + 3 Sn(NO3)2","double replacement"),
("6 Li + N2 = 2 Li3N","synthesis"),
("6 Mg + P4 = 2 Mg3P2","synthesis"),
("6 NO2 + 8 HNCO = 7 N2 + 8 CO2 + 4 H2O","uncategorized"),
("6 S2Cl2 + 4 NH4Cl = S4N4 + 8 S + 16 HCl","uncategorized"),
("8 Fe + S8 = 8 FeS","synthesis"),
("Ag + Br = AgBr","synthesis"),
("Ag2S + 2 HCl = 2 AgCl + H2S","double replacement"),
("Ag2SO4 + 2 NaCl = 2 AgCl + Na2SO4","double replacement"),
("AgCl = Ag + Cl","decomposition"),
("AgNO3 + HCl = AgCl + HNO3","double replacement"),
("AgNO3 + NaCl = AgCl + NaNO3","double replacement"),
("Al + 3 Cl = AlCl3","synthesis"),
("Al + Cu2S = 2 Cu + AlS","single replacement"),
("Al(OH)3 + 3 HBr = AlBr3 + 3 H2O","double replacement"),
("Al(OH)3 + 3 HPO3 = Al(PO3)3 + 3 H2O","double replacement"),
("Al2(SO4)3 + 3 Ca(OH)2 = 2 Al(OH)3 + 3 CaSO4","double replacement"),
("Al2(SO4)3 + 3 MgO = Al2O3 + 3 MgSO4","double replacement"),
("Al2(SO4)3 + 3 NaAl2O3 + 15 H2O = 8 Al(OH)3 + 3 NaSO4 + 3 H2","uncategorized"),
("Al2(SO4)3 + 6 NaCl = 2 AlCl3 + 3 Na2SO4","double replacement"),
("Al2(SO4)3 + 6 NaOH = 2 Al(OH)3 + 3 Na2SO4","double replacement"),
("Al2O3 + 3 H2SO4 = Al2(SO4)3 + 3 H2O","double replacement"),
("Al2S3 + 6 H2O = 2 Al(OH)3 + 3 H2S","uncategorized"),
("AlCl3 + 3 H2O = Al(OH)3 + 3 HCl","uncategorized"),
("AlCl3 + 3 NH3 + 3 H2O = Al(OH)3 + 3 NH4Cl","uncategorized"),
("AlCl3 + 3 NaOH = Al(OH)3 + 3 NaCl","double replacement"),
("As2O5 + 3 H2O = 2 H3AsO4","synthesis"),
("Au2S3 + 3 H2 = 2 Au + 3 H2S","uncategorized"),
("B2O3 + 3 H2O = 2 H3BO3","synthesis"),
("Ba(OH)2 + H2SO4 = BaSO4 + 2 H2O","double replacement"),
("BaCO3 = BaO + CO2","decomposition"),
("BaCl2 + K2(CO3) = Ba(CO3) + 2 KCl","double replacement"),
("BaCl2 + Na2CO3 = BaCO3 + 2 NaCl","double replacement"),
("BaCl2 + Na2SO4 = BaSO4 + 2 NaCl","double replacement"),
("BaO + H2O = Ba(OH)2","synthesis"),
("BaO2 + 2 HCl = H2O2 + BaCl2","double replacement"),
("BaS + PtF2 = BaF2 + PtS","double replacement"),
("Bi + 4 HNO3 = Bi(NO3)3 + NO + 2 H2O","uncategorized"),
("C + HCl = HCCl","synthesis"),
("C + O2 = CO2","synthesis"),
("C15H31COOH + 23 O2 = 16 CO2 + 16 H2O","combustion"),
("C25H52 + 38 O2 = 25 CO2 + 26 H2O","combustion"),
("C2H4 + 3 O2 = 2 CO2 + 2 H2O","combustion"),
("C2H4O2 + 2 O2 = 2 CO2 + 2 H2O","combustion"),
("C2H5OH + 2 O2 = 2 CO + 3 H2O","combustion"),
("C2H5OH + 3 O2 = 2 CO2 + 3 H2O","combustion"),
("C2H6O + 3 O2 = 2 CO2 + 3 H2O","combustion"),
("C3H8 + 5 O2 = 3 CO2 + 4 H2O","combustion"),
("C3H8O3 + 3 HNO3 = C3H5N3O9 + 3 H2O","uncategorized"),
("C4H10O + 6 O2 = 4 CO2 + 5 H2O","combustion"),
("C4H6O3 + H2O = 2 C2H4O2","synthesis"),
("C4H8 + 6 O2 = 4 CO2 + 4 H2O","combustion"),
("C5H12 + 8 O2 = 5 CO2 + 6 H2O","combustion"),
("C5H8O2 + 2 NaH + 2 HCl = C5H12O2 + 2 NaCl","uncategorized"),
("C6H10O5 + 6 O2 = 6 CO2 + 5 H2O","combustion"),
("C6H12 + 9 O2 = 6 CO2 + 6 H2O","combustion"),
("C6H12O6 + 6 O2 = 6 CO2 + 6 H2O","combustion"),
("C7H16 + 11 O2 = 7 CO2 + 8 H2O","combustion"),
("C8H8O3 + H2O = C7H6O3 + CH3OH","uncategorized"),
("CF4 + 2 Br2 = CBr4 + 2 F2","uncategorized"),
("CH3CH2OH + 3 O2 = 2 CO2 + 3 H2O","combustion"),
("CH3COOH + LiOH = H2O + LiC2H3O2","uncategorized"),
("CH3COOH + NaHCO3 = CH3COONa + H2CO3","uncategorized"),
("CH3COOH + NaHCO3 = NaC2H3O2 + H2O + CO2","uncategorized"),
("CH3COOH + NaOH = NaCH3COO + H2O","uncategorized"),
("CH4 + 2 O2 = CO2 + 2 H2O","combustion"),
("CH4 + 4 CuO = 4 Cu + CO2 + 2 H2O","uncategorized"),
("CH4 + 4 S = CS2 + 2 H2S","uncategorized"),
("CH4 + Cl2 = CH3Cl + HCl","uncategorized"),
("CH4 + H2O = CO + 3 H2","uncategorized"),
("CO + 2 H2 = CH3OH","synthesis"),
("CO(NH2)2 + 2 NaOH = Na2CO3 + 2 NH3","uncategorized"),
("CO2 + 2 LiOH = Li2CO3 + H2O","uncategorized"),
("CO2 + C = 2 CO","synthesis"),
("CO2 + H2O = H2CO3","synthesis"),
("CS2 + 3 O2 = CO2 + 2 SO2","uncategorized"),
("CUCO3 + H2SO4 = CUSO4 + H2O + CO2","uncategorized"),
("Ca + 2 H2O = Ca(OH)2 + H2","single replacement"),
("Ca + 2 OH = Ca(OH)2","synthesis"),
("Ca + F2 = CaF2","synthesis"),
("Ca(HCO3)2 + 2 HCl = CaCl2 + 2 CO2 + 2 H2O","uncategorized"),
("Ca(HCO3)2 + Ca(OH)2 = 2 CaCO3 + 2 H2O","double replacement"),
("Ca(NO3)2 + 2 NaCl = CaCl2 + 2 NaNO3","double replacement"),
("Ca(NO3)2 + Na2O = CaO + 2 NaNO3","double replacement"),
("Ca(NO3)2 + Na2SO4 = CaSO4 + Na2(NO3)2","double replacement"),
("Ca(NO3)2 + Na2SO4 = CaSO4 + Na2(NO3)2","double replacement"),
("Ca(OH)2 + 2 CH3COOH = Ca(CH3COO)2 + 2 H2O","uncategorized"),
("Ca(OH)2 + 2 HNO3 = Ca(NO3)2 + 2 H2O","double replacement"),
("Ca(OH)2 + CO2 = CaCO3 + H2O","uncategorized"),
("Ca(OH)2 + SO3 = CaSO4 + H2O","uncategorized"),
("Ca3(PO4)2 + 3 SiO2 + 5 C = 3 CaSiO3 + 5 CO + 2 P","uncategorized"),
("Ca3P2 + 6 H2O = 3 Ca(OH)2 + 2 PH3","uncategorized"),
("Ca3P2 + 6 H2O = 3 Ca(OH)2 + 2 PH3","uncategorized"),
("CaC2 + 2 H2O = C2H2 + Ca(OH)2","uncategorized"),
("CaCO3 + 2 HF = CaF2 + H2O + CO2","uncategorized"),
("CaCO3 + 2 HNO3 = Ca(NO3)2 + CO2 + H2O","uncategorized"),
("CaCO3 + H2O + CO2 = Ca(HCO3)2","synthesis"),
("CaCO3 + H2SO4 = CaSO4 + H2O + CO2","uncategorized"),
("CaCO3 + SiO2 = CaSiO3 + CO2","uncategorized"),
("CaCO3 = CaO + CO2","decomposition"),
("CaCl2 + 2 AgNO3 = 2 AgCl + Ca(NO3)2","double replacement"),
("CaCl2 + 2 H2O = Ca(OH)2 + 2 HCl","uncategorized"),
("CaCl2 + H2SO4 = CaSO4 + 2 HCl","double replacement"),
("CaCl2 = Ca + 2 Cl","decomposition"),
("CaCl2 = Ca + Cl2","decomposition"),
("CaF2 + H2SO4 = CaSO4 + 2 HF","double replacement"),
("CaH2 + 2 H2O = Ca(OH)2 + 2 H2","uncategorized"),
("CaO + 2 HNO3 = Ca(NO3)2 + H2O","double replacement"),
("CaO + 2 NH4Cl = 2 NH3 + H2O + CaCl2","uncategorized"),
("CaO + CO2 = CaCO3","synthesis"),
("CaO + H2O = Ca(OH)2","synthesis"),
("Cl + O = ClO","synthesis"),
("Cl2 + 2 KI = I2 + 2 KCl","single replacement"),
("Cl2 + 2 NaBr = 2 NaCl + Br2","single replacement"),
("CoCl2 + 2 NaOH = Co(OH)2 + 2 NaCl","double replacement"),
("CrCl3 + 3 AgNO3 = Cr(NO3)3 + 3 AgCl","double replacement"),
("Cu + 2 AgNO3 = Cu(NO3)2 + 2 Ag","single replacement"),
("Cu + 2 HCl = CuCl2 + H2","single replacement"),
("Cu + 2 NaNO3 = Cu(NO3)2 + 2 Na","single replacement"),
("Cu + 4 HNO3 = Cu(NO3)2 + 2 NO2 + 2 H2O","uncategorized"),
("Cu + FeSO4 = CuSO4 + Fe","single replacement"),
("Cu + O = CuO","synthesis"),
("Cu + S = CuS","synthesis"),
("Cu + ZnSO4 = CuSO4 + Zn","single replacement"),
("Cu2O + C = 2 Cu + CO","single replacement"),
("CuBr2 + Ca = CaBr2 + Cu","single replacement"),
("CuCO3 + H2SO4 = CuSO4 + H2O + CO2","uncategorized"),
("CuCO3 = CuO + CO2","decomposition"),
("CuCl2 + 2 AgNO3 = Cu(NO3)2 + 2 AgCl","double replacement"),
("CuCl2 + H2S = CuS + 2 HCl","double replacement"),
("CuFeS2 + 3 O2 = CuO + FeO + 2 SO2","uncategorized"),
("CuO + 2 HCl = CuCl2 + H2O","double replacement"),
("CuO + C = Cu + CO","single replacement"),
("CuO + CO = Cu + CO2","uncategorized"),
("CuS + 8 HNO3 = CuSO4 + 8 NO2 + 4 H2O","uncategorized"),
("F2 + 2 KCl = 2 KF + Cl2","single replacement"),
("Fe + (SCN)2 = Fe(SCN)2","synthesis"),
("Fe + 2 HCl = FeCl2 + H2","single replacement"),
("Fe + CuSO4 = Cu + FeSO4","single replacement"),
("Fe + CuSO4 = FeSO4 + Cu","single replacement"),
("Fe + S = FeS","synthesis"),
("Fe(OH)3 + 3 HCl = FeCl3 + 3 H2O","double replacement"),
("Fe2O3 + 3 C = 2 Fe + 3 CO","single replacement"),
("Fe2O3 + 3 C = 3 CO + 2 Fe","single replacement"),
("Fe2O3 + 3 CO = 2 Fe + 3 CO2","uncategorized"),
("Fe2O3 + 3 CO2 = Fe2(CO3)3","synthesis"),
("Fe2O3 + 3 H2 = 2 Fe + 3 H2O","single replacement"),
("Fe2O3 + 6 H = 2 Fe + 3 H2O","single replacement"),
("Fe2O3 + C = 2 FeO + CO","uncategorized"),
("Fe2O3 + Ca3(PO4)2 = 3 CaO + 2 Fe(PO4)","double replacement"),
("Fe2O3 + 3 CO = 2 Fe + 3 CO2","uncategorized"),
("Fe2S3 + 6 HCl = 2 FeCl3 + 3 H2S","double replacement"),
("FeCl3 + 3 NaOH = Fe(OH)3 + 3 NaCl","double replacement"),
("FeSO4 + 2 NaOH = Fe(OH)2 + Na2SO4","double replacement"),
("Ge + S = GeS","synthesis"),
("H + Cl = HCl","synthesis"),
("H2 + F2 = 2 HF","synthesis"),
("H2 + I2 = 2 HI","synthesis"),
("H2CO3 = H2O + CO2","decomposition"),
("H2CO3 + H2O = HCO3 + H3O","uncategorized"),
("H2O + K2SO4 = H2SO4 + K2O","uncategorized"),
("H2S + 2 H2O = 3 H2 + SO2","uncategorized"),
("H2SO3 + Ca(OH)2 = CaSO3 + 2 H2O","double replacement"),
("H2SO3 = H2O + SO2","decomposition"),
("H2SO4 + 2 KOH = K2SO4 + 2 H2O","double replacement"),
("H2SO4 + 2 NaOH = Na2SO4 + 2 H2O","double replacement"),
("H2SO4 + Mg(OH)2 = MgSO4 + 2 H2O","double replacement"),
("H2SO4 + Sr(OH)2 = 2 H2O + SrSO4","double replacement"),
("H2SO4 + Sr(OH)2 = SrSO4 + 2 H2O","double replacement"),
("H3PO4 + 3 NaOH = Na3PO4 + 3 H2O","double replacement"),
("H3PO4 + 5 HCl = PCl5 + 4 H2O","uncategorized"),
("HBr + NaOH = NaBr + H2O","double replacement"),
("HCI + NaOH = NaCI + H2O","double replacement"),
("HCl + LiOH = H2O + LiCl","double replacement"),
("HCl + NaOH = NaCl + H2O","double replacement"),
("HClO4 + 2 SO2 + 2 H2 = 2 H2SO4 + HCl","uncategorized"),
("HClO4 + NaOH = HOH + NaClO4","double replacement"),
("HClO4 + NaOH = NaClO4 + H2O","double replacement"),
("HI + NaOH = NaI + H2O","double replacement"),
("HNO3 + NaOH = Na(NO3) + H2O","double replacement"),
("HNO3 + NaOH = NaNO3 + H2O","double replacement"),
("I2 + 2 Na2S2O3 = 2 NaI + Na2S4O6","uncategorized"),
("I2O5 = I2 + O5","decomposition"),
("K + H2O = KOH + H","single replacement"),
("K + O = KO","synthesis"),
("K + O2 = KO2","synthesis"),
("K2O + H2O = 2 KOH","synthesis"),
("K2SO4 + BaCl2 = BaSO4 + 2 KCl","double replacement"),
("KCN + HCl = KCl + HCN","double replacement"),
("KOH + HBr = KBr + H2O","double replacement"),
("Li + NO3 = LiNO3","synthesis"),
("Li2O + 2 HCl = 2 LiCl + H2O","double replacement"),
("Li2S + Cu(NO3)2 = 2 LiNO3 + CuS","double replacement"),
("Mg + 2 AgNO3 = Mg(NO3)2 + 2 Ag","single replacement"),
("Mg + 2 CH3COOH = C4H6MgO4 + H2","uncategorized"),
("Mg + 2 CH3COOH = Mg(CH3COO)2 + H2","uncategorized"),
("Mg + 2 H2O = Mg(OH)2 + H2","single replacement"),
("Mg + 2 HCl = MgCl2 + H2","single replacement"),
("Mg + 2 HNO3 = H2 + Mg(NO3)2","single replacement"),
("Mg + CH3Br = CH3MgBr","synthesis"),
("Mg + Cl2 = MgCl2","synthesis"),
("Mg + H2O = MgO + H2","single replacement"),
("Mg + O = MgO","synthesis"),
("Mg(OH)2 + 2 HCl = MgCl2 + 2 H2O","double replacement"),
("Mg3N2 + 6 H2O = 3 Mg(OH)2 + 2 NH3","uncategorized"),
("MgCl2 + Li2CO3 = MgCO3 + 2 LiCl","double replacement"),
("MgO + CO2 = MgCO3","synthesis"),
("Mn + 2 H2O2 = MnO2 + 2 H2O","uncategorized"),
("MnO2 + 4 HCl = MnCl2 + 2 H2O + Cl2","uncategorized"),
("N + O2 = NO2","synthesis"),
("N2 + 3 H2 = 2 NH3","synthesis"),
("N2 + O2 = 2 NO","synthesis"),
("NH3 + H2O = NH4OH","synthesis"),
("NH3 + HCl = NH4Cl","synthesis"),
("NH4Cl + NaNO2 = N2 + 2 H2O + NaCl","uncategorized"),
("NO + CO = N + CO2","uncategorized"),
("Na + H = NaH","synthesis"),
("Na + KCl = NaCl + K","single replacement"),
("Na2CO3 + 2 HCl = 2 NaCl + H2O + CO2","uncategorized"),
("Na2CO3 + Ca(OH)2 = 2 NaOH + CaCO3","double replacement"),
("Na2CO3 + HOH = NaOH + NaHCO3","uncategorized"),
("Na2O + CO2 = Na2CO3","synthesis"),
("Na2O + H2O = 2 NaOH","synthesis"),
("Na2O + SO3 = Na2SO4","synthesis"),
("Na2O + CO2 = Na2CO3","synthesis"),
("Na2S + 2 HCl = 2 NaCl + H2S","double replacement"),
("Na2SO4 + 2 C = Na2S + 2 CO2","uncategorized"),
("Na2SO4 + 4 C = Na2S + 4 CO","uncategorized"),
("Na2SO4 + CaCl2 = CaSO4 + 2 NaCl","double replacement"),
("Na3PO4 + 3 KOH = 3 NaOH + K3PO4","double replacement"),
("NaCl + AgN = AgCl + NaN","double replacement"),
("NaCl + AgNi = AgCl + NaNi","double replacement"),
("NaClO + NaCl + H2O = Cl2 + 2 NaOH","uncategorized"),
("NaHCO3 + CH3COOH = CH3COONa + H2O + CO2","uncategorized"),
("NaHCO3 + CH3COOH = H2CO3 + NaCH3COO","uncategorized"),
("NaHCO3 = NaOH + CO2","decomposition"),
("NaOH + C15H31COOH = C15H31COONa + H2O","uncategorized"),
("NaOH + HCl = NaCl + HOH","double replacement"),
("Ni + Br2 = NiBr2","synthesis"),
("Ni + MgCl2 = NiCl2 + Mg","single replacement"),
("Ni(NO3)2 + Na2CO3 = NiCO3 + 2 NaNO3","double replacement"),
("Ni(OH)2 + H2SO4 = NiSO4 + 2 H2O","double replacement"),
("NiCO3 + 2 HCl = NiCl2 + CO2 + H2O","uncategorized"),
("NiCl2 + 3 O2 = NiO + Cl2O5","uncategorized"),
("OF2 + H2O = O2 + 2 HF","uncategorized"),
("P2O5 + 6 NaOH = 2 Na3PO4 + 3 H2O","uncategorized"),
("P4 + 10 O2 = 2 P2O10","synthesis"),
("P4 + 3 O2 = 2 P2O3","synthesis"),
("P4 + 5 O2 = P4O10","synthesis"),
("P4 + 6 Cl2 = 4 PCl3","synthesis"),
("P4 + 626 Cl2 = 4 PCl313","synthesis"),
("P4O10 + 6 H2O = 4 H3PO4","synthesis"),
("Pb + FeSO4 = PbSO4 + Fe","single replacement"),
("Pb(NO3)2 + 2 KI = PbI2 + 2 KNO3","double replacement"),
("Pb(NO3)2 + 2 KOH = Pb(OH)2 + 2 KNO3","double replacement"),
("Pb(NO3)2 + 2 NaI = PbI2 + 2 NaNO3","double replacement"),
("Pb(NO3)2 + H2S = PbS + 2 HNO3","double replacement"),
("Pb(NO3)2 + K2CrO4 = PbCrO4 + 2 KNO3","double replacement"),
("Pb(NO3)2 + 2 NaI = PbI2 + 2 NaNO3","double replacement"),
("Pb(OH)2 + 2 HCl = 2 H2O + PbCl2","double replacement"),
("PbO = Pb + O","decomposition"),
("PbO2 + 2 H2 = Pb + 2 H2O","single replacement"),
("PbO2 + H2 = PbO + H2O","uncategorized"),
("S + O2 = SO2","synthesis"),
("SO2 + H2O = H2SO3","synthesis"),
("SO3 + H2O = H2SO4","synthesis"),
("SO3 + H2O = H2SO4","synthesis"),
("SeCl6 + O2 = SeO2 + 3 Cl2","uncategorized"),
("Si + 2 Cl2 = SiCl4","synthesis"),
("SiCl4 + 4 H2O = H4SiO4 + 4 HCl","uncategorized"),
("SiO2 + 3 C = SiC + 2 CO","uncategorized"),
("SiO2 + 4 HF = SiF4 + 2 H2O","uncategorized"),
("SiO2 + Na2CO3 = Na2SiO3 + CO2","uncategorized"),
("SiO2 + 4 HF = SiF4 + 2 H2O","uncategorized"),
("Sn + 2 NaOH = Na2SnO2 + H2","single replacement"),
("SnO + 2 HCl = SnCl2 + H2O","double replacement"),
("SnO2 + 2 H2S = SnS2 + 2 H2O","double replacement"),
("Sr + 2 H2O = Sr(OH)2 + H2","single replacement"),
("TiCl4 + 2 H2O = TiO2 + 4 HCl","uncategorized"),
("Zn + 2 AgNO3 = Zn(NO3)2 + 2 Ag","single replacement"),
("Zn + 2 HCl = ZnCl2 + H2","single replacement"),
("Zn + 2 NaOH + 2 H2O = Na2Zn(OH)4 + H2","uncategorized"),
("Zn + CuSO4 = ZnSO4 + Cu","single replacement"),
("Zn + FeSO4 = ZnSO4 + Fe","single replacement"),
("Zn + NaOH = NaZnO + H","single replacement"),
("Zn + Pb(NO3)2 = Zn(NO3)2 + Pb","single replacement"),
("Zn + 2 AgNO3 = Zn(NO3)2 + 2 Ag","single replacement"),
("Zn + 2 HCl = ZnCl2 + H2","single replacement"),
("Zn + H2SO4 = ZnSO4 + H2","single replacement"),
("ZnCO3 = ZnO + CO2","decomposition"),
("ZnCl2 + H2S = ZnS + 2 HCl","double replacement"),
])
