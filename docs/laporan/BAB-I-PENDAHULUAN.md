# BAB I — PENDAHULUAN

## 1.1 Latar Belakang

Pengembangan aplikasi modern tidak hanya berfokus pada penulisan kode program, tetapi juga mencakup cara aplikasi dikemas, dijalankan, diuji, dan dipantau. Aplikasi yang terdiri dari beberapa layanan memerlukan pengelolaan dependensi dan komunikasi antarkomponen yang konsisten. Apabila setiap layanan dijalankan secara terpisah tanpa konfigurasi yang terorganisasi, proses instalasi, pengujian, dan pemeliharaan dapat menjadi lebih sulit.

Containerization merupakan salah satu pendekatan untuk mengemas aplikasi beserta lingkungan runtime-nya. Docker menyediakan mekanisme untuk membangun dan menjalankan container, sedangkan Docker Compose membantu mendefinisikan beberapa layanan dalam satu konfigurasi. Dengan pendekatan tersebut, layanan aplikasi, database, dan reverse proxy dapat dijalankan sebagai satu platform.

Selain itu, aplikasi yang berjalan perlu diuji dan dipantau. Automated testing membantu memeriksa perilaku aplikasi secara berulang, sedangkan Continuous Integration (CI) dapat menjalankan pengujian dan proses build secara otomatis ketika perubahan kode dikirimkan ke repository. Untuk observability, Prometheus dapat mengumpulkan metrik, cAdvisor menyediakan metrik penggunaan resource container, dan Grafana menampilkan metrik dalam bentuk dashboard.

Berdasarkan kebutuhan tersebut, proyek ini membangun **Docker Multi-Container Inventory Platform**, yaitu platform inventaris sederhana berbasis FastAPI dan PostgreSQL yang dikelola dengan Docker Compose, diakses melalui Nginx, serta dilengkapi pipeline CI dan monitoring.

## 1.2 Rumusan Masalah

Rumusan masalah dalam proyek ini adalah:

1. Bagaimana menjalankan aplikasi inventaris dan database sebagai layanan yang terpisah menggunakan Docker Compose?
2. Bagaimana menyediakan akses aplikasi melalui reverse proxy Nginx?
3. Bagaimana menguji endpoint aplikasi dan konektivitas database?
4. Bagaimana mengotomatisasi pengujian dan build image menggunakan GitHub Actions?
5. Bagaimana mengumpulkan serta menampilkan metrik container menggunakan cAdvisor, Prometheus, dan Grafana?

## 1.3 Tujuan

Tujuan proyek ini adalah:

1. Membangun aplikasi REST API inventaris menggunakan FastAPI.
2. Menggunakan PostgreSQL untuk penyimpanan data inventaris.
3. Mengelola layanan melalui Docker Compose dan menyediakan akses melalui Nginx.
4. Menjalankan automated testing dan proses build Docker image dalam workflow CI.
5. Mengimplementasikan pengumpulan metrik dan dashboard monitoring.
6. Mendokumentasikan implementasi, pengujian, dan hasil proyek sebagai portofolio pembelajaran DevOps.

## 1.4 Manfaat

Manfaat yang diharapkan dari proyek ini meliputi:

- Memahami penerapan containerization dan orkestrasi layanan sederhana.
- Memahami hubungan antara API, database, dan reverse proxy.
- Melatih penggunaan automated testing dan GitHub Actions.
- Memahami dasar observability menggunakan Prometheus, cAdvisor, dan Grafana.
- Menghasilkan proyek yang dapat ditinjau melalui repository GitHub.

## 1.5 Batasan Masalah

Ruang lingkup proyek dibatasi pada:

1. Aplikasi inventaris dengan endpoint pemeriksaan kesehatan, pengambilan data, dan pembuatan item.
2. Layanan FastAPI, PostgreSQL, Nginx, Prometheus, Grafana, dan cAdvisor yang dijalankan melalui Docker Compose.
3. Workflow CI yang menjalankan pengujian otomatis dan membangun Docker image.
4. Pengujian dilakukan pada lingkungan lokal dan hasil yang tersedia dari workflow GitHub Actions.
5. Pemulihan API yang telah diuji dilakukan dengan menjalankan kembali container secara manual. Pengujian ini belum membuktikan pemulihan otomatis tanpa intervensi.
6. Proyek ini bukan sistem inventaris produksi dan belum mencakup pengujian beban, high availability, atau audit keamanan menyeluruh.

## 1.6 Sistematika Penulisan

Laporan terdiri atas lima bab. BAB I menjelaskan latar belakang, rumusan masalah, tujuan, manfaat, dan batasan. BAB II membahas teori yang mendukung implementasi. BAB III menjelaskan metodologi, kebutuhan, dan rancangan sistem. BAB IV memaparkan implementasi serta hasil pengujian. BAB V berisi kesimpulan dan saran pengembangan.
