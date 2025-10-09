#!/usr/bin/env python3
"""
One-shot builder for periodic_table.db
Run:  python build_db.py
"""
import sqlite3
import os

DB_FILE = "periodic_table.db"

# ------------------------------------------------------------------
# 1.  Wipe old DB (comment out if you want to keep it)
# ------------------------------------------------------------------
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# ------------------------------------------------------------------
# 2.  Create fresh DB + table
# ------------------------------------------------------------------
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute("""
CREATE TABLE elements (
    atomic_number            INTEGER PRIMARY KEY,
    symbol                   TEXT NOT NULL UNIQUE,
    name                     TEXT NOT NULL,
    atomic_mass              REAL,
    category                 TEXT,
    xpos                     INTEGER,          -- group (column on table)
    ypos                     INTEGER,          -- period (row on table)
    electron_configuration   TEXT,
    electronegativity_pauling REAL,
    electron_affinity        REAL,
    density                  TEXT,
    melting_point            TEXT,
    boiling_point            TEXT
);
""")

# ------------------------------------------------------------------
# 3.  Raw data copied 1-for-1 from index.html <script> block
# ------------------------------------------------------------------
raw = [
  # Period 1
  {"name":"Hydrogen",   "number":1,   "symbol":"H",  "mass":1.008,  "category":"nonmetal",               "group":1,  "period":1, "config":"1s¹",  "en":2.2,   "ea":72.8,  "density":0.08988, "mp":-259.16, "bp":-252.87},
  {"name":"Helium",     "number":2,   "symbol":"He", "mass":4.0026, "category":"noble-gas",              "group":18, "period":1, "config":"1s²",  "en":None,"ea":-48,   "density":0.1786,  "mp":None,    "bp":-268.93},
  # Period 2
  {"name":"Lithium",    "number":3,   "symbol":"Li", "mass":6.94,   "category":"alkali-metal",           "group":1,  "period":2, "config":"[He] 2s¹",  "en":0.98,  "ea":59.6,  "density":0.534,   "mp":180.54,  "bp":1342},
  {"name":"Beryllium",  "number":4,   "symbol":"Be", "mass":9.0122, "category":"alkaline-earth-metal",   "group":2,  "period":2, "config":"[He] 2s²",  "en":1.57,  "ea":-48,   "density":1.85,    "mp":1287,    "bp":2471},
  {"name":"Boron",      "number":5,   "symbol":"B",  "mass":10.81,  "category":"metalloid",              "group":13, "period":2, "config":"[He] 2s² 2p¹",  "en":2.04,  "ea":27.7,  "density":2.34,    "mp":2076,    "bp":3927},
  {"name":"Carbon",     "number":6,   "symbol":"C",  "mass":12.011, "category":"nonmetal",               "group":14, "period":2, "config":"[He] 2s² 2p²",  "en":2.55,  "ea":122.3, "density":2.267,  "mp":3550,    "bp":4027},
  {"name":"Nitrogen",   "number":7,   "symbol":"N",  "mass":14.007, "category":"nonmetal",               "group":15, "period":2, "config":"[He] 2s² 2p³",  "en":3.04,  "ea":-8,    "density":1.251,  "mp":-210,    "bp":-195.8},
  {"name":"Oxygen",     "number":8,   "symbol":"O",  "mass":15.999, "category":"nonmetal",               "group":16, "period":2, "config":"[He] 2s² 2p⁴",  "en":3.44,  "ea":141,   "density":1.429,  "mp":-218.79, "bp":-182.95},
  {"name":"Fluorine",   "number":9,   "symbol":"F",  "mass":18.998, "category":"halogen",                "group":17, "period":2, "config":"[He] 2s² 2p⁵",  "en":3.98,  "ea":328,   "density":1.696,  "mp":-219.67, "bp":-188.11},
  {"name":"Neon",       "number":10,  "symbol":"Ne", "mass":20.180, "category":"noble-gas",              "group":18, "period":2, "config":"[He] 2s² 2p⁶",  "en":None,"ea":-116,  "density":0.9,      "mp":-248.59, "bp":-246.08},
  # Period 3
  {"name":"Sodium",     "number":11,  "symbol":"Na", "mass":22.990, "category":"alkali-metal",           "group":1,  "period":3, "config":"[Ne] 3s¹",  "en":0.93,  "ea":53,    "density":0.971,  "mp":97.8,     "bp":883},
  {"name":"Magnesium",  "number":12,  "symbol":"Mg", "mass":24.305, "category":"alkaline-earth-metal",   "group":2,  "period":3, "config":"[Ne] 3s²",  "en":1.31,  "ea":-40,   "density":1.738,  "mp":650,     "bp":1090},
  {"name":"Aluminum",   "number":13,  "symbol":"Al", "mass":26.982, "category":"post-transition-metal",  "group":13, "period":3, "config":"[Ne] 3s² 3p¹",  "en":1.61,  "ea":42.5,  "density":2.7,    "mp":660.32,  "bp":2519},
  {"name":"Silicon",    "number":14,  "symbol":"Si", "mass":28.085, "category":"metalloid",              "group":14, "period":3, "config":"[Ne] 3s² 3p²",  "en":1.9,   "ea":134,   "density":2.329,  "mp":1414,    "bp":3265},
  {"name":"Phosphorus", "number":15,  "symbol":"P",  "mass":30.974, "category":"nonmetal",               "group":15, "period":3, "config":"[Ne] 3s² 3p³",  "en":2.19,  "ea":72,    "density":1.82,   "mp":44.15,   "bp":280.5},
  {"name":"Sulfur",     "number":16,  "symbol":"S",  "mass":32.06,  "category":"nonmetal",               "group":16, "period":3, "config":"[Ne] 3s² 3p⁴",  "en":2.58,  "ea":200,   "density":2.07,   "mp":115.21,  "bp":444.6},
  {"name":"Chlorine",   "number":17,  "symbol":"Cl", "mass":35.45,  "category":"halogen",                "group":17, "period":3, "config":"[Ne] 3s² 3p⁵",  "en":3.16,  "ea":349,   "density":3.2,    "mp":-101.5,  "bp":-34.04},
  {"name":"Argon",      "number":18,  "symbol":"Ar", "mass":39.948, "category":"noble-gas",              "group":18, "period":3, "config":"[Ne] 3s² 3p⁶",  "en":None,"ea":-96,   "density":1.784,  "mp":-189.3,  "bp":-185.8},
  # Period 4
  {"name":"Potassium",  "number":19,  "symbol":"K",  "mass":39.098, "category":"alkali-metal",           "group":1,  "period":4, "config":"[Ar] 4s¹",  "en":0.82,  "ea":48,    "density":0.862,  "mp":63.5,     "bp":759},
  {"name":"Calcium",    "number":20,  "symbol":"Ca", "mass":40.078, "category":"alkaline-earth-metal",   "group":2,  "period":4, "config":"[Ar] 4s²",  "en":1,     "ea":2.4,   "density":1.55,   "mp":842,     "bp":1484},
  {"name":"Scandium",   "number":21,  "symbol":"Sc", "mass":44.956, "category":"transition-metal",       "group":3,  "period":4, "config":"[Ar] 3d¹ 4s²",  "en":1.36,  "ea":18,    "density":2.985,  "mp":1541,    "bp":2836},
  {"name":"Titanium",   "number":22,  "symbol":"Ti", "mass":47.867, "category":"transition-metal",       "group":4,  "period":4, "config":"[Ar] 3d² 4s²",  "en":1.54,  "ea":7.6,   "density":4.506,  "mp":1668,    "bp":3287},
  {"name":"Vanadium",   "number":23,  "symbol":"V",  "mass":50.942, "category":"transition-metal",       "group":5,  "period":4, "config":"[Ar] 3d³ 4s²",  "en":1.63,  "ea":50.6,  "density":6,      "mp":1910,    "bp":3407},
  {"name":"Chromium",   "number":24,  "symbol":"Cr", "mass":51.996, "category":"transition-metal",       "group":6,  "period":4, "config":"[Ar] 3d⁵ 4s¹",  "en":1.66,  "ea":64.3,  "density":7.19,   "mp":1857,    "bp":2671},
  {"name":"Manganese",  "number":25,  "symbol":"Mn", "mass":54.938, "category":"transition-metal",       "group":7,  "period":4, "config":"[Ar] 3d⁵ 4s²",  "en":1.55,  "ea":-50,   "density":7.47,   "mp":1246,    "bp":2061},
  {"name":"Iron",       "number":26,  "symbol":"Fe", "mass":55.845, "category":"transition-metal",       "group":8,  "period":4, "config":"[Ar] 3d⁶ 4s²",  "en":1.83,  "ea":16,    "density":7.874,  "mp":1538,    "bp":2862},
  {"name":"Cobalt",     "number":27,  "symbol":"Co", "mass":58.933, "category":"transition-metal",       "group":9,  "period":4, "config":"[Ar] 3d⁷ 4s²",  "en":1.88,  "ea":63.9,  "density":8.9,    "mp":1495,    "bp":2927},
  {"name":"Nickel",     "number":28,  "symbol":"Ni", "mass":58.693, "category":"transition-metal",       "group":10, "period":4, "config":"[Ar] 3d⁸ 4s²",  "en":1.91,  "ea":112,   "density":8.908,  "mp":1455,    "bp":2913},
  {"name":"Copper",     "number":29,  "symbol":"Cu", "mass":63.546, "category":"transition-metal",       "group":11, "period":4, "config":"[Ar] 3d¹⁰ 4s¹",  "en":1.9,   "ea":119,   "density":8.96,   "mp":1084.62, "bp":2562},
  {"name":"Zinc",       "number":30,  "symbol":"Zn", "mass":65.38,  "category":"transition-metal",       "group":12, "period":4, "config":"[Ar] 3d¹⁰ 4s²",  "en":1.65,  "ea":-58,   "density":7.14,   "mp":419.53,  "bp":907},
  {"name":"Gallium",    "number":31,  "symbol":"Ga", "mass":69.723, "category":"post-transition-metal",  "group":13, "period":4, "config":"[Ar] 3d¹⁰ 4s² 4p¹",  "en":1.81,  "ea":41,    "density":5.904,  "mp":29.76,   "bp":2403},
  {"name":"Germanium",  "number":32,  "symbol":"Ge", "mass":72.63,  "category":"metalloid",              "group":14, "period":4, "config":"[Ar] 3d¹⁰ 4s² 4p²",  "en":2.01,  "ea":119,   "density":5.323,  "mp":938.25,  "bp":2833},
  {"name":"Arsenic",    "number":33,  "symbol":"As", "mass":74.922, "category":"metalloid",              "group":15, "period":4, "config":"[Ar] 3d¹⁰ 4s² 4p³",  "en":2.18,  "ea":78,    "density":5.727,  "mp":817,     "bp":614},
  {"name":"Selenium",   "number":34,  "symbol":"Se", "mass":78.971, "category":"nonmetal",               "group":16, "period":4, "config":"[Ar] 3d¹⁰ 4s² 4p⁴",  "en":2.55,  "ea":195,   "density":4.819,  "mp":221,     "bp":685},
  {"name":"Bromine",    "number":35,  "symbol":"Br", "mass":79.904, "category":"halogen",                "group":17, "period":4, "config":"[Ar] 3d¹⁰ 4s² 4p⁵",  "en":2.96,  "ea":325,   "density":3.1028, "mp":-7.2,    "bp":58.8},
  {"name":"Krypton",    "number":36,  "symbol":"Kr", "mass":83.798, "category":"noble-gas",              "group":18, "period":4, "config":"[Ar] 3d¹⁰ 4s² 4p⁶",  "en":3,     "ea":-96,   "density":3.75,   "mp":-157.36, "bp":-153.22},
  # Period 5
  {"name":"Rubidium",   "number":37,  "symbol":"Rb", "mass":85.468, "category":"alkali-metal",           "group":1,  "period":5, "config":"[Kr] 5s¹",  "en":0.82,  "ea":47,    "density":1.532,  "mp":39.31,   "bp":688},
  {"name":"Strontium",  "number":38,  "symbol":"Sr", "mass":87.62,  "category":"alkaline-earth-metal",   "group":2,  "period":5, "config":"[Kr] 5s²",  "en":0.95,  "ea":5,     "density":2.64,   "mp":777,     "bp":1382},
  {"name":"Yttrium",    "number":39,  "symbol":"Y",  "mass":88.906, "category":"transition-metal",       "group":3,  "period":5, "config":"[Kr] 4d¹ 5s²",  "en":1.22,  "ea":30,    "density":4.47,   "mp":1522,    "bp":3338},
  {"name":"Zirconium",  "number":40,  "symbol":"Zr", "mass":91.224, "category":"transition-metal",       "group":4,  "period":5, "config":"[Kr] 4d² 5s²",  "en":1.33,  "ea":41,    "density":6.52,   "mp":1855,    "bp":4409},
  {"name":"Niobium",    "number":41,  "symbol":"Nb", "mass":92.906, "category":"transition-metal",       "group":5,  "period":5, "config":"[Kr] 4d⁴ 5s¹",  "en":1.6,   "ea":86.1,  "density":8.57,   "mp":2477,    "bp":4744},
  {"name":"Molybdenum", "number":42,  "symbol":"Mo", "mass":95.95,  "category":"transition-metal",       "group":6,  "period":5, "config":"[Kr] 4d⁵ 5s¹",  "en":2.16,  "ea":71.9,  "density":10.28,  "mp":2623,    "bp":4639},
  {"name":"Technetium", "number":43,  "symbol":"Tc", "mass":98,     "category":"transition-metal",       "group":7,  "period":5, "config":"[Kr] 4d⁵ 5s²",  "en":1.9,   "ea":53,    "density":11.5,   "mp":2157,    "bp":4265},
  {"name":"Ruthenium",  "number":44,  "symbol":"Ru", "mass":101.07, "category":"transition-metal",       "group":8,  "period":5, "config":"[Kr] 4d⁷ 5s¹",  "en":2.2,   "ea":101,   "density":12.45,  "mp":2334,    "bp":4150},
  {"name":"Rhodium",    "number":45,  "symbol":"Rh", "mass":102.91, "category":"transition-metal",       "group":9,  "period":5, "config":"[Kr] 4d⁸ 5s¹",  "en":2.28,  "ea":110,   "density":12.41,  "mp":1964,    "bp":3695},
  {"name":"Palladium",  "number":46,  "symbol":"Pd", "mass":106.42, "category":"transition-metal",       "group":10, "period":5, "config":"[Kr] 4d¹⁰",  "en":2.2,   "ea":54,    "density":12.02,  "mp":1554.9,  "bp":2963},
  {"name":"Silver",     "number":47,  "symbol":"Ag", "mass":107.87, "category":"transition-metal",       "group":11, "period":5, "config":"[Kr] 4d¹⁰ 5s¹",  "en":1.93,  "ea":126,   "density":10.49,  "mp":961.78,  "bp":2162},
  {"name":"Cadmium",    "number":48,  "symbol":"Cd", "mass":112.41, "category":"transition-metal",       "group":12, "period":5, "config":"[Kr] 4d¹⁰ 5s²",  "en":1.69,  "ea":-68,   "density":8.65,   "mp":321.07,  "bp":767},
  {"name":"Indium",     "number":49,  "symbol":"In", "mass":114.82, "category":"post-transition-metal",  "group":13, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p¹",  "en":1.78,  "ea":39,    "density":7.31,   "mp":156.6,   "bp":2072},
  {"name":"Tin",        "number":50,  "symbol":"Sn", "mass":118.71, "category":"post-transition-metal",  "group":14, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p²",  "en":1.96,  "ea":107,   "density":7.31,   "mp":231.93,  "bp":2602},
  {"name":"Antimony",   "number":51,  "symbol":"Sb", "mass":121.76, "category":"metalloid",              "group":15, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p³",  "en":2.05,  "ea":101,   "density":6.697,  "mp":630.63,  "bp":1587},
  {"name":"Tellurium",  "number":52,  "symbol":"Te", "mass":127.60, "category":"metalloid",              "group":16, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁴",  "en":2.1,   "ea":190,   "density":6.24,   "mp":449.5,   "bp":988},
  {"name":"Iodine",     "number":53,  "symbol":"I",  "mass":126.90, "category":"halogen",                "group":17, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁵",  "en":2.66,  "ea":295,   "density":4.933,  "mp":113.7,   "bp":184.3},
  {"name":"Xenon",      "number":54,  "symbol":"Xe", "mass":131.29, "category":"noble-gas",              "group":18, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁶",  "en":2.6,   "ea":-77,   "density":5.894,  "mp":-111.7,  "bp":-108.1},
  # Period 6
  {"name":"Caesium",    "number":55,  "symbol":"Cs", "mass":132.91, "category":"alkali-metal",           "group":1,  "period":6, "config":"[Xe] 6s¹",  "en":0.79,  "ea":45.5,  "density":1.93,   "mp":28.5,    "bp":671},
  {"name":"Barium",     "number":56,  "symbol":"Ba", "mass":137.33, "category":"alkaline-earth-metal",   "group":2,  "period":6, "config":"[Xe] 6s²",  "en":0.89,  "ea":14,    "density":3.51,   "mp":727,     "bp":1897},
  {"name":"Lanthanum",  "number":57,  "symbol":"La", "mass":138.91, "category":"lanthanide",             "group":3,  "period":6, "config":"[Xe] 5d¹ 6s²",  "en":1.1,   "ea":53,    "density":6.162,  "mp":920,     "bp":3464},
  {"name":"Cerium",     "number":58,  "symbol":"Ce", "mass":140.12, "category":"lanthanide",             "group":None,"period":6, "config":"[Xe] 4f¹ 5d¹ 6s²",  "en":1.12,  "ea":55,    "density":6.77,   "mp":795,     "bp":3443},
  {"name":"Praseodymium","number":59, "symbol":"Pr", "mass":140.91, "category":"lanthanide",             "group":None,"period":6, "config":"[Xe] 4f³ 6s²",  "en":bp":1382},
  {"name":"Yttrium",    "number":39,  "symbol":"Y",  "mass":88.906, "category":"transition-metal",       "group":3,  "period":5, "config":"[Kr] 4d¹ 5s²",  "en":1.22,  "ea":30,    "density":4.47,   "mp":1522,    "bp":3338},
  {"name":"Zirconium",  "number":40,  "symbol":"Zr", "mass":91.224, "category":"transition-metal",       "group":4,  "period":5, "config":"[Kr] 4d² 5s²",  "en":1.33,  "ea":41,    "density":6.52,   "mp":1855,    "bp":4409},
  {"name":"Niobium",    "number":41,  "symbol":"Nb", "mass":92.906, "category":"transition-metal",       "group":5,  "period":5, "config":"[Kr] 4d⁴ 5s¹",  "en":1.6,   "ea":86.1,  "density":8.57,   "mp":2477,    "bp":4744},
  {"name":"Molybdenum", "number":42,  "symbol":"Mo", "mass":95.95,  "category":"transition-metal",       "group":6,  "period":5, "config":"[Kr] 4d⁵ 5s¹",  "en":2.16,  "ea":71.9,  "density":10.28,  "mp":2623,    "bp":4639},
  {"name":"Technetium", "number":43,  "symbol":"Tc", "mass":98,     "category":"transition-metal",       "group":7,  "period":5, "config":"[Kr] 4d⁵ 5s²",  "en":1.9,   "ea":53,    "density":11.5,   "mp":2157,    "bp":4265},
  {"name":"Ruthenium",  "number":44,  "symbol":"Ru", "mass":101.07, "category":"transition-metal",       "group":8,  "period":5, "config":"[Kr] 4d⁷ 5s¹",  "en":2.2,   "ea":101,   "density":12.45,  "mp":2334,    "bp":4150},
  {"name":"Rhodium",    "number":45,  "symbol":"Rh", "mass":102.91, "category":"transition-metal",       "group":9,  "period":5, "config":"[Kr] 4d⁸ 5s¹",  "en":2.28,  "ea":110,   "density":12.41,  "mp":1964,    "bp":3695},
  {"name":"Palladium",  "number":46,  "symbol":"Pd", "mass":106.42, "category":"transition-metal",       "group":10, "period":5, "config":"[Kr] 4d¹⁰",  "en":2.2,   "ea":54,    "density":12.02,  "mp":1554.9,  "bp":2963},
  {"name":"Silver",     "number":47,  "symbol":"Ag", "mass":107.87, "category":"transition-metal",       "group":11, "period":5, "config":"[Kr] 4d¹⁰ 5s¹",  "en":1.93,  "ea":126,   "density":10.49,  "mp":961.78,  "bp":2162},
  {"name":"Cadmium",    "number":48,  "symbol":"Cd", "mass":112.41, "category":"transition-metal",       "group":12, "period":5, "config":"[Kr] 4d¹⁰ 5s²",  "en":1.69,  "ea":-68,   "density":8.65,   "mp":321.07,  "bp":767},
  {"name":"Indium",     "number":49,  "symbol":"In", "mass":114.82, "category":"post-transition-metal",  "group":13, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p¹",  "en":1.78,  "ea":39,    "density":7.31,   "mp":156.6,   "bp":2072},
  {"name":"Tin",        "number":50,  "symbol":"Sn", "mass":118.71, "category":"post-transition-metal",  "group":14, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p²",  "en":1.96,  "ea":107,   "density":7.31,   "mp":231.93,  "bp":2602},
  {"name":"Antimony",   "number":51,  "symbol":"Sb", "mass":121.76, "category":"metalloid",              "group":15, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p³",  "en":2.05,  "ea":101,   "density":6.697,  "mp":630.63,  "bp":1587},
  {"name":"Tellurium",  "number":52,  "symbol":"Te", "mass":127.60, "category":"metalloid",              "group":16, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁴",  "en":2.1,   "ea":190,   "density":6.24,   "mp":449.5,   "bp":988},
  {"name":"Iodine",     "number":53,  "symbol":"I",  "mass":126.90, "category":"halogen",                "group":17, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁵",  "en":2.66,  "ea":295,   "density":4.933,  "mp":113.7,   "bp":184.3},
  {"name":"Xenon",      "number":54,  "symbol":"Xe", "mass":131.29, "category":"noble-gas",              "group":18, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁶",  "en":2.6,   "ea":-77,   "density":5.894,  "mp":-111.7,  "bp":-108.1},
  # Period 6
  {"name":"Caesium",    "number":55,  "symbol":"Cs", "mass":132.91, "category":"alkali-metal",           "group":1,  "period":6, "config":"[Xe] 6s¹",  "en":0.79,  "ea":45.5,  "density":1.93,   "mp":28.5,    "bp":671},
  {"name":"Barium",     "number":56,  "symbol":"Ba", "mass":137.33, "category":"alkaline-earth-metal",   "group":2,  "period":6, "config":"[Xe] 6s²",  "en":0.89,  "ea":14,    "density":3.51,   "mp":727,     "bp":1897},
  {"name":"Lanthanum",  "number":57,  "symbol":"La", "mass":138.91, "category":"lanthanide",             "group":3,  "period":6, "config":"[Xe] 5d¹ 6s²",  "en":1.1,   "ea":53,    "density":6.162,  "mp":920,     "bp":3464},
  {"name":"Cerium",     "number":58,  "symbol":"Ce", "mass":140.12, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹ 5d¹ 6s²",  "en":1.12, "ea":55,    "density":6.77,   "mp":795,     "bp":3443},
  {"name":"Praseodymium","number":59,"symbol":"Pr", "mass":140.91, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f³ 6s²",  "en":1.13,  "ea":50,    "density":6.77,   "mp":935,     "bp":3520},
  {"name":"Neodymium",  "number":60,  "symbol":"Nd", "mass":144.24, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁴ 6s²",  "en":1.14,  "ea":43,    "density":7.01,   "mp":1021,    "bp":3074},
  {"name":"Promethium", "number":61,  "symbol":"Pm", "mass":145,    "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁵ 6s²",  "en":1.13,  "ea":12,    "density":7.26,   "mp":1042,    "bp":3000},
  {"name":"Samarium",   "number":62,  "symbol":"Sm", "mass":150.36, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁶ 6s²",  "en":1.17,  "ea":16,    "density":7.52,   "mp":1074,    "bp":1794},
  {"name":"Europium",   "number":63,  "symbol":"Eu", "mass":151.96, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁷ 6s²",  "en":None,  "ea":10,    "density":5.244,  "mp":822,     "bp":1529},
  {"name":"Gadolinium", "number":64,  "symbol":"Gd", "mass":157.25, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁷ 5d¹ 6s²",  "en":1.2, "ea":13,    "density":7.9,    "mp":1313,    "bp":3273},
  {"name":"Terbium",    "number":65,  "symbol":"Tb", "mass":158.93, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁹ 6s²",  "en":1.1,   "ea":112,   "density":8.23,   "mp":1356,    "bp":3230},
  {"name":"Dysprosium", "number":66,  "symbol":"Dy", "mass":162.50, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹⁰ 6s²",  "en":1.22,  "ea":34,    "density":8.551,  "mp":1407,    "bp":2567},
  {"name":"Holmium",    "number":67,  "symbol":"Ho", "mass":164.93, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹¹ 6s²",  "en":1.23,  "ea":58,    "density":8.795,  "mp":1474,    "bp":2700},
  {"name":"Erbium",     "number":68,  "symbol":"Er", "mass":167.26, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹² 6s²",  "en":1.24,  "ea":30.1,  "density":9.066,  "mp":1529,    "bp":2868},
  {"name":"Thulium",    "number":69,  "symbol":"Tm", "mass":168.93, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹³ 6s²",  "en":1.25,  "ea":99,    "density":9.32,   "mp":1545,    "bp":1950},
  {"name":"Ytterbium",  "number":70,  "symbol":"Yb", "mass":173.05, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹⁴ 6s²",  "en":None,  "ea":-1,    "density":6.965,  "mp":819,     "bp":1196},
  {"name":"Lutetium",   "number":71,  "symbol":"Lu", "mass":174.97, "category":"lanthanide",             "group":3,  "period":6, "config":"[Xe] 4f¹⁴ 5d¹ 6s²",  "en":1.27, "ea":33,    "density":9.84,   "mp":1663,    "bp":3402},
  {"name":"Hafnium",    "number":72,  "symbol":"Hf", "mass":178.49, "category":"transition-metal",       "group":4,  "period":6, "config":"[Xe] 4f¹⁴ 5d² 6s²",  "en":1.3,  "ea":17,    "density":13.31,  "mp":2233,    "bp":4603},
  {"name":"Tantalum",   "number":73,  "symbol":"Ta", "mass":180.95, "category":"transition-metal",       "group":5,  "period":6, "config":"[Xe] 4f¹⁴ 5d³ 6s²",  "en":1.5,  "ea":31,    "density":16.69,  "mp":3017,    "bp":5458},
  {"name":"Tungsten",   "number":74,  "symbol":"W",  "mass":183.84, "category":"transition-metal",       "group":6,  "period":6, "config":"[Xe] 4f¹⁴ 5d⁴ 6s²",  "en":2.36,  "ea":78.6,  "density":19.25,  "mp":3422,    "bp":5930},
  {"name":"Rhenium",    "number":75,  "symbol":"Re", "mass":186.21, "category":"transition-metal",       "group":7,  "period":6, "config":"[Xe] 4f¹⁴ 5d⁵ 6s²",  "en":1.9,  "ea":5.8,   "density":21.02,  "mp":3186,    "bp":5630},
  {"name":"Osmium",     "number":76,  "symbol":"Os", "mass":190.23, "category":"transition-metal",       "group":8,  "period":6, "config":"[Xe] 4f¹⁴ 5d⁶ 6s²",  "en":2.2,  "ea":106.1, "density":22.59,  "mp":3033,    "bp":5012},
  {"name":"Iridium",    "number":77,  "symbol":"Ir", "mass":192.22, "category":"transition-metal",       "group":9,  "period":6, "config":"[Xe] 4f¹⁴ 5d⁷ 6s²",  "en":2.2,  "ea":151,   "density":22.56,  "mp":2466,    "bp":4428},
  {"name":"Platinum",   "number":78,  "symbol":"Pt", "mass":195.08, "category":"transition-metal",       "group":10, "period":6, "config":"[Xe] 4f¹⁴ 5d⁹ 6s¹",  "en":2.28,  "ea":205,   "density":21.45,  "mp":1768.3,  "bp":3825},
  {"name":"Gold",       "number":79,  "symbol":"Au", "mass":196.97, "category":"transition-metal",       "group":11, "period":6, "config":"[Xe] 4f¹⁴ 5d¹⁰ 6s¹",  "en":2.54,  "ea":223,   "density":19.3,   "mp":1064.18, "bp":2856},
  {"name":"Mercury",    "number":80,  "symbol":"Hg", "mass":200.59, "category":"transition-metal",       "group":12, "period":6,bp":1382},
  {"name":"Yttrium",    "number":39,  "symbol":"Y",  "mass":88.906, "category":"transition-metal",       "group":3,  "period":5, "config":"[Kr] 4d¹ 5s²",  "en":1.22,  "ea":30,    "density":4.47,   "mp":1522,    "bp":3338},
  {"name":"Zirconium",  "number":40,  "symbol":"Zr", "mass":91.224, "category":"transition-metal",       "group":4,  "period":5, "config":"[Kr] 4d² 5s²",  "en":1.33,  "ea":41,    "density":6.52,   "mp":1855,    "bp":4409},
  {"name":"Niobium",    "number":41,  "symbol":"Nb", "mass":92.906, "category":"transition-metal",       "group":5,  "period":5, "config":"[Kr] 4d⁴ 5s¹",  "en":1.6,   "ea":86.1,  "density":8.57,   "mp":2477,    "bp":4744},
  {"name":"Molybdenum", "number":42,  "symbol":"Mo", "mass":95.95,  "category":"transition-metal",       "group":6,  "period":5, "config":"[Kr] 4d⁵ 5s¹",  "en":2.16,  "ea":71.9,  "density":10.28,  "mp":2623,    "bp":4639},
  {"name":"Technetium", "number":43,  "symbol":"Tc", "mass":98,     "category":"transition-metal",       "group":7,  "period":5, "config":"[Kr] 4d⁵ 5s²",  "en":1.9,   "ea":53,    "density":11.5,   "mp":2157,    "bp":4265},
  {"name":"Ruthenium",  "number":44,  "symbol":"Ru", "mass":101.07, "category":"transition-metal",       "group":8,  "period":5, "config":"[Kr] 4d⁷ 5s¹",  "en":2.2,   "ea":101,   "density":12.45,  "mp":2334,    "bp":4150},
  {"name":"Rhodium",    "number":45,  "symbol":"Rh", "mass":102.91, "category":"transition-metal",       "group":9,  "period":5, "config":"[Kr] 4d⁸ 5s¹",  "en":2.28,  "ea":110,   "density":12.41,  "mp":1964,    "bp":3695},
  {"name":"Palladium",  "number":46,  "symbol":"Pd", "mass":106.42, "category":"transition-metal",       "group":10, "period":5, "config":"[Kr] 4d¹⁰",  "en":2.2,   "ea":54,    "density":12.02,  "mp":1554.9,  "bp":2963},
  {"name":"Silver",     "number":47,  "symbol":"Ag", "mass":107.87, "category":"transition-metal",       "group":11, "period":5, "config":"[Kr] 4d¹⁰ 5s¹",  "en":1.93,  "ea":126,   "density":10.49,  "mp":961.78,  "bp":2162},
  {"name":"Cadmium",    "number":48,  "symbol":"Cd", "mass":112.41, "category":"transition-metal",       "group":12, "period":5, "config":"[Kr] 4d¹⁰ 5s²",  "en":1.69,  "ea":-68,   "density":8.65,   "mp":321.07,  "bp":767},
  {"name":"Indium",     "number":49,  "symbol":"In", "mass":114.82, "category":"post-transition-metal",  "group":13, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p¹",  "en":1.78,  "ea":39,    "density":7.31,   "mp":156.6,   "bp":2072},
  {"name":"Tin",        "number":50,  "symbol":"Sn", "mass":118.71, "category":"post-transition-metal",  "group":14, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p²",  "en":1.96,  "ea":107,   "density":7.31,   "mp":231.93,  "bp":2602},
  {"name":"Antimony",   "number":51,  "symbol":"Sb", "mass":121.76, "category":"metalloid",              "group":15, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p³",  "en":2.05,  "ea":101,   "density":6.697,  "mp":630.63,  "bp":1587},
  {"name":"Tellurium",  "number":52,  "symbol":"Te", "mass":127.60, "category":"metalloid",              "group":16, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁴",  "en":2.1,   "ea":190,   "density":6.24,   "mp":449.5,   "bp":988},
  {"name":"Iodine",     "number":53,  "symbol":"I",  "mass":126.90, "category":"halogen",                "group":17, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁵",  "en":2.66,  "ea":295,   "density":4.933,  "mp":113.7,   "bp":184.3},
  {"name":"Xenon",      "number":54,  "symbol":"Xe", "mass":131.29, "category":"noble-gas",              "group":18, "period":5, "config":"[Kr] 4d¹⁰ 5s² 5p⁶",  "en":2.6,   "ea":-77,   "density":5.894,  "mp":-111.7,  "bp":-108.1},
  # Period 6
  {"name":"Caesium",    "number":55,  "symbol":"Cs", "mass":132.91, "category":"alkali-metal",           "group":1,  "period":6, "config":"[Xe] 6s¹",  "en":0.79,  "ea":45.5,  "density":1.93,   "mp":28.5,    "bp":671},
  {"name":"Barium",     "number":56,  "symbol":"Ba", "mass":137.33, "category":"alkaline-earth-metal",   "group":2,  "period":6, "config":"[Xe] 6s²",  "en":0.89,  "ea":14,    "density":3.51,   "mp":727,     "bp":1897},
  {"name":"Lanthanum",  "number":57,  "symbol":"La", "mass":138.91, "category":"lanthanide",             "group":3,  "period":6, "config":"[Xe] 5d¹ 6s²",  "en":1.1,   "ea":53,    "density":6.162,  "mp":920,     "bp":3464},
  {"name":"Cerium",     "number":58,  "symbol":"Ce", "mass":140.12, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹ 5d¹ 6s²",  "en":1.12,  "ea":55,    "density":6.77,   "mp":795,     "bp":3443},
  {"name":"Praseodymium","number":59,"symbol":"Pr", "mass":140.91, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f³ 6s²",  "en":1.13,  "ea":50,    "density":6.77,   "mp":935,     "bp":3520},
  {"name":"Neodymium",  "number":60,  "symbol":"Nd", "mass":144.24, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁴ 6s²",  "en":1.14,  "ea":43,    "density":7.01,   "mp":1021,    "bp":3074},
  {"name":"Promethium", "number":61,  "symbol":"Pm", "mass":145,    "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁵ 6s²",  "en":1.13,  "ea":12,    "density":7.26,   "mp":1042,    "bp":3000},
  {"name":"Samarium",   "number":62,  "symbol":"Sm", "mass":150.36, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁶ 6s²",  "en":1.17,  "ea":16,    "density":7.52,   "mp":1074,    "bp":1794},
  {"name":"Europium",   "number":63,  "symbol":"Eu", "mass":151.96, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁷ 6s²",  "en":None,  "ea":10,    "density":5.244,  "mp":822,     "bp":1529},
  {"name":"Gadolinium", "number":64,  "symbol":"Gd", "mass":157.25, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁷ 5d¹ 6s²",  "en":1.2,   "ea":13,    "density":7.9,    "mp":1313,    "bp":3273},
  {"name":"Terbium",    "number":65,  "symbol":"Tb", "mass":158.93, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f⁹ 6s²",  "en":1.1,   "ea":112,   "density":8.23,   "mp":1356,    "bp":3230},
  {"name":"Dysprosium", "number":66,  "symbol":"Dy", "mass":162.50, "category":"lanthanide",             "group":None,"period":6,"config":"[Xe] 4f¹⁰ 6s²",  "en":1.22,  "ea":34,    "density":8.551,  "mp":1407,    "bp":2567},
 
