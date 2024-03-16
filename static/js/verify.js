async function getCookieToken() {
    const cookies = document.cookie.split(";");
    for (const cookie of cookies) {
      const [name, value] = cookie.trim().split("=");
      if (name === "token") {
        return value;
      }
    }
    return null;
  }
  
  async function getProfileData(usernameClassName, emailClassName) {
    try {
      const usernameElements = document.getElementsByClassName(usernameClassName);
      const emailElements = document.getElementsByClassName(emailClassName);
  
    
  
      Array.from(usernameElements).forEach(element => element.textContent = "Loading...");
      Array.from(emailElements).forEach(element => element.textContent = "Loading...");
  
      const responseDecode = await fetch("/api/verify", {
        method: "GET",
      });
  
      const dataDecode = await responseDecode.json();
  
      if (responseDecode.ok) {
        const userId = dataDecode.user_id;
        const token = await getCookieToken();
  
        const responseProfile = await fetch(`/api/profile/${userId}/`, {
          method: "GET",
          headers: {
            "Cookie": `token=${token}`,
            "Content-Type": "application/json",
          },
        });
  
        const dataProfile = await responseProfile.json();
  
        if (responseProfile.ok) {
          Array.from(usernameElements).forEach(element => element.textContent = dataProfile.username);
          Array.from(emailElements).forEach(element => element.textContent = dataProfile.email);
        } else {
          console.error(dataProfile.message);
        }
      }
    } catch (error) {
      console.error(error);
    }
  }
  
