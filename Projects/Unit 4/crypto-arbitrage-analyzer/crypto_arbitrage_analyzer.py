cripto = {
    "BTC": {"Binance": 58650, "Kraken": 58560, "Coinbase": 58720,},
    "ETH": {"Binance": 2450, "Kraken": 2497, "Coinbase": 2430,},
    "SOL": {"Binance": 132.15, "Kraken": 133.80, "Coinbase": 135.06},
}
maxTiendaBTC = max(cripto["BTC"], key=cripto["BTC"].get)
maxBTC = cripto["BTC"][maxTiendaBTC]
minTiendaBTC = min(cripto["BTC"], key=cripto["BTC"].get)
minBTC = cripto["BTC"][minTiendaBTC]

maxTiendaETH = max(cripto["ETH"], key=cripto["ETH"].get)
maxETH = cripto["ETH"][maxTiendaETH]
minTiendaETH = min(cripto["ETH"], key=cripto["ETH"].get)
minETH = cripto["ETH"][minTiendaETH]

maxTiendaSOL = max(cripto["SOL"], key=cripto["SOL"].get)
maxSOL = cripto["SOL"][maxTiendaSOL]
minTiendaSOL = min(cripto["SOL"], key=cripto["SOL"].get)
minSOL = cripto["SOL"][minTiendaSOL]

seleccion = input("Bienvenido al analizador de chollos de criptomonedas, que moneda deseas analizar:\nBTC, ETH  o SOL\n").upper()
if seleccion == "BTC":
    print(f'La tienda que mas valor tiene es {maxTiendaBTC}, {maxBTC}, y la que menor valor tiene es {minTiendaBTC}, {minBTC}')
    ganancia_sin_resta = round(maxBTC-minBTC, 2)
    ganancia_con_resta = round(ganancia_sin_resta*0.991, 2)
    print(f"Si comprases en {minTiendaBTC} y vendieses en {maxTiendaBTC} tendrias una ganancia de {ganancia_sin_resta}, tras 0.9% de comisiones seria {ganancia_con_resta}")
elif seleccion == "ETH":
    print(f'La tienda que mas valor tiene es {maxTiendaETH}, {maxETH}, y la que menor valor tiene es {minTiendaETH}, {minETH}')
    ganancia_sin_resta = round(maxETH-minETH, 2)
    ganancia_con_resta = round(ganancia_sin_resta*0.991, 2)
    print(f"Si comprases en {minTiendaETH} y vendieses en {maxTiendaETH} tendrias una ganancia de {ganancia_sin_resta}, tras 0.9% de comisiones seria {ganancia_con_resta}")
elif seleccion == "SOL":
    print(f'La tienda que mas valor tiene es {maxTiendaSOL}, {maxSOL}, y la que menor valor tiene es {minTiendaSOL}, {minSOL}')
    ganancia_sin_resta = round(maxSOL-minSOL, 2)
    ganancia_con_resta = round(ganancia_sin_resta*0.991, 2)
    print(f"Si comprases en {minTiendaSOL} y vendieses en {maxTiendaSOL} tendrias una ganancia de {ganancia_sin_resta}, tras 0.9% de comisiones seria {ganancia_con_resta}")
else:
    print("Esa opcion no estaba disponible, porfavor, reinicie el programa y elija una de las opciones disponibles")