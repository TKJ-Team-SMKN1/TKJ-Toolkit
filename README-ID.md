# TKJ Network Toolkit

Toolkit jaringan modular yang dikembangkan oleh **TKJ-Team-SMKN1** untuk pembelajaran, praktik networking, diagnostik, dan berbagai kebutuhan utilitas jaringan.

Proyek ini dirancang menggunakan arsitektur modular agar setiap tool jaringan dapat dikembangkan, diuji, dan dipelihara secara terpisah tanpa kehilangan integrasinya sebagai satu toolkit.

> English: [README.md](README.md)

---

## Status Proyek

**Versi Saat Ini:** `V1.0.0`  
**Modul Saat Ini:** `IPv4 Calculator`  
**Status:** Development

Rilis pertama berfokus pada pengalamatan IPv4 dan perhitungan subnet dasar.

---

## Fitur

### IPv4 Calculator

Modul IPv4 saat ini menyediakan:

- Validasi alamat IPv4
- Validasi prefix CIDR
- Perhitungan subnet mask
- Perhitungan network address
- Perhitungan broadcast address
- Perhitungan first usable host
- Perhitungan last usable host
- Perhitungan jumlah usable host
- Perhitungan jumlah total alamat IPv4

Modul ini mengikuti aturan pengalamatan IPv4 standar, termasuk dukungan untuk network `/31` dan `/32`.

---

## Arsitektur

Proyek memisahkan antarmuka grafis, logika networking, dan pengujian development.

```text
Toolkit-TKJ/
├── GUI/
│   ├── __init__.py
│   └── main.py
│
├── IPv4/
│   ├── __init__.py
│   ├── ip_addr.py
│   ├── cidr.py
│   ├── subnet.py
│   ├── network_addr.py
│   ├── broadcast.py
│   ├── usable_hosts.py
│   └── total_addr.py
│
├── IPv4-Dev/
│   ├── __init__.py
│   ├── test_ip_addr.py
│   ├── test_cidr.py
│   ├── test_subnet.py
│   ├── test_network_addr.py
│   ├── test_broadcast.py
│   ├── test_usable_hosts.py
│   └── test_total_addr.py
│
├── requirements.txt
├── requirements-dev.txt
├── requirements-alpine.txt
├── README.md
├── README-ID.md
└── VERSION.md
```

### Pemisahan Modul

- **GUI/** berisi antarmuka grafis aplikasi.
- **IPv4/** berisi logika inti untuk validasi dan perhitungan IPv4.
- **IPv4-Dev/** berisi automated test untuk modul IPv4.

GUI menggunakan fungsi dari package IPv4 dan tidak mengulang perhitungan networking di dalam layer antarmuka.

---

## Requirements

- Python 3
- Linux atau environment Python yang kompatibel
- PyQt6 untuk antarmuka grafis

Dependency Python tambahan tercantum pada:

- `requirements.txt` — dependency runtime standar
- `requirements-dev.txt` — dependency untuk development dan testing
- `requirements-alpine.txt` — dependency Python untuk Alpine Linux

Package sistem operasi yang bersifat spesifik terhadap distribusi Linux dipasang secara terpisah menggunakan package manager masing-masing.

---

## Instalasi

### Linux Umum

Install dependency Python:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi dari root project:

```bash
python -m GUI.main
```

---

### Alpine Linux

Alpine Linux menggunakan lingkungan sistem yang berbeda dari sebagian besar distribusi Linux berbasis glibc. Oleh karena itu, PyQt6 dapat dipasang melalui package manager Alpine daripada dibangun dari source oleh pip.

Install PyQt6:

```bash
apk add py3-qt6
```

Kemudian install dependency Python lainnya:

```bash
pip install -r requirements-alpine.txt
```

Jalankan aplikasi:

```bash
python -m GUI.main
```

Aplikasi GUI juga membutuhkan graphical display server apabila dijalankan di luar desktop environment biasa.

---

## Development

Install dependency development:

```bash
pip install -r requirements-dev.txt
```

Jalankan seluruh test:

```bash
python -m pytest -v
```

Automated test digunakan untuk memvalidasi fungsi-fungsi inti IPv4 secara terpisah dari GUI.

---

## Prinsip Pengembangan

Proyek mengikuti beberapa prinsip utama:

1. **Modularitas**
   Setiap fungsi networking dipisahkan menjadi modul yang dapat dikelola secara independen.
2. **Testability**
   Logika inti networking diuji secara terpisah dari antarmuka grafis.
3. **Portabilitas**
   Dependency Python dipisahkan dari package sistem operasi yang spesifik terhadap distribusi.
4. **Maintainability**
   Perhitungan networking berada di luar layer GUI untuk menghindari duplikasi logika.
5. **Praktikalitas**
   Tool dirancang berdasarkan konsep networking yang relevan untuk pembelajaran dan praktik TKJ.

---

## Ruang Lingkup Saat Ini

### V1 — IPv4 Calculator

Ruang lingkup V1:

- IPv4 address
- CIDR
- Subnet mask
- Network address
- Broadcast address
- First usable host
- Last usable host
- Jumlah usable host
- Jumlah total address

IPv6, VLSM, dan utilitas networking tambahan belum termasuk dalam scope V1.

---

## Roadmap

Versi berikutnya dapat memperluas toolkit dengan utilitas networking tambahan.

Area pengembangan yang direncanakan dapat mencakup:

- Utilitas IPv4 tambahan
- Utilitas IPv6
- VLSM dan subnet planning
- Utilitas DNS
- Network information
- Packet dan protocol analysis
- Network diagnostics

Sebuah fitur dianggap bagian dari release setelah diimplementasikan dan diuji.

---

## Versioning

Informasi versi dipelihara pada `VERSION.md`.

Format versi:

`MAJOR.MINOR.PATCH`

- **MAJOR** — perubahan arsitektur atau kompatibilitas besar
- **MINOR** — penambahan fitur yang tetap backward compatible
- **PATCH** — perbaikan bug dan koreksi kecil

---

## Organisasi

Dikembangkan di bawah:

**TKJ-Team-SMKN1**

Proyek ini ditujukan untuk mendukung pembelajaran dan pengembangan praktis di bidang TKJ (Teknik Komputer dan Jaringan).

---

## License

License proyek akan ditambahkan secara terpisah pada repository.