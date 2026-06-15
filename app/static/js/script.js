// document.addEventListener('DOMContentLoaded', function() {
//     const btnAnalisis = document.getElementById('btnAnalisis');
//     const inputGambar = document.getElementById('inputGambar'); 

//     btnAnalisis.addEventListener('click', function(e) {
//         e.preventDefault();

//         // 1. Cek apakah gambar sudah dipilih
//         if (!inputGambar.files || inputGambar.files.length === 0) {
//             alert('Silakan pilih atau unggah foto daun teh terlebih dahulu.');
//             return;
//         }

//         // 2. Siapkan data untuk dikirim (FormData)
//         const formData = new FormData();
//         formData.append('file', inputGambar.files);

//         // 3. Tampilkan Loading (Opsional tapi bagus untuk skripsi)
//         btnAnalisis.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Menganalisis...';
//         btnAnalisis.disabled = true;

//         // 4. Kirim data ke Flask Route /predict
//         fetch('/predict', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === 'success') {
//                 // 5. Simpan hasil ke sessionStorage agar bisa diambil di halaman hasil.html
//                 sessionStorage.setItem('hasilKlasifikasi', JSON.stringify(data.hasil));
                
//                 // 6. Pindah ke halaman hasil
//                 window.location.href = '/klasifikasi/hasil'; 
//                 // Catatan: sesuaikan URL di atas dengan route Flask untuk hasil.html
//             } else {
//                 alert('Gagal: ' + data.error);
//                 resetButton();
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('Terjadi kesalahan koneksi ke server AI.');
//             resetButton();
//         });
//     });

//     function resetButton() {
//         btnAnalisis.innerHTML = 'Analisis Sekarang';
//         btnAnalisis.disabled = false;
//     }
// });