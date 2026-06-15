from flask import Blueprint, render_template, request, jsonify
from app.utils.preprocessing import prepare_image
from app.utils.predict import get_prediction
from app.utils.helper import (
    get_kondisi_daun,
    format_label,
    format_hasil_multitask,
    get_keterangan_lengkap,
    get_penanganan
)

import os
import uuid
from datetime import datetime

# Inisialisasi Blueprint
main_bp = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join('app', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/klasifikasi')
def klasifikasi():
    return render_template('klasifikasi.html')

@main_bp.route('/hasil')
def hasil():
    return render_template('hasil.html')

# HALAMAN ARTIKEL
@main_bp.route('/artikel-penyakit')
def artikel_penyakit():
    return render_template('artikel-penyakit.html')

@main_bp.route('/artikel-kesiapan')
def artikel_kesiapan():
    return render_template('artikel-kesiapan.html')

@main_bp.route('/artikel-penanganan')
def artikel_penanganan():
    return render_template('artikel-penanganan.html')

@main_bp.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({
            'error': 'Tidak ada file yang diunggah'
        }), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({
            'error': 'Nama file tidak valid'
        }), 400

    try:
        # SIMPAN FOLDER UPLOADS
        ext = os.path.splitext(file.filename)[1]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        short_uuid = uuid.uuid4().hex[:6]
        filename = (f"teh_{timestamp}_{short_uuid}{ext}")

        file_path = os.path.join(UPLOAD_FOLDER,filename)
        file.save(file_path)

        # PRAPEMROSESAN GAMBAR
        processed_img = prepare_image(file_path)

        if processed_img is None:
            return jsonify({
                'error':
                'Gagal memproses gambar'
            }), 500
        
        raw_results = get_prediction(processed_img)

        if not raw_results:
            return jsonify({
                'error':
                'Gagal melakukan prediksi'
            }), 500

        # VALIDASI THRESHOLD
        if raw_results.get('status') == 'invalid':
            return jsonify({
                'status': 'invalid',
                'message': raw_results['message']
            })

        # FORMAT HASIL
        nama_p = format_label(raw_results['penyakit'])
        nama_k = format_label(raw_results['kesiapan'])
        kondisi_data = get_kondisi_daun(nama_p)
        estimasi_final = (format_hasil_multitask(nama_k, raw_results['estimasi_raw']))
        keterangan_gabungan = (get_keterangan_lengkap(nama_p, nama_k))
        penanganan = get_penanganan(nama_p)

        # RESPON
        return jsonify({
            'status': 'success',
            'hasil': {
                'kondisi_teks': kondisi_data['teks'],
                'kondisi_status': kondisi_data['status'],
                'kesiapan': nama_k,
                'estimasi': estimasi_final,
                'akurasi_penyakit': f"{raw_results['akurasi_p']:.2f}%",
                'akurasi_kesiapan': f"{raw_results['akurasi_k']:.2f}%",
                'keterangan': keterangan_gabungan,
                'penanganan': penanganan,
                'gambar': f"/app/uploads/{filename}"
            }
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500