document.addEventListener('DOMContentLoaded', function() {
    const dataSesi = sessionStorage.getItem('hasilKlasifikasi');

    if (dataSesi) {
        const hasil = JSON.parse(dataSesi);
        const elemenKondisi = document.getElementById('kondisi-daun');
        const elemenEstimasi = document.getElementById('estimasi-panen');
        const elemenKesiapan = document.getElementById('kesiapan-panen');
        const elemenAkurasiP = document.getElementById('akurasi-p');
        const elemenAkurasiK = document.getElementById('akurasi-k');
        const elemenKeterangan = document.getElementById('keterangan');
        const elemenPenanganan = document.getElementById('penanganan');

        if (elemenKondisi) {
            elemenKondisi.innerText = hasil.kondisi_teks;
            elemenKondisi.style.color = (hasil.kondisi_status === 'sehat') ? '#2E7D32' : '#C62828';
        }

        if (elemenEstimasi) elemenEstimasi.innerText = hasil.estimasi;
        if (elemenKesiapan) elemenKesiapan.innerText = hasil.kesiapan;
        if (elemenAkurasiP) elemenAkurasiP.innerText = hasil.akurasi_penyakit;
        if (elemenAkurasiK) elemenAkurasiK.innerText = hasil.akurasi_kesiapan;
        if (elemenKeterangan) {
            elemenKeterangan.innerText = hasil.keterangan;
        }
        if (elemenPenanganan) {
            elemenPenanganan.innerText = hasil.penanganan;
        }

    } else {
        alert("Data tidak ditemukan. Silakan lakukan klasifikasi terlebih dahulu.");
        window.location.href = "/klasifikasi";
    }
});