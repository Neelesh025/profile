function validateForm() {

    let name = document.getElementById("name").value;
    let phone = document.getElementById("phone").value;
    let pin = document.getElementById("pin").value;

    if (name === "") {
        alert("Enter name");
        return false;
    }

    if (!/^[0-9]{10}$/.test(phone)) {
        alert("Enter valid phone");
        return false;
    }

    if (!/^[0-9]{6}$/.test(pin)) {
        alert("Enter valid PIN");
        return false;
    }

    alert("Order placed successfully!");
    return true;
}