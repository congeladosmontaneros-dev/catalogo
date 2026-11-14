"""Actualiza precios y agotados del catálogo desde el respaldo de la app de caja.
Uso: python3 tools/sincronizar.py respaldo-inventario-AAAA-MM-DD.json
- Cambia el precio de cada variante cuyo id exista en el respaldo.
- Escribe const AGOTADOS=[...] con los productos en 0 o menos.
- Escribe const ACTUALIZADO="..." con la fecha del respaldo.
No inventa precios: si un id no está en el respaldo, deja el precio como estaba.
"""
import json, sys, re, datetime, collections
ruta = sys.argv[1]
b = json.load(open(ruta, encoding="utf-8"))
precio = {p["id"]: p.get("precio") for p in b["productos"]}
stock = collections.Counter()
for m in b["movimientos"]:
    q = m.get("cantidad") or 0
    t = (m.get("tipo") or "").lower()
    stock[m["productoId"]] += -q if t.startswith("s") else q
ultimo = max((m["ts"] for m in b["movimientos"]), default=0)
fecha = datetime.datetime.fromtimestamp(ultimo/1000, datetime.UTC).replace(tzinfo=None) - datetime.timedelta(hours=5)

t = open("index.html", encoding="utf-8").read()
i = t.find("const DATA=") + len("const DATA=")
data, end = json.JSONDecoder().raw_decode(t[i:])
cambios = []
for g in data["groups"]:
    for v in g["v"]:
        p = precio.get(v["id"])
        if p and p != v["price"]:
            cambios.append(f'{g["name"]} ({v["label"]}): {v["price"]} -> {p}')
            v["price"] = p
ids = {v["id"] for g in data["groups"] for v in g["v"]}
agot = sorted(x for x in ids if x in precio and stock[x] == 0)  # negativo = entrada sin registrar, no se marca
t = t[:i] + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + t[i+end:]
linea = "const AGOTADOS=" + json.dumps(agot) + ";const ACTUALIZADO=" + json.dumps(fecha.strftime("%d/%m/%Y")) + ";"
if "const AGOTADOS=" in t:
    t = re.sub(r"const AGOTADOS=\[[^\]]*\];const ACTUALIZADO=\"[^\"]*\";", linea, t)
else:
    t = t.replace("const UNITS={};", linea + "\nconst UNITS={};", 1)
open("index.html", "w", encoding="utf-8").write(t)
print("Precios cambiados:", len(cambios)); print("\n".join(cambios))
print("Agotados:", len(agot)); print("Respaldo del", fecha.strftime("%d/%m/%Y %H:%M"))
