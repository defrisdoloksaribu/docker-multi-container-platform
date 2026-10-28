> **Catatan gambar:** PNG yang disertakan pada `docs/screenshots/` adalah ilustrasi/mockup, bukan bukti pengujian aktual. Ganti dengan screenshot asli sebelum laporan diserahkan sebagai laporan hasil pengujian.

# BAB IV — IMPLEMENTASI DAN PENGUJIAN

## 4.1 Implementasi Struktur Proyek

Repository proyek berada pada:

`https://github.com/defrisdoloksaribu/docker-multi-container-platform`

Direktori utama memuat source code aplikasi, test, Dockerfile, konfigurasi Compose, workflow GitHub Actions, dan konfigurasi monitoring. Konfigurasi monitoring Prometheus disimpan pada `monitoring/prometheus/prometheus.yml`.

**Bukti dokumentasi:** tambahkan screenshot struktur repository atau tampilan file pada GitHub sebagai Gambar 4.1.

> **Gambar 4.1.** Struktur repository proyek.  
> *(Tambahkan screenshot aktual ke `docs/screenshots/` dan tautkan di sini.)*

## 4.2 Implementasi Multi-Container

Layanan dikelola melalui `compose.yaml`. Layanan inti mencakup API, database PostgreSQL, dan Nginx. Komponen monitoring mencakup cAdvisor, Prometheus, dan Grafana. Docker Compose digunakan untuk menjalankan layanan dalam satu konfigurasi dan memeriksa statusnya.

Perintah pemeriksaan yang digunakan:

```cmd
docker compose ps
```

Pada pemeriksaan yang dilaporkan, keenam container terlihat berjalan. API, database, cAdvisor, dan Nginx menampilkan status health check yang tersedia sebagai sehat. Prometheus dan Grafana terlihat berjalan.

**Bukti dokumentasi:** tambahkan screenshot output `docker compose ps`.

> **Gambar 4.2.** Status layanan Docker Compose.  
> *(Tambahkan screenshot aktual.)*

## 4.3 Pengujian Health Endpoint

Pengujian dilakukan dengan mengirim permintaan ke endpoint kesehatan melalui Nginx:

```cmd
curl http://localhost:8080/health
```

Output yang diperoleh:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

Hasil tersebut menunjukkan bahwa endpoint memberikan status sehat dan aplikasi melaporkan koneksi database terhubung pada saat pengujian.

> **Gambar 4.3.** Hasil pengujian endpoint `/health`.  
> *(Tambahkan screenshot aktual.)*

## 4.4 Pengujian Data Inventaris

Pengambilan data dilakukan melalui perintah:

```cmd
curl http://localhost:8080/items
```

Output yang diperoleh pada pengujian:

```json
[
  {
    "id": 1,
    "name": "Keyboard",
    "quantity": 10
  }
]
```

Respons tersebut menunjukkan bahwa API berhasil mengembalikan satu item inventaris bernama `Keyboard` dengan kuantitas `10` pada saat pengujian.

> **Gambar 4.4.** Hasil pengambilan data inventaris.  
> *(Tambahkan screenshot aktual.)*

## 4.5 Automated Testing

Pengujian otomatis dijalankan menggunakan pytest melalui container Python 3.12:

```cmd
docker run --rm -v "%cd%:/workspace" -w /workspace python:3.12-slim sh -c "pip install --no-cache-dir -r requirements-dev.txt && python -m pytest tests"
```

Hasil pengujian yang tercatat adalah:

`3 passed, 1 warning`

Tiga test berhasil dijalankan. Peringatan yang muncul berkaitan dengan deprecation pada Starlette TestClient terkait penggunaan `httpx`; peringatan tersebut tidak menyebabkan test gagal. Peringatan ini dapat ditinjau kembali pada pemeliharaan dependensi berikutnya.

> **Gambar 4.5.** Output pytest dengan tiga test berhasil.  
> *(Tambahkan screenshot aktual.)*

## 4.6 Implementasi Continuous Integration

Workflow CI disimpan pada `.github/workflows/ci.yml`. Workflow dipicu oleh push dan pull request ke branch `main`. Langkah utama workflow adalah checkout repository, menyiapkan Python 3.12, memasang dependensi pengembangan, menjalankan pytest, dan membangun Docker image.

Workflow CI sebelumnya telah dilaporkan berhasil dengan status hijau pada GitHub Actions. Perubahan konfigurasi monitoring kemudian di-commit dan di-push ke branch `main` dengan commit `083745e` (`feat: add Prometheus and Grafana monitoring`). Status workflow setelah commit tersebut perlu diperiksa kembali sebelum dinyatakan berhasil untuk versi terbaru.

> **Gambar 4.6.** Hasil workflow GitHub Actions.  
> *(Tambahkan screenshot aktual dari run yang berhasil.)*

## 4.7 Implementasi Monitoring

### 4.7.1 Prometheus

Prometheus dikonfigurasi menggunakan `monitoring/prometheus/prometheus.yml` dengan interval scrape global 15 detik dan dua target, yaitu Prometheus sendiri serta cAdvisor.

Target diperiksa melalui:

`http://localhost:9090/targets`

Pada screenshot pengujian, target Prometheus dan cAdvisor terlihat berstatus `UP`. Status tersebut menunjukkan target dapat dijangkau dan scrape berhasil.

> **Gambar 4.7.** Status target Prometheus dan cAdvisor.  
> *(Tambahkan screenshot aktual.)*

### 4.7.2 Query Status Target

Query berikut digunakan untuk memeriksa target cAdvisor:

```promql
up{job="cadvisor"}
```

Hasil yang diperoleh bernilai `1` dengan satu result series. Hasil tersebut menunjukkan bahwa Prometheus berhasil mengambil metrik dari target cAdvisor.

> **Gambar 4.8.** Hasil query status cAdvisor.  
> *(Tambahkan screenshot aktual.)*

### 4.7.3 Query Metrik Memori

Metrik memori diperiksa menggunakan query:

```promql
container_memory_working_set_bytes
```

Prometheus menampilkan banyak seri metrik. Kondisi ini dapat terjadi karena cAdvisor pada Docker Desktop dapat mengekspos metrik dari lingkungan Linux dan container lain yang dikelola oleh Docker Desktop, tidak hanya container aplikasi proyek. Karena itu, hasil mentah perlu difilter lebih lanjut sebelum digunakan untuk menyimpulkan pemakaian memori setiap layanan proyek.

> **Gambar 4.9.** Hasil query metrik memori.  
> *(Tambahkan screenshot aktual.)*

### 4.7.4 Grafana

Grafana digunakan untuk menyajikan metrik dalam dashboard. Dashboard proyek telah dibuat dan memuat panel monitoring yang dikonfigurasi selama pengerjaan. URL lokal Grafana adalah `http://localhost:3000`.

Kredensial login diambil dari konfigurasi lokal dan tidak boleh ditulis pada laporan atau repository publik.

> **Gambar 4.10.** Dashboard monitoring Grafana.  
> *(Tambahkan screenshot dashboard aktual.)*

## 4.8 Pengujian Pemulihan API

Pengujian pemulihan dilakukan dengan menghentikan container API dan menjalankannya kembali secara manual. Perintah yang digunakan:

```cmd
docker compose kill api
docker compose ps -a
docker compose up -d api
docker compose ps
```

Setelah API dijalankan kembali, pemeriksaan dilakukan melalui:

```cmd
curl http://localhost:8080/health
curl http://localhost:8080/items
```

Hasil yang diperoleh menunjukkan endpoint health kembali melaporkan status `healthy` dan database `connected`. Endpoint inventaris juga kembali mengembalikan data `Keyboard` dengan kuantitas `10`.

Pengujian ini menunjukkan bahwa layanan dapat dipulihkan setelah dijalankan kembali secara manual. Pengujian tersebut **tidak** membuktikan bahwa container otomatis pulih tanpa intervensi pengguna. Pengujian automatic restart perlu dilakukan secara terpisah jika fitur tersebut ingin dinyatakan sebagai kemampuan sistem.

> **Gambar 4.11.** Proses penghentian dan pemulihan API.  
> *(Tambahkan screenshot aktual.)*

## 4.9 Ringkasan Hasil Pengujian

| No. | Skenario | Hasil yang Diharapkan | Hasil Aktual | Status |
|---:|---|---|---|---|
| 1 | Memeriksa container | Layanan berjalan sesuai konfigurasi | Enam container terlihat berjalan pada pemeriksaan | Berhasil |
| 2 | Memanggil `/health` | API sehat dan database terhubung | `healthy`, `connected` | Berhasil |
| 3 | Memanggil `/items` | Data inventaris dikembalikan | Item `Keyboard`, kuantitas `10` | Berhasil |
| 4 | Menjalankan pytest | Test berjalan tanpa kegagalan | `3 passed`, dengan satu warning | Berhasil |
| 5 | Memeriksa target Prometheus | Target monitoring dapat di-scrape | Prometheus dan cAdvisor berstatus `UP` | Berhasil |
| 6 | Query `up{job="cadvisor"}` | Nilai status target tersedia | Nilai `1` | Berhasil |
| 7 | Query metrik memori | Seri metrik memori ditampilkan | Banyak seri metrik ditampilkan | Berhasil |
| 8 | Memulihkan API secara manual | API kembali dapat diakses | Health dan item endpoint berhasil setelah API dimulai kembali | Berhasil |
| 9 | CI untuk commit monitoring terbaru | Workflow terbaru sukses | Perlu verifikasi run setelah commit `083745e` | Belum dikonfirmasi |

## 4.10 Analisis

Berdasarkan pengujian yang tersedia, platform telah menjalankan fungsi utama aplikasi inventaris, akses melalui reverse proxy, koneksi database, automated testing, dan pengumpulan metrik monitoring. Docker Compose mempermudah pengelolaan layanan yang saling bergantung, sedangkan GitHub Actions menyediakan pemeriksaan otomatis terhadap perubahan kode.

Hasil query memori menunjukkan bahwa monitoring telah mengumpulkan seri metrik, tetapi jumlah seri yang banyak mengindikasikan perlunya penyaringan berdasarkan container atau label yang tepat. Dashboard sebaiknya hanya menampilkan metrik yang relevan agar mudah digunakan untuk pemantauan.

Pengujian pemulihan menunjukkan API dapat kembali berfungsi setelah container dimulai kembali secara manual. Untuk menguji ketahanan secara lebih lanjut, diperlukan pengujian kebijakan restart otomatis, pengujian persistensi setelah database direstart, serta verifikasi CI terbaru.

## 4.11 Kendala dan Tindak Lanjut

Beberapa hal yang perlu ditindaklanjuti:

1. Memastikan workflow GitHub Actions untuk commit terbaru berhasil.
2. Memfilter query Prometheus agar dashboard menampilkan metrik container proyek yang relevan.
3. Memastikan file `.env` tidak masuk ke version control dan kredensial tidak terekspos.
4. Melakukan pengujian khusus untuk restart otomatis jika ingin mengklaim fitur tersebut.
5. Melengkapi screenshot asli untuk seluruh gambar yang disebutkan dalam bab ini.
