$(function () {
    $('[data-toggle="tooltip"]').tooltip()
});

var detailsModal = document.getElementById("detailsModal");

detailsModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var name = button.getAttribute("data-bs-name");
    var brand = button.getAttribute("data-bs-brand");
    var description = button.getAttribute("data-bs-description");
    var images = button.getAttribute("data-bs-images");
    const imageList = JSON.parse(document.getElementById(images).textContent)
    var modalTitle = detailsModal.querySelector(".modal-title");
    var modalSubtitle = detailsModal.querySelector(".modal-subtitle");
    var modalBodyP = detailsModal.querySelector(".modal-body p");
    var carouselDetailsModal = detailsModal.querySelector("#carouselDetailsModal");
    var carouselInner = document.createElement("div"); carouselInner.setAttribute("class", "carousel-inner");

    modalTitle.textContent = name;
    modalSubtitle.textContent = brand;
    if (description) modalBodyP.textContent = description;
    
    removeAllElements(carouselDetailsModal);
    carouselDetailsModal.appendChild(carouselInner);
    
    for (x in imageList) {
        var carouselItem = document.createElement("div");
        if (x < 1) {
            carouselItem.setAttribute("class", "carousel-item active");
        } else {
            carouselItem.setAttribute("class", "carousel-item");
        };
        carouselItem.setAttribute("data-bs-interval", "3000");
        
        var carouselItemImage = document.createElement("img");
        carouselItemImage.setAttribute("src", imageList[x]);
        carouselItemImage.setAttribute("class", "d-block w-100 rounded-5");
        if (x > 0) carouselItemImage.setAttribute("loading", "lazy");
        carouselItemImage.setAttribute("alt", "Imagem do carrossel");
        
        carouselItem.appendChild(carouselItemImage);
        carouselInner.appendChild(carouselItem);
    };

    if (imageList.length > 1) {
        var btnNext = document.createElement("button");
        btnNext.setAttribute("class", "carousel-control-next");
        btnNext.setAttribute("type", "button");
        btnNext.setAttribute("data-bs-target", "#carouselDetailsModal");
        btnNext.setAttribute("data-bs-slide", "next");
        var spanNext1 = document.createElement("span");
        spanNext1.setAttribute("class", "carousel-control-next-icon");
        spanNext1.setAttribute("aria-hidden", "true");
        var spanNext2 = document.createElement("span");
        spanNext2.setAttribute("class", "visually-hidden");
        spanNext2.textContent = "Próximo";

        btnNext.appendChild(spanNext1);
        spanNext1.after(spanNext2);
        carouselInner.after(btnNext);

        var btnPrev = document.createElement("button");
        btnPrev.setAttribute("class", "carousel-control-prev");
        btnPrev.setAttribute("type", "button");
        btnPrev.setAttribute("data-bs-target", "#carouselDetailsModal");
        btnPrev.setAttribute("data-bs-slide", "prev");
        var spanPrev1 = document.createElement("span");
        spanPrev1.setAttribute("class", "carousel-control-prev-icon");
        spanPrev1.setAttribute("aria-hidden", "true");
        var spanPrev2 = document.createElement("span");
        spanPrev2.setAttribute("class", "visually-hidden");
        spanPrev2.textContent = "Anterior";
        
        btnPrev.appendChild(spanPrev1);
        spanPrev1.after(spanPrev2);
        carouselDetailsModal.insertBefore(btnPrev, btnNext);
    };
});

function removeAllElements(element) {
    children = element.querySelectorAll("*")

    if (children.length > 0) {
        for (child of children) {
            child.remove()
        };
    };
};

function decreaseFont() {
    const fontSizes = [9, 10, 13, 16, 18, 24, 32]
    var p = detailsModal.querySelector(".modal-body p");
    styleFontSize = window.getComputedStyle(p).getPropertyValue("font-size");

    fontSizes.forEach(function (item, indice) {
        if (item == parseInt(styleFontSize)){
            p.style.fontSize = String(fontSizes[indice-1]) + "px"
        };
      });
};

function increaseFont() {
    const fontSizes = [9, 10, 13, 16, 18, 24, 32]
    var p = detailsModal.querySelector(".modal-body p");
    styleFontSize = window.getComputedStyle(p).getPropertyValue("font-size");

    fontSizes.forEach(function (item, indice) {
        if (item == parseInt(styleFontSize)){
            p.style.fontSize = String(fontSizes[indice+1]) + "px"
        };
      });
};