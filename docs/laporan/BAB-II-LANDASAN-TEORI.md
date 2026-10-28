# BAB II — LANDASAN TEORI

## 2.1 Containerization

Containerization adalah pendekatan untuk mengemas aplikasi beserta komponen yang diperlukan agar aplikasi dapat dijalankan dalam lingkungan yang terisolasi. Container menggunakan kernel sistem operasi host, sehingga karakteristiknya berbeda dari virtual machine yang umumnya menjalankan sistem operasi tamu tersendiri. Dalam proyek ini, container digunakan untuk memisahkan layanan aplikasi, database, reverse proxy, dan monitoring.

## 2.2 Docker

Docker menyediakan perangkat untuk membangun image dan menjalankan container. Image berisi filesystem dan konfigurasi yang diperlukan oleh aplikasi, sedangkan container merupakan instance berjalan dari image tersebut. Dockerfile digunakan untuk mendefinisikan proses build image.

## 2.3 Docker Compose

Docker Compose digunakan untuk mendefinisikan dan mengelola aplikasi multi-container melalui file konfigurasi, pada proyek ini bernama `compose.yaml`. Konfigurasi tersebut mendefinisikan layanan, port, jaringan, volume, dan pengaturan lain yang diperlukan untuk menjalankan platform. Perintah seperti `docker compose up -d`, `docker compose ps`, dan `docker compose down` digunakan untuk mengelola siklus hidup layanan.

## 2.4 FastAPI dan REST API

FastAPI merupakan framework Python untuk membangun API. REST API memungkinkan klien berinteraksi dengan sumber daya menggunakan metode HTTP. Proyek ini menyediakan endpoint `GET /health`, `GET /items`, dan `POST /items`. Endpoint kesehatan digunakan untuk memeriksa kondisi aplikasi dan koneksi database, sedangkan endpoint inventaris digunakan untuk mengambil dan menambahkan item.

## 2.5 PostgreSQL

PostgreSQL adalah sistem manajemen basis data relasional. Pada proyek ini, PostgreSQL menyimpan data inventaris dan dijalankan sebagai layanan terpisah dari aplikasi. Docker volume digunakan untuk mempertahankan data di luar siklus hidup container database. Kredensial database dikonfigurasi melalui environment variables.

## 2.6 Nginx sebagai Reverse Proxy

Nginx dapat menerima permintaan dari klien dan meneruskannya ke layanan aplikasi. Dalam proyek ini, Nginx menjadi titik akses dari host melalui port `8080`, kemudian meneruskan permintaan ke aplikasi FastAPI pada jaringan container. Database tidak perlu dipublikasikan langsung ke host untuk digunakan oleh aplikasi.

## 2.7 Automated Testing

Automated testing menjalankan pemeriksaan terhadap perilaku aplikasi melalui kode pengujian. Proyek ini menggunakan pytest untuk menjalankan test yang tersedia pada direktori `tests`. Hasil pengujian yang tercatat selama pengerjaan adalah tiga test berhasil (`3 passed`).

## 2.8 Continuous Integration

Continuous Integration (CI) merupakan praktik menjalankan pemeriksaan otomatis terhadap perubahan kode. Workflow GitHub Actions pada proyek ini dipicu oleh push dan pull request ke branch `main`. Tahap workflow meliputi checkout repository, menyiapkan Python, memasang dependensi pengembangan, menjalankan pytest, dan membangun Docker image.

## 2.9 Monitoring dan Observability

Monitoring mengamati kondisi layanan melalui metrik yang dikumpulkan secara berkala. Prometheus mengambil metrik dari target yang dikonfigurasi dan menyediakan bahasa query PromQL. cAdvisor menyediakan metrik terkait resource container. Grafana digunakan untuk memvisualisasikan metrik dalam dashboard.

Status target Prometheus bernilai `UP` menunjukkan bahwa target berhasil dijangkau dan proses scrape berhasil. Namun, status tersebut tidak dengan sendirinya membuktikan bahwa seluruh metrik telah difilter hanya untuk container aplikasi proyek.

## 2.10 Docker Volume dan Jaringan

Docker volume menyimpan data secara terpisah dari filesystem container sehingga data dapat bertahan ketika container dibuat ulang, selama volume tidak dihapus. Jaringan Docker memungkinkan layanan berkomunikasi menggunakan nama layanan. Pemisahan jaringan dan tidak memublikasikan port database ke host membantu membatasi jalur akses, tetapi tidak menggantikan kebutuhan pengamanan kredensial dan konfigurasi jaringan yang tepat.
