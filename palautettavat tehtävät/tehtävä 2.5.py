luodinPaino = 13.3
leiviskässänauloja = 20
naulassaLuoteja = 32
leiviskät = int(input("anna leiviskät: "))
naulat = int(input("naulat: "))
luodit = int(input("luodit: "))
kokonaisluodit = (leiviskät * leiviskässänauloja * naulassaLuoteja + naulat * naulassaLuoteja + luodit )
grammat = kokonaisluodit * luodinPaino
kilot = int(grammat // 1000)
jäännösGrammat = grammat % 1000
print(f"massa nykymittojen mukaan: {kilot} kilogrammaa ja {jäännösGrammat: .2f} grammaa.")




