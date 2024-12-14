# RecurCrawl - Analisis Algoritma Crawler Iteratif dan Rekursif

![RecurCrawl](https://github.com/user-attachments/assets/c1f63bb3-bd3c-40a3-ad7e-525d6127c571)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-orange.svg)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-blueviolet.svg)](https://tailwindcss.com/)

Platform web untuk menganalisis & membandingkan efisiensi runtime algoritma crawler data media sosial (iteratif vs. rekursif).

## Tentang Proyek

**RecurCrawl** adalah aplikasi web yang dirancang untuk menganalisis dan membandingkan efisiensi dua pendekatan algoritma fundamental—iteratif dan rekursif—dalam konteks web crawling data dari platform media sosial Threads.

## Fitur Utama

- **Analisis Performa**: Membandingkan waktu eksekusi (runtime) kedua algoritma pada berbagai ukuran dataset.
- **Unggah Dataset**: Pengguna dapat mengunggah berkas JSON sebagai dataset untuk diuji.
- **Input Dinamis**: Memasukkan berbagai ukuran dataset untuk diuji secara bersamaan.
- **Hasil Visual**: Hasil analisis ditampilkan secara dinamis dalam bentuk tabel dan grafik yang mudah dipahami.

## Tumpukan Teknologi

- Backend: Flask (Python)
- Frontend: HTML, Tailwindcss, JavaScript
- Visualisasi: Matplotlib

## Arsitektur Pengujian

Pengujian dilakukan di hosting **Anymhost** dengan spesifikasi memori **10GB** untuk memastikan lingkungan yang stabil dan mampu menangani pemrosesan data dalam jumlah besar.

## Hasil Pengujian

Berikut adalah contoh hasil analisis yang dijalankan pada dataset `10k.json` dengan ukuran 1000, 5000, dan 10.000 data.

### Grafik Perbandingan
<details>
  <summary>Klik untuk melihat gambar</summary>

  ![RecurCrawl - Analisis Algoritma](https://github.com/user-attachments/assets/6b55672b-a434-4f42-b6cf-6da43c487a9e)

</details>

### Tabel Waktu Eksekusi

| Ukuran Data | Iterative Time (s) | Recursive Time (s) |
|:----------- |:------------------ |:------------------ |
| 1000        | 0.0039             | 0.0023             |
| 5000        | 0.1121             | 0.0126             |
| 10000       | 0.2392             | 0.0277             |

## Kesimpulan

Berdasarkan pengujian, algoritma **rekursif** menunjukkan performa yang lebih unggul pada dataset kecil hingga menengah. Namun, untuk dataset yang sangat besar dan dalam, pendekatan **iteratif** cenderung lebih stabil dan aman dari risiko *stack overflow*. Pemilihan hosting dengan memori **10GB** terbukti memadai untuk mendukung pengujian ini secara optimal.

## Instalasi dan Menjalankan Proyek

1.  **Clone Repositori:**
    ```bash
    git clone https://github.com/RozhakDev/RecurCrawl.git
    cd RecurCrawl
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Server:**
    ```bash
    python run.py
    ```

4.  **Akses Web:** Buka `http://127.0.0.1:5000/` di browser Anda.

## Cara Berkontribusi

Kami sangat terbuka untuk kontribusi! Jika Anda ingin berkontribusi pada proyek ini, silakan *fork* repositori ini dan buat *pull request* dengan perubahan Anda. Anda juga bisa membuka *issue* jika menemukan bug atau memiliki saran fitur.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.

## Referensi

- Analisis Perbandingan Kinerja Metode Rekursif dan Iteratif