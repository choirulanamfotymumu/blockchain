"""
Script Penguji Nilai Praktikum Blockchain
=========================================
Penggunaan:
    python cek_nilai.py 1              -> Menguji Level 1
    python cek_nilai.py 1 2 3 4 5      -> Menguji Level 1 s.d. 5
    python cek_nilai.py all            -> Menguji Seluruh Level
"""

import os
import sys
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
LATIHAN_DIR = os.path.join(HERE, "latihan") if os.path.isdir(os.path.join(HERE, "latihan")) else HERE

LEVEL_MAP = {
    "1": os.path.join(LATIHAN_DIR, "test_level01_hash.py"),
    "2": os.path.join(LATIHAN_DIR, "test_level02_blok.py"),
    "3": os.path.join(LATIHAN_DIR, "test_level03_tampering.py"),
    "4": os.path.join(LATIHAN_DIR, "test_level04_transaksi.py"),
    "5": os.path.join(LATIHAN_DIR, "test_level05_pow_nonce.py"),
}


def main():
    args = sys.argv[1:]
    if not args or "all" in [a.lower() for a in args] or "semua" in [a.lower() for a in args]:
        print("\n==================== MENGUJI SEMUA LEVEL (1 - 5) ====================")
        files = [LEVEL_MAP[k] for k in sorted(LEVEL_MAP.keys()) if os.path.exists(LEVEL_MAP[k])]
        exit_code = pytest.main(["-v"] + files)
        sys.exit(exit_code)

    files_to_test = []
    for arg in args:
        if arg in LEVEL_MAP and os.path.exists(LEVEL_MAP[arg]):
            files_to_test.append(LEVEL_MAP[arg])
        else:
            print(f"Peringatan: Level '{arg}' tidak valid atau file pengujian tidak ditemukan.")

    if not files_to_test:
        print("Tidak ada file pengujian yang ditemukan.")
        print("Gunakan: python cek_nilai.py [1|2|3|4|5|all]")
        sys.exit(1)

    print(f"\n==================== MENGUJI LEVEL {', '.join(args)} ====================")
    exit_code = pytest.main(["-v"] + files_to_test)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
