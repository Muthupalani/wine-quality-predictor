document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        alert('Submitting your data!');
        form.submit();
    });
});
