elements = {
    "logIn": [
        "//span[@class='label'][contains(.,'Account')]",
        "//a[text()='Log In']",
        "//input[@id='email']",
        "//input[@id='pass']",
        "//button[@title='Login']",
        "(//img[@alt='TealiumEcommerce Demo'])[1]"],

    "addProduct": [
        "(//li[@class='item last'])[",
        "//li[@class='option-white is-media']",
        "//span[@class='swatch-label'][contains(.,'XS')]",
        "(//button[@type='button'])[",
    ],

    "Shipping": [
        "(//span[contains(.,'Proceed to Checkout')])[",
        "//input[@id='billing:street1']",
        "//input[@id='billing:city']",
        "//input[@id='billing:postcode']",
        "//input[@id='billing:telephone']",
        "//select[@id='billing:region_id']",
        "(//span[contains(.,'Continue')])["],

    "Select_Shipping_Price":[
        "(//input[@name='shipping_method'])["],

    "Payment":["(//span[contains(.,'Place Order')])["]

}
