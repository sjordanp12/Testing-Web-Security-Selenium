# 🔐 SQL Injection Test Automation with Selenium

Skrip ini digunakan untuk **mengautomasi pengujian SQL Injection** pada halaman login menggunakan Selenium WebDriver. Tujuannya adalah mengidentifikasi apakah form login rentan terhadap serangan SQL Injection sederhana.

---

## 📋 Fitur

- Mengakses halaman login: `https://bempenusa.cloud/login`
- Mengisi input `username` dan `password` dengan payload SQL Injection.
- Mencoba login dan mendeteksi apakah berhasil masuk ke dashboard secara tidak sah.
- Menampilkan hasil pengujian di terminal/console.

---

## 🚀 Teknologi

- Python
- Selenium WebDriver
- ChromeDriver

---

## 🛠️ Instalasi

1. **Clone repo atau salin file Python**
2. **Pasang dependensi Selenium** (jika belum):

```bash
pip install selenium
```
