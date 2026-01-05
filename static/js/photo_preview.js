document.addEventListener("DOMContentLoaded", function () {
    const photoInput = document.getElementById("photoInput");
    const previewImage = document.getElementById("previewImage");

    photoInput.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result;
                previewImage.style.display = "block";
                previewImage.style.maxWidth = "100px"; // optionnel
                previewImage.style.borderRadius = "8px"; // optionnel
            };
            reader.readAsDataURL(file);
        }
    });
});
