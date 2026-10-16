# Laporan Tugas Personal Blockchain Level 1–5

- **Nama:** CHOIRUL ANAM FOTTYMUMU
- **NIM (4 digit terakhir):** 2104
- **Dibuat:** 2026-10-16 14:57  (waktu proses 1.8 detik)
- **Kode verifikasi:** `2AE83D2E2A95`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 1 — Hash data pribadi

| Hasil | Nilai |
|---|---|
| SHA-256 nama | `46f9eed44bb35269405ba5dfa531007f925f409bc9bbff8ba23bbddc88d7f9f3` |
| hash_dict profil | `2dc49f6fea4c41df9771d5ac05d30c9bb1e9d80ff52d48a188e0a33263b10e13` |
| hash_dict profil (urutan key dibalik) | `2dc49f6fea4c41df9771d5ac05d30c9bb1e9d80ff52d48a188e0a33263b10e13` |
| Bit berubah: tanggal lahir vs tanggal lahir + 1 hari | 54.3% |
| ID mahasiswa (Modifikasi 1) | `eece0bf7` |

## Level 2 — Blockchain personal

- Proof genesis: **2104** (dari NIM)
- Proof blok 2, 3, 4: **35376, 150242, 28752**
- Pemilik setiap blok: `eece0bf7`
- Rantai valid: True

## Level 3 — Pemalsuan data pribadi

- Posisi yang dipalsukan: **1**
- Data asli: `CHOIRUL ANAM FOTTYMUMU lahir 2004-09-01`
- Data palsu: `CHOIRUL ANAM FOTTYMUMU lahir 2004-09-01 (DIPALSUKAN)`
- Valid sebelum dipalsukan: True
- Tautan putus di indeks: **2**
- Valid setelah dipalsukan: **False**
- Valid setelah disambung ulang: **True**

## Level 4 — Transaksi dari data pribadi

| Blok | Pengirim | Penerima | Jumlah |
|---|---|---|---|
| 2 | CHOIRUL ANAM FOTTYMUMU | TEMAN_A | 1 |
| 2 | TEMAN_A | CHOIRUL ANAM FOTTYMUMU | 9 |
| 3 | CHOIRUL ANAM FOTTYMUMU | DOSEN | 5 |

- Ringkasan saldo (Modifikasi 4): masuk **9**, keluar **6**, bersih **3**
- Kirim ke diri sendiri ditolak: True
- Amount 0 ditolak: True

## Level 5 — Proof of Work dengan nonce (deterministik)

| Blok | Nonce | Hash |
|---|---|---|
| 0 | 111722 | `00005a7604a18916cc378d00…` |
| 1 | 107954 | `0000cb87cdab894f33bbd67a…` |
| 2 | 59188 | `0000632badef19bcd3c6708b…` |
| 3 | 25432 | `00006cea54fd10f572edde7c…` |

- Valid: True → setelah blok 1 dipalsukan: **False**
- Percobaan hash untuk menambang ulang blok 1–3: **170.723**
- Valid setelah ditambang ulang: True

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 1.** Bandingkan SHA-256 nama Anda dengan milik seorang teman. Apakah ada pola yang mirip? Jelaskan juga mengapa dua hash profil Anda sama, dan mengapa hanya menambah 1 hari pada tanggal lahir mengubah 54.3% bit.

   _Jawaban:_
   - **Perbandingan dengan milik teman:** Nilai SHA-256 nama saya (`46f9eed44bb3...`) sama sekali tidak memiliki pola yang mirip dengan milik teman, meskipun panjang nama atau susunan hurufnya mirip. Output fungsi hash SHA-256 terdistribusi secara seragam (*uniform distribution*) dan bersifat *pseudorandom*, sehingga tidak ada korelasi visual antarnilai hash.
   - **Mengapa dua hash profil sama:** Nilai hash profil asli dan profil dengan urutan key dibalik bernilai identik (`2dc49f6f...`) karena implementasi fungsi `hash_dict` menerapkan serialisasi kanonik `json.dumps(data, sort_keys=True)`. Sebelum string di-encode dan dihitung hash-nya, semua key diurutkan secara alfabetis terlebih dahulu. Dengan demikian, urutan penulisan key di dalam dictionary tidak mengubah string JSON yang dihasilkan.
   - **Perubahan 1 hari mengubah 54.3% bit:** Fenomena ini merupakan karakteristik utama fungsi hash kriptografis yang disebut *Avalanche Effect* (efek longsoran salju). Perubahan kecil pada input (hanya 1 karakter/1 hari pada string tanggal lahir) menghasilkan perubahan drastis di setiap putaran (*round*) kompresi internal SHA-256, sehingga sekitar 50% bit output (pada data saya 54.3%) berubah secara acak.

2. **Level 2.** Kode Anda dan teman sama persis, tetapi proof Anda (35376, 150242, 28752) berbeda. Jelaskan penyebabnya.

   _Jawaban:_
   - Perbedaan ini disebabkan oleh **proof blok genesis** yang dipersonalisasi menggunakan 4 digit terakhir NIM masing-masing mahasiswa (`int(nim4)`). Pada data saya, proof genesis bernilai `2104`, sedangkan teman-teman lain memiliki NIM yang berbeda.
   - Pada mekanisme Proof of Work Level 2, pencarian proof suatu blok dihitung berdasarkan formula `proof**2 - previous_proof**2`. Karena `previous_proof` untuk blok ke-2 diambil dari proof genesis yang unik (`2104`), maka nilai proof blok ke-2 yang lolos kriteria *difficulty* menjadi berbeda (`35376`).
   - Selanjutnya, proof blok ke-3 bergantung pada proof blok ke-2, dan proof blok ke-4 bergantung pada proof blok ke-3. Akibat perbedaan pada *initial seed* (proof genesis), seluruh deret proof blok berikutnya ikut berbeda secara berantai (*chain effect*), meskipun algoritma dan kodenya identik.

3. **Level 3.** Anda memalsukan posisi 1 dan tautan putus terdeteksi di indeks 2, sedangkan valid setelah dipalsukan = False. Jelaskan hasil ini, lalu bandingkan dengan teman yang posisi pemalsuannya berbeda.

   _Jawaban:_
   - **Penyebab putus di indeks 2 dan status False:** Posisi yang dipalsukan dihitung dari rumus `1 + int(nim4) % 4`. Untuk NIM `2104`, `1 + (2104 % 4) = 1 + 0 = 1`. Ketika data pada blok indeks 1 diubah (ditambahi teks `(DIPALSUKAN)`), nilai hash blok 1 berubah total. Blok indeks 2 masih menyimpan `previous_hash` yang merujuk pada hash lama blok 1. Saat validasi dijalankan, ketidakcocokan hash (*broken link*) langsung terdeteksi pada blok penerusnya, yaitu indeks 2 (`chain[2]["previous_hash"] != hash_blok(chain[1])`), sehingga status validitas rantai menjadi `False`.
   - **Perbandingan dengan teman:** Teman dengan sisa bagi NIM yang berbeda memalsukan blok pada posisi lain (misalnya posisi 2, 3, atau 4). Jika teman memalsukan blok posisi 2, maka tautan putus akan terdeteksi di indeks 3. Khusus teman yang memalsukan blok terakhir (posisi 4), tautan putus tidak akan terdeteksi oleh `cari_tautan_putus` karena blok 4 tidak memiliki blok penerus yang menunjuk kepadanya (namun integritas data di blok tersebut tetap rusak).
   - **Kelemahan PoW GfG:** Setelah dijalankan `sambung_ulang`, status validitas kembali menjadi `True`. Ini membuktikan kelemahan desain PoW Level 2/3 ala GeeksforGeeks, di mana pembuktian kerja (*proof*) tidak mengikat data transaksi atau isi blok, sehingga penyerang dapat memalsukan data dan menyambung ulang rantai tanpa perlu menambang ulang PoW.

4. **Level 4.** Jelaskan dari mana angka masuk 9, keluar 6, dan bersih 3 berasal. Mengapa transaksi ke diri sendiri perlu ditolak?

   _Jawaban:_
   - **Asal angka saldo:**
     1. Transaksi 1: `CHOIRUL ANAM FOTTYMUMU` mengirim ke `TEMAN_A` sebesar tanggal lahir saya, yaitu **1** (1 September 2004) -> keluar 1.
     2. Transaksi 2: `TEMAN_A` mengirim ke `CHOIRUL ANAM FOTTYMUMU` sebesar bulan lahir saya, yaitu **9** (September) -> masuk 9.
     3. Transaksi 3: `CHOIRUL ANAM FOTTYMUMU` mengirim ke `DOSEN` sebesar `(int(nim4) % 50) + 1` = `(2104 % 50) + 1` = `4 + 1` = **5** -> keluar 5.
     - **Total Masuk:** 9
     - **Total Keluar:** 1 + 5 = 6
     - **Saldo Bersih:** 9 - 6 = **3**.
   - **Mengapa transaksi ke diri sendiri harus ditolak:**
     1. **Mencegah spam & pemborosan ruang blok (*block space*):** Transaksi ke diri sendiri tidak mengubah kepemilikan aset tetapi membebani mempool dan kapasitas penyimpanan buku besar (*ledger*) yang harus disimpan oleh seluruh node jaringan.
     2. **Mencegah manipulasi volume (*wash trading*):** Pengguna jahat bisa membuat ilusi likuiditas semu atau volume perdagangan palsu dengan mentransfer dana bolak-balik ke dirinya sendiri.
     3. **Efisiensi komputasi:** Node tidak perlu membuang sumber daya komputasi untuk memverifikasi transaksi tanpa dampak ekonomi riil.

5. **Level 5.** Penyerang butuh 170.723 percobaan hash untuk memalsukan rantai Anda. Mengapa nonce Anda selalu sama setiap kali program dijalankan, padahal di demo Level 5 asli nonce berubah-ubah?

   _Jawaban:_
   - Pada demo Level 5 standar (`level05_pow_nonce.py`), field `timestamp` menggunakan `datetime.now()` yang nilainya terus berubah dalam satuan mikrodetik setiap kali program dieksekusi. Karena isi string blok selalu berbeda sedikit pun, hash yang dihasilkan berubah dan nilai nonce yang memenuhi target *difficulty* ikut bergeser secara acak.
   - Pada `BlockchainDeterministik` di tugas personal ini, nilai `timestamp` dibuat konstan dan deterministik (blok genesis menggunakan string `2004-09-01`, sedangkan blok 1–3 menggunakan format `2004-09-01 #1`, `2004-09-01 #2`, dan `2004-09-01 #3`).
   - Selain itu, seluruh isi blok (data transaksi personal, ID mahasiswa, previous hash, dan urutan indeks) bersifat statis, serta proses pencarian nonce selalu dimulai secara berurutan dari angka 0 (`nonce = 0, 1, 2, ...`). Karena algoritma SHA-256 bersifat deterministik murni, kombinasi input yang identik dengan iterasi nonce yang sama pasti akan selalu menghasilkan nonce yang sama persis (111722, 107954, 59188, 25432) dan total percobaan penambangan ulang yang persis sama (**170.723** percobaan).

6. **Etika data.** Anda baru saja menyimpan nama dan tanggal lahir di dalam blockchain. Jika ini blockchain publik, apa risikonya? Kaitkan dengan sifat immutability dan UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, terutama hak untuk menghapus data.

   _Jawaban:_
   - **Risiko di Blockchain Publik:**
     Nama lengkap dan tanggal lahir merupakan Data Pribadi yang bersifat sensitif/teridentifikasi. Jika dicatat di blockchain publik, data tersebut dapat diakses dan diunduh oleh siapa saja di seluruh dunia secara permanen. Hal ini membuka risiko pencurian identitas (*identity theft*), penipuan berbasis rekayasa sosial (*phishing/social engineering*), serta pelacakan profil individu tanpa izin (*doxxing*).
   - **Konflik dengan Sifat Immutability dan UU No. 27 Tahun 2022 (UU PDP):**
     - Sifat dasar blockchain adalah **immutability** (kekekalan), yaitu data yang sudah tercatat di dalam blok dan divalidasi oleh konsensus jaringan mustahil untuk diubah, diedit, atau dihapus.
     - Di sisi lain, berdasarkan **Pasal 8 dan Pasal 43 UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)**, setiap Subjek Data Pribadi memiliki hak untuk menarik persetujuan dan menuntut penghapusan serta pemusnahan data pribadi miliknya (*right to erasure* / *right to be forgotten*).
     - Terjadi pertentangan mendasar antara hukum dan teknologi: administrator sistem blockchain publik tidak memiliki mekanisme teknis untuk menghapus data pribadi yang sudah terlanjur tercatat di dalam rantai blok tanpa merusak seluruh hash blok berikutnya dan membatalkan konsensus rantai.
   - **Solusi Rekayasa / Praktik Terbaik:**
     Data pribadi (PII) seharusnya tidak pernah disimpan secara langsung (*plaintext on-chain*) di blockchain publik. Praktik terbaik adalah menyimpan data di server/database terenkripsi di luar rantai (*off-chain storage*), dan hanya mencatat bukti kriptografisnya (*hash pointer*, komitmen kriptografi, atau Zero-Knowledge Proofs) di dalam blockchain (*on-chain*). Dengan cara ini, jika pengguna meminta datanya dihapus sesuai amanat UU PDP, data di server off-chain dapat dimusnahkan tanpa merusak struktur dan integritas buku besar blockchain.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "profil": {
    "nama": "CHOIRUL ANAM FOTTYMUMU",
    "nim4": "2104",
    "tanggal_lahir": "2004-09-01",
    "kota_asal": "Sorong",
    "hobi": "Otomotif"
  },
  "level1": {
    "hash_nama": "46f9eed44bb35269405ba5dfa531007f925f409bc9bbff8ba23bbddc88d7f9f3",
    "hash_profil": "2dc49f6fea4c41df9771d5ac05d30c9bb1e9d80ff52d48a188e0a33263b10e13",
    "hash_profil_urutan_terbalik": "2dc49f6fea4c41df9771d5ac05d30c9bb1e9d80ff52d48a188e0a33263b10e13",
    "avalanche_tanggal_persen": 54.3,
    "id_mahasiswa": "eece0bf7"
  },
  "level2": {
    "proof_genesis": 2104,
    "proof_blok": [
      35376,
      150242,
      28752
    ],
    "pemilik_semua_blok": [
      "eece0bf7"
    ],
    "valid": true
  },
  "level3": {
    "posisi_dipalsukan": 1,
    "data_asli": "CHOIRUL ANAM FOTTYMUMU lahir 2004-09-01",
    "data_palsu": "CHOIRUL ANAM FOTTYMUMU lahir 2004-09-01 (DIPALSUKAN)",
    "valid_asli": true,
    "tautan_putus_di": 2,
    "valid_setelah_dipalsukan": false,
    "valid_setelah_disambung_ulang": true
  },
  "level4": {
    "riwayat": [
      [
        2,
        {
          "sender": "CHOIRUL ANAM FOTTYMUMU",
          "recipient": "TEMAN_A",
          "amount": 1
        }
      ],
      [
        2,
        {
          "sender": "TEMAN_A",
          "recipient": "CHOIRUL ANAM FOTTYMUMU",
          "amount": 9
        }
      ],
      [
        3,
        {
          "sender": "CHOIRUL ANAM FOTTYMUMU",
          "recipient": "DOSEN",
          "amount": 5
        }
      ]
    ],
    "ringkasan_saldo": {
      "masuk": 9,
      "keluar": 6,
      "bersih": 3
    },
    "kirim_ke_diri_sendiri_ditolak": true,
    "amount_nol_ditolak": true,
    "jumlah_blok": 3
  },
  "level5": {
    "nonce": [
      111722,
      107954,
      59188,
      25432
    ],
    "hash": [
      "00005a7604a18916cc378d00c76403a68c460915eb3685d55bec661f78c5917a",
      "0000cb87cdab894f33bbd67a0c7ad7e9028db2a181383a7ca4ad4d34e257f3fb",
      "0000632badef19bcd3c6708b95b9be29d9542c3fa69a5ac85b40ea94ac68927c",
      "00006cea54fd10f572edde7c6b6e22446ce70f7c3fa226ae93080fae012d3654"
    ],
    "valid": true,
    "valid_setelah_dipalsukan": false,
    "percobaan_tambang_ulang": 170723,
    "valid_setelah_tambang_ulang": true
  },
  "kode_verifikasi": "2AE83D2E2A95"
}
```
