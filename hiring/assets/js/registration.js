function validatePhone(input) {
    var phonePattern = /^\d{10}$/;
    if (input.value.match(phonePattern)) {
      return true;
    } else {
      alert("Please enter a valid 10-digit phone number.");
      return false;
    }
  }
