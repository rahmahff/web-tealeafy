INFO_PENYAKIT = {
    'Algal Leaf Spot': {
        'penyebab': 'Alga Chephaleuros virescens.',
        'ciri': 'Terdapat bercak cokelat tidak beraturan pada daun, dengan bagian tengah berwarna abu-abu.',
        'penanganan': 'Apabila gejalanya ringan dapat dilakukan dengan pemangkasan pada daun yang terinfeksi. Namun, apabila kondisi terinfeksi sudah parah maka disarankan'
        'untuk melakukan penyemprotan fungisida (salah satu jenis pestisida yang dapat mencegah perkembangan jamur).'
    },
    'Blister Blight': {
        'penyebab': 'Jamur Exobasidium vexans.',
        'ciri': 'Munculnya bintik-bintik berwarna yang kontras dengan warna hijau daun teh, di mana pada tingkat keparahan tertentu daun akan menggulung secara tidak beraturan.',
        'penanganan': 'Dapat dilakukan melalui pemangkasan daun yang terinfeksi, pemanenan pucuk secara berkala, pembuangan daun yang menunjukkan gejala serangan,'
        'serta penggunaan fungisida untuk menghambat penyebaran.'
    },
    'Brown Blight': {
        'penyebab': 'Jamur Pestalotiopsis sp.',
        'ciri': 'Terdapat bintik kecil berwarna kekuningan yang kemudian menyebar dan berkembang menjadi warna cokelat gelap, dimulai dari tepi hingga tengah permukaan daun.',
        'penanganan': 'Dapat dilakukan dengan peningkatan ketahanan tanaman inang dengan memperkuat sistem pertahanan alami tanaman, serta pemangkasan untuk mencegah penyebaran penyakit.'
    },
    'Gray Blight': {
        'penyebab': 'Patogen Pestalotiopsis thedae.',
        'ciri': 'Bercak berwarna cokelat pada bagian tengah daun, kemudian berubah menjadi warna abu-abu dengan tepian cokelat dan menyebar pada permukaan daun.',
        'penanganan': 'Dapat menerapkan proses sanitasi kebun untuk meminimalkan keberadaan sumber patogen serta penggunaan pengendali kimia secara tepat guna menghambat penyebaran penyakit.'
    },
    'Helopeltis': {
        'penyebab': 'Hama kepik penghisap cairan daun (Helopeltis antonii).',
        'ciri': 'Terdapat bercak berwarna hitam akibat bekas tusukan pada daun teh, kemudian akan mengering menyebabkan jaringan tanaman mengalami kematian.',
        'penanganan': 'Dapat menerapkan pendekatan Pengendalian Hama Terpadu (HPT), mencakup kultur teknis (pemetikan pucuk, pemangkasan, pengelolaan naungan, dan sanitasi lingkungan), '
        'pengendalian hayati, penggunaan varietas yang tahan terhadap penyakit, serta pemanfaatan pestisida nabati dan kimiawi sesuai kebutuhan.'
    },
    'Red Rust': {
        'penyebab': 'Alga Cephaleuros parasiticus Karst.',
        'ciri': 'Munculnya bintik pada daun akibat penyebaran melalui angin atau percikan air dalam jumlah banyak atau sedikit yang tersebar di permukaan daun.',
        'penanganan': 'Dapat dilakukan melalui kombinasi tindakan sanitasi kebun, pemangkasan, dan penyemprotan fungisida untuk menjaga kesehatan tanaman.'
    },
    'Red Spider Mite': {
        'penyebab': 'Tungau merah (Oligonychus coffeae).',
        'ciri': 'Daun yang terinfeksi mengalami perubahan warna menjadi merah kecokelatan yang mengakibatkan daun menjadi layu, rontok, hingga kering.',
        'penanganan': 'Dapat diterapkan melalui penggunaan varietas tanaman yang tahan terhadap serangan hama, mendukung keberadaan musuh alami sebagai pengendalian hayati, '
        'serta menjaga kebersihan peralatan yang digunakan selama kegiatan operasional di lapangan.'
    },
    'Sehat': {
        'penyebab': 'Tanaman dalam kondisi optimal dan terawat.',
        'ciri': 'Daun memiliki warna hijau cerah dengan permukaan yang halus dan seragam, tanpa adanya perubahan warna akibat serangan penyakit atau hama.',
        'penanganan': 'Daun teh berada dalam kondisi sehat. Untuk itu lakukan pemeliharaan yang rutin agar kesehatan tanaman dapat terjaga dengan baik.'
    }
}

INFO_KESIAPAN = {
    'Siap Panen': 'Daun dengan memiliki kuncup disertai tiga daun muda dibawahnya telah mencapai kematangan optimal dan memenuhi standar petikan.',
    'Belum Siap Panen': 'Daun dengan memiliki kuncup disertai satu atau dua daun muda dibawahnya masih dalam tahap pertumbuhan, sehingga memerlukan waktu untuk mencapai standar petikan.',
    'Tidak Layak Panen': 'Daun tidak memenuhi kriteria untuk dilakukan pemetikan karena berada dalam kondisi sakit, sehingga estimasi waktu panen tidak tersedia.'
}

def get_detail_penyakit(label):
    return INFO_PENYAKIT.get(label, {'penyebab': 'Informasi tidak tersedia.', 'ciri': 'Informasi tidak tersedia.'})

def get_kondisi_daun(label_penyakit):
    if label_penyakit == 'Sehat':
        return {
            'teks': "Sehat",
            'status': "sehat"
        }
    else:
        return {
            'teks': f"Sakit ({label_penyakit})",
            'status': "sakit"
        }

def get_detail_kesiapan(label):
    return INFO_KESIAPAN.get(label, 'Informasi status tidak tersedia.')

def get_penanganan(label):
    data = INFO_PENYAKIT.get(label, {})
    return data.get(
        'penanganan',
        'Informasi penanganan tidak tersedia.'
    )

def format_label(label):
    if not label: return ""
    return str(label).replace('_', ' ').title()

def format_hasil_multitask(label_kesiapan, nilai_estimasi):
    if label_kesiapan == 'Tidak Layak Panen':
        return "Tidak Tersedia"
    
    hari_final = round(float(nilai_estimasi))
    return f"{max(0, hari_final)} Hari"

def get_keterangan_lengkap(label_penyakit, label_kesiapan):
    detail_p = INFO_PENYAKIT.get(
        label_penyakit,
        {
            'penyebab': 'Informasi tidak tersedia.',
            'ciri': 'informasi tidak tersedia.'
        }
    )

    penyebab = detail_p['penyebab'].rstrip('.')
    ciri = detail_p['ciri'].rstrip('.')
    
    if label_penyakit == 'Sehat':
        paragraf_penyakit = (
            "Daun teh berada dalam kondisi sehat dan tidak menunjukkan "
            "adanya gejala serangan penyakit maupun hama. "
            f"Hal ini ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Algal Leaf Spot':
        paragraf_penyakit = (
            f"Daun teh mengalami penyakit {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Hal ini ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Blister Blight':
        paragraf_penyakit = (
            f"Daun teh mengalami penyakit {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Kondisi ini ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Brown Blight':
        paragraf_penyakit = (
            f"Daun teh mengalami penyakit {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Gejalanya ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Gray Blight':
        paragraf_penyakit = (
            f"Daun teh mengalami penyakit {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Penyakit ini ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Helopeltis':
        paragraf_penyakit = (
            f"Daun teh mengalami serangan {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Hal ini ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Red Rust':
        paragraf_penyakit = (
            f"Daun teh mengalami penyakit {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Kondisi ini ditandai dengan {ciri.lower()}."
        )

    elif label_penyakit == 'Red Spider Mite':
        paragraf_penyakit = (
            f"Daun teh mengalami serangan {label_penyakit} yang disebabkan oleh "
            f"{penyebab.lower()}. Gejala yang terlihat yaitu {ciri.lower()}."
        )

    else:
        paragraf_penyakit = (
            f"Daun teh mengalami kondisi {label_penyakit}. "
            f"Penyebabnya adalah {penyebab.lower()} "
            f"dengan ciri-ciri berupa {ciri.lower()}."
        )

    # DESKRIPSI KESIAPAN PANEN
    if label_kesiapan == 'Siap Panen':
        paragraf_kesiapan = (
            "Daun telah memenuhi kriteria untuk dilakukan pemetikan "
            "dan berada pada kondisi optimal untuk dipanen."
        )

    elif label_kesiapan == 'Belum Siap Panen':
        paragraf_kesiapan = (
            "Daun masih berada dalam tahap pertumbuhan sehingga "
            "memerlukan waktu lebih lanjut untuk mencapai kondisi panen yang optimal."
        )

    elif label_kesiapan == 'Tidak Layak Panen':
        paragraf_kesiapan = (
            "Daun tidak memenuhi kriteria untuk dilakukan pemetikan, "
            "sehingga estimasi waktu panen tidak tersedia."
        )

    else:
        paragraf_kesiapan = (
            "Informasi kesiapan panen tidak tersedia."
        )

    return f"{paragraf_penyakit} {paragraf_kesiapan}"