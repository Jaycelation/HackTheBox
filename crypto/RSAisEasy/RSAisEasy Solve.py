from Crypto.Util.number import inverse, long_to_bytes

n1 = 101302608234750530215072272904674037076286246679691423280860345380727387460347553585319149306846617895151397345134725469568034944362725840889803514170441153452816738520513986621545456486260186057658467757935510362350710672577390455772286945685838373154626020209228183673388592030449624410459900543470481715269
#n2 = # (insert value)
c1 = 92506893588979548794790672542461288412902813248116064711808481112865246689691740816363092933206841082369015763989265012104504500670878633324061404374817814507356553697459987468562146726510492528932139036063681327547916073034377647100888763559498314765496171327071015998871821569774481702484239056959316014064
c2 = 46096854429474193473315622000700040188659289972305530955007054362815555622172000229584906225161285873027049199121215251038480738839915061587734141659589689176363962259066462128434796823277974789556411556028716349578708536050061871052948425521408788256153194537438422533790942307426802114531079426322801866673
e = 65537

p = 8413387656561188778435613942028835678781206299389177514340760123063579360223360470566083306606450007991287094526418200038784207648097820069671213638771543
q = 12040644312371555810530782070969893153760288255333349208608058511112776958879208815174991008199408527954332776642365069284747758115478414463195873149420483
#z = 

phi_n1 = (p - 1) * (q - 1)
#phi_n2 = (q - 1) * (z - 1)

d1 = inverse(e, phi_n1)
#d2 = inverse(e, phi_n2)

m1 = pow(c1, d1, n1)
#m2 = pow(c2, d2, n2)

flag1_recovered = long_to_bytes(m1)
#flag2_recovered = long_to_bytes(m2)

print(f"Recovered flag1: {flag1_recovered}")
#print(f"Recovered flag2: {flag2_recovered}")
