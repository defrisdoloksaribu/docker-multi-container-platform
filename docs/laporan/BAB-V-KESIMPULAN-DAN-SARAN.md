# BAB V — KESIMPULAN DAN SARAN

## 5.1 Kesimpulan

Berdasarkan implementasi dan hasil pengujian yang tersedia, dapat disimpulkan bahwa:

1. Platform inventaris berhasil dijalankan menggunakan Docker Compose dengan layanan FastAPI, PostgreSQL, dan Nginx serta komponen monitoring.
2. Endpoint `/health` memberikan status `healthy` dan melaporkan database `connected`. Endpoint `/items` juga berhasil mengembalikan data inventaris.
3. Automated testing menggunakan pytest menghasilkan tiga test berhasil (`3 passed`), meskipun terdapat satu peringatan deprecation yang perlu ditinjau pada pemeliharaan berikutnya.
4. Prometheus dan cAdvisor berhasil berkomunikasi dalam pengujian monitoring, ditunjukkan oleh target berstatus `UP` dan query `up{job="cadvisor"}` bernilai `1`.
5. Pengujian penghentian dan pemulihan API menunjukkan bahwa layanan kembali berfungsi setelah container dimulai kembali secara manual.
6. Proyek ini memberikan praktik langsung mengenai containerization, service orchestration, CI, database persistence, dan observability. Namun, pengujian automatic restart, pemfilteran metrik yang lebih tepat, dan verifikasi CI terbaru masih perlu dituntaskan atau didokumentasikan.

## 5.2 Saran Pengembangan

Pengembangan berikutnya dapat dilakukan dengan:

1. Memperbaiki query Prometheus agar dashboard fokus pada container aplikasi proyek.
2. Menambahkan alert rules dan mekanisme notifikasi untuk kondisi layanan tertentu.
3. Menguji restart policy secara terpisah untuk membuktikan perilaku pemulihan otomatis.
4. Menambahkan pengujian integrasi dan pengujian beban sesuai kebutuhan.
5. Meninjau versi dependensi dan menyelesaikan warning deprecation.
6. Meninjau pengelolaan secrets, konfigurasi jaringan, dan hak akses sebelum digunakan pada lingkungan yang lebih kritis.
7. Melengkapi dokumentasi dengan screenshot asli serta memastikan seluruh klaim sesuai dengan hasil pengujian.
