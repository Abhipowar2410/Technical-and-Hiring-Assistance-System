// registration.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const phoneInput = document.getElementById("phone");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    form.addEventListener("submit", function(event) {
        let valid = true;

        // Validate phone number (10 digits)
        const phonePattern = /^\d{10}$/;
        if (!phonePattern.test(phoneInput.value)) {
            alert("Please enter a valid 10-digit phone number.");
            valid = false;
        }

        // Validate email (simple email pattern)
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailInput.value)) {
            alert("Please enter a valid email address.");
            valid = false;
        }

        // Validate password (minimum 8 characters)
        if (passwordInput.value.length < 8) {
            alert("Password must be at least 8 characters long.");
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
        }
    });
});
