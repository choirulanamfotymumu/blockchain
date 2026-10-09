"""
Script Penguji Nilai Praktikum Blockchain
=========================================
Penggunaan:
    python cek_nilai.py 1    -> Menguji Level 1
    python cek_nilai.py 2    -> Menguji Level 2
    python cek_nilai.py 3    -> Menguji Level 3
    python cek_nilai.py 4    -> Menguji Level 4
    python cek_nilai.py 5    -> Menguji Level 5
    python cek_nilai.py all  -> Menguji Seluruh Level (1 - 5)
"""

import sys
import pytest

LEVEL_MAP = {
    "1": "test_level01_hash.py",
    "2": "test_level02_blok.py",
    "3": "test_level03_tampering.py",
    "4": "test_level04_transaksi.py",
    "5": "test_level05_pow_nonce.py",
}


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    if arg in LEVEL_MAP:
        test_file = LEVEL_MAP[arg]
        print(f"\n==================== MENGUJI LEVEL {arg} ====================")
        exit_code = pytest.main(["-v", test_file])
    elif arg.lower() in ("all", "semua"):
        print("\n==================== MENGUJI SEMUA LEVEL (1 - 5) ====================")
        exit_code = pytest.main(["-v"])
    else:
        print(f"Argumen '{arg}' tidak valid.")
        print("Gunakan: python cek_nilai.py [1|2|3|4|5|all]")
        exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
