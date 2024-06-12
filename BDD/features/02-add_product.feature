Feature: Compras en una tienda en línea

  Scenario Outline: Agregar productos al carrito
    Given que el usuario está en la página web de la aplicación Pais: "<country_code>" Brand: "<brand>"
    When el usuario hace clic en "Iniciar Sesión" e ingresa email: "<email>" y password: "<password>"
    When el usuario agrega productos al carrito
    Examples:
      | email                           | password      | country_code | brand   |
      | automationtestingqa@yopmail.com | Test123456789 | AR           | store_1 |
#      | test123456@yopmail.com | Test123456789 | AR           | store_2 |
#      | test123456@yopmail.com | Test123456789 | AR           | store_3 |
