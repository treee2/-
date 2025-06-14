document.addEventListener('DOMContentLoaded', function () { 
    // Обработчик для выдвижной панели
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    // const content = document.getElementById('content');
    const content = document.getElementsByClassName('content');
    sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('sidebar-open');
        content.classList.toggle('sidebar-open');
    });

    // Существующий код для подменю
    var menuItems = document.querySelectorAll('#menu > li.has-submenu > a'); 
 
    menuItems.forEach(function (menuItem) { 
        menuItem.addEventListener('click', function (e) { 
            e.preventDefault(); 
            var submenu = this.nextElementSibling; 
 
            if (submenu.style.display === 'block') { 
                submenu.style.display = 'none'; 
            } else { 
                submenu.style.display = 'block'; 
            } 
        }); 
    }); 
});