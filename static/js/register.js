document.getElementById("register-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const user = {
        name: name,
        email: email,
        password: password,
    };

    try {
        const response = await fetch("/api/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        });

        const data = await response.json();

        if (response.ok) {
            window.location.href = "/login/";
        } else {
            const errorMessage = data;
            for (const field in errorMessage) {
                // Acessa a mensagem de erro para o campo atual
                const errorMessages = errorMessage[field];

                // Itera sobre as mensagens de erro para o campo atual
                errorMessages.forEach(errorMessage => {
                    document.getElementById("error-message").textContent = errorMessage;
                    document.getElementById("error-container").classList.remove("hidden");
                });
            }
        }
    } catch (error) {
        console.error("Oops, an error occurred");
    }
});
