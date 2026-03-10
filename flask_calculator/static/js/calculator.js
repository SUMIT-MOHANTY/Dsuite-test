document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculatorForm');
    const resultDiv = document.getElementById('result');
    const resultValue = document.getElementById('result-value');
    const errorDiv = document.getElementById('error');
    const errorMessage = document.getElementById('error-message');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Hide previous results
        resultDiv.style.display = 'none';
        errorDiv.style.display = 'none';
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                body: new URLSearchParams(formData),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            });
            
            const data = await response.json();
            
            if (data.success) {
                resultValue.textContent = data.result;
                resultDiv.style.display = 'block';
            } else {
                errorMessage.textContent = data.error;
                errorDiv.style.display = 'block';
            }
        } catch (error) {
            errorMessage.textContent = 'An unexpected error occurred. Please try again.';
            errorDiv.style.display = 'block';
        }
    });
});
