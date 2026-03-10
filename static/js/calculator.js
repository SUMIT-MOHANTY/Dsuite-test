$(document).ready(function() {
    $('#calculatorForm').on('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            num1: $('#num1').val(),
            num2: $('#num2').val(),
            operation: $('#operation').val()
        };
        
        $.ajax({
            url: '/calculate',
            method: 'POST',
            data: formData,
            success: function(response) {
                const resultDiv = $('#result');
                
                if (response.success) {
                    resultDiv.removeClass('alert-danger').addClass('alert-success');
                    resultDiv.html(`
                        <strong>Result:</strong> ${response.result}
                    `);
                } else {
                    resultDiv.removeClass('alert-success').addClass('alert-danger');
                    resultDiv.html(`<strong>Error:</strong> ${response.error}`);
                }
                
                resultDiv.show();
            },
            error: function() {
                $('#result')
                    .removeClass('alert-success').addClass('alert-danger')
                    .html('<strong>Error:</strong> Failed to contact server')
                    .show();
            }
        });
    });
});
