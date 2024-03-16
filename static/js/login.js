document
  .getElementById("login-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const user = {
      email: email,
      password: password,
    };

    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(user),
      });

      const data = await response.json();

      if (response.ok) {
        document.cookie = `token=${data["x-access-token"]}; path=/`;
        window.location.href = "/dashboard";
      } else {
        const errorMessage = data.detail;
        document.getElementById("error-message").textContent = errorMessage;
        document.getElementById("error-container").classList.remove("hidden");
      }
    } catch (error) {
      console.error("Oops, an error occurred");
    }
  });