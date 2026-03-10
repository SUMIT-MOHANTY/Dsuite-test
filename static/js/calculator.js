// Optimization: Minified JS with caching
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculatorForm');
    const result = document.getElementById('result');
    
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
                result.innerHTML = `<div class="alert alert-success">Result: ${data.result}</div>`;
            } else {
                result.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
            }
        } catch (error) {
            result.innerHTML = `<div class="alert alert-danger">Network error occurred</div>`;
        }
    });
});
