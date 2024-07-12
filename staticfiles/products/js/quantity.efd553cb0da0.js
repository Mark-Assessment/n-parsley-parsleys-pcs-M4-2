document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".increment-qty").forEach((button) => {
    button.addEventListener("click", function () {
      const qtyInput = this.closest(".input-group").querySelector(".qty_input");
      qtyInput.value = parseInt(qtyInput.value) + 1;
    });
  });

  document.querySelectorAll(".decrement-qty").forEach((button) => {
    button.addEventListener("click", function () {
      const qtyInput = this.closest(".input-group").querySelector(".qty_input");
      if (parseInt(qtyInput.value) > 1) {
        qtyInput.value = parseInt(qtyInput.value) - 1;
      }
    });
  });
});
