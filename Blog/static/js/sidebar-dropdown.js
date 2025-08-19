// Script para inicializar dropdowns en el sidebar personalizado
// Archivo: static/js/sidebar-dropdown.js

document.addEventListener('DOMContentLoaded', function () {
    var dropdownToggles = document.querySelectorAll('#sidebar .dropdown-toggle');
    dropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            var menu = this.nextElementSibling;
            if (menu.classList.contains('show')) {
                menu.classList.remove('show');
            } else {
                // Cierra otros dropdowns
                dropdownToggles.forEach(function(otherToggle) {
                    if (otherToggle !== toggle && otherToggle.nextElementSibling.classList.contains('show')) {
                        otherToggle.nextElementSibling.classList.remove('show');
                    }
                });
                menu.classList.add('show');
            }
        });
    });
    // Cierra el dropdown si se hace click fuera
    document.addEventListener('click', function(e) {
        if (!e.target.closest('#sidebar .nav-item.dropdown')) {
            dropdownToggles.forEach(function(toggle) {
                if (toggle.nextElementSibling.classList.contains('show')) {
                    toggle.nextElementSibling.classList.remove('show');
                }
            });
        }
    });
});
