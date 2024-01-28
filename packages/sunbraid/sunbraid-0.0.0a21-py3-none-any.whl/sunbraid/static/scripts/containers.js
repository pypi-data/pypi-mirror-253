// Bring magnifiable components over the hover.
console.log('Running containers.js');

document.querySelectorAll('.magnifiable').forEach(container => {
    container.addEventListener('mouseover', () => {
        container.style.zIndex = 1000;  // Bring to front on hover
        console.log('mouseover')
    });
    container.addEventListener('mouseout', () => {
        console.log('mouseout')
        container.style.zIndex = 1;     // Reset on mouse out
    });
});