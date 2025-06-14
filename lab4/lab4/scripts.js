document.addEventListener("DOMContentLoaded", function () {
    const browserInfoElement = document.getElementById("browser-info");
    if (browserInfoElement) {
        browserInfoElement.textContent = navigator.userAgent;
    }
    document.getElementById("version-info").textContent = navigator.appVersion;
    document.getElementById("os-info").textContent = window.navigator.userAgentData && window.navigator.userAgentData.platform
        ? window.navigator.userAgentData.platform
        : (window.navigator.platform || "Неизвестно");
    document.getElementById("platform-info").textContent = navigator.platform;
    document.getElementById("language-info").textContent = navigator.language;
    // Добавьте другие свойства объекта navigator по необходимости
   });