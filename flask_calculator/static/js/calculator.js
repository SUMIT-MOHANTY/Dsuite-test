document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculator-form');
    const resultArea = document.getElementById('result-area');
    
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        // Reset previous results
        resultArea.classList.add('d-none');
        resultArea.innerHTML = '';
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });
            const data = await response.json();
            
            if (data.success) {
                resultArea.innerHTML = `
                    <div class="card">
                        <div class="card-header bg-primary text-white">
                            <h5 class="card-title mb-0">Result</h5>
                        </div>
                        <div class="card-body">
                            <p class="card-text fs-4">${data.result}</p>
                        </div>
                    </div>
                `;
            } else {
                resultArea.innerHTML = `
                    <div class="alert alert-danger" role="alert">
                        ${data.error || 'An error occurred'}
                    </div>
                `;
            }
            resultArea.classList.remove('d-none');
        } catch (error) {
            resultArea.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    Failed to process calculation: ${error.message}
                </div>
            `;
            resultArea.classList.remove('d-none');
        }
    });
    
    // Bootstrap form validation
    const inputs = form.querySelectorAll('.form-control, .form-select');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.checkValidity()) {
                this.classList.remove('is-invalid');
            }
        });
    });
});
