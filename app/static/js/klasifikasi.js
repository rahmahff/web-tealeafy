const uploadModal = new bootstrap.Modal(document.getElementById('uploadModal')),
      dropArea = document.getElementById('drop-area'),
      fileElem = document.getElementById('fileElem'),
      btnSubmit = document.getElementById('btn-submit'),
      video = document.getElementById('camera-stream'),
      canvas = document.getElementById('camera-canvas'),
      cameraContainer = document.getElementById('camera-container'),
      captureButton = document.getElementById('captureButton'),
      cancelCameraButton = document.getElementById('cancelCameraButton');

let activeStream = null;

// UPLOAD
dropArea.addEventListener('click', () => uploadModal.show());

// UNGGAH DARI PERANGKAT
document.getElementById('opt-upload').addEventListener('click', () => {
    fileElem.removeAttribute("capture");
    fileElem.click();
    uploadModal.hide();
});

// AMBIL FOTO
document.getElementById('opt-camera').addEventListener('click', async () => {
    uploadModal.hide();

    const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

    // HP
    if (isMobile) {
        fileElem.setAttribute("capture", "environment");
        fileElem.click();
        return;
    }

    // LAPTOP
    try {
        activeStream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        video.srcObject = activeStream;
        cameraContainer.classList.remove('d-none');

    } catch (err) {
        console.error(err);
        Swal.fire({
            title: 'Kamera Tidak Dapat Dibuka',
            text: 'Pastikan browser memiliki izin mengakses kamera.',
            icon: 'error'
        });
    }
});

// FUNGSI AMBIL FOTO
captureButton.addEventListener('click', () => {
    const ctx = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
        const file = new File(
            [blob],
            "camera-photo.jpg",
            { type: "image/jpeg" }
        );
        const dt = new DataTransfer();
        dt.items.add(file);
        fileElem.files = dt.files;
        fileElem.dispatchEvent(new Event("change"));
    }, "image/jpeg");
    stopCamera();
});

// BATAL
cancelCameraButton.addEventListener('click', () => {
    stopCamera();
});

// STOP CAMERA
function stopCamera() {
    if (activeStream) {
        activeStream.getTracks().forEach(track => track.stop());
        activeStream = null;
    }
    cameraContainer.classList.add('d-none');
}

// VALIDASI DAN PREVIEW
fileElem.addEventListener("change", function () {
    const file = this.files[0];
    if (!file) return;

    const allowedTypes = ["image/jpeg", "image/png", "image/jpg"];
    if (!allowedTypes.includes(file.type)) {

        btnSubmit.disabled = true;

        Swal.fire({
            title: 'Format Tidak Sesuai',
            text: 'Silakan unggah gambar dalam format JPG, JPEG, atau PNG.',
            icon: 'error',
            iconColor: '#C62828',
            buttonsStyling: false,
            customClass: {
                popup: 'swal2-popup',
                title: 'custom-swal-title',
                htmlContainer: 'custom-swal-text',
                confirmButton: 'btn-ok-custom'
            }
        });

        this.value = "";
        return;
    }

    const reader = new FileReader(),
        imgPreview = document.getElementById("img-preview"),
        fileNameLabel = document.getElementById("file-name"),
        uploadIcon = document.querySelector(".upload-area i");

    reader.onload = e => {
        imgPreview.src = e.target.result;
        imgPreview.classList.remove("d-none");

        if (uploadIcon) uploadIcon.style.display = "none";
        if (fileNameLabel) fileNameLabel.style.display = "none";

        btnSubmit.disabled = false;
    };
    reader.readAsDataURL(file);
});

// SUBMIT KLASIFIKASI
btnSubmit.addEventListener('click', function () {
    const file = fileElem.files[0];
    Swal.fire({
        title: 'Konfirmasi Klasifikasi Gambar',
        showConfirmButton: true,
        showCancelButton: true,
        confirmButtonText: 'Lanjutkan Klasifikasi',
        cancelButtonText: 'Tidak Lanjutkan',
        showCloseButton: false,
        buttonsStyling: false,
        customClass: {
            popup: 'swal2-popup',
            title: 'custom-swal-title title-left',
            confirmButton: 'btn-confirm-custom',
            cancelButton: 'btn-cancel-custom',
            actions: 'swal2-actions',
        }
    }).then(async result => {

        if (!result.isConfirmed) return;
        try {
            Swal.fire({
                title: 'Sedang Menganalisis Gambar...',
                text: 'Mohon tunggu',
                allowOutsideClick: false,
                customClass: {
                    popup: 'loading-popup',
                    title: 'loading-title',
                    htmlContainer: 'loading-text'
                },
                didOpen: () => Swal.showLoading()
            });

            const formData = new FormData();
            formData.append("file", file);
            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            if (data.status === "success") {

                sessionStorage.setItem(
                    'hasilKlasifikasi',
                    JSON.stringify(data.hasil)
                );

                setTimeout(() => {
                    window.location.href = "/hasil";
                }, 1500);

            } else {
                Swal.fire({
                    title: 'Prediksi Gagal',
                    text: data.error || 'Terjadi kesalahan saat klasifikasi.',
                    icon: 'error',
                    iconColor: '#C62828',
                    buttonsStyling: false,
                    customClass: {
                        popup: 'swal2-popup',
                        title: 'custom-swal-title',
                        htmlContainer: 'custom-swal-text',
                        confirmButton: 'btn-ok-custom'
                    }
                });
            } 
        } catch (error) {
            console.error(error);

            Swal.fire({
                title: 'Error',
                text: 'Gagal terhubung ke server',
                icon: 'error',
                iconColor: '#C62828',
                buttonsStyling: false,
                customClass: {
                    popup: 'swal2-popup',
                    title: 'custom-swal-title',
                    htmlContainer: 'custom-swal-text',
                    confirmButton: 'btn-ok-custom'
                }
            });
        }
    });
});