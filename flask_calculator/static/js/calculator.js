document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculator-form');
    const resultDiv = document.getElementById('result');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.success) {
                resultDiv.innerHTML = `<div class="alert alert-success" role="alert">Result: ${data.result}</div>`;
            } else {
                resultDiv.innerHTML = `<div class="alert alert-danger" role="alert">Error: ${data.error}</div>`;
            }
        } catch (error) {
            resultDiv.innerHTML = `<div class="alert alert-danger" role="alert">Error: ${error.message}</div>`;
        }
    });
});
