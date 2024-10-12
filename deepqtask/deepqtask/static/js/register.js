const usernameField = document.querySelector('#usernameField');
const feedbackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector('#emailField');
const emailFeedbackArea = document.querySelector(".invalid-emailfeedback");
const submitBtn = document.querySelector(".submit-btn");

submitBtn.disabled = true;

usernameField.addEventListener('keyup',(e) => {
    const usernameVal = e.target.value;

    if(usernameVal.length > 0){
        //fetch API
        fetch('/authentication/validate-username', {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res => res.json()).then(data => {
            console.log("data", data);
            if(data.username_error){
                submitBtn.disabled = true;
                usernameField.classList.add('is-invalid');
                feedbackArea.style.display = "block"; 
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`
            } else {
                submitBtn.disabled = false;
                usernameField.classList.remove('is-invalid');
                feedbackArea.style.display = 'none'; // Hide feedback when valid
            }
        });
    }
});

emailField.addEventListener('keyup',(e) => {
    const emailVal = e.target.value;
    if(emailVal.length > 0){
        fetch('/authentication/validate-email', {
            body: JSON.stringify({email: emailVal}),
            method: "POST"
        }).then(res => res.json()).then(data => {
            console.log("data", data);
            if(data.email_error){
                submitBtn.disabled = true;
                emailField.classList.add('is-invalid');
                emailFeedbackArea.style.display = "block"; 
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`
            } else {
                submitBtn.disabled = false;
                emailField.classList.remove('is-invalid');
                emailFeedbackArea.style.display = 'none'; // Hide feedback when valid
            }
        })
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const passwordField = document.getElementById('passwordField');
    const togglePassword = document.getElementById('togglePassword');
    const passwordIcon = document.getElementById('passwordIcon');

    togglePassword.addEventListener('click', function() {
        // Toggle the type attribute
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);

        // Toggle the text and icon
        if (type === 'text') {
            togglePassword.textContent = 'HIDE';
            passwordIcon.classList.remove('fa-eye');
            passwordIcon.classList.add('fa-eye-slash');
        } else {
            togglePassword.textContent = 'SHOW';
            passwordIcon.classList.remove('fa-eye-slash');
            passwordIcon.classList.add('fa-eye');
        }
    });
});
