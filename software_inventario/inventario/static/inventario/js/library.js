$(document).ready(function() {
    $('#dropdownMenuButton').on('click', function() {
      $('.dropdown-menu-form').toggle(); // Alterna la visibilidad del formulario
    });

    // Cierra el formulario si se hace clic fuera de él
    $(document).click(function(e) {
      if (!$(e.target).closest('.dropdown').length) {
        $('.dropdown-menu-form').hide();
      }
    });
  });