const buttonInstall = document.querySelector("#btn-installPWA");

console.log(window.beforeintallprompt);

window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    window.deferredPrompt = e;
    // buttonInstall.classList.toggle("d-none", false);
    // buttonInstall.setAttribute("disabled", true);
    buttonInstall.removeAttribute("disabled");
});

buttonInstall.addEventListener("click", async () => {
    if (!window.deferredPrompt) { return }
    window.deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    window.deferredPrompt = null;
});

window.addEventListener('appinstalled', () => {
    // buttonInstall.classList.toggle("d-none", true);
    buttonInstall.setAttribute("disabled", true);
    window.deferredPrompt = null;
});