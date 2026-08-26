// OmniShield - Core DOM Controller (Vanilla JS)
document.addEventListener("DOMContentLoaded", () => {
    console.log("[OMNISHIELD DOM] Interface initialisée et sécurisée.");
});

function updateSystemStatus(statusText, isSecure = true) {
    const badge = document.getElementById('license-status');
    if (badge) {
        badge.innerText = statusText;
        badge.style.color = isSecure ? "#10b981" : "#ef4444";
    }
}