// OmniShield - I18N Frontend Loader (Vanilla JS)
const translations = {
    fr: { title: "OmniShield Sécurité", audit: "Lancer un audit" },
    en: { title: "OmniShield Security", audit: "Run Audit" },
    es: { title: "OmniShield Seguridad", audit: "Ejecutar auditoría" }
};

function changeFrontendLanguage(langCode) {
    const dict = translations[langCode] || translations["fr"];
    console.log(`[I18N] Langue basculée vers : ${langCode}`);
    return dict;
}