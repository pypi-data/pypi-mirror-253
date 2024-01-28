// Bring magnifiable components over the hover.
document.querySelectorAll('.magnifiable').forEach(container => {
    container.addEventListener('mouseover', () => {
        container.style.zIndex = 1000;  // Bring to front on hover
    });
    container.addEventListener('mouseout', () => {
        container.style.zIndex = 1;     // Reset on mouse out
    });
});