# BAB III — METODOLOGI

## 3.1 Jenis Pengerjaan

Proyek ini merupakan implementasi teknis berbasis praktik (*implementation project*). Pengerjaan dilakukan dengan merancang layanan, menyiapkan konfigurasi container, menjalankan aplikasi lokal, menguji endpoint, membangun workflow CI, serta menambahkan monitoring.

## 3.2 Perangkat dan Teknologi

Perangkat dan teknologi yang digunakan meliputi:

| No. | Komponen | Kegunaan |
|---:|---|---|
| 1 | Windows dan terminal CMD | Lingkungan kerja lokal |
| 2 | Git | Version control |
| 3 | GitHub | Penyimpanan repository dan workflow CI |
| 4 | Docker Desktop | Menjalankan container |
| 5 | Docker Compose | Mengelola layanan multi-container |
| 6 | Python dan FastAPI | Implementasi REST API |
| 7 | PostgreSQL 17 | Penyimpanan data inventaris |
| 8 | Nginx | Reverse proxy |
| 9 | pytest | Automated testing |
| 10 | GitHub Actions | CI workflow |
| 11 | Prometheus | Pengumpulan dan query metrik |
| 12 | cAdvisor | Metrik resource container |
| 13 | Grafana | Dashboard monitoring |

Versi komponen selain yang disebutkan secara eksplisit perlu dicatat dari konfigurasi aktual sebelum laporan final dipublikasikan.

## 3.3 Kebutuhan Fungsional

Kebutuhan fungsional yang ditetapkan adalah:

1. Klien dapat memeriksa kesehatan API melalui endpoint `/health`.
2. Klien dapat mengambil data inventaris melalui endpoint `/items`.
3. Klien dapat menambahkan item inventaris melalui metode `POST`.
4. Aplikasi dapat berkomunikasi dengan PostgreSQL.
5. Layanan dapat dijalankan dan dihentikan melalui Docker Compose.
6. Metrik monitoring dapat dikumpulkan dan ditampilkan melalui perangkat monitoring yang dikonfigurasi.
7. Workflow CI dapat menjalankan pengujian dan membangun Docker image.

## 3.4 Kebutuhan Nonfungsional

Kebutuhan nonfungsional meliputi:

- Konfigurasi layanan dapat disimpan dalam repository.
- Kredensial dikelola melalui environment variables dan tidak dipublikasikan.
- Data database disimpan menggunakan volume persisten.
- Layanan memiliki health check sesuai konfigurasi.
- Pengujian dapat dijalankan secara berulang.
- Status layanan dan metrik dapat diperiksa melalui antarmuka monitoring.

## 3.5 Rancangan Arsitektur

Sistem terdiri dari lapisan akses, aplikasi, penyimpanan, CI, dan monitoring.

1. **Lapisan akses:** klien mengakses aplikasi melalui Nginx pada port host `8080`.
2. **Lapisan aplikasi:** FastAPI menangani permintaan REST API.
3. **Lapisan data:** PostgreSQL menyimpan data inventaris.
4. **Lapisan CI:** GitHub Actions menjalankan automated tests dan Docker image build.
5. **Lapisan monitoring:** cAdvisor menyediakan metrik container, Prometheus melakukan scrape, dan Grafana menampilkan visualisasi.

Diagram arsitektur dapat dilihat pada bagian BAB IV atau README repository.

## 3.6 Tahapan Pengerjaan

Tahapan pengerjaan dilakukan sebagai berikut:

1. Menyiapkan repository GitHub dan lingkungan kerja lokal.
2. Menyiapkan aplikasi FastAPI dan dependensi.
3. Membuat Dockerfile untuk membangun image aplikasi.
4. Mendefinisikan layanan aplikasi, PostgreSQL, dan Nginx pada `compose.yaml`.
5. Menjalankan aplikasi dan memeriksa health endpoint serta data inventaris.
6. Menyiapkan automated tests dan workflow GitHub Actions.
7. Menambahkan konfigurasi Prometheus, cAdvisor, dan Grafana.
8. Memeriksa status target monitoring dan menjalankan query metrik.
9. Menguji pemulihan API setelah container dihentikan.
10. Mendokumentasikan hasil dan menyimpan perubahan ke GitHub.

## 3.7 Metode Pengujian

Pengujian dilakukan melalui pengamatan status container, permintaan HTTP menggunakan `curl`, eksekusi pytest, pemeriksaan workflow CI, dan pemeriksaan antarmuka Prometheus. Hasil pengujian dicatat berdasarkan output yang benar-benar diperoleh selama pengerjaan.
