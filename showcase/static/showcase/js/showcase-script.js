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
    var carouselInner = detailsModal.querySelector("#carouselDetailsModal .carousel-inner")

    if (!description)
        description = "Infelizmente nenhuma descrição foi informada para o item selecionado!!!"

    modalTitle.textContent = name;
    modalSubtitle.textContent = brand;
    modalBodyP.textContent = description;

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
        carouselItemImage.setAttribute("alt", "...");
        
        carouselItem.appendChild(carouselItemImage);
        carouselInner.appendChild(carouselItem);
    };
});

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